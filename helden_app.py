"""
Helden Inc. — Homepage Showcase
Streamlit single-file app · deploy to Streamlit Cloud via GitHub

Design: Bold black-and-yellow brand identity.
        Bebas Neue (display) + DM Sans (body) + DM Mono (data).
        Game-board geometry as decorative language.
        Sections: Hero, Value Prop, Products, Clients, CTA.
"""

import streamlit as st

st.set_page_config(
    page_title="Helden Inc. — Gamified Internal Communication",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

:root {
  --black:   #0a0a0a;
  --black2:  #111111;
  --black3:  #1a1a1a;
  --yellow:  #FFD600;
  --yellow2: #FFE84D;
  --ydim:    rgba(255,214,0,0.08);
  --yline:   rgba(255,214,0,0.18);
  --white:   #f5f0e8;
  --grey:    #6b6b6b;
  --grey2:   #2a2a2a;
  --sans:    'DM Sans', sans-serif;
  --display: 'Bebas Neue', sans-serif;
  --mono:    'DM Mono', monospace;
}

html, body, [class*="css"] {
  font-family: var(--sans) !important;
  background: var(--black) !important;
  color: var(--white) !important;
  -webkit-font-smoothing: antialiased !important;
}

.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

#MainMenu, header, footer,
div[data-testid="stDecoration"],
div[data-testid="stToolbar"] { display: none !important; }

/* ── Scroll animations ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes slideIn {
  from { opacity: 0; transform: translateX(-32px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes pulse-yellow {
  0%,100% { box-shadow: 0 0 0 0 rgba(255,214,0,0); }
  50%      { box-shadow: 0 0 32px 8px rgba(255,214,0,0.18); }
}
@keyframes ticker {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
@keyframes counter {
  from { opacity: 0; transform: scale(0.8); }
  to   { opacity: 1; transform: scale(1); }
}

/* ── NAV ── */
.nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(10,10,10,0.92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--yline);
  padding: 0 5vw;
  display: flex; align-items: center; justify-content: space-between;
  height: 64px;
}
.nav-logo {
  display: flex; align-items: center; gap: 12px;
}
.nav-mark {
  width: 36px; height: 36px;
  background: var(--yellow);
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  display: flex; align-items: center; justify-content: center;
}
.nav-name {
  font-family: var(--display);
  font-size: 1.5rem;
  color: var(--white);
  letter-spacing: 0.05em;
}
.nav-links {
  display: flex; gap: 2rem;
  font-size: 0.8125rem; font-weight: 500;
  color: var(--grey);
}
.nav-links a {
  color: var(--grey); text-decoration: none;
  transition: color 0.2s;
}
.nav-links a:hover { color: var(--yellow); }
.nav-cta {
  background: var(--yellow);
  color: var(--black) !important;
  padding: 0.5rem 1.25rem;
  border-radius: 3px;
  font-weight: 600;
  font-size: 0.8125rem;
  text-decoration: none;
  transition: background 0.2s, transform 0.15s;
  display: inline-block;
}
.nav-cta:hover {
  background: var(--yellow2);
  transform: translateY(-1px);
}

/* ── TICKER ── */
.ticker-wrap {
  background: var(--yellow);
  overflow: hidden;
  height: 36px;
  display: flex; align-items: center;
}
.ticker-track {
  display: flex; gap: 0;
  animation: ticker 28s linear infinite;
  white-space: nowrap;
}
.ticker-item {
  font-family: var(--display);
  font-size: 0.9rem;
  color: var(--black);
  letter-spacing: 0.12em;
  padding: 0 2rem;
}
.ticker-dot {
  color: rgba(0,0,0,0.3);
  font-size: 1.2rem;
  vertical-align: middle;
}

