# Helden Inc. — The Definitive Showcase
### Awwwards-Quality · Orano-Inspired · 15 Fullscreen Slides

---

## 🚀 Deploy Free in 3 Steps

### 1. Create GitHub Repo
github.com/new → name it anything → Public → Create

### 2. Upload Files
```
helden_slider.py    ← main app
requirements.txt    ← streamlit>=1.32.0
```
Also create `.streamlit/config.toml` with:
```toml
[theme]
base = "dark"
backgroundColor = "#08080d"

[server]
headless = true
```

### 3. Deploy on Streamlit Cloud
share.streamlit.io → New app → select repo
Main file: `helden_slider.py` → Deploy ✅

---

## 🎮 Navigation

| Input | Action |
|-------|--------|
| Mouse scroll | Next / prev slide |
| ↑ ↓ ← → Arrow keys | Navigate |
| Space / PageDown | Next |
| Home / End | First / Last |
| Sidebar titles | Jump to any slide |
| ↑ ↓ Arrow buttons | Navigate |
| Touch swipe | Mobile |

---

## 🎨 Design System

### Concept: Dark ↔ Light Cinematic Rhythm
Dark slides and light slides alternate — the same contrast rhythm
Apple uses in product pages. Each context switch makes the content
feel fresh and the journey feel varied.

### Typography
- **Fraunces** — editorial italic serif (display, headlines)
- **Figtree** — geometric humanist sans (body, UI)
- **DM Mono** — technical monospace (labels, metadata)

### Colors
| Token | Value | Use |
|-------|-------|-----|
| `--ink` | `#08080d` | Void black background |
| `--paper` | `#fafaf8` | Warm white background |
| `--y` | `#FFD600` | Helden yellow (dark slides) |
| `--ydark` | `#C8A800` | Helden yellow (light slides) |

### Transition System
1. **72ms shutter flash** — cinema-cut blackout at every transition
2. **Scale morph (exit)** — slides scale to 0.95 + blur 8px
3. **Scale morph (enter)** — slides emerge from scale 1.06 + blur 14px → 0
4. **Easing** — `cubic-bezier(0.76, 0, 0.24, 1)` (Orano's signature)

### Animation Variants
- **`rise`** — translateY(24px) → 0 + fade (headlines)
- **`fade`** — opacity 0 → 1 (labels, copy)
- **`wipe`** — clip-path left→right (divider lines)
- **`pop`** — scale(0.72) → 1 with spring overshoot (badges, icons)

---

## 📊 All 15 Slides

| # | Slide | Type | Visual |
|---|-------|------|--------|
| 01 | **Hero** | Dark | Ken Burns dot grid + radial glow + cursor trail |
| 02 | **Mission** | Light | Typography contrast — dim italic vs bold |
| 03 | **Problem** | Dark | Giant "10%" stat — 38rem Fraunces |
| 04 | **Insight** | Dark | Two-line contrast: dim → bright |
| 05 | **FutureGame** | Dark | Live animated game board (wave patterns) |
| 06 | **Escape Room** | Light | Spinning concentric hexagons |
| 07 | **Escape Box** | Dark | CSS isometric 3-face box illustration |
| 08 | **Onboarding** | Light | Journey path with node states |
| 09 | **Micro Learning** | Dark | Phone mockup + 3 floating stat cards |
| 10 | **Custom Escape** | Light | 4-step process cards |
| 11 | **GamePlan** | Dark | Interactive strategy board diagram |
| 12 | **Learning Events** | Light | 2×2 event format grid |
| 13 | **All 9 Products** | Light | Staggered 3×3 typography grid |
| 14 | **Clients** | Light | "200+" + 12 clients cascade + 3 testimonials |
| 15 | **CTA** | Yellow | "Make them remember." + pulsing rings |

---

*Content from helden-inc.com/en/#games · Design system inspired by orano.group*
