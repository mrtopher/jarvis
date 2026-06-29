---
type: guide
status: active
tags: [setup, vault]
---

# Setup Guide

## Required
- Obsidian
- An AI harness that can read this vault and use the command/workflow files

## Recommended
- Claude Code or another harness that respects `.claude/commands/`
- Python 3 for script-backed workflows
- `yt-dlp` for YouTube/media workflows
- FFmpeg for caption or media processing workflows

## Open-as-vault flow
1. Extract the folder anywhere.
2. Open Obsidian.
3. Choose **Open folder as vault**.
4. Select this folder.
5. Open your AI harness from the same folder.

## Google Calendar import (optional, used by `/today`)
`/today` can pull your real calendar events via `gcalcli`. One-time setup:
1. Install: `brew install gcalcli`
2. Create Google OAuth credentials (gcalcli ships none of its own):
   - Go to the Google Cloud Console, create or pick a project.
   - Enable the **Google Calendar API**.
   - On the OAuth consent screen, set the app to **External**, and add your own Google account under **Test users**.
   - Create an **OAuth client ID** of type **Desktop app**. Copy the Client ID and Client Secret.
3. Authenticate once: `gcalcli init` (paste the Client ID and Secret when prompted, then approve in the browser). You will likely see an "unverified app" warning; click **Advanced** then **Go to gcalcli (unsafe)** to proceed. This is expected for your own client.
4. Verify: `gcalcli agenda today tomorrow --nocolor`
After this, the OAuth token is cached, so `/today` runs `gcalcli agenda` with no secrets in the command. If `gcalcli` is missing or unauthenticated, `/today` simply skips the import.

## First run
- `/start` = orientation
- `/interview` = personalization
- `/today` = plan your day
- `/new` = route brain dumps
- `/closeday` = close the loop