/* ── HERO ── */
.hero {
  min-height: 92vh;
  padding: 6vw 5vw;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4vw;
  align-items: center;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  top: -200px; right: -200px;
  width: 600px; height: 600px;
  border: 1px solid var(--yline);
  border-radius: 50%;
  pointer-events: none;
}
.hero::after {
  content: '';
  position: absolute;
  top: -120px; right: -120px;
  width: 400px; height: 400px;
  border: 1px solid rgba(255,214,0,0.08);
  border-radius: 50%;
  pointer-events: none;
}
.hero-eyebrow {
  font-family: var(--mono);
  font-size: 0.65rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--yellow);
  margin-bottom: 1.25rem;
  animation: fadeUp 0.6s ease both;
}
.hero-headline {
  font-family: var(--display);
  font-size: clamp(3.5rem, 7vw, 7rem);
  line-height: 0.92;
  color: var(--white);
  letter-spacing: 0.01em;
  margin-bottom: 1.5rem;
  animation: fadeUp 0.6s 0.1s ease both;
}
.hero-headline span {
  color: var(--yellow);
}
.hero-sub {
  font-size: 1.125rem;
  color: var(--grey);
  line-height: 1.7;
  max-width: 480px;
  margin-bottom: 2.5rem;
  animation: fadeUp 0.6s 0.2s ease both;
}
.hero-actions {
  display: flex; gap: 1rem; flex-wrap: wrap;
  animation: fadeUp 0.6s 0.3s ease both;
}
.btn-primary {
  background: var(--yellow);
  color: var(--black);
  padding: 0.875rem 2rem;
  font-weight: 600;
  font-size: 0.9375rem;
  border-radius: 3px;
  text-decoration: none;
  transition: background 0.2s, transform 0.15s;
  display: inline-block;
}
.btn-primary:hover {
  background: var(--yellow2);
  transform: translateY(-2px);
}
.btn-outline {
  background: transparent;
  color: var(--white);
  padding: 0.875rem 2rem;
  font-weight: 500;
  font-size: 0.9375rem;
  border: 1px solid var(--grey2);
  border-radius: 3px;
  text-decoration: none;
  transition: border-color 0.2s, color 0.2s, transform 0.15s;
  display: inline-block;
}
.btn-outline:hover {
  border-color: var(--yellow);
  color: var(--yellow);
  transform: translateY(-2px);
}

/* Hero right — game board visual */
.hero-visual {
  position: relative;
  height: 520px;
  animation: fadeUp 0.7s 0.15s ease both;
}
.game-board {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-template-rows: repeat(5, 1fr);
  gap: 8px;
}
.game-cell {
  background: var(--black2);
  border: 1px solid var(--yline);
  border-radius: 4px;
  transition: background 0.3s;
}
.game-cell.lit {
  background: rgba(255,214,0,0.12);
  border-color: rgba(255,214,0,0.4);
}
.game-cell.bright {
  background: var(--yellow);
  border-color: var(--yellow);
  animation: pulse-yellow 2.5s ease infinite;
}
.board-card {
  position: absolute;
  background: var(--black2);
  border: 1px solid var(--yline);
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
}
.board-card.top-right {
  top: -12px; right: -12px;
  width: 200px;
  border-left: 3px solid var(--yellow);
}
.board-card.bottom-left {
  bottom: -12px; left: -12px;
  width: 220px;
  border-left: 3px solid var(--yellow);
}
.board-card-num {
  font-family: var(--display);
  font-size: 2rem;
  color: var(--yellow);
  line-height: 1;
  margin-bottom: 2px;
}
.board-card-label {
  font-family: var(--mono);
  font-size: 0.58rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--grey);
}
.floating-badge {
  position: absolute;
  background: var(--yellow);
  color: var(--black);
  font-family: var(--mono);
  font-size: 0.6rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.35rem 0.75rem;
  border-radius: 3px;
  white-space: nowrap;
}
.floating-badge.pos1 { top: 45%; left: 15%; }
.floating-badge.pos2 { top: 25%; left: 35%; }

/* ── STATS ── */
.stats-section {
  padding: 4rem 5vw;
  border-top: 1px solid var(--yline);
  border-bottom: 1px solid var(--yline);
  background: var(--black2);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}
.stat-item {
  padding: 2rem 2.5rem;
  border-right: 1px solid var(--yline);
  animation: counter 0.5s ease both;
}
.stat-item:last-child { border-right: none; }
.stat-num {
  font-family: var(--display);
  font-size: 3.5rem;
  color: var(--yellow);
  line-height: 1;
  letter-spacing: -0.01em;
  margin-bottom: 0.375rem;
}
.stat-label {
  font-family: var(--mono);
  font-size: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: var(--grey);
}
.stat-desc {
  font-size: 0.8125rem;
  color: var(--grey);
  margin-top: 0.25rem;
}

