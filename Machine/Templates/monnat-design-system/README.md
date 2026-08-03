# Fofana Design System — bundle

What's in here and how to use each piece:

- **`DESIGN_SYSTEM.md`** — the full written reference: color, type, spacing, component
  rules, imagery style, and a ready-to-paste **image-generation prompt kit**. Open this
  when you need to brief another AI tool (coding agent, image generator, copywriter) and
  want it to stay on-brand.

- **`tokens.css`** — the same color/type/spacing values as real CSS custom properties
  (`--fof-*`), plus a handful of optional component classes (`.fof-button`,
  `.fof-icon-chip`, etc). Drop this into any web project and `@import` or `<link>` it, or
  use it as the source when porting the palette to Tailwind config / JSON tokens.

- **`style-guide.html`** — a self-contained, open-anywhere visual reference. Double-click
  to open in a browser: every color, type size, and component renders live, and each
  image-gen prompt block has a copy button. No build step, no server needed — fonts are
  embedded directly in the file.

- **`img/`** — the two original SVG assets referenced by the style guide (hero
  illustration, favicon mark).

## Quick start

- Referencing the system in a prompt elsewhere → paste from `DESIGN_SYSTEM.md`.
- Building a new page in a different codebase → copy `tokens.css` in.
- Just want to look something up → open `style-guide.html`.
