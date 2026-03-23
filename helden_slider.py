"""
Helden Inc. — Cinematic Slider Experience
Fullscreen slide-based storytelling. Inspired by Orano's innovation page.
Deploy: GitHub → Streamlit Cloud
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Helden Inc.",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip ALL Streamlit chrome so the iframe fills the screen
st.markdown("""
<style>
html,body{margin:0;padding:0;overflow:hidden;background:#08080a;}
.stApp{background:#08080a!important;overflow:hidden;}
.block-container{padding:0!important;max-width:100vw!important;overflow:hidden;}
#MainMenu,header,footer,
[data-testid="stDecoration"],
[data-testid="stToolbar"],
[data-testid="stHeader"],
[data-testid="stStatusWidget"]{display:none!important;}
iframe{border:none!important;display:block!important;}
section[data-testid="stMain"]{padding:0!important;}
div[data-testid="stVerticalBlock"]{gap:0!important;}
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Helden Inc.</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=Sora:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
:root{
  --black:#08080a;
  --dark:#0e0e12;
  --card:#131318;
  --y:#FFD600;
  --ydim:rgba(255,214,0,.10);
  --yline:rgba(255,214,0,.18);
  --white:#f2ede6;
  --grey:#5a5a6e;
  --grey2:#2a2a38;
  --serif:'Cormorant Garamond',Georgia,serif;
  --sans:'Sora',system-ui,sans-serif;
  --mono:'DM Mono',monospace;
  --dur:900ms;
  --ease:cubic-bezier(0.77,0,0.175,1);
}
html,body{
  width:100%;height:100%;overflow:hidden;
  background:var(--black);color:var(--white);
  -webkit-font-smoothing:antialiased;
}

/* ── SLIDER CONTAINER ── */
#slider{
  width:100vw;height:100vh;
  position:relative;overflow:hidden;
}
.slide{
  position:absolute;inset:0;
  display:flex;align-items:center;justify-content:center;
  opacity:0;
  transform:translateY(60px);
  pointer-events:none;
  transition:
    opacity var(--dur) var(--ease),
    transform var(--dur) var(--ease);
  will-change:opacity,transform;
}
.slide.active{
  opacity:1;transform:translateY(0);pointer-events:all;
}
.slide.exit-up{
  opacity:0;transform:translateY(-60px);
}
.slide.exit-down{
  opacity:0;transform:translateY(60px);
}

/* ── NAV DOTS ── */
#nav-dots{
  position:fixed;right:28px;top:50%;transform:translateY(-50%);
  z-index:100;display:flex;flex-direction:column;gap:10px;
}
.dot{
  width:6px;height:6px;border-radius:50%;
  background:var(--grey2);
  border:1px solid var(--grey);
  cursor:pointer;
  transition:background .3s,transform .3s,border-color .3s;
}
.dot.active{background:var(--y);border-color:var(--y);transform:scale(1.4);}

/* ── COUNTER ── */
#counter{
  position:fixed;bottom:32px;right:36px;
  font-family:var(--mono);font-size:.6rem;
  color:var(--grey);letter-spacing:.18em;
  z-index:100;
  transition:opacity .3s;
}
#counter span{color:var(--white);}

/* ── ARROW HINT ── */
#arrow-hint{
  position:fixed;bottom:32px;left:50%;transform:translateX(-50%);
  display:flex;flex-direction:column;align-items:center;gap:6px;
  z-index:100;
  transition:opacity .6s;
}
#arrow-hint svg{animation:arrowBounce 2s ease infinite;}
#arrow-hint p{
  font-family:var(--mono);font-size:.55rem;
  letter-spacing:.22em;text-transform:uppercase;color:var(--grey);
}
@keyframes arrowBounce{
  0%,100%{transform:translateY(0);}
  50%{transform:translateY(5px);}
}

/* ── LOGO (fixed) ── */
#logo{
  position:fixed;top:28px;left:36px;z-index:100;
  display:flex;align-items:center;gap:10px;
}
.logo-hex{
  width:28px;height:28px;background:var(--y);
  clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
  flex-shrink:0;
}
.logo-text{
  font-family:var(--mono);font-size:.65rem;
  letter-spacing:.28em;text-transform:uppercase;
  color:var(--white);
}
/* hide logo on yellow slide */
.logo-dark .logo-hex{background:var(--black);}
.logo-dark .logo-text{color:var(--black);}