/* ── SECTION HEADER ── */
.section-header {
  padding: 5rem 5vw 2rem;
}
.section-eyebrow {
  font-family: var(--mono);
  font-size: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.22em;
  color: var(--yellow);
  margin-bottom: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.section-eyebrow::before {
  content: '';
  width: 24px;
  height: 1px;
  background: var(--yellow);
}
.section-title {
  font-family: var(--display);
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  color: var(--white);
  line-height: 0.95;
  letter-spacing: 0.01em;
  max-width: 800px;
}
.section-title span { color: var(--yellow); }
.section-sub {
  font-size: 1rem;
  color: var(--grey);
  line-height: 1.75;
  max-width: 560px;
  margin-top: 1.25rem;
}

/* ── VALUE PROPS ── */
.value-section {
  padding: 1rem 5vw 5rem;
}
.value-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-top: 2.5rem;
}
.value-card {
  background: var(--black2);
  border: 1px solid var(--yline);
  border-radius: 6px;
  padding: 2rem 2rem 2.5rem;
  position: relative;
  overflow: hidden;
  transition: background 0.2s, border-color 0.2s, transform 0.2s;
}
.value-card:hover {
  background: var(--black3);
  border-color: rgba(255,214,0,0.45);
  transform: translateY(-4px);
}
.value-card::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 2px;
  background: var(--yellow);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s;
}
.value-card:hover::after { transform: scaleX(1); }
.value-icon {
  width: 48px; height: 48px;
  background: var(--ydim);
  border: 1px solid var(--yline);
  border-radius: 4px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 1.25rem;
}
.value-num {
  font-family: var(--display);
  font-size: 2.5rem;
  color: var(--yellow);
  line-height: 1;
  margin-bottom: 0.25rem;
}
.value-title {
  font-weight: 600;
  font-size: 1rem;
  color: var(--white);
  margin-bottom: 0.625rem;
  letter-spacing: -0.01em;
}
.value-desc {
  font-size: 0.875rem;
  color: var(--grey);
  line-height: 1.7;
}

/* ── PRODUCTS ── */
.products-section {
  padding: 0 0 5rem;
  background: var(--black2);
}
.products-header {
  padding: 5rem 5vw 2.5rem;
}
.products-grid {
  padding: 0 5vw;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}
.products-grid-3 {
  padding: 0 5vw;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 16px;
  margin-top: 16px;
}
.product-card {
  background: var(--black);
  border: 1px solid var(--yline);
  border-radius: 6px;
  padding: 2rem 2.25rem 2.5rem;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s, border-color 0.2s;
  cursor: default;
}
.product-card:hover {
  transform: translateY(-3px);
  border-color: rgba(255,214,0,0.5);
}
.product-card.featured {
  border-color: var(--yellow);
  background: var(--ydim);
}
.product-tag {
  font-family: var(--mono);
  font-size: 0.58rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--yellow);
  background: var(--ydim);
  border: 1px solid var(--yline);
  padding: 0.2rem 0.6rem;
  border-radius: 2px;
  display: inline-block;
  margin-bottom: 1rem;
}
.product-tag.featured-tag {
  background: var(--yellow);
  color: var(--black);
  border-color: var(--yellow);
}
.product-name {
  font-family: var(--display);
  font-size: 1.75rem;
  color: var(--white);
  letter-spacing: 0.02em;
  margin-bottom: 0.5rem;
  line-height: 1.1;
}
.product-desc {
  font-size: 0.875rem;
  color: var(--grey);
  line-height: 1.7;
  margin-bottom: 1.25rem;
}
.product-features {
  list-style: none;
  padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: 0.375rem;
}
.product-features li {
  font-size: 0.8125rem;
  color: var(--grey);
  display: flex; align-items: center; gap: 0.5rem;
}
.product-features li::before {
  content: '▸';
  color: var(--yellow);
  font-size: 0.7rem;
}
.product-corner {
  position: absolute;
  top: 16px; right: 16px;
  font-size: 2rem;
  opacity: 0.15;
}

