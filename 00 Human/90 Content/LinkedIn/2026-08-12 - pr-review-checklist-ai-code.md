---
type: content
channel: linkedin
status: scheduled
date: "2026-08-12"
scheduled_for: "2026-08-12 09:00 ET"
topic: The checklist a senior engineer runs on AI-generated code before it ships
pillar: AI slop vs quality (fast output is not good output)
format: infographic
tags: [content, linkedin]
---

# LinkedIn - The AI code review checklist

## Angle
> AI writes the code in seconds. The review is where quality is won or lost. Here is the actual checklist a senior engineer runs on AI-generated code before it goes near a customer.

## Hook (first 2 lines)
AI can write a working feature in thirty seconds.
The thirty minutes that decide whether it ships are the review.

## Body
> Image-led post: the graphic carries the 7 items, so the caption points at it instead of repeating the list.

AI can write a working feature in thirty seconds. The thirty minutes that decide whether it ships are the review.

The demo always shows the happy path. The review is where you find everything the demo skipped. When the typing gets cheap, the checking gets expensive, and that is where AI slop either gets caught or gets shipped.

The seven things I check on AI-written code are in the graphic. None of them are exotic. A good senior engineer always checked them. What changed is the volume. The tool produces far more code, far faster, so the review became the real bottleneck. Skip it to keep up and you are not moving faster. You are shipping problems you have not read yet.

## Takeaway / CTA
Which line do you quietly skip when things get busy?

## Image alt text / first comment (full checklist)
> Set this as the graphic's alt text on LinkedIn (accessibility + searchability), and optionally drop it as the first comment so the specifics live in the thread.

The full checklist I run on AI-written code before it goes near a customer:
- Handles bad inputs: empty, huge, malformed, hostile.
- Fails safely when a call times out or a service is down.
- Secure: no unescaped queries, no leaked secrets, no permissions it granted itself.
- Fits how the system already works instead of inventing a new pattern.
- No scope creep: no extra endpoints, dependencies, or abstractions nobody needed.
- Readable in a year, because confident code no human understands is a future outage.
- Tests that prove the behavior, not tests that only pass.

## Hashtags
#AI #SoftwareEngineering #CodeReview #AISlop #EngineeringLeadership

## Cover image
> Format: INFOGRAPHIC, square 1024x1024 (the allowed exception to the no-infographics rule, because a checklist post specifically calls for one). SQUARE on purpose: LinkedIn caps feed images at 4:5 and crops anything taller, so the earlier 1024x1536 portrait version displayed badly. Use the square file below. Labels are short so the image renders legibly; the caption + alt-text block carry the detail.
> Prompt: A clean, modern square infographic titled "The AI Code Review Checklist". Minimal editorial design, muted professional palette of deep navy and warm off-white with one restrained teal accent, generous whitespace, a single clean sans-serif typeface, no clip-art, no stock photography, no decorative icons beyond simple checkboxes. Title across the top, then a single vertical column of seven items, each with a small square checkbox and a short bold label, spelled exactly: "Handles bad inputs", "Fails safely", "Secure by default", "Fits the codebase", "No scope creep", "Readable in a year", "Tests prove behavior". Footer line: "7 things a senior engineer checks before AI code ships." Balanced layout that fills the square, all text crisp, correctly spelled, legible. No other text.

![[assets/2026-08-12 - pr-review-checklist-ai-code-infographic-square.png]]

## Notes
- Pillar: AI slop vs quality. Format: real artifact / saveable checklist (deliberately a how-to, not another study reaction). Goal: saves + comments (the closing question invites people to admit which line they skip).
- Diff vs recent posts: the 7/24 and 7/27 agile posts argued the concept that judgment/review is the new bottleneck; this post delivers the actual checklist (the artifact), which is a different value to the reader (do-this vs think-this). The 8/5 METR post used data to show verification eats the time saved; this shows WHAT that verification is. Complementary, not a repeat.
- Checklist items are Chris's own engineering judgment, not sourced claims, so no citations needed. Nothing invented; these are standard senior-review concerns.
- Voice/anti-slop: no em dashes; no sentence starts with "and"; closed on a concrete question, not a mic-drop aphorism. Humanizer audit pass: cut a colon-reveal ("What changed is the volume: the tool produces...") into two plain sentences.
- 2026-08-08 update (Chris request): turned this into an INFOGRAPHIC post. Generated a vertical checklist graphic (short labels, gpt-image-1 rendered text cleanly on the first try), switched to an image-led caption (graphic carries the 7 items, caption points at it), moved the full detailed list to an alt-text/first-comment block. Scheduled for Wed 8/12 9:00 AM ET; card moved to Scheduled on [[Pipeline]]. Chris publishes (no direct LinkedIn posting integration).

## Sources
- None required (first-person engineering practice). Optional: link a longer version or the METR study in the first comment, not the body.