/* ── NOISE OVERLAY ── */
#noise{
  position:fixed;inset:0;z-index:200;pointer-events:none;
  opacity:.028;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* ═══════════════════════════════════
   SLIDE 1 — HERO
═══════════════════════════════════ */
#s1{background:var(--black);}
.s1-bg{
  position:absolute;inset:0;overflow:hidden;
}
.s1-hex-grid{
  position:absolute;inset:-10%;
  opacity:.04;
  background-image:
    radial-gradient(circle, rgba(255,214,0,.6) 1px, transparent 1px);
  background-size:48px 48px;
}
.s1-glow{
  position:absolute;
  bottom:-20%;left:50%;transform:translateX(-50%);
  width:60vw;height:40vh;
  background:radial-gradient(ellipse, rgba(255,214,0,.05) 0%, transparent 65%);
  pointer-events:none;
}
.s1-inner{
  position:relative;z-index:2;
  text-align:center;
  padding:0 6vw;
}
.s1-label{
  font-family:var(--mono);
  font-size:.6rem;letter-spacing:.32em;text-transform:uppercase;
  color:var(--y);opacity:.7;
  margin-bottom:2.5rem;
}
.s1-headline{
  font-family:var(--serif);
  font-size:clamp(4rem,11vw,11.5rem);
  font-weight:300;font-style:italic;
  line-height:.88;
  letter-spacing:-.01em;
  color:var(--white);
}
.s1-headline em{
  font-style:normal;font-weight:600;
  color:var(--y);
}
.s1-sub{
  font-family:var(--sans);
  font-size:clamp(.875rem,1.1vw,1.1rem);
  font-weight:300;
  color:var(--grey);
  letter-spacing:.04em;
  margin-top:2.5rem;
}

/* ═══════════════════════════════════
   SLIDE 2 — THE PROBLEM
═══════════════════════════════════ */
#s2{background:var(--black);}
.s2-inner{
  width:90vw;max-width:1200px;
  display:grid;grid-template-columns:1fr 1fr;
  gap:8vw;align-items:center;
  padding:0 2vw;
}
.s2-left{
  position:relative;
}
.s2-num{
  font-family:var(--serif);
  font-size:clamp(8rem,20vw,22rem);
  font-weight:300;
  line-height:.85;
  color:var(--white);
  letter-spacing:-.04em;
}
.s2-num sup{
  font-size:.3em;vertical-align:super;
  color:var(--grey);
}
.s2-num-label{
  font-family:var(--mono);
  font-size:.58rem;letter-spacing:.22em;text-transform:uppercase;
  color:var(--y);margin-top:1.5rem;
  display:block;
}
.s2-line{
  position:absolute;
  top:0;bottom:0;right:-4vw;
  width:1px;background:var(--grey2);
}
.s2-right{}
.s2-section-tag{
  font-family:var(--mono);font-size:.56rem;
  letter-spacing:.22em;text-transform:uppercase;
  color:var(--grey);margin-bottom:1.75rem;
  display:flex;align-items:center;gap:.75rem;
}
.s2-section-tag::before{
  content:'';width:20px;height:1px;background:var(--grey);
}
.s2-headline{
  font-family:var(--serif);
  font-size:clamp(1.75rem,3.2vw,3.5rem);
  font-weight:400;
  line-height:1.15;
  color:var(--white);
  letter-spacing:-.01em;
  margin-bottom:1.5rem;
}
.s2-body{
  font-family:var(--sans);
  font-size:clamp(.875rem,1vw,1rem);
  font-weight:300;
  color:var(--grey);
  line-height:1.8;
}

