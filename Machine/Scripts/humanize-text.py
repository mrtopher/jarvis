#!/usr/bin/env python3
"""Humanize AI-generated prose via the GPTHuman AI Humanizer API.

This is an OPTIONAL early mechanical pass. Per CLAUDE.md rule #6 the VOICE.md +
humanizer audit still runs LAST and is the final authority: GPTHuman can
reintroduce em dashes / generic phrasing that VOICE.md bans, so always re-check
its output against VOICE.md (no em dashes, short-punchy, don't start with "and").

Scope (decided with Chris 2026-08-08): use for public /content pieces and
resumes/cover letters. NOT research briefs.

API key resolution order:
  1. GPTHUMAN_API_KEY environment variable
  2. Machine/Scripts/.secrets  (KEY=VALUE lines, gitignored, key: GPTHUMAN_API_KEY)

The endpoint is overridable via GPTHUMAN_API_URL (default below). Confirm the
exact host from your GPTHuman dashboard docs if requests 404/401.

Usage:
  ~/.venvs/jarvis/bin/python Machine/Scripts/humanize-text.py --text "..."
  ~/.venvs/jarvis/bin/python Machine/Scripts/humanize-text.py --file draft.md
  cat draft.md | ~/.venvs/jarvis/bin/python Machine/Scripts/humanize-text.py
  # options: --tone College --mode Balanced

Prints the rewritten text to stdout; metrics (humanScore, credits, etc.) go to
stderr so you can pipe/redirect stdout cleanly.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SECRETS_FILE = SCRIPT_DIR / ".secrets"
DEFAULT_API_URL = "https://api.gpthuman.ai/v1/humanize"
# Possible keys the API may use for the rewritten text, in preference order.
OUTPUT_KEYS = ("output", "humanizedText", "humanized", "result", "text", "content")


def load_api_key() -> str:
    key = os.environ.get("GPTHUMAN_API_KEY")
    if key:
        return key.strip()
    if SECRETS_FILE.exists():
        for line in SECRETS_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, _, value = line.partition("=")
            if name.strip() == "GPTHUMAN_API_KEY":
                return value.strip().strip('"').strip("'")
    sys.exit(
        "No GPTHuman API key found. Set GPTHUMAN_API_KEY or add it to "
        f"{SECRETS_FILE} as GPTHUMAN_API_KEY=..."
    )


def read_input(args) -> str:
    if args.text is not None:
        return args.text
    if args.file:
        return Path(args.file).read_text()
    if not sys.stdin.isatty():
        return sys.stdin.read()
    sys.exit("No input text. Pass --text, --file, or pipe text on stdin.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Humanize text via GPTHuman API.")
    parser.add_argument("--text", help="Text to humanize (else use --file or stdin).")
    parser.add_argument("--file", help="Path to a file whose contents to humanize.")
    parser.add_argument("--tone", default="College", help="GPTHuman tone (default College).")
    parser.add_argument("--mode", default="Balanced", help="GPTHuman mode (default Balanced).")
    args = parser.parse_args()

    text = read_input(args).strip()
    if not text:
        sys.exit("Input text is empty.")
    # GPTHuman requires >300 chars and <2000 words; check up front to skip
    # cleanly (workflows treat a non-zero exit here as a graceful skip).
    if len(text) <= 300:
        sys.exit(f"Text is {len(text)} chars; GPTHuman needs more than 300. Skipping.")
    if len(text.split()) >= 2000:
        sys.exit(f"Text is {len(text.split())} words; GPTHuman caps at under 2000. Skipping.")

    payload = json.dumps({"text": text, "tone": args.tone, "mode": args.mode}).encode()
    api_url = os.environ.get("GPTHUMAN_API_URL", DEFAULT_API_URL)
    request = urllib.request.Request(
        api_url,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {load_api_key()}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            # A browser-like UA avoids Cloudflare's default bot block (error 1010)
            # that rejects urllib's default User-Agent.
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            body = json.loads(response.read().decode())
    except urllib.error.HTTPError as err:
        detail = err.read().decode(errors="replace")
        sys.exit(f"GPTHuman API error {err.code}: {detail}")
    except urllib.error.URLError as err:
        sys.exit(f"Could not reach GPTHuman API at {api_url}: {err.reason}")

    output = next((body[k] for k in OUTPUT_KEYS if isinstance(body.get(k), str)), None)
    if output is None:
        sys.exit(f"Could not find rewritten text in response. Raw: {json.dumps(body)}")

    for label in ("humanScore", "similarity", "readability", "creditUsage", "creditBalance"):
        if label in body:
            print(f"{label}: {body[label]}", file=sys.stderr)

    print(output)


if __name__ == "__main__":
    main()
