#!/usr/bin/env python3
"""Generate a cover image for a content piece via the OpenAI Images API.

Used by the /content workflow (Machine/Workflows/content.md). Given a prompt and
an output path, it calls gpt-image-1 and writes a PNG.

API key resolution order:
  1. OPENAI_API_KEY environment variable
  2. Machine/Scripts/.secrets  (KEY=VALUE lines, gitignored, key: OPENAI_API_KEY)

Usage:
  ~/.venvs/jarvis/bin/python Machine/Scripts/generate-content-image.py \
      --prompt "..." --out "00 Human/90 Content/LinkedIn/assets/<slug>.png" \
      [--size 1536x1024]
"""
import argparse
import base64
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SECRETS_FILE = SCRIPT_DIR / ".secrets"
VALID_SIZES = {"1024x1024", "1536x1024", "1024x1536", "auto"}


def load_api_key() -> str:
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        return key.strip()
    if SECRETS_FILE.exists():
        for line in SECRETS_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, _, value = line.partition("=")
            if name.strip() == "OPENAI_API_KEY":
                return value.strip().strip('"').strip("'")
    sys.exit(
        "No OpenAI API key found. Set OPENAI_API_KEY or add it to "
        f"{SECRETS_FILE} as OPENAI_API_KEY=sk-..."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a content cover image.")
    parser.add_argument("--prompt", required=True, help="Image generation prompt.")
    parser.add_argument("--out", required=True, help="Output PNG path (vault-relative or absolute).")
    parser.add_argument("--size", default="1536x1024", help=f"One of {sorted(VALID_SIZES)}.")
    args = parser.parse_args()

    if args.size not in VALID_SIZES:
        sys.exit(f"Invalid size {args.size!r}. Choose from {sorted(VALID_SIZES)}.")

    from openai import OpenAI

    client = OpenAI(api_key=load_api_key())
    result = client.images.generate(
        model="gpt-image-1",
        prompt=args.prompt,
        size=args.size,
        n=1,
    )
    image_b64 = result.data[0].b64_json
    if not image_b64:
        sys.exit("API returned no image data.")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(base64.b64decode(image_b64))
    print(out_path)


if __name__ == "__main__":
    main()