/* ═══════════════════════════════════
   SLIDE 3 — THE INSIGHT
═══════════════════════════════════ */
#s3{background:var(--dark);}
.s3-inner{
  text-align:center;
  padding:0 8vw;
  max-width:900px;
}
.s3-section-tag{
  font-family:var(--mono);font-size:.56rem;
  letter-spacing:.22em;text-transform:uppercase;
  color:var(--grey);margin-bottom:3rem;
}
.s3-line1{
  font-family:var(--serif);
  font-size:clamp(2.5rem,5.5vw,6rem);
  font-weight:300;
  line-height:1.05;
  color:var(--grey);
  letter-spacing:-.01em;
  margin-bottom:1rem;
}
.s3-line2{
  font-family:var(--serif);
  font-size:clamp(2.5rem,5.5vw,6rem);
  font-weight:300;
  line-height:1.05;
  color:var(--white);
  letter-spacing:-.01em;
  font-style:italic;
}
.s3-line2 strong{
  color:var(--y);font-weight:600;font-style:normal;
}
.s3-divider{
  width:48px;height:1px;background:var(--yline);
  margin:2.5rem auto;
}
.s3-sub{
  font-family:var(--sans);
  font-size:clamp(.8rem,.95vw,.95rem);
  font-weight:300;color:var(--grey);
  line-height:1.8;letter-spacing:.02em;
}

/* ═══════════════════════════════════
   SLIDE 4 — SOLUTION STATEMENT
═══════════════════════════════════ */
#s4{background:var(--black);}
.s4-bg-glow{
  position:absolute;
  bottom:-10%;left:50%;transform:translateX(-50%);
  width:80vw;height:60vh;
  background:radial-gradient(ellipse, rgba(255,214,0,.04) 0%, transparent 65%);
}
.s4-inner{
  position:relative;z-index:2;
  text-align:center;padding:0 6vw;
}
.s4-eyebrow{
  font-family:var(--mono);font-size:.58rem;
  letter-spacing:.3em;text-transform:uppercase;
  color:var(--y);opacity:.8;margin-bottom:2rem;
}
.s4-headline{
  font-family:var(--serif);
  font-size:clamp(3rem,8.5vw,9.5rem);
  font-weight:300;
  line-height:.9;
  color:var(--white);
  letter-spacing:-.015em;
}
.s4-headline .accent{
  font-style:italic;color:var(--y);
}
.s4-sub{
  font-family:var(--sans);
  font-size:clamp(.875rem,1.1vw,1.1rem);
  font-weight:300;color:var(--grey);
  line-height:1.8;letter-spacing:.02em;
  max-width:560px;margin:2.5rem auto 0;
}

/* ═══════════════════════════════════
   SLIDE 5 — FUTUREGAME
═══════════════════════════════════ */
#s5{background:var(--black);}
.s5-bg{
  position:absolute;inset:0;overflow:hidden;
}
.s5-grid{
  position:absolute;inset:0;
  display:grid;
  grid-template-columns:repeat(12,1fr);
  grid-template-rows:repeat(8,1fr);
  gap:6px;padding:6px;
  opacity:.06;
}
.s5-cell{background:var(--y);border-radius:2px;}
.s5-glow{
  position:absolute;top:10%;right:5%;
  width:50vw;height:70vh;
  background:radial-gradient(ellipse, rgba(255,214,0,.06) 0%, transparent 60%);
}
.s5-inner{
  position:relative;z-index:2;
  width:90vw;max-width:1200px;
  display:grid;grid-template-columns:1fr 1fr;
  gap:8vw;align-items:center;
}
.s5-left{}
.s5-tag{
  display:inline-flex;align-items:center;
  background:var(--y);color:var(--black);
  font-family:var(--mono);font-size:.56rem;
  letter-spacing:.14em;text-transform:uppercase;
  padding:.25rem .75rem;border-radius:2px;
  margin-bottom:1.5rem;
}
.s5-name{
  font-family:var(--serif);
  font-size:clamp(3rem,6.5vw,7.5rem);
  font-weight:600;
  line-height:.88;
  color:var(--white);
  letter-spacing:-.01em;
  margin-bottom:1.25rem;
}
.s5-desc{
  font-family:var(--sans);
  font-size:clamp(.875rem,1.1vw,1.1rem);
  font-weight:300;
  color:var(--grey);
  line-height:1.8;
  margin-bottom:2rem;
  max-width:420px;
}
.s5-features{
  list-style:none;
  display:flex;flex-direction:column;gap:.625rem;
}
.s5-features li{
  font-family:var(--sans);
  font-size:.875rem;
  color:var(--white);
  display:flex;align-items:center;gap:.75rem;
  font-weight:300;
}
.s5-features li::before{
  content:'';
  width:18px;height:1px;
  background:var(--y);flex-shrink:0;
}

