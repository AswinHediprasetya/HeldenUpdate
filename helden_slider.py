"""
Helden Inc. — Complete Cinematic Experience v4
12-slide Orano-style fullscreen storytelling
All content from helden-inc.com/en/#games

Deploy: GitHub → share.streamlit.io → Main file: helden_slider.py
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Helden Inc. — Game-Based Learning",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html,body{margin:0;padding:0;overflow:hidden;background:#07070a;}
.stApp{background:#07070a!important;overflow:hidden;}
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
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Helden Inc.</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=Outfit:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}

/* ─── DESIGN TOKENS ─── */
:root{
  --bg:      #07070a;
  --s1:      #0c0c10;
  --s2:      #101015;
  --card:    #13131a;
  --y:       #FFD600;
  --ydim:    rgba(255,214,0,.08);
  --yline:   rgba(255,214,0,.15);
  --yglow:   rgba(255,214,0,.22);
  --w:       #ede8de;
  --g:       #484860;
  --g2:      #1c1c28;
  --g3:      rgba(255,255,255,.04);
  --serif:   'Cormorant Garamond',Georgia,serif;
  --sans:    'Outfit',system-ui,sans-serif;
  --mono:    'DM Mono',monospace;

  /* Cinema transition system */
  --in-dur:  1050ms;
  --out-dur: 750ms;
  --ease:    cubic-bezier(0.76,0,0.24,1);
  --ease-out:cubic-bezier(0.22,1,0.36,1);

  /* Stagger delays */
  --d0:.14s; --d1:.26s; --d2:.38s;
  --d3:.50s; --d4:.62s; --d5:.74s;
  --d6:.86s; --d7:.98s;
}

html,body{
  width:100%;height:100%;overflow:hidden;
  background:var(--bg);color:var(--w);
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
}

/* ─── FILM GRAIN ─── */
#grain{
  position:fixed;inset:0;z-index:400;pointer-events:none;
  opacity:.02;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.82' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* ─── SHUTTER (black flash on cut) ─── */
#shutter{
  position:fixed;inset:0;z-index:600;
  background:var(--bg);opacity:0;pointer-events:none;
  transition:opacity 70ms linear;
}
#shutter.on{opacity:1;}

/* ─── PROGRESS BAR ─── */
#pbar{
  position:fixed;top:0;left:0;z-index:300;
  height:1.5px;background:var(--y);
  width:8.33%;transition:width .9s var(--ease),opacity .4s;
}

/* ─── LOGO ─── */
#logo{
  position:fixed;top:24px;left:32px;z-index:300;
  display:flex;align-items:center;gap:9px;
  transition:opacity .4s;
}
.lhex{
  width:24px;height:24px;background:var(--y);
  clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
  transition:background .4s;
}
.lname{
  font-family:var(--mono);font-size:.58rem;
  letter-spacing:.32em;text-transform:uppercase;
  color:var(--w);transition:color .4s;
}
#logo.dark .lhex{background:var(--bg);}
#logo.dark .lname{color:var(--bg);}

/* ─── SLIDE NUMBER (top right) ─── */
#slidenum{
  position:fixed;top:24px;right:36px;z-index:300;
  font-family:var(--mono);font-size:.55rem;letter-spacing:.2em;
  color:var(--g);transition:color .4s;
}
#slidenum b{color:var(--w);font-weight:400;}
#slidenum.dark{color:rgba(0,0,0,.4);}
#slidenum.dark b{color:var(--bg);}

/* ─── NAV DOTS (right side) ─── */
#dots{
  position:fixed;right:22px;top:50%;transform:translateY(-50%);
  z-index:300;display:flex;flex-direction:column;gap:7px;
}
.dot{
  width:4px;height:4px;border-radius:50%;
  background:var(--g2);border:1px solid var(--g);
  cursor:pointer;
  transition:background .25s,transform .25s,border-color .25s,height .25s;
}
.dot.on{background:var(--y);border-color:var(--y);transform:scale(1.6);}
#dots.dark .dot{border-color:rgba(0,0,0,.2);}
#dots.dark .dot.on{background:var(--bg);border-color:var(--bg);}

/* ─── SCROLL CUE ─── */
#cue{
  position:fixed;bottom:24px;left:50%;transform:translateX(-50%);
  z-index:300;display:flex;flex-direction:column;align-items:center;gap:5px;
  transition:opacity .5s;
}
#cue.hide{opacity:0;pointer-events:none;}
.cue-tick{
  width:1px;height:28px;
  background:linear-gradient(var(--g),transparent);
  animation:tickDrop 1.9s ease infinite;
}
@keyframes tickDrop{
  0%{transform:scaleY(0);transform-origin:top;}
  49%{transform:scaleY(1);transform-origin:top;}
  50%{transform-origin:bottom;}
  100%{transform:scaleY(0);transform-origin:bottom;}
}
.cue-lbl{
  font-family:var(--mono);font-size:.48rem;
  letter-spacing:.28em;text-transform:uppercase;color:var(--g);
}

/* ─── SLIDE CONTAINER ─── */
#slider{width:100vw;height:100vh;position:relative;overflow:hidden;}

/* ─── SLIDE BASE STATE ─── */
.slide{
  position:absolute;inset:0;
  display:flex;align-items:center;justify-content:center;
  /* Hidden default */
  opacity:0;
  transform:scale(1.05);
  filter:blur(10px);
  pointer-events:none;
  will-change:opacity,transform,filter;
}
.slide.active{
  pointer-events:all;
  animation:sIn var(--in-dur) var(--ease) both;
}
.slide.exit{
  pointer-events:none;
  animation:sOut var(--out-dur) var(--ease) both;
}
@keyframes sIn{
  from{opacity:0;transform:scale(1.06);filter:blur(12px);}
  to  {opacity:1;transform:scale(1);  filter:blur(0);}
}
@keyframes sOut{
  from{opacity:1;transform:scale(1);  filter:blur(0);}
  to  {opacity:0;transform:scale(.95);filter:blur(8px);}
}

/* ─── ELEMENT ANIMATION CLASSES ─── */
/* Up-float + fade stagger (headlines, key elements) */
.u{opacity:0;transform:translateY(22px);}
.slide.active .u{animation:uIn .8s var(--ease-out) both;}
.slide.active .u[data-d="0"]{animation-delay:var(--d0);}
.slide.active .u[data-d="1"]{animation-delay:var(--d1);}
.slide.active .u[data-d="2"]{animation-delay:var(--d2);}
.slide.active .u[data-d="3"]{animation-delay:var(--d3);}
.slide.active .u[data-d="4"]{animation-delay:var(--d4);}
.slide.active .u[data-d="5"]{animation-delay:var(--d5);}
.slide.active .u[data-d="6"]{animation-delay:var(--d6);}
@keyframes uIn{
  from{opacity:0;transform:translateY(20px);}
  to  {opacity:1;transform:translateY(0);}
}

/* Pure fade (supporting copy, labels) */
.f{opacity:0;}
.slide.active .f{animation:fIn .95s var(--ease) both;}
.slide.active .f[data-d="0"]{animation-delay:var(--d0);}
.slide.active .f[data-d="1"]{animation-delay:var(--d1);}
.slide.active .f[data-d="2"]{animation-delay:var(--d2);}
.slide.active .f[data-d="3"]{animation-delay:var(--d3);}
.slide.active .f[data-d="4"]{animation-delay:var(--d4);}
.slide.active .f[data-d="5"]{animation-delay:var(--d5);}
.slide.active .f[data-d="6"]{animation-delay:var(--d6);}
@keyframes fIn{from{opacity:0;}to{opacity:1;}}

/* Horizontal clip-reveal (lines, dividers, rules) */
.r{clip-path:inset(0 100% 0 0);}
.slide.active .r{animation:rIn .9s var(--ease) both;}
.slide.active .r[data-d="0"]{animation-delay:var(--d0);}
.slide.active .r[data-d="1"]{animation-delay:var(--d1);}
.slide.active .r[data-d="2"]{animation-delay:var(--d2);}
.slide.active .r[data-d="3"]{animation-delay:var(--d3);}
@keyframes rIn{
  from{clip-path:inset(0 100% 0 0);}
  to  {clip-path:inset(0 0% 0 0);}
}

/* Scale-in (icons, tags, numbers) */
.s{opacity:0;transform:scale(.85);}
.slide.active .s{animation:sIn2 .65s var(--ease-out) both;}
.slide.active .s[data-d="0"]{animation-delay:var(--d0);}
.slide.active .s[data-d="1"]{animation-delay:var(--d1);}
.slide.active .s[data-d="2"]{animation-delay:var(--d2);}
.slide.active .s[data-d="3"]{animation-delay:var(--d3);}
@keyframes sIn2{
  from{opacity:0;transform:scale(.82);}
  to  {opacity:1;transform:scale(1);}
}

/* ─── SHARED TYPOGRAPHY ─── */
.eyebrow{
  font-family:var(--mono);font-size:.56rem;
  letter-spacing:.28em;text-transform:uppercase;
  color:var(--y);opacity:.75;
}
.tag-pill{
  display:inline-flex;
  background:var(--y);color:var(--bg);
  font-family:var(--mono);font-size:.5rem;
  letter-spacing:.12em;text-transform:uppercase;
  padding:.2rem .65rem;border-radius:2px;
  font-weight:500;
}
.tag-outline{
  display:inline-flex;
  border:1px solid var(--yline);color:var(--y);
  font-family:var(--mono);font-size:.5rem;
  letter-spacing:.12em;text-transform:uppercase;
  padding:.2rem .65rem;border-radius:2px;
}
.hdline{
  font-family:var(--serif);
  font-size:clamp(3.5rem,9vw,11rem);
  font-weight:300;
  line-height:.88;
  color:var(--w);
  letter-spacing:-.01em;
  display:block;
}
.hdline.italic{font-style:italic;}
.hdline em{font-style:italic;color:var(--y);}
.hdline strong{font-weight:600;font-style:normal;}
.body-copy{
  font-family:var(--sans);
  font-size:clamp(.8rem,.95vw,.95rem);
  font-weight:300;color:var(--g);
  line-height:1.8;letter-spacing:.01em;
  display:block;
}
.rule-y{
  display:block;
  background:var(--y);opacity:.4;
  height:1px;
}
.rule-g{
  display:block;
  background:var(--g2);
  height:1px;
}

/* ─── COMMON LAYOUT ─── */
.center-col{
  text-align:center;
  display:flex;flex-direction:column;align-items:center;
  gap:.75rem;
}
.split{
  width:88vw;max-width:1240px;
  display:grid;grid-template-columns:1fr 1fr;
  gap:7vw;align-items:center;
}
.content-col{
  display:flex;flex-direction:column;
  gap:1rem;
}
.feature-list{
  list-style:none;
  display:flex;flex-direction:column;gap:.5rem;
  margin-top:.25rem;
}
.feature-list li{
  font-family:var(--sans);font-size:.875rem;
  color:var(--w);font-weight:300;
  display:flex;align-items:center;gap:.75rem;
}
.feature-list li::before{
  content:'';
  width:16px;height:1px;
  background:var(--y);flex-shrink:0;
}

/* ════════════════════════════════════════
   S1 — HERO
════════════════════════════════════════ */
#s1{background:var(--bg);}
.s1-bg{position:absolute;inset:0;overflow:hidden;}
.s1-dots{
  position:absolute;inset:-15%;
  background-image:radial-gradient(circle,rgba(255,214,0,.5) 1px,transparent 1px);
  background-size:52px 52px;
  opacity:.038;
  animation:kBurns 22s ease-in-out infinite alternate;
}
@keyframes kBurns{
  from{transform:scale(1) translate(0,0);}
  to  {transform:scale(1.1) translate(-3%,2%);}
}
.s1-glow{
  position:absolute;
  bottom:-10%;left:50%;transform:translateX(-50%);
  width:80vw;height:55vh;
  background:radial-gradient(ellipse,rgba(255,214,0,.055) 0%,transparent 62%);
  animation:glowBreath 7s ease-in-out infinite alternate;
}
@keyframes glowBreath{from{opacity:.7;}to{opacity:1;}}
.s1-h{
  font-family:var(--serif);
  font-size:clamp(5.5rem,14vw,16rem);
  font-weight:300;font-style:italic;
  line-height:.85;letter-spacing:-.015em;
  color:var(--w);display:block;
}
.s1-h em{font-style:normal;font-weight:600;color:var(--y);}
.s1-byline{
  font-family:var(--mono);font-size:.52rem;
  letter-spacing:.3em;text-transform:uppercase;
  color:var(--g);display:block;
  margin-top:.5rem;
}

/* ════════════════════════════════════════
   S2 — MISSION STATEMENT
════════════════════════════════════════ */
#s2{background:var(--s1);}
.s2-lede{
  font-family:var(--serif);
  font-size:clamp(2rem,5vw,5.5rem);
  font-weight:300;font-style:italic;
  line-height:1.05;letter-spacing:-.01em;
  color:var(--g);display:block;
}
.s2-punch{
  font-family:var(--serif);
  font-size:clamp(2rem,5vw,5.5rem);
  font-weight:600;
  line-height:1.05;letter-spacing:-.01em;
  color:var(--w);display:block;
}
.s2-punch em{color:var(--y);font-style:normal;}
.s2-kicker{
  font-family:var(--sans);
  font-size:clamp(.75rem,.9vw,.9rem);
  font-weight:300;color:var(--g);
  line-height:1.8;letter-spacing:.02em;
  display:block;max-width:560px;
}

/* ════════════════════════════════════════
   S3 — THE PROBLEM (big number)
════════════════════════════════════════ */
#s3{background:var(--bg);}
.s3-big{
  font-family:var(--serif);
  font-size:clamp(14rem,34vw,42rem);
  font-weight:300;line-height:.78;
  letter-spacing:-.04em;color:var(--w);
  display:block;
}
.s3-pct{font-size:.3em;vertical-align:super;color:var(--y);font-weight:300;}
.s3-cap{
  font-family:var(--serif);
  font-size:clamp(1.25rem,2.2vw,2.5rem);
  font-weight:300;font-style:italic;
  color:var(--g);display:block;
  letter-spacing:-.005em;max-width:480px;
}

/* ════════════════════════════════════════
   S4 — THE INSIGHT
════════════════════════════════════════ */
#s4{background:var(--s1);}
.s4-line1{
  font-family:var(--serif);
  font-size:clamp(2.25rem,5.8vw,7rem);
  font-weight:300;line-height:1.0;
  color:var(--g);letter-spacing:-.01em;
  display:block;
}
.s4-line2{
  font-family:var(--serif);
  font-size:clamp(2.25rem,5.8vw,7rem);
  font-weight:600;font-style:italic;
  line-height:1.0;color:var(--w);
  letter-spacing:-.01em;display:block;
}
.s4-line2 span{color:var(--y);}
.s4-stat{
  font-family:var(--mono);font-size:.6rem;
  letter-spacing:.22em;text-transform:uppercase;
  color:var(--g);display:block;
}
.s4-stat b{color:var(--y);font-weight:400;}

/* ════════════════════════════════════════
   S5 — FUTUREGAME
════════════════════════════════════════ */
#s5{background:var(--bg);}
.s5-glow{
  position:absolute;top:10%;right:0%;
  width:55vw;height:80vh;
  background:radial-gradient(ellipse,rgba(255,214,0,.05) 0%,transparent 60%);
  pointer-events:none;
}
.s5-name{
  font-family:var(--serif);
  font-size:clamp(4rem,8.5vw,10.5rem);
  font-weight:600;line-height:.83;
  color:var(--w);letter-spacing:-.01em;
  display:block;
}
.s5-desc{
  font-family:var(--sans);font-size:clamp(.8rem,1vw,1rem);
  font-weight:300;color:var(--g);line-height:1.8;
  display:block;max-width:400px;
}
/* board visual */
.board{
  display:grid;
  grid-template-columns:repeat(8,1fr);
  grid-template-rows:repeat(6,1fr);
  gap:5px;height:420px;
}
.gc{
  border-radius:4px;
  background:var(--card);
  border:1px solid rgba(255,214,0,.065);
  transition:background .6s,border-color .6s,box-shadow .6s;
}
.gc.lit{background:rgba(255,214,0,.1);border-color:rgba(255,214,0,.22);}
.gc.hot{
  background:rgba(255,214,0,.28);
  border-color:rgba(255,214,0,.55);
  box-shadow:0 0 14px rgba(255,214,0,.18);
}
.gc.bright{
  background:var(--y);border-color:var(--y);
  box-shadow:0 0 24px rgba(255,214,0,.38);
}

/* ════════════════════════════════════════
   S6 — ESCAPE ROOM ON LOCATION
════════════════════════════════════════ */
#s6{background:var(--s1);}
.prod-geo{
  position:relative;height:420px;
  display:flex;align-items:center;justify-content:center;
}
/* Concentric hexagons */
.hex-ring{
  position:absolute;
  border:1px solid var(--yline);
  clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
}
.hex1{width:340px;height:340px;}
.hex2{width:240px;height:240px;border-color:rgba(255,214,0,.25);animation:hexSpin 20s linear infinite;}
.hex3{width:140px;height:140px;border-color:rgba(255,214,0,.4);animation:hexSpin 12s linear infinite reverse;}
.hex-center{
  width:60px;height:60px;background:var(--y);
  clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
}
@keyframes hexSpin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.hex-stat{
  position:absolute;
  font-family:var(--mono);font-size:.56rem;
  letter-spacing:.14em;text-transform:uppercase;
  color:var(--y);opacity:.7;
}
.hex-stat.top{top:18px;left:50%;transform:translateX(-50%);}
.hex-stat.bl{bottom:40px;left:30px;}
.hex-stat.br{bottom:40px;right:30px;}

/* ════════════════════════════════════════
   S7 — ESCAPE BOX
════════════════════════════════════════ */
#s7{background:var(--bg);}
.box-visual{
  position:relative;height:420px;
  display:flex;align-items:center;justify-content:center;
}
/* Isometric box illusion */
.iso-box{position:relative;width:280px;height:280px;}
.iso-top{
  position:absolute;
  top:0;left:20%;width:60%;height:30%;
  background:var(--y);
  clip-path:polygon(0 50%,50% 0,100% 50%,50% 100%);
  opacity:.9;
}
.iso-left{
  position:absolute;
  bottom:0;left:0;width:50%;height:70%;
  background:rgba(255,214,0,.2);
  border:1px solid var(--yline);
}
.iso-right{
  position:absolute;
  bottom:0;right:0;width:50%;height:70%;
  background:rgba(255,214,0,.08);
  border:1px solid rgba(255,214,0,.1);
}
.box-badge{
  position:absolute;
  font-family:var(--mono);font-size:.5rem;
  letter-spacing:.14em;text-transform:uppercase;
  color:var(--g);
}
.box-badge.t1{top:20px;right:20px;}
.box-badge.t2{bottom:60px;left:20px;}
.box-badge.t3{top:50%;right:20px;transform:translateY(-50%);}

/* ════════════════════════════════════════
   S8 — ONBOARDING GAME
════════════════════════════════════════ */
#s8{background:var(--s1);}
.steps-visual{
  position:relative;height:420px;width:100%;
  display:flex;align-items:center;justify-content:center;
}
.step-path{
  display:flex;flex-direction:column;
  align-items:center;gap:0;
  position:relative;
}
.step-path::before{
  content:'';
  position:absolute;
  left:50%;top:0;bottom:0;
  width:1px;background:var(--g2);
  transform:translateX(-50%);
}
.step-node{
  position:relative;z-index:2;
  width:44px;height:44px;border-radius:50%;
  background:var(--card);border:1px solid var(--yline);
  display:flex;align-items:center;justify-content:center;
  font-family:var(--mono);font-size:.6rem;color:var(--y);
  margin:12px 0;
}
.step-node.active{background:var(--y);color:var(--bg);border-color:var(--y);}
.step-label{
  position:absolute;left:56px;
  font-family:var(--sans);font-size:.8rem;
  color:var(--g);white-space:nowrap;
  font-weight:300;
}
.step-node:nth-child(1) .step-label{top:10px;}
.step-node:nth-child(2) .step-label{top:10px;}
.step-node:nth-child(3) .step-label{top:10px;}
.step-node:nth-child(4) .step-label{top:10px;}

/* ════════════════════════════════════════
   S9 — MICROLEARNING
════════════════════════════════════════ */
#s9{background:var(--bg);}
.micro-visual{
  position:relative;height:420px;width:100%;
  display:flex;align-items:center;justify-content:center;
}
/* Phone frame mockup */
.phone{
  width:200px;height:380px;
  background:var(--card);
  border:1px solid var(--yline);
  border-radius:24px;
  position:relative;overflow:hidden;
  display:flex;flex-direction:column;
  align-items:center;padding:20px 16px;
}
.phone::before{
  content:'';
  position:absolute;top:12px;left:50%;transform:translateX(-50%);
  width:40px;height:4px;
  background:var(--g2);border-radius:2px;
}
.phone-bar{
  width:100%;height:6px;
  background:var(--y);border-radius:2px;
  margin-top:28px;
}
.phone-bar.s2{width:75%;background:var(--g2);margin-top:8px;}
.phone-bar.s3{width:90%;background:var(--g2);}
.phone-module{
  width:100%;margin-top:12px;
  background:var(--s1);border:1px solid var(--g2);
  border-radius:6px;padding:8px 10px;
}
.pm-tag{font-family:var(--mono);font-size:.46rem;letter-spacing:.12em;text-transform:uppercase;color:var(--y);}
.pm-title{font-family:var(--sans);font-size:.72rem;color:var(--w);margin-top:2px;font-weight:400;}
.pm-time{font-family:var(--mono);font-size:.44rem;color:var(--g);margin-top:4px;letter-spacing:.08em;}
.phone-progress{
  width:100%;margin-top:12px;
  display:flex;align-items:center;gap:6px;
}
.pp-bar{flex:1;height:3px;background:var(--g2);border-radius:2px;}
.pp-bar.done{background:var(--y);}
.pp-pct{font-family:var(--mono);font-size:.48rem;color:var(--y);}
/* Floating stat cards */
.float-card{
  position:absolute;
  background:var(--s1);
  border:1px solid var(--yline);
  border-radius:6px;padding:10px 14px;
  white-space:nowrap;
}
.fc-num{
  font-family:var(--mono);font-size:1.25rem;
  color:var(--y);letter-spacing:-.02em;line-height:1;
}
.fc-lbl{
  font-family:var(--mono);font-size:.48rem;
  text-transform:uppercase;letter-spacing:.12em;
  color:var(--g);margin-top:2px;
}
.float-card.fc1{top:20px;right:20px;}
.float-card.fc2{bottom:30px;right:10px;}
.float-card.fc3{bottom:80px;left:10px;}

/* ════════════════════════════════════════
   S10 — ALL 9 PRODUCTS
════════════════════════════════════════ */
#s10{background:var(--s1);}
.s10-inner{width:88vw;max-width:1100px;}
.s10-hdr{
  display:flex;align-items:baseline;justify-content:space-between;
  padding-bottom:1.25rem;border-bottom:1px solid var(--g2);
  margin-bottom:.0625rem;
}
.s10-title{
  font-family:var(--serif);
  font-size:clamp(2rem,4.5vw,5rem);
  font-weight:300;color:var(--w);
  line-height:.92;letter-spacing:-.01em;
}
.s10-title em{font-style:italic;color:var(--y);}
.s10-count{
  font-family:var(--mono);font-size:.54rem;
  letter-spacing:.2em;text-transform:uppercase;color:var(--g);
}
.pgrid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:1px;background:var(--g2);
  border:1px solid var(--g2);border-radius:3px;overflow:hidden;
}
.pi{
  background:var(--s1);padding:1.125rem 1.375rem;
  position:relative;overflow:hidden;
  transition:background .2s;
}
.pi:hover{background:var(--card);}
.pi::after{
  content:'';position:absolute;
  bottom:0;left:0;right:0;height:1.5px;
  background:var(--y);
  transform:scaleX(0);transform-origin:left;
  transition:transform .28s var(--ease);
}
.pi:hover::after{transform:scaleX(1);}
.pi-idx{
  font-family:var(--mono);font-size:.46rem;
  text-transform:uppercase;letter-spacing:.18em;
  color:var(--g);display:block;margin-bottom:.35rem;
}
.pi-name{
  font-family:var(--serif);
  font-size:clamp(.95rem,1.4vw,1.5rem);
  font-weight:400;color:var(--w);
  line-height:1.2;letter-spacing:-.004em;
}
.pi.star .pi-name{color:var(--y);}
/* stagger */
.slide.active .pi{animation:piSlide .5s var(--ease-out) both;}
.slide.active .pi:nth-child(1){animation-delay:.18s;}
.slide.active .pi:nth-child(2){animation-delay:.22s;}
.slide.active .pi:nth-child(3){animation-delay:.26s;}
.slide.active .pi:nth-child(4){animation-delay:.30s;}
.slide.active .pi:nth-child(5){animation-delay:.34s;}
.slide.active .pi:nth-child(6){animation-delay:.38s;}
.slide.active .pi:nth-child(7){animation-delay:.42s;}
.slide.active .pi:nth-child(8){animation-delay:.46s;}
.slide.active .pi:nth-child(9){animation-delay:.50s;}
@keyframes piSlide{
  from{opacity:0;transform:translateY(10px);}
  to  {opacity:1;transform:translateY(0);}
}

/* ════════════════════════════════════════
   S11 — CLIENTS + TESTIMONIAL
════════════════════════════════════════ */
#s11{background:var(--bg);}
.s11-inner{width:88vw;max-width:1100px;}
.s11-split{display:grid;grid-template-columns:1fr 1fr;gap:6vw;align-items:start;}
.big-num{
  font-family:var(--serif);
  font-size:clamp(7rem,16vw,20rem);
  font-weight:300;line-height:.8;
  letter-spacing:-.04em;color:var(--w);
  display:block;
}
.big-num sup{font-size:.32em;vertical-align:super;color:var(--y);}
.clients-label{
  font-family:var(--mono);font-size:.54rem;
  letter-spacing:.24em;text-transform:uppercase;
  color:var(--g);display:block;margin-bottom:1rem;
}
.big-sub{
  font-family:var(--serif);
  font-size:clamp(1rem,1.8vw,2rem);
  font-weight:300;font-style:italic;
  color:var(--g);display:block;
  margin-bottom:1.75rem;
}
.cstrip{display:flex;flex-wrap:wrap;gap:6px;}
.cn{
  font-family:var(--mono);font-size:.52rem;
  letter-spacing:.1em;text-transform:uppercase;
  color:var(--g);padding:.32rem .8rem;
  border:1px solid var(--g2);border-radius:2px;
  transition:border-color .2s,color .2s;
  opacity:0;
}
.cn:hover{border-color:var(--yline);color:var(--y);}
.slide.active .cn{animation:cnPop .4s var(--ease-out) both;}
.slide.active .cn:nth-child(1){animation-delay:.50s;}
.slide.active .cn:nth-child(2){animation-delay:.54s;}
.slide.active .cn:nth-child(3){animation-delay:.58s;}
.slide.active .cn:nth-child(4){animation-delay:.62s;}
.slide.active .cn:nth-child(5){animation-delay:.66s;}
.slide.active .cn:nth-child(6){animation-delay:.70s;}
.slide.active .cn:nth-child(7){animation-delay:.74s;}
.slide.active .cn:nth-child(8){animation-delay:.78s;}
.slide.active .cn:nth-child(9){animation-delay:.82s;}
.slide.active .cn:nth-child(10){animation-delay:.86s;}
.slide.active .cn:nth-child(11){animation-delay:.90s;}
.slide.active .cn:nth-child(12){animation-delay:.94s;}
@keyframes cnPop{from{opacity:0;transform:scale(.88);}to{opacity:1;transform:scale(1);}}
/* Testimonial right */
.tcard{
  background:var(--s2);border:1px solid var(--yline);
  border-radius:6px;padding:1.75rem 2rem;
}
.tq{
  font-family:var(--serif);
  font-size:clamp(1rem,1.4vw,1.5rem);
  font-weight:300;font-style:italic;
  color:var(--w);line-height:1.7;
  display:block;margin-bottom:1.25rem;
}
.tauthor{
  font-family:var(--sans);
  font-size:.875rem;font-weight:500;
  color:var(--w);display:block;
}
.trole{
  font-family:var(--mono);font-size:.52rem;
  letter-spacing:.12em;text-transform:uppercase;
  color:var(--g);display:block;margin-top:.25rem;
}

/* ════════════════════════════════════════
   S12 — CTA (yellow)
════════════════════════════════════════ */
#s12{background:var(--y);}
.s12-ring1{
  position:absolute;top:-55%;left:50%;transform:translateX(-50%);
  width:140vw;height:140vw;border-radius:50%;
  border:1px solid rgba(0,0,0,.055);pointer-events:none;
  animation:ringBreath 6s ease-in-out infinite;
}
.s12-ring2{
  position:absolute;top:-30%;left:50%;transform:translateX(-50%);
  width:85vw;height:85vw;border-radius:50%;
  border:1px solid rgba(0,0,0,.04);pointer-events:none;
  animation:ringBreath 6s ease-in-out infinite .4s;
}
@keyframes ringBreath{
  0%,100%{transform:translateX(-50%) scale(1);}
  50%{transform:translateX(-50%) scale(1.015);}
}
.s12-inner{
  position:relative;z-index:2;
  text-align:center;padding:0 8vw;
}
.s12-h{
  font-family:var(--serif);
  font-size:clamp(5rem,14vw,17rem);
  font-weight:300;font-style:italic;
  line-height:.83;color:var(--bg);
  letter-spacing:-.02em;display:block;
  margin-bottom:2.5rem;
}
.s12-cta{
  display:inline-flex;align-items:center;gap:.75rem;
  background:var(--bg);color:var(--y);
  font-family:var(--sans);font-size:.9375rem;font-weight:500;
  padding:.875rem 2.25rem;border-radius:3px;
  text-decoration:none;
  transition:background .2s,transform .15s;
}
.s12-cta:hover{background:#111;transform:translateY(-2px);}
.s12-cta svg{transition:transform .2s;}
.s12-cta:hover svg{transform:translateX(5px);}
.s12-url{
  font-family:var(--mono);font-size:.52rem;
  letter-spacing:.22em;text-transform:uppercase;
  color:rgba(0,0,0,.32);display:block;margin-top:2rem;
}
.s12-tagline{
  font-family:var(--sans);font-size:.875rem;
  color:rgba(0,0,0,.5);font-weight:300;
  display:block;margin-bottom:2rem;
}
</style>
</head>
<body>

<!-- CHROME -->
<div id="grain"></div>
<div id="shutter"></div>
<div id="pbar"></div>

<div id="logo"><div class="lhex"></div><span class="lname">HELDEN</span></div>
<div id="slidenum"><b>01</b> / 12</div>

<div id="dots">
  <div class="dot on"  data-i="0"></div>
  <div class="dot"     data-i="1"></div>
  <div class="dot"     data-i="2"></div>
  <div class="dot"     data-i="3"></div>
  <div class="dot"     data-i="4"></div>
  <div class="dot"     data-i="5"></div>
  <div class="dot"     data-i="6"></div>
  <div class="dot"     data-i="7"></div>
  <div class="dot"     data-i="8"></div>
  <div class="dot"     data-i="9"></div>
  <div class="dot"     data-i="10"></div>
  <div class="dot"     data-i="11"></div>
</div>

<div id="cue"><div class="cue-tick"></div><span class="cue-lbl">scroll</span></div>

<!-- ═════════════ SLIDES ═════════════ -->
<div id="slider">

  <!-- S1 · HERO ─────────────────── -->
  <div class="slide active" id="s1">
    <div class="s1-bg"><div class="s1-dots"></div><div class="s1-glow"></div></div>
    <div class="center-col" style="gap:.5rem;">
      <span class="eyebrow f" data-d="0">Helden Inc. · Haarlem, Netherlands</span>
      <span class="s1-h u" data-d="1">We don't<br>do <em>workshops</em>.</span>
      <span class="s1-byline f" data-d="2">Game-Based Learning & Internal Communication · Since 2010</span>
    </div>
  </div>

  <!-- S2 · MISSION ─────────────────── -->
  <div class="slide" id="s2">
    <div class="center-col" style="max-width:900px;padding:0 6vw;gap:.6rem;">
      <span class="eyebrow f" data-d="0">Our mission</span>
      <span class="s2-lede u" data-d="1">Boring training, endless PowerPoints,<br>passive audiences —</span>
      <span class="s2-punch u" data-d="2">We replace all of it<br>with <em>unforgettable games</em>.</span>
      <span class="rule-y r" data-d="3" style="width:48px;margin:1rem 0;"></span>
      <span class="s2-kicker f" data-d="4">We help HR and communications teams make serious topics fun, visual, and highly impactful — through escape rooms, simulations, microlearning, and events that people actually remember.</span>
    </div>
  </div>

  <!-- S3 · THE PROBLEM ─────────────────── -->
  <div class="slide" id="s3">
    <div class="split" style="align-items:flex-end;padding:0 4vw;">
      <div>
        <span class="eyebrow f" data-d="0" style="margin-bottom:1.25rem;display:block;">The problem</span>
        <span class="s3-big u" data-d="1">10<span class="s3-pct">%</span></span>
      </div>
      <div style="padding-bottom:2.5rem;">
        <span class="rule-y r" data-d="2" style="width:100%;display:block;margin-bottom:1.5rem;"></span>
        <span class="s3-cap u" data-d="3">of information is retained after a traditional presentation or workshop.</span>
        <span class="body-copy f" data-d="4" style="margin-top:1rem;">The other 90% is forgotten within days. Your message, your strategy, your culture — gone. There's a better way.</span>
      </div>
    </div>
  </div>

  <!-- S4 · THE INSIGHT ─────────────────── -->
  <div class="slide" id="s4">
    <div class="center-col" style="max-width:900px;padding:0 6vw;gap:.6rem;">
      <span class="eyebrow f" data-d="0">The insight</span>
      <span class="s4-line1 u" data-d="1">People don't learn by watching.</span>
      <span class="s4-line2 u" data-d="2">People learn by <span>playing</span>.</span>
      <span class="rule-y r" data-d="3" style="width:40px;margin:1.25rem 0;"></span>
      <span class="s4-stat f" data-d="4"><b>3× higher</b> knowledge retention · <b>100%</b> active participation · <b>−60%</b> resistance to change</span>
    </div>
  </div>

  <!-- S5 · FUTUREGAME ─────────────────── -->
  <div class="slide" id="s5">
    <div class="s5-glow"></div>
    <div class="split">
      <div class="content-col">
        <span class="tag-pill s" data-d="0">🏆 Bestseller</span>
        <span class="s5-name u" data-d="1">Future<br>Game</span>
        <span class="s5-desc f" data-d="2">An interactive strategic simulation that lets your team experience possible futures of your organisation — not just discuss them. Ideas and insights are automatically saved and sent to you periodically.</span>
        <ul class="feature-list f" data-d="3">
          <li>Strategy, change management & new policy</li>
          <li>4 to 200 participants · Half or full day</li>
          <li>Online via browser or on location</li>
          <li>Fully automated with built-in hints</li>
          <li>100% tailor-made — 48h concept delivery</li>
        </ul>
        <span class="tag-outline f" data-d="4" style="width:fit-content;margin-top:.5rem;">Max 2 clients per month · Waitlist</span>
      </div>
      <div class="board f" data-d="2" id="board"></div>
    </div>
  </div>

  <!-- S6 · ESCAPE ROOM ON LOCATION ─────────────────── -->
  <div class="slide" id="s6">
    <div class="split">
      <div class="content-col">
        <span class="tag-pill s" data-d="0">On Location</span>
        <span class="hdline u" data-d="1">Escape<br>Room<br><em>on Location</em></span>
        <span class="body-copy f" data-d="2">A professional escape room at your office or event space. We handle everything — concept, build-up, hosting, and tear-down. Fully themed to your organisation, culture, or learning goals.</span>
        <ul class="feature-list f" data-d="3">
          <li>20 to 120 participants simultaneously</li>
          <li>60–90 minute sessions</li>
          <li>Professional hosts from theater & film</li>
          <li>Guided by app with hints & live leaderboard</li>
          <li>Custom themes & corporate content</li>
        </ul>
      </div>
      <div class="prod-geo f" data-d="1">
        <div class="hex-ring hex1"></div>
        <div class="hex-ring hex2"></div>
        <div class="hex-ring hex3"></div>
        <div class="hex-center"></div>
        <span class="hex-stat top">120 players</span>
        <span class="hex-stat bl">60–90 min</span>
        <span class="hex-stat br">All locations</span>
      </div>
    </div>
  </div>

  <!-- S7 · ESCAPE BOX ─────────────────── -->
  <div class="slide" id="s7">
    <div class="split">
      <div class="box-visual f" data-d="0">
        <div class="iso-box">
          <div class="iso-top"></div>
          <div class="iso-left"></div>
          <div class="iso-right"></div>
        </div>
        <span class="box-badge t1">4–6 per box</span>
        <span class="box-badge t2">30 / 60 / 90 min</span>
        <span class="box-badge t3">Up to 300 players</span>
      </div>
      <div class="content-col">
        <span class="tag-pill s" data-d="0">Portable</span>
        <span class="hdline u" data-d="1">Escape<br><em>Box</em></span>
        <span class="body-copy f" data-d="2">An escape room packed into a box. Teams of 4–6 solve puzzles, riddles, and challenges within a set time. Multiple boxes run simultaneously for groups of up to 300 participants. Indoor and outdoor. Dutch and English.</span>
        <ul class="feature-list f" data-d="3">
          <li>Groups of 20 to 300 participants</li>
          <li>Standard themes or fully personalised</li>
          <li>Guided by enthusiastic hosts & trainers</li>
          <li>Complete build-up & dismantling included</li>
          <li>Ideal for team events, conferences & training</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- S8 · ONBOARDING GAME ─────────────────── -->
  <div class="slide" id="s8">
    <div class="split">
      <div class="content-col">
        <span class="tag-pill s" data-d="0">Day One</span>
        <span class="hdline u" data-d="1">Onboarding<br><em>Game</em></span>
        <span class="body-copy f" data-d="2">Turn day one from nerve-wracking to unforgettable. New employees experience your culture, values, and colleagues through a game — breaking the ice and building connection from the very first hour.</span>
        <ul class="feature-list f" data-d="3">
          <li>Culture, values & organisational structure</li>
          <li>Scalable for large cohorts</li>
          <li>Digital or physical format</li>
          <li>Reusable — adapt for different teams</li>
          <li>Developed with UMC Utrecht & DSM</li>
        </ul>
      </div>
      <div class="steps-visual f" data-d="1">
        <div class="step-path">
          <div class="step-node active">1<span class="step-label">Day one welcome</span></div>
          <div class="step-node active">2<span class="step-label">Culture deep-dive</span></div>
          <div class="step-node">3<span class="step-label">Meet your team</span></div>
          <div class="step-node">4<span class="step-label">First challenge</span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- S9 · MICROLEARNING ─────────────────── -->
  <div class="slide" id="s9">
    <div class="split">
      <div class="micro-visual f" data-d="0">
        <div class="phone">
          <div class="phone-bar"></div>
          <div class="phone-bar s2"></div>
          <div class="phone-bar s3"></div>
          <div class="phone-module">
            <span class="pm-tag">Module 3 of 8</span>
            <span class="pm-title">Sustainability Strategy</span>
            <span class="pm-time">⏱ 5 min · Escape format</span>
          </div>
          <div class="phone-module" style="margin-top:8px;">
            <span class="pm-tag">Quick Challenge</span>
            <span class="pm-title">New Policy Update</span>
            <span class="pm-time">⏱ 3 min · Quiz format</span>
          </div>
          <div class="phone-progress">
            <div class="pp-bar done"></div>
            <div class="pp-bar done"></div>
            <div class="pp-bar done"></div>
            <div class="pp-bar"></div>
            <div class="pp-bar"></div>
            <span class="pp-pct">62%</span>
          </div>
        </div>
        <div class="float-card fc1"><div class="fc-num">2–10</div><div class="fc-lbl">min per module</div></div>
        <div class="float-card fc2"><div class="fc-num">3×</div><div class="fc-lbl">retention lift</div></div>
        <div class="float-card fc3"><div class="fc-num">∞</div><div class="fc-lbl">reusable</div></div>
      </div>
      <div class="content-col">
        <span class="tag-pill s" data-d="0">Always On</span>
        <span class="hdline u" data-d="1">Micro<br><em>Learning</em></span>
        <span class="body-copy f" data-d="2">Short, powerful learning modules that deliver the right knowledge at the right moment. Monthly escape-room-style challenges in your browser — no download needed. Developed with RVKO, integrates with any LMS.</span>
        <ul class="feature-list f" data-d="3">
          <li>2–15 minutes per module</li>
          <li>Monthly game-based knowledge updates</li>
          <li>Custom content per department or theme</li>
          <li>Mobile-first, no installation required</li>
          <li>Compliance, culture, skills & beyond</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- S10 · ALL 9 PRODUCTS ─────────────────── -->
  <div class="slide" id="s10">
    <div class="s10-inner">
      <div class="s10-hdr">
        <span class="s10-title u" data-d="0">Nine ways to<br>make them <em>remember</em>.</span>
        <span class="s10-count f" data-d="1">09 products</span>
      </div>
      <div class="pgrid">
        <div class="pi star"><span class="pi-idx">01</span><span class="pi-name">FutureGame</span></div>
        <div class="pi"><span class="pi-idx">02</span><span class="pi-name">Escape Room on Location</span></div>
        <div class="pi"><span class="pi-idx">03</span><span class="pi-name">Custom Escape Room</span></div>
        <div class="pi"><span class="pi-idx">04</span><span class="pi-name">Escape Box</span></div>
        <div class="pi"><span class="pi-idx">05</span><span class="pi-name">In-Company Training Box</span></div>
        <div class="pi"><span class="pi-idx">06</span><span class="pi-name">Onboarding Game</span></div>
        <div class="pi"><span class="pi-idx">07</span><span class="pi-name">GamePlan</span></div>
        <div class="pi"><span class="pi-idx">08</span><span class="pi-name">Micro Learning</span></div>
        <div class="pi"><span class="pi-idx">09</span><span class="pi-name">Learning Events</span></div>
      </div>
    </div>
  </div>

  <!-- S11 · CLIENTS ─────────────────── -->
  <div class="slide" id="s11">
    <div class="s11-inner">
      <div class="s11-split">
        <div>
          <span class="clients-label f" data-d="0">Trusted by</span>
          <span class="big-num u" data-d="1">200<sup>+</sup></span>
          <span class="big-sub f" data-d="2">enterprise organisations across the Benelux and beyond</span>
          <div class="cstrip">
            <span class="cn">Heineken</span><span class="cn">KLM</span>
            <span class="cn">ING</span><span class="cn">ABN AMRO</span>
            <span class="cn">EY</span><span class="cn">Schiphol</span>
            <span class="cn">L'Oréal</span><span class="cn">Disney</span>
            <span class="cn">BMW</span><span class="cn">Deloitte</span>
            <span class="cn">ArboNed</span><span class="cn">UMC Utrecht</span>
          </div>
        </div>
        <div class="content-col" style="gap:1.25rem;">
          <span class="eyebrow f" data-d="1">What clients say</span>
          <div class="tcard f" data-d="2">
            <span class="tq">"Holy Sh*t, the game is amazing! The students were so busy with the puzzles they didn't have time to ask anything."</span>
            <span class="tauthor">Eva Kleine</span>
            <span class="trole">Company Doctor · ArboNed</span>
          </div>
          <div class="tcard f" data-d="3">
            <span class="tq">"Together with Helden Inc. we developed a great game as part of our onboarding program. Our team was very enthusiastic."</span>
            <span class="tauthor">Nicole Blom</span>
            <span class="trole">L&amp;D Manager · UMC Utrecht</span>
          </div>
          <div class="tcard f" data-d="4">
            <span class="tq">"The event was enjoyed by almost everyone. Your commitment, creativity and energy contributed to a very successful event!"</span>
            <span class="tauthor">Jeroen Kluytman</span>
            <span class="trole">Manager Employability · DSM</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- S12 · CTA ─────────────────── -->
  <div class="slide" id="s12">
    <div class="s12-ring1"></div>
    <div class="s12-ring2"></div>
    <div class="s12-inner">
      <span class="s12-h u" data-d="0">Make them<br>remember.</span>
      <span class="s12-tagline f" data-d="1">Free consultation · Concept within 48 hours · No commitment</span>
      <a class="s12-cta f" data-d="2" href="https://helden-inc.com/en/" target="_blank">
        Plan your demo
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path d="M2.5 7h9M8 3.5L11.5 7 8 10.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </a>
      <span class="s12-url f" data-d="3">helden-inc.com</span>
    </div>
  </div>

</div><!-- /slider -->

<script>
(function(){
'use strict';

const TOTAL    = 12;
const IN_DUR   = 1050;
const SHUTTER  = 70;

const shutter  = document.getElementById('shutter');
const pbar     = document.getElementById('pbar');
const logo     = document.getElementById('logo');
const snum     = document.getElementById('slidenum');
const dotsEl   = document.getElementById('dots');
const cue      = document.getElementById('cue');
const slides   = document.querySelectorAll('.slide');
const dots     = document.querySelectorAll('.dot');

let cur  = 0;
let busy = false;

/* ── Build game board ── */
(function(){
  const b = document.getElementById('board');
  if(!b) return;
  const LIT    = new Set([2,3,9,10,11,17,18,19,25,26,27,33,34,35]);
  const HOT    = new Set([10,11,18,19,26,27]);
  const BRIGHT = new Set([18,19]);
  for(let i=0;i<48;i++){
    const c=document.createElement('div');
    c.className='gc'+
      (BRIGHT.has(i)?' bright':HOT.has(i)?' hot':LIT.has(i)?' lit':'');
    b.appendChild(c);
  }
})();

/* ── Board animation waves ── */
let boardTick = null;
const WAVES = [
  [1,2,9,10],[9,10,17,18],[17,18,25,26],[25,26,33,34],
  [2,3,10,11],[18,19,26,27],[3,11,19,27],[0,8,16,24],
  [4,12,20,28],[5,13,21,29],[6,14,22,30],[7,15,23,31],
];
let wi=0;
function boardStart(){
  clearInterval(boardTick);
  boardTick=setInterval(()=>{
    document.querySelectorAll('.gc.hot').forEach(c=>c.classList.remove('hot'));
    WAVES[wi%WAVES.length].forEach(i=>{
      const c=document.querySelectorAll('.gc')[i];
      if(c&&!c.classList.contains('bright')) c.classList.add('hot');
    });
    wi++;
  },750);
}
function boardStop(){
  clearInterval(boardTick);
  document.querySelectorAll('.gc.hot').forEach(c=>c.classList.remove('hot'));
}

/* ── Chrome update ── */
function chrome(idx){
  pbar.style.width=((idx+1)/TOTAL*100)+'%';
  pbar.style.opacity=idx===11?'0':'1';

  snum.innerHTML='<b>'+String(idx+1).padStart(2,'0')+'</b> / 12';
  snum.className=idx===11?'dark':'';

  logo.className=idx===11?'dark':'';
  dotsEl.className=idx===11?'dark':'';

  dots.forEach((d,i)=>d.classList.toggle('on',i===idx));
  cue.classList.toggle('hide',idx!==0);
}

/* ── Reset animations on a slide ── */
function resetAnims(slide){
  slide.querySelectorAll('.u,.f,.r,.s,.pi,.cn').forEach(el=>{
    el.style.animation='none';
    el.style.opacity='';
  });
  void slide.offsetHeight;
  slide.querySelectorAll('.u,.f,.r,.s,.pi,.cn').forEach(el=>{
    el.style.animation='';
  });
}

/* ── Core goTo ── */
function goTo(next){
  if(busy||next===cur||next<0||next>=TOTAL) return;
  busy=true;

  const prev=slides[cur];
  const nxt=slides[next];

  // 1. Flash shutter
  shutter.classList.add('on');

  setTimeout(()=>{
    // 2. Swap at peak darkness
    prev.classList.remove('active');
    prev.classList.add('exit');
    resetAnims(nxt);
    nxt.classList.add('active');

    // 3. Board
    if(next===4) boardStart();
    else boardStop();

    // 4. Open shutter
    shutter.classList.remove('on');
    chrome(next);
    cur=next;

    setTimeout(()=>{
      prev.classList.remove('exit');
      busy=false;
    }, IN_DUR+100);

  }, SHUTTER);
}

/* ── Init ── */
chrome(0);

/* ── Wheel ── */
let wAcc=0,wT=null;
window.addEventListener('wheel',e=>{
  e.preventDefault();
  wAcc+=Math.abs(e.deltaY);
  clearTimeout(wT);
  wT=setTimeout(()=>wAcc=0,220);
  if(wAcc>50){wAcc=0;goTo(cur+(e.deltaY>0?1:-1));}
},{passive:false});

/* ── Keys ── */
window.addEventListener('keydown',e=>{
  if(['ArrowDown','PageDown','Space'].includes(e.key)){e.preventDefault();goTo(cur+1);}
  if(['ArrowUp','PageUp'].includes(e.key)){e.preventDefault();goTo(cur-1);}
  if(e.key==='Home') goTo(0);
  if(e.key==='End')  goTo(TOTAL-1);
});

/* ── Touch ── */
let ty0=0;
window.addEventListener('touchstart',e=>{ty0=e.touches[0].clientY;},{passive:true});
window.addEventListener('touchend',e=>{
  const d=ty0-e.changedTouches[0].clientY;
  if(Math.abs(d)>44) goTo(cur+(d>0?1:-1));
},{passive:true});

/* ── Dots ── */
dots.forEach(d=>d.addEventListener('click',()=>goTo(+d.dataset.i)));

/* ── Cue click ── */
cue.addEventListener('click',()=>goTo(1));

/* ── Streamlit height ── */
function sendH(){
  const h=Math.max(window.innerHeight,700);
  try{window.parent.postMessage({isStreamlitMessage:true,type:'streamlit:setFrameHeight',height:h},'*');}catch(_){}
}
sendH();
window.addEventListener('resize',sendH);

})();
</script>
</body>
</html>"""

components.html(HTML, height=900, scrolling=False)