/* ── HOW IT WORKS ── */
.how-section {
  padding: 5rem 5vw;
}
.steps-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
  margin-top: 3rem;
  position: relative;
}
.steps-grid::before {
  content: '';
  position: absolute;
  top: 32px; left: calc(12.5% + 16px); right: calc(12.5% + 16px);
  height: 1px;
  background: var(--yline);
  z-index: 0;
}
.step {
  padding: 0 1.5rem;
  position: relative;
  z-index: 1;
}
.step-num {
  width: 64px; height: 64px;
  background: var(--black2);
  border: 1px solid var(--yellow);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--display);
  font-size: 1.5rem;
  color: var(--yellow);
  margin-bottom: 1.25rem;
}
.step-title {
  font-weight: 600;
  font-size: 0.9375rem;
  color: var(--white);
  margin-bottom: 0.5rem;
  letter-spacing: -0.01em;
}
.step-desc {
  font-size: 0.8125rem;
  color: var(--grey);
  line-height: 1.7;
}

/* ── CLIENTS ── */
.clients-section {
  padding: 5rem 5vw;
  background: var(--black2);
  border-top: 1px solid var(--yline);
}
.clients-label {
  font-family: var(--mono);
  font-size: 0.58rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: var(--grey);
  text-align: center;
  margin-bottom: 2.5rem;
}
.clients-logos {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
  align-items: center;
}
.client-chip {
  background: var(--black);
  border: 1px solid var(--yline);
  border-radius: 4px;
  padding: 0.625rem 1.25rem;
  font-family: var(--mono);
  font-size: 0.7rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--grey);
  transition: border-color 0.2s, color 0.2s;
}
.client-chip:hover {
  border-color: var(--yellow);
  color: var(--yellow);
}

/* ── TESTIMONIALS ── */
.testimonials-section {
  padding: 5rem 5vw;
}
.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-top: 2.5rem;
}
.testimonial-card {
  background: var(--black2);
  border: 1px solid var(--yline);
  border-radius: 6px;
  padding: 2rem;
}
.testimonial-quote {
  font-size: 2rem;
  color: var(--yellow);
  line-height: 1;
  margin-bottom: 0.75rem;
  font-family: var(--display);
}
.testimonial-text {
  font-size: 0.9375rem;
  color: var(--white);
  line-height: 1.75;
  margin-bottom: 1.5rem;
  font-style: italic;
}
.testimonial-author {
  font-weight: 600;
  font-size: 0.875rem;
  color: var(--white);
}
.testimonial-role {
  font-family: var(--mono);
  font-size: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--grey);
  margin-top: 0.25rem;
}

/* ── CTA ── */
.cta-section {
  padding: 6rem 5vw;
  background: var(--yellow);
  position: relative;
  overflow: hidden;
  text-align: center;
}
.cta-section::before {
  content: '';
  position: absolute;
  top: -60px; left: 50%;
  transform: translateX(-50%);
  width: 400px; height: 400px;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 50%;
  pointer-events: none;
}
.cta-section::after {
  content: '';
  position: absolute;
  top: 20px; left: 50%;
  transform: translateX(-50%);
  width: 250px; height: 250px;
  border: 1px solid rgba(0,0,0,0.06);
  border-radius: 50%;
  pointer-events: none;
}
.cta-eyebrow {
  font-family: var(--mono);
  font-size: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.22em;
  color: rgba(0,0,0,0.5);
  margin-bottom: 1rem;
}
.cta-headline {
  font-family: var(--display);
  font-size: clamp(2.5rem, 6vw, 5.5rem);
  color: var(--black);
  line-height: 0.92;
  letter-spacing: 0.01em;
  margin-bottom: 1.25rem;
  position: relative;
  z-index: 1;
}
.cta-sub {
  font-size: 1.0625rem;
  color: rgba(0,0,0,0.65);
  max-width: 480px;
  margin: 0 auto 2.5rem;
  line-height: 1.7;
  position: relative;
  z-index: 1;
}
.cta-actions {
  display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;
  position: relative; z-index: 1;
}
.btn-dark {
  background: var(--black);
  color: var(--yellow);
  padding: 0.9375rem 2.25rem;
  font-weight: 600;
  font-size: 1rem;
  border-radius: 3px;
  text-decoration: none;
  transition: background 0.2s, transform 0.15s;
  display: inline-block;
}
.btn-dark:hover {
  background: var(--black2);
  transform: translateY(-2px);
}
.btn-ghost-dark {
  background: transparent;
  color: var(--black);
  padding: 0.9375rem 2.25rem;
  font-weight: 500;
  font-size: 1rem;
  border: 1.5px solid rgba(0,0,0,0.3);
  border-radius: 3px;
  text-decoration: none;
  transition: border-color 0.2s, transform 0.15s;
  display: inline-block;
}
.btn-ghost-dark:hover {
  border-color: var(--black);
  transform: translateY(-2px);
}