/* Right side — game board visual */
.s5-right{
  position:relative;
  height:420px;
}
.game-board-vis{
  position:absolute;inset:0;
  display:grid;
  grid-template-columns:repeat(8,1fr);
  grid-template-rows:repeat(6,1fr);
  gap:5px;
}
.gv-cell{
  border-radius:3px;
  background:var(--card);
  border:1px solid rgba(255,214,0,.08);
  transition:background .4s,border-color .4s;
}
.gv-cell.glow{
  background:rgba(255,214,0,.12);
  border-color:rgba(255,214,0,.3);
}
.gv-cell.hot{
  background:rgba(255,214,0,.28);
  border-color:rgba(255,214,0,.6);
}
.gv-cell.bright{
  background:var(--y);
  border-color:var(--y);
}

/* ═══════════════════════════════════
   SLIDE 6 — PRODUCTEN GRID
═══════════════════════════════════ */
#s6{background:var(--dark);}
.s6-inner{
  width:90vw;max-width:1100px;
}
.s6-header{
  display:flex;align-items:flex-end;justify-content:space-between;
  margin-bottom:3rem;
  padding-bottom:1.5rem;
  border-bottom:1px solid var(--grey2);
}
.s6-title{
  font-family:var(--serif);
  font-size:clamp(2rem,4.5vw,5rem);
  font-weight:300;
  color:var(--white);
  line-height:.95;
  letter-spacing:-.01em;
}
.s6-title em{font-style:italic;color:var(--y);}
.s6-count{
  font-family:var(--mono);font-size:.58rem;
  letter-spacing:.18em;text-transform:uppercase;
  color:var(--grey);
}
.products-grid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:1px;
  background:var(--grey2);
  border:1px solid var(--grey2);
  border-radius:4px;
  overflow:hidden;
}
.prod-item{
  background:var(--dark);
  padding:1.5rem 1.75rem;
  transition:background .25s;
  cursor:default;
  position:relative;
  overflow:hidden;
}
.prod-item:hover{background:var(--card);}
.prod-item::after{
  content:'';
  position:absolute;
  bottom:0;left:0;right:0;
  height:2px;background:var(--y);
  transform:scaleX(0);transform-origin:left;
  transition:transform .3s;
}
.prod-item:hover::after{transform:scaleX(1);}
.prod-num{
  font-family:var(--mono);font-size:.52rem;
  text-transform:uppercase;letter-spacing:.18em;
  color:var(--grey);margin-bottom:.5rem;
}
.prod-name{
  font-family:var(--serif);
  font-size:clamp(1.1rem,1.6vw,1.7rem);
  font-weight:400;
  color:var(--white);
  line-height:1.2;
  letter-spacing:-.005em;
}
.prod-item.featured-prod .prod-name{color:var(--y);}

/* ═══════════════════════════════════
   SLIDE 7 — KLANTEN
═══════════════════════════════════ */
#s7{background:var(--black);}
.s7-inner{
  text-align:center;
  width:90vw;max-width:1000px;
}
.s7-label{
  font-family:var(--mono);font-size:.56rem;
  letter-spacing:.26em;text-transform:uppercase;
  color:var(--grey);margin-bottom:2rem;
}
.s7-num{
  font-family:var(--serif);
  font-size:clamp(5rem,14vw,16rem);
  font-weight:300;
  color:var(--white);
  line-height:.85;
  letter-spacing:-.04em;
  margin-bottom:.5rem;
}
.s7-num sup{
  font-size:.28em;vertical-align:super;color:var(--y);
}
.s7-sub{
  font-family:var(--serif);
  font-size:clamp(1rem,2vw,2rem);
  font-weight:300;font-style:italic;
  color:var(--grey);
  margin-bottom:3rem;
}
.clients-strip{
  display:flex;flex-wrap:wrap;gap:8px;
  justify-content:center;
}
.client-name{
  font-family:var(--mono);font-size:.58rem;
  letter-spacing:.14em;text-transform:uppercase;
  color:var(--grey);
  padding:.4rem .9rem;
  border:1px solid var(--grey2);
  border-radius:2px;
  transition:border-color .2s,color .2s;
}
.client-name:hover{border-color:var(--yline);color:var(--y);}

