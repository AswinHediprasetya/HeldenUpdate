"""
Helden Inc. — Cinematic Slider v3
Product-launch grade: film-shutter transitions, word-level reveals, minimal text.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Helden Inc.",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html,body{margin:0;padding:0;overflow:hidden;background:#08080a;}
.stApp{background:#08080a!important;overflow:hidden;}
.block-container{padding:0!important;max-width:100vw!important;overflow:hidden;}
#MainMenu,header,footer,
[data-testid="stDecoration"],[data-testid="stToolbar"],
[data-testid="stHeader"],[data-testid="stStatusWidget"]{display:none!important;}
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
<title>Helden</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,300;1,600&family=Sora:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
:root{
  --bg:     #08080a;
  --surface:#0d0d10;
  --card:   #111116;
  --y:      #FFD600;
  --ydim:   rgba(255,214,0,.09);
  --yline:  rgba(255,214,0,.16);
  --w:      #f0ebe2;
  --g:      #4e4e62;
  --g2:     #1e1e28;
  --serif:  'Cormorant Garamond',Georgia,serif;
  --sans:   'Sora',system-ui,sans-serif;
  --mono:   'DM Mono',monospace;

  /* ── Cinema transition ── */
  /* Enter: emerge from slight zoom-out + blur
     Exit:  recede into slight zoom-out + blur
     Both run simultaneously behind a shutter flash */
  --te: 1100ms;
  --cx: cubic-bezier(0.76,0,0.24,1);
}

html,body{
  width:100%;height:100%;overflow:hidden;
  background:var(--bg);color:var(--w);
  -webkit-font-smoothing:antialiased;
}

/* ═══════ SHUTTER FLASH ═══════ */
#shutter{
  position:fixed;inset:0;z-index:500;
  background:var(--bg);
  pointer-events:none;
  opacity:0;
  transition:opacity 80ms linear;
}
#shutter.flash{ opacity:1; }

/* ═══════ GRAIN ═══════ */
#grain{
  position:fixed;inset:0;z-index:300;pointer-events:none;
  opacity:.022;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* ═══════ PROGRESS ═══════ */
#bar{
  position:fixed;top:0;left:0;height:1.5px;
  background:var(--y);z-index:200;
  width:12.5%;
  transition:width .8s var(--cx), opacity .4s;
}

/* ═══════ LOGO ═══════ */
#logo{
  position:fixed;top:26px;left:36px;z-index:200;
  display:flex;align-items:center;gap:10px;
  mix-blend-mode:normal;
  transition:opacity .4s;
}
.lhex{
  width:26px;height:26px;background:var(--y);
  clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
}
.ltxt{
  font-family:var(--mono);font-size:.6rem;
  letter-spacing:.3em;text-transform:uppercase;color:var(--w);
  transition:color .4s;
}
#logo.invert .lhex{background:var(--bg);}
#logo.invert .ltxt{color:var(--bg);}

/* ═══════ DOTS ═══════ */
#dots{
  position:fixed;right:26px;top:50%;transform:translateY(-50%);
  z-index:200;display:flex;flex-direction:column;gap:8px;
  transition:opacity .4s;
}
.dot{
  width:5px;height:5px;border-radius:50%;
  background:var(--g2);border:1px solid var(--g);
  cursor:pointer;
  transition:background .25s,transform .25s,border-color .25s;
}
.dot.on{background:var(--y);border-color:var(--y);transform:scale(1.5);}
#dots.invert .dot{border-color:rgba(0,0,0,.3);}
#dots.invert .dot.on{background:var(--bg);border-color:var(--bg);}

/* ═══════ COUNTER ═══════ */
#ctr{
  position:fixed;bottom:28px;right:34px;z-index:200;
  font-family:var(--mono);font-size:.55rem;
  letter-spacing:.2em;color:var(--g);
  transition:color .4s;
}
#ctr b{color:var(--w);font-weight:400;}
#ctr.invert{color:rgba(0,0,0,.4);}
#ctr.invert b{color:var(--bg);}

/* ═══════ SCROLL CUE ═══════ */
#cue{
  position:fixed;bottom:26px;left:50%;transform:translateX(-50%);
  z-index:200;
  display:flex;flex-direction:column;align-items:center;gap:5px;
  opacity:1;transition:opacity .5s;
}
#cue.hide{opacity:0;pointer-events:none;}
.cue-line{
  width:1px;height:32px;
  background:linear-gradient(var(--g),transparent);
  animation:cueDrop 1.8s ease infinite;
}
.cue-txt{
  font-family:var(--mono);font-size:.5rem;
  letter-spacing:.28em;text-transform:uppercase;color:var(--g);
}
@keyframes cueDrop{
  0%{transform:scaleY(0);transform-origin:top;}
  50%{transform:scaleY(1);transform-origin:top;}
  51%{transform:scaleY(1);transform-origin:bottom;}
  100%{transform:scaleY(0);transform-origin:bottom;}
}

/* ═══════ SLIDER ═══════ */
#slider{width:100vw;height:100vh;position:relative;overflow:hidden;}

.slide{
  position:absolute;inset:0;
  display:flex;align-items:center;justify-content:center;
  /* default: hidden */
  opacity:0;
  transform:scale(1.04);
  filter:blur(8px);
  pointer-events:none;
  will-change:opacity,transform,filter;
  /* NO transition here — we use keyframe animations */
}
.slide.active{
  opacity:1;transform:scale(1);filter:blur(0);pointer-events:all;
  animation:slideIn var(--te) var(--cx) both;
}
.slide.exit{
  pointer-events:none;
  animation:slideOut calc(var(--te) * .85) var(--cx) both;
}

@keyframes slideIn{
  from{opacity:0;transform:scale(1.06);filter:blur(10px);}
  to  {opacity:1;transform:scale(1);filter:blur(0);}
}
@keyframes slideOut{
  from{opacity:1;transform:scale(1);filter:blur(0);}
  to  {opacity:0;transform:scale(.96);filter:blur(6px);}
}

/* ── Element stagger ── */
.w{  /* word / element unit */
  display:inline-block;
  opacity:0;
  transform:translateY(20px);
}
.slide.active .w{
  animation:wIn .75s var(--cx) both;
}
/* stagger via data-i */
.slide.active .w[data-i="0"]{animation-delay:.18s;}
.slide.active .w[data-i="1"]{animation-delay:.30s;}
.slide.active .w[data-i="2"]{animation-delay:.42s;}
.slide.active .w[data-i="3"]{animation-delay:.54s;}
.slide.active .w[data-i="4"]{animation-delay:.66s;}
.slide.active .w[data-i="5"]{animation-delay:.78s;}
.slide.active .w[data-i="6"]{animation-delay:.90s;}
@keyframes wIn{
  from{opacity:0;transform:translateY(18px);}
  to  {opacity:1;transform:translateY(0);}
}

/* fade variant */
.f{opacity:0;}
.slide.active .f{animation:fIn .9s var(--cx) both;}
.slide.active .f[data-i="0"]{animation-delay:.22s;}
.slide.active .f[data-i="1"]{animation-delay:.40s;}
.slide.active .f[data-i="2"]{animation-delay:.58s;}
.slide.active .f[data-i="3"]{animation-delay:.76s;}
.slide.active .f[data-i="4"]{animation-delay:.94s;}
@keyframes fIn{from{opacity:0;}to{opacity:1;}}

/* line reveal variant — clip from left */
.r{clip-path:inset(0 100% 0 0);}
.slide.active .r{
  animation:rIn .85s var(--cx) both;
}
.slide.active .r[data-i="0"]{animation-delay:.20s;}
.slide.active .r[data-i="1"]{animation-delay:.38s;}
.slide.active .r[data-i="2"]{animation-delay:.56s;}
@keyframes rIn{
  from{clip-path:inset(0 100% 0 0);}
  to  {clip-path:inset(0 0% 0 0);}
}

/* ═══════════════════════════════════
   SHARED TYPOGRAPHY TOKENS
═══════════════════════════════════ */
.eyebrow{
  font-family:var(--mono);font-size:.56rem;
  letter-spacing:.28em;text-transform:uppercase;
  color:var(--y);opacity:.75;
  display:block;
}
.tag{
  display:inline-flex;
  background:var(--y);color:var(--bg);
  font-family:var(--mono);font-size:.52rem;
  letter-spacing:.12em;text-transform:uppercase;
  padding:.22rem .7rem;border-radius:2px;
}

/* ═══════════════════════════════════
   S1 — HERO
═══════════════════════════════════ */
#s1{background:var(--bg);}
.s1-bg{position:absolute;inset:0;overflow:hidden;}
/* slow-ken-burns dot grid */
.s1-dots{
  position:absolute;inset:-20%;
  background-image:radial-gradient(circle,rgba(255,214,0,.55) 1px,transparent 1px);
  background-size:52px 52px;
  opacity:.045;
  animation:kenBurns 18s ease-in-out infinite alternate;
}
@keyframes kenBurns{
  from{transform:scale(1) translate(0,0);}
  to  {transform:scale(1.08) translate(-2%,2%);}
}
.s1-glow{
  position:absolute;bottom:-15%;left:50%;transform:translateX(-50%);
  width:70vw;height:50vh;
  background:radial-gradient(ellipse,rgba(255,214,0,.055) 0%,transparent 65%);
  animation:glowPulse 6s ease-in-out infinite alternate;
}
@keyframes glowPulse{
  from{opacity:.7;}to{opacity:1;}
}
.s1-content{
  position:relative;z-index:2;
  text-align:center;
}
.s1-h{
  font-family:var(--serif);
  font-size:clamp(5rem,13vw,14rem);
  font-weight:300;font-style:italic;
  line-height:.87;
  letter-spacing:-.01em;
  color:var(--w);
  display:block;
}
.s1-h em{
  font-style:normal;font-weight:600;color:var(--y);
}
.s1-byline{
  font-family:var(--mono);font-size:.52rem;
  letter-spacing:.3em;text-transform:uppercase;
  color:var(--g);margin-top:2.25rem;
  display:block;
}

/* ═══════════════════════════════════
   S2 — PROBLEM (the number IS the message)
═══════════════════════════════════ */
#s2{background:var(--bg);}
.s2-wrap{
  display:flex;flex-direction:column;
  align-items:flex-start;
  padding:0 8vw;
  width:100%;
}
.s2-n{
  font-family:var(--serif);
  font-size:clamp(12rem,28vw,32rem);
  font-weight:300;
  line-height:.82;
  color:var(--w);
  letter-spacing:-.04em;
  /* number takes 90% of screen height visually */
}
.s2-pct{
  font-size:.35em;vertical-align:super;
  color:var(--y);font-weight:300;
}
.s2-rule{
  display:block;
  width:clamp(80px,18vw,200px);height:1px;
  background:var(--g2);
  margin:1.75rem 0;
}
.s2-caption{
  font-family:var(--serif);
  font-size:clamp(1.25rem,2.5vw,2.75rem);
  font-weight:300;font-style:italic;
  color:var(--g);
  letter-spacing:-.005em;
  line-height:1.2;
  max-width:520px;
}

/* ═══════════════════════════════════
   S3 — INSIGHT (contrast of two lines)
═══════════════════════════════════ */
#s3{background:var(--surface);}
.s3-wrap{text-align:center;padding:0 6vw;}
.s3-dim{
  font-family:var(--serif);
  font-size:clamp(2.25rem,5.5vw,6.5rem);
  font-weight:300;
  line-height:1.0;
  color:var(--g);
  letter-spacing:-.01em;
  display:block;
}
.s3-bright{
  font-family:var(--serif);
  font-size:clamp(2.25rem,5.5vw,6.5rem);
  font-weight:600;
  line-height:1.0;
  color:var(--w);
  letter-spacing:-.01em;
  font-style:italic;
  display:block;
  margin-top:.3rem;
}
.s3-bright span{color:var(--y);}
.s3-divider{
  display:block;
  width:40px;height:1px;
  background:var(--yline);
  margin:2rem auto;
}
.s3-stat{
  font-family:var(--mono);font-size:.6rem;
  letter-spacing:.22em;text-transform:uppercase;
  color:var(--g);display:block;
}
.s3-stat b{color:var(--y);font-weight:400;}

/* ═══════════════════════════════════
   S4 — SOLUTION (the word IS the slide)
═══════════════════════════════════ */
#s4{background:var(--bg);}
.s4-glow{
  position:absolute;
  bottom:-5%;left:50%;transform:translateX(-50%);
  width:90vw;height:65vh;
  background:radial-gradient(ellipse,rgba(255,214,0,.05) 0%,transparent 62%);
  pointer-events:none;
}
.s4-content{
  position:relative;z-index:2;
  text-align:center;
}
.s4-eyebrow{margin-bottom:2rem;}
.s4-h{
  font-family:var(--serif);
  font-size:clamp(4rem,10.5vw,12.5rem);
  font-weight:300;
  line-height:.88;
  color:var(--w);
  letter-spacing:-.015em;
  display:block;
}
.s4-h em{font-style:italic;color:var(--y);}
.s4-sub{
  font-family:var(--sans);
  font-size:clamp(.8rem,1vw,1rem);
  font-weight:300;color:var(--g);
  letter-spacing:.06em;
  margin-top:2rem;
  display:block;
}

/* ═══════════════════════════════════
   S5 — FUTUREGAME
═══════════════════════════════════ */
#s5{background:var(--bg);}
.s5-inner{
  position:relative;z-index:2;
  width:88vw;max-width:1200px;
  display:grid;grid-template-columns:1fr 1fr;
  gap:7vw;align-items:center;
}
.s5-name{
  font-family:var(--serif);
  font-size:clamp(4rem,8vw,9.5rem);
  font-weight:600;
  line-height:.85;
  color:var(--w);
  letter-spacing:-.01em;
  display:block;
  margin:1rem 0 1.5rem;
}
.s5-desc{
  font-family:var(--sans);font-size:clamp(.8rem,1vw,1rem);
  font-weight:300;color:var(--g);line-height:1.75;
  max-width:380px;display:block;
}
/* game board */
.s5-board{
  position:relative;height:460px;
  display:grid;
  grid-template-columns:repeat(8,1fr);
  grid-template-rows:repeat(6,1fr);
  gap:6px;
}
.gc{
  border-radius:4px;
  background:var(--card);
  border:1px solid rgba(255,214,0,.07);
  transition:background .5s,border-color .5s,box-shadow .5s;
}
.gc.lit{
  background:rgba(255,214,0,.13);
  border-color:rgba(255,214,0,.28);
}
.gc.hot{
  background:rgba(255,214,0,.30);
  border-color:rgba(255,214,0,.55);
  box-shadow:0 0 12px rgba(255,214,0,.18);
}
.gc.bright{
  background:var(--y);
  border-color:var(--y);
  box-shadow:0 0 20px rgba(255,214,0,.35);
}

/* ═══════════════════════════════════
   S6 — 9 PRODUCTS (staggered list)
═══════════════════════════════════ */
#s6{background:var(--surface);}
.s6-inner{
  width:88vw;max-width:1100px;
}
.s6-header{
  display:flex;align-items:baseline;justify-content:space-between;
  margin-bottom:2.5rem;
  padding-bottom:1.25rem;
  border-bottom:1px solid var(--g2);
}
.s6-title{
  font-family:var(--serif);
  font-size:clamp(2.25rem,5vw,5.5rem);
  font-weight:300;color:var(--w);
  line-height:.92;letter-spacing:-.01em;
}
.s6-title em{font-style:italic;color:var(--y);}
.s6-tally{
  font-family:var(--mono);font-size:.55rem;
  letter-spacing:.2em;text-transform:uppercase;color:var(--g);
}
.plist{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:1px;
  background:var(--g2);
  border:1px solid var(--g2);
  border-radius:3px;overflow:hidden;
}
.pi{
  background:var(--surface);
  padding:1.25rem 1.5rem;
  position:relative;overflow:hidden;
  transition:background .2s;
}
.pi:hover{background:var(--card);}
.pi::after{
  content:'';position:absolute;
  bottom:0;left:0;right:0;height:1.5px;
  background:var(--y);
  transform:scaleX(0);transform-origin:left;
  transition:transform .28s;
}
.pi:hover::after{transform:scaleX(1);}
.pi-n{
  font-family:var(--mono);font-size:.48rem;
  text-transform:uppercase;letter-spacing:.18em;
  color:var(--g);display:block;margin-bottom:.4rem;
}
.pi-name{
  font-family:var(--serif);
  font-size:clamp(1rem,1.5vw,1.6rem);
  font-weight:400;color:var(--w);
  line-height:1.2;letter-spacing:-.004em;
}
.pi.star .pi-name{color:var(--y);}
/* stagger plist items */
.slide.active .pi{
  animation:piIn .6s var(--cx) both;
}
.slide.active .pi:nth-child(1){animation-delay:.22s;}
.slide.active .pi:nth-child(2){animation-delay:.28s;}
.slide.active .pi:nth-child(3){animation-delay:.34s;}
.slide.active .pi:nth-child(4){animation-delay:.40s;}
.slide.active .pi:nth-child(5){animation-delay:.46s;}
.slide.active .pi:nth-child(6){animation-delay:.52s;}
.slide.active .pi:nth-child(7){animation-delay:.58s;}
.slide.active .pi:nth-child(8){animation-delay:.64s;}
.slide.active .pi:nth-child(9){animation-delay:.70s;}
@keyframes piIn{
  from{opacity:0;transform:translateY(12px);}
  to  {opacity:1;transform:translateY(0);}
}

/* ═══════════════════════════════════
   S7 — CLIENTS
═══════════════════════════════════ */
#s7{background:var(--bg);}
.s7-inner{text-align:center;width:88vw;max-width:960px;}
.s7-num{
  font-family:var(--serif);
  font-size:clamp(8rem,20vw,24rem);
  font-weight:300;
  color:var(--w);
  line-height:.82;
  letter-spacing:-.04em;
  display:block;
}
.s7-plus{font-size:.4em;vertical-align:super;color:var(--y);}
.s7-label{
  font-family:var(--serif);
  font-size:clamp(1.25rem,2.2vw,2.5rem);
  font-weight:300;font-style:italic;
  color:var(--g);
  display:block;margin-top:.25rem;margin-bottom:2.5rem;
}
.cstrip{
  display:flex;flex-wrap:wrap;gap:7px;
  justify-content:center;
}
.cn{
  font-family:var(--mono);font-size:.55rem;
  letter-spacing:.12em;text-transform:uppercase;
  color:var(--g);padding:.35rem .85rem;
  border:1px solid var(--g2);border-radius:2px;
  transition:border-color .2s,color .2s;
  opacity:0;
}
.cn:hover{border-color:var(--yline);color:var(--y);}
/* stagger clients */
.slide.active .cn{animation:cnIn .4s var(--cx) both;}
.slide.active .cn:nth-child(1){animation-delay:.48s;}
.slide.active .cn:nth-child(2){animation-delay:.52s;}
.slide.active .cn:nth-child(3){animation-delay:.56s;}
.slide.active .cn:nth-child(4){animation-delay:.60s;}
.slide.active .cn:nth-child(5){animation-delay:.64s;}
.slide.active .cn:nth-child(6){animation-delay:.68s;}
.slide.active .cn:nth-child(7){animation-delay:.72s;}
.slide.active .cn:nth-child(8){animation-delay:.76s;}
.slide.active .cn:nth-child(9){animation-delay:.80s;}
.slide.active .cn:nth-child(10){animation-delay:.84s;}
.slide.active .cn:nth-child(11){animation-delay:.88s;}
.slide.active .cn:nth-child(12){animation-delay:.92s;}
@keyframes cnIn{from{opacity:0;transform:scale(.9);}to{opacity:1;transform:scale(1);}}

/* ═══════════════════════════════════
   S8 — CTA
═══════════════════════════════════ */
#s8{background:var(--y);}
.s8-ring1{
  position:absolute;
  top:-50%;left:50%;transform:translateX(-50%);
  width:130vw;height:130vw;
  border-radius:50%;
  border:1px solid rgba(0,0,0,.055);
  pointer-events:none;
  animation:ringPulse 5s ease-in-out infinite;
}
.s8-ring2{
  position:absolute;
  top:-30%;left:50%;transform:translateX(-50%);
  width:80vw;height:80vw;
  border-radius:50%;
  border:1px solid rgba(0,0,0,.04);
  pointer-events:none;
  animation:ringPulse 5s ease-in-out infinite .5s;
}
@keyframes ringPulse{
  0%,100%{transform:translateX(-50%) scale(1);}
  50%{transform:translateX(-50%) scale(1.02);}
}
.s8-content{
  position:relative;z-index:2;
  text-align:center;padding:0 8vw;
}
.s8-h{
  font-family:var(--serif);
  font-size:clamp(5rem,13vw,15rem);
  font-weight:300;font-style:italic;
  line-height:.85;
  color:var(--bg);
  letter-spacing:-.02em;
  display:block;
  margin-bottom:2.5rem;
}
.s8-cta{
  display:inline-flex;align-items:center;gap:.75rem;
  background:var(--bg);color:var(--y);
  font-family:var(--sans);font-size:.9375rem;font-weight:500;
  padding:.875rem 2.25rem;border-radius:3px;
  text-decoration:none;
  transition:background .2s,transform .15s;
}
.s8-cta:hover{background:#111;transform:translateY(-2px);}
.s8-cta svg{transition:transform .2s;}
.s8-cta:hover svg{transform:translateX(5px);}
.s8-url{
  font-family:var(--mono);font-size:.52rem;
  letter-spacing:.22em;text-transform:uppercase;
  color:rgba(0,0,0,.3);margin-top:2rem;
  display:block;
}
</style>
</head>
<body>

<!-- UI chrome -->
<div id="shutter"></div>
<div id="grain"></div>
<div id="bar"></div>

<div id="logo">
  <div class="lhex"></div>
  <span class="ltxt">HELDEN</span>
</div>

<div id="dots">
  <div class="dot on" data-i="0"></div>
  <div class="dot" data-i="1"></div>
  <div class="dot" data-i="2"></div>
  <div class="dot" data-i="3"></div>
  <div class="dot" data-i="4"></div>
  <div class="dot" data-i="5"></div>
  <div class="dot" data-i="6"></div>
  <div class="dot" data-i="7"></div>
</div>

<div id="ctr"><b>01</b> / 08</div>

<div id="cue">
  <div class="cue-line"></div>
  <span class="cue-txt">scroll</span>
</div>

<!-- ════════════════ SLIDES ════════════════ -->
<div id="slider">

  <!-- S1 HERO -->
  <div class="slide active" id="s1">
    <div class="s1-bg">
      <div class="s1-dots"></div>
      <div class="s1-glow"></div>
    </div>
    <div class="s1-content">
      <span class="eyebrow f" data-i="0">Helden Inc.</span>
      <span class="s1-h w" data-i="1">Workshops<br>zijn<br><em>verleden</em><br>tijd.</span>
      <span class="s1-byline f" data-i="2">Haarlem · 200+ enterprise clients</span>
    </div>
  </div>

  <!-- S2 PROBLEM -->
  <div class="slide" id="s2">
    <div class="s2-wrap">
      <span class="eyebrow f" data-i="0" style="margin-bottom:1rem;">Het probleem</span>
      <span class="s2-n w" data-i="1">10<span class="s2-pct">%</span></span>
      <span class="s2-rule r" data-i="2"></span>
      <span class="s2-caption w" data-i="3">Onthoudt na een presentatie.</span>
    </div>
  </div>

  <!-- S3 INSIGHT -->
  <div class="slide" id="s3">
    <div class="s3-wrap">
      <span class="s3-dim w" data-i="0">Mensen leren niet<br>door te kijken.</span>
      <span class="s3-bright w" data-i="1">Mensen leren door<br>te <span>spelen</span>.</span>
      <span class="s3-divider r" data-i="2"></span>
      <span class="s3-stat f" data-i="3"><b>3× hogere</b> kennisretentie · <b>100%</b> actieve deelname</span>
    </div>
  </div>

  <!-- S4 SOLUTION -->
  <div class="slide" id="s4">
    <div class="s4-glow"></div>
    <div class="s4-content">
      <span class="eyebrow s4-eyebrow f" data-i="0">De oplossing</span>
      <span class="s4-h w" data-i="1">Gamified<br><em>Internal</em><br>Communication</span>
      <span class="s4-sub f" data-i="2">Van strategiesessie tot onboarding — altijd als spel.</span>
    </div>
  </div>

  <!-- S5 FUTUREGAME -->
  <div class="slide" id="s5">
    <div class="s5-inner">
      <div>
        <span class="tag f" data-i="0">Bestseller</span>
        <span class="s5-name w" data-i="1">Future<br>Game</span>
        <span class="s5-desc f" data-i="2">De interactieve strategiesimulatie.<br>Uw team ervaart de toekomst.</span>
      </div>
      <div class="s5-board f" data-i="3" id="board"></div>
    </div>
  </div>

  <!-- S6 PRODUCTS -->
  <div class="slide" id="s6">
    <div class="s6-inner">
      <div class="s6-header">
        <span class="s6-title w" data-i="0">Negen<br><em>ervaringen</em></span>
        <span class="s6-tally f" data-i="1">09 producten</span>
      </div>
      <div class="plist">
        <div class="pi star"><span class="pi-n">01</span><span class="pi-name">FutureGame</span></div>
        <div class="pi"><span class="pi-n">02</span><span class="pi-name">Escape Room on Location</span></div>
        <div class="pi"><span class="pi-n">03</span><span class="pi-name">Learning Events</span></div>
        <div class="pi"><span class="pi-n">04</span><span class="pi-name">Custom Escape Rooms</span></div>
        <div class="pi"><span class="pi-n">05</span><span class="pi-name">Escape Box</span></div>
        <div class="pi"><span class="pi-n">06</span><span class="pi-name">In-Company Training Box</span></div>
        <div class="pi"><span class="pi-n">07</span><span class="pi-name">Onboarding Game</span></div>
        <div class="pi"><span class="pi-n">08</span><span class="pi-name">GamePlan</span></div>
        <div class="pi"><span class="pi-n">09</span><span class="pi-name">Micro Learning</span></div>
      </div>
    </div>
  </div>

  <!-- S7 CLIENTS -->
  <div class="slide" id="s7">
    <div class="s7-inner">
      <span class="eyebrow f" data-i="0" style="margin-bottom:1.25rem;">Vertrouwd door</span>
      <span class="s7-num w" data-i="1">200<span class="s7-plus">+</span></span>
      <span class="s7-label f" data-i="2">enterprise organisaties</span>
      <div class="cstrip">
        <span class="cn">Heineken</span><span class="cn">KLM</span>
        <span class="cn">ING</span><span class="cn">ABN AMRO</span>
        <span class="cn">EY</span><span class="cn">Schiphol</span>
        <span class="cn">L'Oréal</span><span class="cn">Disney</span>
        <span class="cn">BMW</span><span class="cn">Deloitte</span>
        <span class="cn">Shell</span><span class="cn">Philips</span>
      </div>
    </div>
  </div>

  <!-- S8 CTA -->
  <div class="slide" id="s8">
    <div class="s8-ring1"></div>
    <div class="s8-ring2"></div>
    <div class="s8-content">
      <span class="s8-h w" data-i="0">Plan een<br>demo.</span>
      <a class="s8-cta f" data-i="1" href="https://helden-inc.com" target="_blank">
        Neem contact op
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path d="M2.5 7h9M8 3.5l3.5 3.5L8 10.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </a>
      <span class="s8-url f" data-i="2">helden-inc.com</span>
    </div>
  </div>

</div><!-- /slider -->

<script>
(function(){
  'use strict';

  const slides   = document.querySelectorAll('.slide');
  const dots     = document.querySelectorAll('.dot');
  const bar      = document.getElementById('bar');
  const ctr      = document.getElementById('ctr');
  const cue      = document.getElementById('cue');
  const logo     = document.getElementById('logo');
  const dotsEl   = document.getElementById('dots');
  const shutter  = document.getElementById('shutter');
  const TOTAL    = slides.length;
  let cur        = 0;
  let busy       = false;

  const DUR      = 1100;  // matches --te
  const SHUTTER  = 80;    // shutter flash ms

  /* ─── Build game board ─── */
  (function(){
    const b = document.getElementById('board');
    if(!b) return;
    const ROWS=6, COLS=8, N=ROWS*COLS;
    const LIT    = new Set([3,4,10,11,12,18,19,20,26,27,28,35,36]);
    const HOT    = new Set([11,12,19,20,27]);
    const BRIGHT = new Set([19,20]);
    for(let i=0;i<N;i++){
      const c = document.createElement('div');
      c.className = 'gc'
        + (BRIGHT.has(i)?' bright' : HOT.has(i)?' hot' : LIT.has(i)?' lit' : '');
      b.appendChild(c);
    }
  })();

  /* ─── Board animation ─── */
  let boardTick = null;
  function boardStart(){
    boardStop();
    const cells = document.querySelectorAll('.gc');
    const N = cells.length;
    // Wave pattern: animate clusters
    const waves = [
      [2,3,10,11],[10,11,18,19],[18,19,26,27],[26,27,34,35],
      [3,4,11,12],[19,20,27,28],[4,12,20,28],[0,8,16,24],
    ];
    let wi = 0;
    boardTick = setInterval(()=>{
      cells.forEach(c=>{ if(!c.classList.contains('bright')) c.classList.remove('hot','lit'); });
      const wave = waves[wi % waves.length];
      wave.forEach(i=>{ if(cells[i] && !cells[i].classList.contains('bright')) cells[i].classList.add('hot'); });
      wi++;
    }, 700);
  }
  function boardStop(){
    clearInterval(boardTick);
    document.querySelectorAll('.gc.hot').forEach(c=>c.classList.remove('hot'));
  }

  /* ─── Update chrome ─── */
  function updateChrome(idx){
    // Progress bar
    bar.style.width = ((idx+1)/TOTAL*100)+'%';
    bar.style.opacity = idx===7 ? '0' : '1';

    // Counter
    ctr.innerHTML = '<b>'+String(idx+1).padStart(2,'0')+'</b> / 08';
    ctr.className = idx===7 ? 'invert' : '';

    // Dots
    dots.forEach((d,i) => d.classList.toggle('on', i===idx));
    dotsEl.className = idx===7 ? 'invert' : '';

    // Logo
    logo.className = idx===7 ? 'invert' : '';

    // Scroll cue
    cue.classList.toggle('hide', idx!==0);
  }

  /* ─── Core transition ─── */
  function goTo(next){
    if(busy || next===cur || next<0 || next>=TOTAL) return;
    busy = true;

    const prev = slides[cur];
    const nxt  = slides[next];

    // 1. Fire shutter flash
    shutter.classList.add('flash');

    setTimeout(()=>{
      // 2. At peak of darkness: swap slides
      // Kill previous .active, start exit animation
      prev.classList.remove('active');
      prev.classList.add('exit');

      // Reset then activate incoming slide
      // Force reflow so animations retrigger
      nxt.style.animation = 'none';
      nxt.querySelectorAll('.w,.f,.r').forEach(el=>{
        el.style.animation='none';
      });
      void nxt.offsetHeight;
      nxt.style.animation = '';
      nxt.querySelectorAll('.w,.f,.r').forEach(el=>{
        el.style.animation='';
      });
      nxt.classList.add('active');

      // 3. Open shutter
      shutter.classList.remove('flash');

      // Board
      if(next===4) boardStart();
      else boardStop();

      updateChrome(next);
      cur = next;

      // Cleanup exit class after transition
      setTimeout(()=>{
        prev.classList.remove('exit');
        busy = false;
      }, DUR);

    }, SHUTTER);
  }

  // Init chrome
  updateChrome(0);

  /* ─── Input: wheel ─── */
  let wAccum = 0, wTick = null;
  window.addEventListener('wheel', e=>{
    e.preventDefault();
    wAccum += Math.abs(e.deltaY);
    clearTimeout(wTick);
    wTick = setTimeout(()=>{ wAccum=0; }, 250);
    if(wAccum > 55){
      wAccum = 0;
      goTo(cur + (e.deltaY>0 ? 1 : -1));
    }
  },{passive:false});

  /* ─── Input: keyboard ─── */
  window.addEventListener('keydown', e=>{
    if(['ArrowDown','PageDown','Space'].includes(e.key)){ e.preventDefault(); goTo(cur+1); }
    if(['ArrowUp','PageUp'].includes(e.key)){ e.preventDefault(); goTo(cur-1); }
  });

  /* ─── Input: touch ─── */
  let ty0 = 0;
  window.addEventListener('touchstart', e=>{ ty0 = e.touches[0].clientY; },{passive:true});
  window.addEventListener('touchend', e=>{
    const dy = ty0 - e.changedTouches[0].clientY;
    if(Math.abs(dy)>45) goTo(cur + (dy>0?1:-1));
  },{passive:true});

  /* ─── Dot clicks ─── */
  dots.forEach(d=>d.addEventListener('click',()=>goTo(+d.dataset.i)));

  /* ─── Cue click ─── */
  document.getElementById('cue').addEventListener('click',()=>goTo(1));

  /* ─── iFrame height ─── */
  function sendH(){
    const h = Math.max(window.innerHeight, 700);
    try{
      window.parent.postMessage(
        {isStreamlitMessage:true,type:'streamlit:setFrameHeight',height:h},
        '*'
      );
    }catch(_){}
  }
  sendH();
  window.addEventListener('resize', sendH);

})();
</script>
</body>
</html>"""

components.html(HTML, height=900, scrolling=False)