/* ── FOOTER ── */
.footer {
  background: var(--black);
  border-top: 1px solid var(--yline);
  padding: 4rem 5vw 2.5rem;
}
.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 3rem;
  margin-bottom: 3rem;
}
.footer-brand-name {
  font-family: var(--display);
  font-size: 1.75rem;
  color: var(--white);
  letter-spacing: 0.05em;
  margin-bottom: 0.75rem;
}
.footer-brand-desc {
  font-size: 0.875rem;
  color: var(--grey);
  line-height: 1.7;
  max-width: 280px;
}
.footer-col-title {
  font-family: var(--mono);
  font-size: 0.58rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--yellow);
  margin-bottom: 1rem;
}
.footer-links {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: 0.5rem;
}
.footer-links li a {
  font-size: 0.875rem;
  color: var(--grey);
  text-decoration: none;
  transition: color 0.2s;
}
.footer-links li a:hover { color: var(--yellow); }
.footer-bottom {
  border-top: 1px solid var(--yline);
  padding-top: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--mono);
  font-size: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--grey);
}

/* ── DIVIDER ── */
.geo-divider {
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--yellow) 30%, var(--yellow) 70%, transparent);
  opacity: 0.3;
}

/* hide streamlit chrome */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-thumb { background: var(--yline); border-radius: 3px; }
::-webkit-scrollbar-track { background: var(--black); }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# NAV
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav">
  <div class="nav-logo">
    <div class="nav-mark"></div>
    <span class="nav-name">HELDEN</span>
  </div>
  <div class="nav-links">
    <a href="#products">Producten</a>
    <a href="#how">Hoe het werkt</a>
    <a href="#clients">Klanten</a>
    <a href="#contact">Contact</a>
  </div>
  <a class="nav-cta" href="https://helden-inc.com" target="_blank">Plan een demo →</a>