/* ═══════════════════════════════════
   SLIDE 8 — CTA
═══════════════════════════════════ */
#s8{background:var(--y);}
.s8-inner{
  text-align:center;
  padding:0 8vw;
  position:relative;z-index:2;
}
.s8-eyebrow{
  font-family:var(--mono);font-size:.58rem;
  letter-spacing:.3em;text-transform:uppercase;
  color:rgba(0,0,0,.4);margin-bottom:1.75rem;
}
.s8-headline{
  font-family:var(--serif);
  font-size:clamp(4rem,11vw,12rem);
  font-weight:300;font-style:italic;
  line-height:.88;
  color:var(--black);
  letter-spacing:-.02em;
  margin-bottom:2.5rem;
}
.s8-cta{
  display:inline-flex;align-items:center;gap:.75rem;
  background:var(--black);color:var(--y);
  font-family:var(--sans);font-size:.9375rem;font-weight:500;
  padding:.875rem 2.25rem;border-radius:3px;
  text-decoration:none;
  transition:background .2s,transform .15s;
}
.s8-cta:hover{background:#111;transform:translateY(-2px);}
.s8-cta svg{transition:transform .2s;}
.s8-cta:hover svg{transform:translateX(4px);}
.s8-domain{
  font-family:var(--mono);font-size:.6rem;
  letter-spacing:.2em;text-transform:uppercase;
  color:rgba(0,0,0,.35);margin-top:2.5rem;
}
/* circle bg decoration */
.s8-circle1{
  position:absolute;
  top:-40%;left:50%;transform:translateX(-50%);
  width:100vw;height:100vh;
  border-radius:50%;
  border:1px solid rgba(0,0,0,.06);
  pointer-events:none;
}
.s8-circle2{
  position:absolute;
  top:-20%;left:50%;transform:translateX(-50%);
  width:60vw;height:60vw;
  border-radius:50%;
  border:1px solid rgba(0,0,0,.04);
  pointer-events:none;
}

/* ── SLIDE ENTER ANIMATIONS ── */
.slide.active .anim-up{
  animation:elemUp .8s var(--ease) both;
}
.slide.active .anim-up:nth-child(1){animation-delay:.1s;}
.slide.active .anim-up:nth-child(2){animation-delay:.22s;}
.slide.active .anim-up:nth-child(3){animation-delay:.34s;}
.slide.active .anim-up:nth-child(4){animation-delay:.46s;}
.slide.active .anim-up:nth-child(5){animation-delay:.58s;}
@keyframes elemUp{
  from{opacity:0;transform:translateY(24px);}
  to{opacity:1;transform:translateY(0);}
}
.slide.active .anim-fade{
  animation:elemFade .9s var(--ease) both;
}
.slide.active .anim-fade:nth-child(1){animation-delay:.05s;}
.slide.active .anim-fade:nth-child(2){animation-delay:.18s;}
.slide.active .anim-fade:nth-child(3){animation-delay:.32s;}
.slide.active .anim-fade:nth-child(4){animation-delay:.46s;}
@keyframes elemFade{
  from{opacity:0;}to{opacity:1;}
}

/* ── PROGRESS LINE ── */
#progress-line{
  position:fixed;top:0;left:0;height:2px;
  background:var(--y);z-index:100;
  transition:width .6s var(--ease);
}
</style>
</head>
<body>

<div id="noise"></div>

<div id="logo">
  <div class="logo-hex"></div>
  <span class="logo-text">HELDEN</span>
</div>

<div id="progress-line" style="width:12.5%"></div>

