---
type: workflow
status: active
trigger: /research
last_verified: "2026-07-14"
modes: "single mode - research a question/topic/URL(s) passed as the argument"
handoff: "optional formatted Google Doc for a vendor/client, created via the Google Drive MCP"
tags: [workflow, research, capture, handoff]
---

# Workflow - /research

Answer a real question with grounded, multi-source research, capture it as a source-of-truth note in the vault, and (optionally) hand it off as a formatted Google Doc for a vendor, client, or collaborator. This is the "research + document creation" workflow: the vault note is what gets captured and kept, the Google Doc is the shareable artifact.

Two halves, like `/job-apply` and `/content`: a **Research** half that writes a vault note, and a **Handoff** half that renders the shareable doc. Run **Context** first, then **Research**, then **Handoff** (if wanted), then **Wrap-up**.

## Step 0 - Read the request
Look at `$ARGUMENTS`. It is a question, a topic, or one or more URLs, optionally with hints:
- **Audience hint** (words like "vendor", "client", "internal", "for a vendor", "for the team"). Default audience is **self** (a personal brief, no handoff doc unless asked).
- **Handoff hint** (words like "google doc", "doc", "handoff", "share", or "no doc"). If present, honor it. If absent and the audience is anything other than self, ask whether to create a handoff doc.
- If `$ARGUMENTS` is **empty**, ask the user what to research (question or topic, target audience, and whether they want a handoff doc). Do not guess a topic.

## Shared phase: Context
Read these so the research and any handoff reflect the operator's situation, goals, and voice:
- `Machine/Personalization/operator-profile.md` (current role, 30-day goals, target areas)
- `00 Human/70 Context/business-profile.md` (background, positioning, who they serve)
- `VOICE.md` (vault root) - the authoritative voice for any **authored prose** in the vault note and the handoff doc (no em dashes, ever; don't start sentences with "and"; short, punchy sentences). If missing, fall back to `00 Human/70 Context/writing-style.md`. **Exception:** verbatim quotes, statistics, and definitions pulled from sources are external content - keep them word-for-word, do not rewrite them to satisfy VOICE.md.

## Shared phase: Research (the research half)
1. **Frame the question.** Restate the question in one line and list what a complete answer must cover (the sub-questions). If the request is broad or ambiguous, state the scope you are assuming.
2. **Gather.** Use `WebSearch` and `WebFetch` across multiple independent sources. Prefer primary and reputable sources; corroborate any load-bearing claim with a second source. If a URL was passed, fetch it first, then widen out. If the topic is broad or needs more than about three queries, dispatch an `Explore` subagent (or several in parallel) to gather breadth without flooding the main context, then synthesize their findings. If a source will not fetch, note it and try an alternative or ask the user to paste the text.
3. **Capture sources as you go.** For every source used, keep title, URL, type, and the one key takeaway it contributed. This feeds the Sources table and keeps claims traceable.
4. **Synthesize.** Organize the findings into a clear answer. Note where sources agree, where they disagree, and what is still uncertain. Separate fact from your interpretation. Do not pad. If the honest answer is "it depends", say what it depends on.

## Shared phase: Capture (write the vault note)
1. Create from `00 Human/80 Templates/Research Brief.md` and save as `00 Human/40 Resources/Research/YYYY-MM-DD - <slug>.md` (kebab-case slug from the question; create the `Research/` folder on demand).
2. Fill it fully:
   - **Question** (with scope), **Answer (TL;DR)** leading with the recommendation, **Key findings** (bulleted, specifics and numbers where they exist), **Recommendation** (the honest call grounded in the operator profile), **My angle** (why it matters to Chris specifically - Dual Logic, job search, content, or a client), **Open questions / gaps**, **Sources** table, and **Connections** (link the related project/person/company/topic).
   - Set frontmatter: `question`, `audience`, `date`, and `tags` (`research`, plus `needs-review` until Chris has read it). Leave `handoff_doc` empty for now.
3. Authored prose follows `VOICE.md`; verbatim source quotes/stats stay as-is.

## Shared phase: Handoff (optional Google Doc)
Only run when a handoff doc is wanted (audience is vendor/client/internal, or the user asked for a doc).
1. **Compose the document** for its audience. A vendor/client handoff is not the raw brief: give it a clear title, a short intro that frames the ask, well-structured sections (headings, bold labels, tables or lists where they help), and a crisp recommendation or next-steps section. Write authored prose in the user's voice per `VOICE.md`. Do not expose internal notes, the "My angle" section, or `needs-review` hedging unless it serves the reader.
2. **Create the Google Doc** with the Google Drive MCP. Call `mcp__claude_ai_Google_Drive__create_file` with:
   - `title`: a clear document title (e.g. "n8n Workflow Automation - Pricing Guidance").
   - `textContent`: the composed document as **HTML** (preferred, for real headings/bold/lists/tables) or Markdown.
   - `contentMimeType`: `text/html` (or `text/markdown`). Leave conversion on so Drive turns it into a native Google Doc (`application/vnd.google-apps.document`). Do NOT set `disableConversionToGoogleType`.
   - `parentId`: only if the user names a target Drive folder; otherwise omit (lands in Drive root).
3. **Record the link back in the vault note.** Put the returned Doc URL in the note's `handoff_doc:` frontmatter and add a `- Handoff: <url>` line under Connections, so the vault stays the source of truth and the artifact is one click away.
4. If the Google Drive MCP is unavailable or the call fails, save the composed document as `00 Human/40 Resources/Research/YYYY-MM-DD - <slug> (handoff).md` instead, tell the user the Doc could not be created, and note it in the vault brief.

## Shared phase: Wrap-up
1. **Log it.** Append a timestamped entry to today's daily note Activity Log: the question researched, the note path, and the handoff Doc link if one was made. If today's daily note does not exist yet, say so and defer the log line (do not stub the daily note; `/today` owns creating it).
2. **Report back.** Tell the user the vault note path, the recommendation in one line, the handoff Doc link (if any), and the suggested next step (usually: read the brief, then share or act on the Doc).

## Error Handling
| Failure Point | Recovery |
|--------------|----------|
| No argument | Ask what to research, the audience, and whether a handoff doc is wanted; do not guess |
| A URL won't fetch | Note it, try an alternative source, or ask the user to paste the text; still cite what you used |
| Sources conflict | Present both sides and say which is better supported and why; do not force a false consensus |
| Google Drive MCP unavailable / call fails | Save the handoff as a `(handoff).md` note in the Research folder and tell the user |
| `VOICE.md` missing | Fall back to `00 Human/70 Context/writing-style.md` and tell the user to create `VOICE.md` |
| Today's daily note missing | Defer the Activity Log line and report it; do not create the daily note here |

## Related
- Template - [[Research Brief]]
- Command - `/research`
- Voice - [[VOICE]]
