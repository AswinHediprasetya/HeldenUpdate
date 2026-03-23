# Helden Inc. — Cinematic Slider Experience

A fullscreen, slide-based cinematic website inspired by Orano's innovation page.
Built with pure HTML/CSS/JS embedded in Streamlit.

## 🚀 Deploy in 3 steps

1. **Create a GitHub repo** (public) → upload the 3 files below
2. **Go to** [share.streamlit.io](https://share.streamlit.io) → New app
3. Set **Main file**: `helden_slider.py` → **Deploy**

## 📁 Required files

```
├── helden_slider.py          ← main app
├── requirements.txt          ← streamlit>=1.32.0  
└── .streamlit/
    └── config.toml           ← theme config
```

## 🎮 Navigation

| Action | Result |
|--------|--------|
| Scroll / Mousewheel | Next / prev slide |
| ↑ ↓ Arrow keys | Navigate |
| Space / PageDown | Next |
| Dot indicators | Jump to slide |
| Touch swipe | Mobile nav |

## 🎨 Design

- 8 fullscreen slides with cinematic vertical transitions (900ms cubic-bezier)
- Cormorant Garamond italic display + Sora + DM Mono
- #08080a black + #FFD600 Helden yellow
- Noise texture overlay, radial glows, animated game board on slide 5