<div id="nav-dots">
  <div class="dot active" data-slide="0"></div>
  <div class="dot" data-slide="1"></div>
  <div class="dot" data-slide="2"></div>
  <div class="dot" data-slide="3"></div>
  <div class="dot" data-slide="4"></div>
  <div class="dot" data-slide="5"></div>
  <div class="dot" data-slide="6"></div>
  <div class="dot" data-slide="7"></div>
</div>

<div id="counter"><span>01</span> / 08</div>

<div id="arrow-hint">
  <svg width="16" height="24" viewBox="0 0 16 24" fill="none">
    <path d="M8 2v20M1 15l7 7 7-7" stroke="rgba(255,255,255,.3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <p>scroll</p>
</div>

<div id="slider">

  <!-- ══ SLIDE 1 — HERO ══ -->
  <div class="slide active" id="s1">
    <div class="s1-bg">
      <div class="s1-hex-grid"></div>
      <div class="s1-glow"></div>
    </div>
    <div class="s1-inner">
      <div class="s1-label anim-fade">Helden Inc. · Gamified Internal Communication</div>
      <h1 class="s1-headline anim-fade">
        Workshops<br>zijn<br><em>verleden</em><br>tijd.
      </h1>
      <p class="s1-sub anim-fade">Haarlem · Nederland · 200+ enterprise clients</p>
    </div>
  </div>

  <!-- ══ SLIDE 2 — THE PROBLEM ══ -->
  <div class="slide" id="s2">
    <div class="s2-inner">
      <div class="s2-left">
        <div class="s2-num anim-up">10<sup>%</sup></div>
        <span class="s2-num-label anim-up">Geheugenretentie na een presentatie</span>
        <div class="s2-line"></div>
      </div>
      <div class="s2-right">
        <div class="s2-section-tag anim-fade">Het probleem</div>
        <h2 class="s2-headline anim-fade">
          Uw team onthoudt<br>bijna niets van<br>wat ze horen.
        </h2>
        <p class="s2-body anim-fade">
          Traditionele workshops en presentaties genereren passieve deelname.
          Mensen zijn er — maar hun aandacht is ergens anders.
        </p>
      </div>
    </div>
  </div>

  <!-- ══ SLIDE 3 — THE INSIGHT ══ -->
  <div class="slide" id="s3">
    <div class="s3-inner">
      <div class="s3-section-tag anim-fade">Het inzicht</div>
      <p class="s3-line1 anim-up">Mensen leren niet<br>door te kijken.</p>
      <p class="s3-line2 anim-up">Mensen leren door<br>te <strong>spelen</strong>.</p>
      <div class="s3-divider anim-fade"></div>
      <p class="s3-sub anim-fade">
        Gamified ervaringen verhogen kennisretentie met 300% en creëren
        betrokkenheid die weken nawerkt.
      </p>
    </div>
  </div>

  <!-- ══ SLIDE 4 — SOLUTION ══ -->
  <div class="slide" id="s4">
    <div class="s4-bg-glow"></div>
    <div class="s4-inner">
      <p class="s4-eyebrow anim-fade">De oplossing</p>
      <h2 class="s4-headline anim-up">
        Gamified<br><span class="accent">Internal</span><br>Communication
      </h2>
      <p class="s4-sub anim-fade">
        Wij vervangen de workshop door de ervaring.<br>
        Van strategiesessie tot onboarding — altijd als spel.
      </p>
    </div>
  </div>

  <!-- ══ SLIDE 5 — FUTUREGAME ══ -->
  <div class="slide" id="s5">
    <div class="s5-bg">
      <div class="s5-grid" id="gamegrid"></div>
      <div class="s5-glow"></div>
    </div>
    <div class="s5-inner">
      <div class="s5-left">
        <span class="s5-tag anim-fade">Bestseller</span>
        <h2 class="s5-name anim-up">Future<br>Game</h2>
        <p class="s5-desc anim-fade">
          De interactieve strategiesimulatie die uw organisatie
          de toekomst laat ervaren — niet bespreken.
        </p>
        <ul class="s5-features anim-fade">
          <li>Strategie & change management</li>
          <li>4–200 deelnemers, half of hele dag</li>
          <li>Volledig op maat gemaakt</li>
          <li>Aantoonbaar resultaat</li>
        </ul>
      </div>
      <div class="s5-right anim-fade">
        <div class="game-board-vis" id="boardvis"></div>
      </div>
    </div>
  </div>

  <!-- ══ SLIDE 6 — PRODUCTEN ══ -->
  <div class="slide" id="s6">
    <div class="s6-inner">
      <div class="s6-header">
        <h2 class="s6-title anim-up">Negen<br><em>ervaringen</em></h2>
        <span class="s6-count anim-fade">09 producten</span>
      </div>
      <div class="products-grid anim-fade">
        <div class="prod-item featured-prod">
          <div class="prod-num">01</div>
          <div class="prod-name">FutureGame</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">02</div>
          <div class="prod-name">Escape Room on Location</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">03</div>
          <div class="prod-name">Learning Events</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">04</div>
          <div class="prod-name">Custom Escape Rooms</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">05</div>
          <div class="prod-name">Escape Box</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">06</div>
          <div class="prod-name">In-Company Training Box</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">07</div>
          <div class="prod-name">Onboarding Game</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">08</div>
          <div class="prod-name">GamePlan</div>
        </div>
        <div class="prod-item">
          <div class="prod-num">09</div>
          <div class="prod-name">Micro Learning</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ══ SLIDE 7 — KLANTEN ══ -->
  <div class="slide" id="s7">
    <div class="s7-inner">
      <p class="s7-label anim-fade">Vertrouwd door</p>
      <div class="s7-num anim-up">200<sup>+</sup></div>
      <p class="s7-sub anim-fade">enterprise organisaties</p>
      <div class="clients-strip anim-fade">
        <span class="client-name">Heineken</span>
        <span class="client-name">KLM</span>
        <span class="client-name">ING</span>
        <span class="client-name">ABN AMRO</span>
        <span class="client-name">EY</span>
        <span class="client-name">Schiphol</span>
        <span class="client-name">L'Oréal</span>
        <span class="client-name">Disney</span>
        <span class="client-name">BMW</span>
        <span class="client-name">Deloitte</span>
        <span class="client-name">Shell</span>
        <span class="client-name">Philips</span>
      </div>
    </div>
  </div>

  <!-- ══ SLIDE 8 — CTA ══ -->
  <div class="slide" id="s8">
    <div class="s8-circle1"></div>
    <div class="s8-circle2"></div>
    <div class="s8-inner">
      <p class="s8-eyebrow anim-fade">Klaar om te starten?</p>
      <h2 class="s8-headline anim-up">
        Plan een<br>demo.
      </h2>
      <a class="s8-cta anim-fade" href="https://helden-inc.com" target="_blank">
        Neem contact op
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </a>
      <p class="s8-domain anim-fade">helden-inc.com</p>
    </div>
  </div>

