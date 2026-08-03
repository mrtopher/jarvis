# Fofana Design System

A portable reference for the visual language built in this project. Paste any section of this
file directly into another prompt — a coding agent, an image generator, a copywriting pass — to
keep new work visually consistent with this site.

---

## 1. Brand personality

Warm, direct, a little playful. One confident accent color against a mostly neutral field —
never more than one saturated hue on screen at a time. Flat, geometric illustration over
photography. Generous whitespace; sections breathe at 120–140px of vertical padding on desktop.

---

## 2. Color

| Token | Hex | Role |
|---|---|---|
| `coral` | `#FF5252` | Primary accent — buttons, links on hover, eyebrow labels, icon chips, price figures |
| `charcoal` | `#333333` | Headings, dark surfaces (features panel, featured pricing card, social icons) |
| `blush` | `#FFF8F8` | Alternate section background (hero, nav, portfolio) — never pure white |
| `muted-plum` | `#676576` | Body copy — a grey with a warm/mauve bias, not neutral grey |
| `deep-plum` | `#1C1622` | Testimonial section base — near-black with a purple undertone |
| `white` | `#FFFFFF` | Card surfaces, button text, primary section background |

Supporting gradient hues (portfolio placeholders — see §6):

| Name | Gradient |
|---|---|
| Sky | `linear-gradient(135deg, #6EC6FF, #4A7FD4)` |
| Amber | `linear-gradient(135deg, #FFD48A, #FF8A65)` |
| Orchid | `linear-gradient(135deg, #FF8AC2, #B06AE0)` |
| Slate | `linear-gradient(135deg, #2B2F3A, #4C5568)` |

**Rule of one accent**: coral is the only saturated color allowed against the neutral
charcoal/blush/white field. If a new section needs emphasis, reach for scale, weight, or
whitespace before reaching for a second color.

---

## 3. Typography

- **Display / Headings** — Montserrat, 700. Used for `h1`–`h5` only.
- **Body** — Roboto, 400 (500 for buttons/labels).
- Google Fonts import: `family=Montserrat:wght@500;600;700;800&family=Roboto:wght@400;500;700`

| Style | Size / Line-height | Weight | Notes |
|---|---|---|---|
| H1 (hero headline) | 70px / 1.05 | 700 | Tight leading, negative optical margin |
| H2 (section headline) | 46px / 1.15 | 700 | Centered, max-width ~560px so it wraps in 2 lines |
| Eyebrow label | 15px / uppercase | 600 | Coral, `letter-spacing: 1px`, sits above every H2 |
| H5 (card/feature titles) | 20px | 600 | Charcoal on light, white on dark surfaces |
| Body | 16px / 28px | 400 | `letter-spacing: 0.3px`, muted-plum |

Mobile: H1 drops to 52px, H2 to 34px below 768px.

---

## 4. Layout & spacing

- Container: max-width `1140px`, `24px` side padding.
- Grid: flexbox rows with `30px` gap — 2-column (features, intro), 3-column (services, pricing),
  or 2×2 (portfolio). No 12-column bootstrap grid; sections define their own simple grid.
- Section rhythm: `120–140px` top/bottom padding on desktop, collapsing to ~60–90px on mobile.
- Cards/panels: `border-radius` 5–15px depending on size (small chips 5–8px, large panels 15px).
- Standard elevation: `box-shadow: 0 5px 38px -6px rgba(0,0,0,0.14)` — soft, wide, low-opacity.
  Used for services' featured card, portfolio caption cards, pricing cards, testimonial card.
- Signature layout move: the dark **features panel overlaps the hero** above it via
  `margin-top: -220px` on a full-bleed dark rounded panel. Reuse this "panel bites into the
  section above" move anywhere you want two sections to feel stitched together rather than
  stacked.

---

## 5. Components

- **Button** — coral fill, white text, `border-radius: 5px`, `padding: 14px 32px`, weight 500.
  Hover inverts to charcoal fill (never darkens coral — it swaps to the neutral).
- **Eyebrow + headline pair** — every section opens with a small coral uppercase label directly
  above a centered H2. This is the section's only wayfinding device; there are no numbered steps
  or icons in headlines.
- **Icon chip (services)** — 60×60px, `border-radius: 8px`, coral fill, white glyph centered.
- **Icon roundel (social/contact)** — 38×38px circle, charcoal fill, white glyph; hover swaps
  fill to coral.