</nav>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TICKER
# ─────────────────────────────────────────────────────────────────────────────
ticker_items = [
    "FutureGame", "Escape Room", "Onboarding Game", "Learning Events",
    "GamePlan", "Micro Learning", "Escape Box", "In-Company Training",
    "Custom Games", "Live Events",
]
ticker_html = "".join(
    f'<span class="ticker-item">{item}<span class="ticker-dot"> ◆ </span></span>'
    for item in ticker_items * 4
)
st.markdown(f"""
<div class="ticker-wrap">
  <div class="ticker-track">{ticker_html}</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────
# Build game board cells
cells = []
lit_positions = {6, 13, 14, 20, 21, 22, 27, 28, 29, 30}
bright_positions = {14, 22}
for i in range(35):
    cls = "game-cell"
    if i in bright_positions:
        cls += " bright"
    elif i in lit_positions:
        cls += " lit"
    cells.append(f'<div class="{cls}"></div>')
cells_html = "\n".join(cells)

st.markdown(f"""
<section class="hero">
  <div class="hero-content">
    <div class="hero-eyebrow">Gamified Internal Communication</div>
    <h1 class="hero-headline">
      Workshops<br>zijn<br><span>verleden</span><br>tijd.
    </h1>
    <p class="hero-sub">
      Helden vervangt saaie presentaties en workshops door meeslepende
      gamified ervaringen. Échte verandering, échte betrokkenheid.
    </p>
    <div class="hero-actions">
      <a class="btn-primary" href="https://helden-inc.com" target="_blank">Plan een demo →</a>
      <a class="btn-outline" href="#products">Bekijk producten</a>
    </div>
  </div>

  <div class="hero-visual">
    <div class="game-board">
      {cells_html}
    </div>
    <div class="board-card top-right">
      <div class="board-card-num">200+</div>
      <div class="board-card-label">Enterprise clients</div>
    </div>
    <div class="board-card bottom-left">
      <div class="board-card-num">9</div>
      <div class="board-card-label">Game products</div>
    </div>
    <div class="floating-badge pos1">▶ FUTUREGAME LIVE</div>
    <div class="floating-badge pos2">🔓 ESCAPE ROOM</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-section">
  <div class="stat-item">
    <div class="stat-num">200+</div>
    <div class="stat-label">Enterprise Klanten</div>
    <div class="stat-desc">Heineken, KLM, ING, Disney, EY &amp; meer</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">9</div>
    <div class="stat-label">Game Producten</div>
    <div class="stat-desc">Van escape rooms tot micro learning</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">98%</div>
    <div class="stat-label">Tevredenheid</div>
    <div class="stat-desc">Deelnemers beoordelen met 9+ gemiddeld</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">15+</div>
    <div class="stat-label">Jaar Ervaring</div>
    <div class="stat-desc">Pionier in gamified communicatie</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# VALUE PROPS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div id="value">
  <div class="section-header">
    <div class="section-eyebrow">Waarom Helden</div>
    <h2 class="section-title">Van weerstand<br>naar <span>draagvlak</span>.</h2>
    <p class="section-sub">
      Mensen leren en veranderen niet door presentaties te ondergaan.
      Ze veranderen door zelf te doen, te ervaren, te spelen.
    </p>
  </div>
  <div class="value-section">
    <div class="value-grid">
      <div class="value-card">
        <div class="value-icon">🎯</div>
        <div class="value-num">3×</div>
        <div class="value-title">Hogere Retentie</div>
        <div class="value-desc">
          Gamified leren zorgt voor driemaal hogere kennisretentie
          dan traditionele workshops. Boodschappen beklijven.
        </div>
      </div>
      <div class="value-card">
        <div class="value-icon">⚡</div>
        <div class="value-num">100%</div>
        <div class="value-title">Actieve Betrokkenheid</div>
        <div class="value-desc">
          Geen passieve deelnemers meer. Iedereen speelt mee,
          beslist mee en voelt de impact van hun keuzes.
        </div>
      </div>
      <div class="value-card">
        <div class="value-icon">🔄</div>
        <div class="value-num">−60%</div>
        <div class="value-title">Minder Weerstand</div>
        <div class="value-desc">
          Veranderingen die via games worden geïntroduceerd stuiten
          op aanzienlijk minder weerstand dan top-down communicatie.
        </div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="geo-divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PRODUCTS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="products-section" id="products">
  <div class="products-header">
    <div class="section-eyebrow">Producten</div>
    <h2 class="section-title">Negen manieren om<br>je team te <span>raken</span>.</h2>
    <p class="section-sub">
      Elk product is ontworpen voor een specifieke uitdaging —
      van onboarding tot strategische verandering.
    </p>
  </div>

  <div class="products-grid">
    <div class="product-card featured">
      <div class="product-tag featured-tag">Bestseller</div>
      <div class="product-corner">🎮</div>
      <div class="product-name">FutureGame</div>
      <div class="product-desc">
        Dé interactieve simulatie voor strategische dialoog. Teams ervaren de toekomst
        van hun organisatie in een veilige, speelse omgeving.
      </div>
      <ul class="product-features">
        <li>Strategie & change management</li>
        <li>4–200 deelnemers</li>
        <li>Halve of hele dag</li>
        <li>Volledig op maat te maken</li>
      </ul>
    </div>
    <div class="product-card">
      <div class="product-tag">Live Experience</div>
      <div class="product-corner">🔐</div>
      <div class="product-name">Escape Room on Location</div>
      <div class="product-desc">
        Een professionele escape room direct bij jou op locatie.
        Teambuilding, thema's en leerdoelen naadloos gecombineerd.
      </div>
      <ul class="product-features">
        <li>Teambuilding & samenwerking</li>
        <li>5–500 deelnemers</li>
        <li>Op maat inhoudelijk thema</li>
        <li>Op locatie, volledig verzorgd</li>
      </ul>
    </div>
  </div>

  <div class="products-grid-3">
    <div class="product-card">
      <div class="product-tag">Digital</div>
      <div class="product-corner">📱</div>
      <div class="product-name">Escape Box</div>
      <div class="product-desc">
        Een fysieke doos vol puzzels en uitdagingen.
        Perfect voor hybride teams of thuiswerkers.
      </div>
      <ul class="product-features">
        <li>Hybride &amp; remote teams</li>
        <li>Per persoon thuis bezorgd</li>
        <li>Eigen branding mogelijk</li>
      </ul>
    </div>
    <div class="product-card">
      <div class="product-tag">Onboarding</div>
      <div class="product-corner">🚀</div>
      <div class="product-name">Onboarding Game</div>
      <div class="product-desc">
        Nieuwe medewerkers leren de organisatie kennen via een
        meeslepend spel. Sneller ingewerkt, beter verbonden.
      </div>
      <ul class="product-features">
        <li>Cultuur &amp; waarden overbrengen</li>
        <li>Schaalbaar voor grote groepen</li>
        <li>Digitaal of fysiek</li>
      </ul>
    </div>
    <div class="product-card">
      <div class="product-tag">Continu Leren</div>
      <div class="product-corner">⚡</div>
      <div class="product-name">Micro Learning</div>
      <div class="product-desc">
        Korte, krachtige leermodules die medewerkers op het
        juiste moment de juiste kennis geven.
      </div>
      <ul class="product-features">
        <li>5–15 minuten per module</li>
        <li>Mobiel-first design</li>
        <li>Geïntegreerd in bestaand LMS</li>
      </ul>
    </div>
  </div>

  <div style="padding: 2rem 5vw 0; display:flex; gap:1rem; flex-wrap:wrap;">
    <div class="product-card" style="flex:1; min-width:200px;">
      <div class="product-tag">Planning</div>
      <div class="product-name" style="font-size:1.25rem;">GamePlan</div>
      <div class="product-desc" style="font-size:0.8125rem;">Strategiesessies als interactief spel.</div>
    </div>
    <div class="product-card" style="flex:1; min-width:200px;">
      <div class="product-tag">Training</div>
      <div class="product-name" style="font-size:1.25rem;">In-Company Training Box</div>
      <div class="product-desc" style="font-size:0.8125rem;">Herbruikbare game voor interne trainers.</div>
    </div>
    <div class="product-card" style="flex:1; min-width:200px;">
      <div class="product-tag">Custom</div>
      <div class="product-name" style="font-size:1.25rem;">Custom Escape Room</div>
      <div class="product-desc" style="font-size:0.8125rem;">Volledig op maat gebouwde experience.</div>
    </div>
    <div class="product-card" style="flex:1; min-width:200px;">
      <div class="product-tag">Events</div>
      <div class="product-name" style="font-size:1.25rem;">Learning Events</div>
      <div class="product-desc" style="font-size:0.8125rem;">Grote groepen, grote impact.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# HOW IT WORKS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="how-section" id="how">
  <div class="section-eyebrow">Hoe het werkt</div>
  <h2 class="section-title">Van brief tot<br><span>wow-moment</span>.</h2>
  <div class="steps-grid">
    <div class="step">
      <div class="step-num">01</div>
      <div class="step-title">Intake & Briefing</div>
      <div class="step-desc">
        We starten met een diepgaand gesprek. Wat is de uitdaging?
        Welke doelen wil je bereiken? Wie zijn de deelnemers?
      </div>
    </div>
    <div class="step">
      <div class="step-num">02</div>
      <div class="step-title">Game Design</div>
      <div class="step-desc">
        Ons team ontwerpt de game-experience op maat.
        Mechanics, verhaal, leerdoelen — alles afgestemd.
      </div>
    </div>
    <div class="step">
      <div class="step-num">03</div>
      <div class="step-title">Live Uitvoering</div>
      <div class="step-desc">
        We verzorgen de volledige uitvoering, inclusief
        professionele game masters en materiaal.
      </div>
    </div>
    <div class="step">
      <div class="step-num">04</div>
      <div class="step-title">Impact & Follow-up</div>
      <div class="step-desc">
        Na afloop meten we de impact en leveren we een
        gedetailleerd rapport met inzichten en actiepunten.
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="geo-divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# CLIENTS
# ─────────────────────────────────────────────────────────────────────────────
clients = [
    "Heineken", "KLM", "ING", "ABN AMRO", "EY", "Schiphol",
    "L'Oréal", "Disney", "BMW", "Deloitte", "Shell", "Philips",
    "KPMG", "Unilever", "Randstad", "Accenture",
]
client_chips = "".join(f'<span class="client-chip">{c}</span>' for c in clients)

st.markdown(f"""
<div class="clients-section" id="clients">
  <div class="clients-label">Vertrouwd door meer dan 200 toonaangevende organisaties</div>
  <div class="clients-logos">
    {client_chips}
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TESTIMONIALS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="testimonials-section">
  <div class="section-eyebrow">Ervaringen</div>
  <h2 class="section-title">Wat onze klanten<br><span>zeggen</span>.</h2>
  <div class="testimonials-grid">
    <div class="testimonial-card">
      <div class="testimonial-quote">"</div>
      <div class="testimonial-text">
        De FutureGame heeft onze strategie-dag volledig getransformeerd.
        Medewerkers die normaal achterin zitten waren ineens de eersten om
        mee te denken. Ongelofelijk wat een game kan doen.
      </div>
      <div class="testimonial-author">Marieke van den Berg</div>
      <div class="testimonial-role">HR Director · Heineken</div>
    </div>
    <div class="testimonial-card">
      <div class="testimonial-quote">"</div>
      <div class="testimonial-text">
        We zochten een manier om onze nieuwe strategie te communiceren
        zonder de zoveelste PowerPoint. Helden leverde een ervaring die
        maanden later nog steeds nawerkt bij ons team.
      </div>
      <div class="testimonial-author">Thomas Akkerman</div>
      <div class="testimonial-role">Directeur Communicatie · ING</div>
    </div>
    <div class="testimonial-card">
      <div class="testimonial-quote">"</div>
      <div class="testimonial-text">
        De escape room op onze locatie was een revelation. Collega's die
        elkaar al jaren kennen ontdekten nieuwe kanten van zichzelf.
        Investering die zich tienvoudig terugbetaalt.
      </div>
      <div class="testimonial-author">Sophie Lemmens</div>
      <div class="testimonial-role">L&amp;D Manager · Schiphol</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# CTA
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-section" id="contact">
  <div class="cta-eyebrow">Klaar om te starten?</div>
  <h2 class="cta-headline">Maak van je<br>volgende event<br>een ervaring.</h2>
  <p class="cta-sub">
    Plan een vrijblijvende demo en ontdek welke game het beste
    past bij jouw organisatie en doelstellingen.
  </p>
  <div class="cta-actions">
    <a class="btn-dark" href="https://helden-inc.com" target="_blank">Plan een demo →</a>
    <a class="btn-ghost-dark" href="mailto:hello@helden-inc.com">Stuur een e-mail</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="footer">
  <div class="footer-grid">
    <div>
      <div class="footer-brand-name">HELDEN</div>
      <div class="footer-brand-desc">
        Helden Inc. is pionier in gamified interne communicatie.
        Gevestigd in Haarlem, actief door heel Nederland en Europa.
      </div>
      <div style="margin-top:1.5rem;font-family:var(--mono);font-size:0.58rem;
                  color:var(--grey);letter-spacing:0.08em;">
        📍 Haarlem, Nederland
      </div>
    </div>
    <div>
      <div class="footer-col-title">Producten</div>
      <ul class="footer-links">
        <li><a href="#">FutureGame</a></li>
        <li><a href="#">Escape Room</a></li>
        <li><a href="#">Onboarding Game</a></li>
        <li><a href="#">Micro Learning</a></li>
        <li><a href="#">GamePlan</a></li>
        <li><a href="#">Escape Box</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Bedrijf</div>
      <ul class="footer-links">
        <li><a href="#">Over Helden</a></li>
        <li><a href="#">Ons team</a></li>
        <li><a href="#">Cases</a></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#">Werken bij Helden</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Contact</div>
      <ul class="footer-links">
        <li><a href="https://helden-inc.com" target="_blank">helden-inc.com</a></li>
        <li><a href="mailto:hello@helden-inc.com">hello@helden-inc.com</a></li>
        <li><a href="#">Plan een demo</a></li>
        <li><a href="#">LinkedIn</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2025 Helden Inc. · Haarlem</span>
    <span>Gamified Internal Communication</span>
    <span>Made with ♟ by Helden</span>
  </div>
</footer>
""", unsafe_allow_html=True)