</div><!-- /slider -->

<script>
(function(){
  const slides = Array.from(document.querySelectorAll('.slide'));
  const dots   = Array.from(document.querySelectorAll('.dot'));
  const counter = document.querySelector('#counter span');
  const progressLine = document.getElementById('progress-line');
  const arrowHint = document.getElementById('arrow-hint');
  const logo = document.getElementById('logo');
  const TOTAL = slides.length;
  let current = 0;
  let animating = false;

  /* ── Build game board ── */
  function buildBoard(id, cols, rows, glowSet, hotSet, brightSet){
    const el = document.getElementById(id);
    if(!el) return;
    const n = cols * rows;
    for(let i=0;i<n;i++){
      const c = document.createElement('div');
      c.className = 'gv-cell' +
        (brightSet.includes(i) ? ' bright' :
         hotSet.includes(i)    ? ' hot'    :
         glowSet.includes(i)   ? ' glow'   : '');
      el.appendChild(c);
    }
  }

  /* background grid (slide 5 decorative) */
  function buildBgGrid(){
    const g = document.getElementById('gamegrid');
    if(!g) return;
    const n = 12*8;
    for(let i=0;i<n;i++){
      const c = document.createElement('div');
      c.className='s5-cell';
      g.appendChild(c);
    }
  }

  buildBgGrid();
  buildBoard('boardvis', 8, 6,
    [3,4,10,11,12,18,19,20,26,27,28,35,36,37],
    [11,12,19,20,27,28],
    [19,20]
  );

  /* ── Animate board cells ── */
  let boardInterval = null;
  function startBoardAnim(){
    clearInterval(boardInterval);
    const cells = document.querySelectorAll('#boardvis .gv-cell');
    const n = cells.length;
    boardInterval = setInterval(()=>{
      const idx = Math.floor(Math.random()*n);
      const c = cells[idx];
      const was = c.classList.contains('glow') || c.classList.contains('hot');
      cells.forEach(x=>{
        if(!x.classList.contains('bright')){
          x.classList.remove('hot');
        }
      });
      if(!was && !c.classList.contains('bright')){
        c.classList.add('hot');
        setTimeout(()=>c.classList.remove('hot'),1200);
      }
    }, 600);
  }
  function stopBoardAnim(){ clearInterval(boardInterval); }

  /* ── Navigate ── */
  function goTo(idx){
    if(animating || idx===current || idx<0 || idx>=TOTAL) return;
    animating = true;

    const dir = idx > current ? 'up' : 'down';
    const prev = slides[current];
    const next = slides[idx];

    prev.classList.add(dir==='up' ? 'exit-up' : 'exit-down');
    prev.classList.remove('active');

    // Remove stale animation classes so they retrigger
    next.querySelectorAll('[class*="anim-"]').forEach(el=>{
      el.style.animation='none';
      void el.offsetHeight; // reflow
      el.style.animation='';
    });

    next.classList.add('active');

    // Board animation
    if(idx===4) startBoardAnim();
    else stopBoardAnim();

    // Logo color on yellow slide
    if(idx===7) logo.classList.add('logo-dark');
    else logo.classList.remove('logo-dark');

    // Arrow hint
    arrowHint.style.opacity = idx===0 ? '1' : '0';

    // Update dots & counter
    dots.forEach((d,i)=>d.classList.toggle('active',i===idx));
    counter.textContent = String(idx+1).padStart(2,'0');

    // Progress bar
    progressLine.style.width = ((idx+1)/TOTAL*100)+'%';
    // Yellow slide — hide progress
    progressLine.style.opacity = idx===7 ? '0' : '1';

    current = idx;
    setTimeout(()=>{
      prev.classList.remove('exit-up','exit-down');
      animating = false;
    }, 950);
  }

  /* ── Wheel ── */
  let wheelTimer = null;
  let wheelAccum = 0;
  window.addEventListener('wheel', e=>{
    e.preventDefault();
    wheelAccum += Math.abs(e.deltaY);
    clearTimeout(wheelTimer);
    wheelTimer = setTimeout(()=>{ wheelAccum=0; }, 200);
    if(wheelAccum > 60){
      wheelAccum = 0;
      goTo(current + (e.deltaY>0 ? 1 : -1));
    }
  }, {passive:false});

  /* ── Keyboard ── */
  window.addEventListener('keydown', e=>{
    if(e.key==='ArrowDown'||e.key==='PageDown'||e.key==='Space') goTo(current+1);
    if(e.key==='ArrowUp'||e.key==='PageUp') goTo(current-1);
  });

  /* ── Touch ── */
  let touchStart = 0;
  window.addEventListener('touchstart', e=>{ touchStart=e.touches[0].clientY; },{passive:true});
  window.addEventListener('touchend', e=>{
    const d = touchStart - e.changedTouches[0].clientY;
    if(Math.abs(d)>50) goTo(current + (d>0?1:-1));
  },{passive:true});

  /* ── Dot clicks ── */
  dots.forEach(d=>d.addEventListener('click',()=>goTo(+d.dataset.slide)));

  /* ── Arrow hint click ── */
  arrowHint.addEventListener('click',()=>goTo(1));

  /* ── Streamlit iframe resize ── */
  function notifyHeight(){
    const h = Math.max(window.innerHeight, document.documentElement.clientHeight, 800);
    window.parent.postMessage({isStreamlitMessage:true, type:'streamlit:setFrameHeight', height:h}, '*');
  }
  notifyHeight();
  window.addEventListener('resize', notifyHeight);
})();
</script>
</body>
</html>"""

components.html(HTML, height=900, scrolling=False)