- **Featured/highlighted card** — the middle item in a 3-up row (services, pricing) is
  distinguished by *elevation or dark fill*, never by size change alone. Pricing's featured
  card inverts to charcoal with blush text; services' featured card stays light but gets the
  standard elevation shadow the siblings lack.
- **Quote card** — white rounded card (15px) floating on a dark section, oversized serif closing
  quotation mark in coral as the only decorative flourish.

---

## 6. Imagery & illustration style

No stock photography. Two visual modes cover every image slot on the site:

**A. Flat illustration (hero figure)**
Geometric, front-facing, cropped at the chest, inside a soft rounded-rect card frame. Flat solid
color fills only — no gradients or shading on the figure itself. A thin coral ring-and-crosshair
line drawing radiates behind the frame as the only decorative flourish.

**B. Abstract gradient tiles (portfolio thumbnails)**
Each project card is a flat 135°-diagonal duotone gradient (see §2 supporting gradients) with
no photography, texture, or objects — the color pairing alone signals the category.

**C. Mood-gradient backdrop (testimonial section)**
A near-black, purple-leaning radial gradient blend (base `#1C1622`, blooms of `#4A3960` and
`#3A2B4D`) under an 86–90% dark overlay — used anywhere text needs to sit on a dark, moody,
non-photographic background.

---

## 7. Iconography

Two distinct icon treatments, used in different contexts — don't mix them within one section:

- **Outline/stroke icons** — feature list on the dark panel. `stroke-width: 1.4`, `fill: none`,
  color inherits (coral on dark charcoal).
- **Solid glyph icons** — services chips, social roundels. Solid white fill sitting inside a
  filled coral or charcoal shape.

---

## 8. Motion

Minimal and functional only: 0.2s ease color/background transitions on hover (links, buttons,
icon roundels), a 4px translate on the "See our work" arrow, and a 0.45s ease slide transform on
the testimonial carousel. No scroll-triggered reveals, no parallax — the brand's energy comes
from color and type, not motion.

---

## 9. Image-generation prompt kit

Copy-paste blocks for keeping new AI-generated imagery on-brand. Swap the bracketed detail;
keep the style language intact.

**Hero-style flat illustration portrait**
```
Flat vector illustration of a person, front-facing, cropped at the chest, [describe pose/role].
Minimal geometric shapes, solid flat color fills with no gradients or shading on the figure.
Warm brown skin tone #E0A780, dark hair #2B2118, wearing a solid charcoal top #333333, one
coral #FF5252 accent line at the collar. Set inside a soft rounded-rectangle card in pale pink
#FFE3E0. Thin coral ring-and-crosshair line-art radiates behind the card. Clean vector
illustration style, no texture, no text, no logo.
```

**Portfolio / project thumbnail**
```
Abstract flat background, diagonal 135-degree gradient from [color A] to [color B], smooth
color blend, no texture, no objects, no photography, rounded corners, minimal flat design tile.
```
Use one of the four brand gradient pairs from §2, or a new pair that keeps the same
"one warm + one cool anchor" logic.

**Moody dark section backdrop**
```
Abstract dark atmospheric background, near-black with a plum/purple undertone (#1C1622 base),
soft radial color bloom in muted violet (#4A3960) upper-left and deep purple (#3A2B4D)
lower-right, heavy dark vignette (~85-90% opacity), subtle grain, cinematic and minimal, no
subject, no text — for use as a text-overlay backdrop.
```

**Icon glyph**
```
Single-color icon glyph, white, centered inside a solid coral #FF5252 rounded-square chip
(60x60px, 8px corner radius) OR a solid charcoal #333333 circle (38px), simple geometric line
or solid-fill style consistent with a minimal flat icon set, no gradients, no outlines beyond
the shape itself.
```

**Brand mark / favicon**
```
Minimal wordmark lockup: bold geometric sans-serif (Montserrat 700) brand name in charcoal
#333333, with a single coral #FF5252 period/dot as the only accent mark. No icon, no gradient,
no drop shadow.
```

---

## 10. Do / Don't

- **Do** keep coral as the only saturated accent on any given screen.
- **Do** use the blush `#FFF8F8` — not pure white — for alternating section backgrounds.
- **Do** pair every H2 with a small coral eyebrow label above it.
- **Don't** introduce photography — the brand is illustration + abstract gradient only.
- **Don't** add a second accent color, even a "complementary" one, to a section.
- **Don't** use pure grey for body text — it should carry `muted-plum`'s slight warm bias.
