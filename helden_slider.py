"""
HELDEN INC. — AWWWARDS-GRADE REBUILD
=====================================
10 major upgrades over the previous version:

1.  CUSTOM MORPHING CURSOR
    Dot + oversized ring. mix-blend-mode:difference = inverts on any bg.
    Ring expands on hover, carries a text label per context.

2.  DIAGONAL CLIP-PATH WIPE TRANSITION
    A yellow-then-void stripe sweeps L→R (advance) or R→L (retreat).
    Uses clip-path:inset() keyframes. Far more cinematic than blur morph.
    Slide content swaps at the midpoint of the stripe crossing.

3.  LINE-BY-LINE CLIP-PATH TEXT REVEALS
    Every headline is split into lines wrapped in overflow:hidden.
    Each line's inner span animates: clip-path inset(0 100% 0 0)→(0 0%).
    Stagger delay creates the "printing press" effect.

4.  GHOST BACKGROUND SLIDE NUMBERS
    Each slide has its index rendered at 40+vw, opacity .024, behind content.
    Pure editorial depth — a layer that exists below everything.

5.  MOUSE PARALLAX
    Hero grid and glow shift ±18px / ±12px on mouse move via RAF lerp.

6.  MARQUEE TICKER
    Continuous product name scroller at bottom of stage.
    Pauses on hover. Yellow accents on key products.

7.  STAT COUNTER ANIMATION
    "10%" and "200+" count up from 0 using RAF with ease-out-cubic.

8.  HERO AT 17VW — DELIBERATE BLEED
    Headline font-size hits clamp(6rem,17vw,22rem).
    "boring." intentionally overflows the right edge. Grid-breaking.

9.  ASYMMETRIC PRODUCT LAYOUTS
    Dark slides: product name right-aligned in 55% column.
    Light slides: name left-aligned with visual pushed right.
    Varies the rhythm so no two consecutive slides feel the same.

10. TIGHTER TYPOGRAPHY
    Body copy at .86rem / 1.9 line-height. Labels at .44rem.
    Generous negative letter-spacing on display: −0.04em.

Deploy: github.com + share.streamlit.io (free, 60 seconds)
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
*{box-sizing:border-box;}
html,body,[data-testid="stApp"],[data-testid="stAppViewContainer"]{
  margin:0!important;padding:0!important;overflow:hidden!important;
  background:#06060b!important;height:100vh!important;width:100vw!important;
}
.block-container,.main{padding:0!important;max-width:100vw!important;overflow:hidden!important;}
#MainMenu,header,footer,[data-testid="stDecoration"],[data-testid="stToolbar"],
[data-testid="stHeader"],[data-testid="stStatusWidget"]{display:none!important;}
section[data-testid="stMain"]{padding:0!important;overflow:hidden!important;}
div[data-testid="stVerticalBlock"]{gap:0!important;}
iframe{border:none!important;display:block!important;}
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Helden Inc.</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,100;0,9..144,300;0,9..144,400;0,9..144,700;0,9..144,900;1,9..144,100;1,9..144,300;1,9..144,400;1,9..144,700;1,9..144,900&family=Figtree:wght@300;400;500;600&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* ╔══════════════════════════════════════════════════════════════╗
   ║  DESIGN TOKENS                                               ║
   ╚══════════════════════════════════════════════════════════════╝ */
:root{
  /* Void surfaces */
  --v0:#06060b;  --v1:#0b0b14;  --v2:#10101c;  --v3:#161625;
  /* Paper surfaces */
  --p0:#f7f6f1;  --p1:#f0efe9;  --p2:#e6e5de;  --p3:#d8d7ce;
  /* Yellow brand */
  --y:#FFD600;  --yd:#C8A800;  --ydk:#1a1200;
  --ydim:rgba(255,214,0,.06);  --yln:rgba(255,214,0,.13);
  /* Text on dark */
  --td1:#e8e3d8;  --td2:#52526a;  --td3:#22223a;
  /* Text on light */
  --tl1:#090912;  --tl2:#686880;  --tl3:#babace;
  /* Borders */
  --bd1:rgba(255,255,255,.045);  --bd2:rgba(255,255,255,.08);  --bd3:rgba(255,255,255,.13);
  --bl1:rgba(0,0,0,.05);        --bl2:rgba(0,0,0,.09);        --bl3:rgba(0,0,0,.14);
  /* Typography */
  --serif:'Fraunces',Georgia,serif;
  --sans: 'Figtree',system-ui,sans-serif;
  --mono: 'DM Mono','Courier New',monospace;
  /* Easing */
  --E: cubic-bezier(0.76,0,0.24,1);   /* Orano / snappy */
  --S: cubic-bezier(0.22,1,0.36,1);   /* Snap */
  --Sp:cubic-bezier(0.34,1.56,0.64,1);/* Spring */
  /* Layout */
  --nav:236px;
}

/* ── RESET ── */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body{
  width:100%;height:100%;overflow:hidden;
  background:var(--v0);color:var(--td1);
  cursor:none;
  -webkit-font-smoothing:antialiased;
}

/* ╔══════════════════════════════════════════════════════════════╗
   ║  1. CUSTOM CURSOR                                            ║
   ║  mix-blend-mode:difference = works on any bg automatically   ║
   ╚══════════════════════════════════════════════════════════════╝ */
#CD{ /* cursor dot */
  position:fixed;z-index:9999;pointer-events:none;
  width:7px;height:7px;border-radius:50%;background:#fff;
  transform:translate(-50%,-50%);
  transition:width .18s var(--S),height .18s var(--S);
  mix-blend-mode:difference;will-change:transform;
}
#CR{ /* cursor ring */
  position:fixed;z-index:9998;pointer-events:none;
  width:42px;height:42px;border-radius:50%;
  border:1.5px solid rgba(255,255,255,.55);
  transform:translate(-50%,-50%);
  transition:width .3s var(--E),height .3s var(--E),border-color .2s,opacity .2s;
  mix-blend-mode:difference;will-change:transform;
}
#CL{ /* cursor label */
  position:fixed;z-index:9997;pointer-events:none;
  font-family:var(--mono);font-size:.4rem;letter-spacing:.15em;
  text-transform:uppercase;color:#fff;
  mix-blend-mode:difference;
  transform:translate(14px,6px);
  opacity:0;transition:opacity .18s;white-space:nowrap;
}
body.chov #CD{width:4px;height:4px;}
body.chov #CR{width:58px;height:58px;border-color:rgba(255,255,255,.85);}
body.chov #CL{opacity:1;}

/* ╔══════════════════════════════════════════════════════════════╗
   ║  2. DIAGONAL WIPE TRANSITION OVERLAY                         ║
   ║  Yellow stripe sweeps across screen at every slide change    ║
   ╚══════════════════════════════════════════════════════════════╝ */
#WP{
  position:fixed;inset:0;z-index:8000;pointer-events:none;
  /* Yellow centre, dark flanks — creates the stripe illusion */
  background:linear-gradient(
    108deg,
    var(--v0)  0%,
    var(--v0)  24%,
    var(--y)   38%,
    var(--y)   62%,
    var(--v0)  76%,
    var(--v0) 100%
  );
  clip-path:inset(0 101% 0 0); /* hidden right */
  will-change:clip-path;
}
#WP.fwd{animation:wFwd .58s var(--E) both;}
#WP.bwd{animation:wBwd .58s var(--E) both;}
@keyframes wFwd{
  0%  {clip-path:inset(0 101% 0 0);}
  48% {clip-path:inset(0 0%   0 0);}
  100%{clip-path:inset(0 0   0 101%);}
}
@keyframes wBwd{
  0%  {clip-path:inset(0 0   0 101%);}
  48% {clip-path:inset(0 0%   0 0);}
  100%{clip-path:inset(0 101% 0 0);}
}

/* ── GRAIN ── */
body::after{
  content:'';position:fixed;inset:0;z-index:7999;pointer-events:none;opacity:.015;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.74' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* ╔══════════════════════════════════════════════════════════════╗
   ║  SIDEBAR                                                     ║
   ╚══════════════════════════════════════════════════════════════╝ */
#SB{
  position:fixed;top:0;left:0;bottom:0;width:var(--nav);z-index:600;
  display:flex;flex-direction:column;justify-content:space-between;
  padding:26px 20px;
  border-right:1px solid var(--bd1);
  background:rgba(6,6,11,.8);
  backdrop-filter:blur(20px) saturate(180%);
  -webkit-backdrop-filter:blur(20px) saturate(180%);
  transition:background .5s,border-color .5s;
}
#SB.lm{background:rgba(247,246,241,.88);border-right-color:var(--bl1);}

.logo{display:flex;align-items:center;gap:9px;text-decoration:none;cursor:none;}
.lhx{width:24px;height:24px;background:var(--y);flex-shrink:0;
  clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
  transition:transform .4s var(--Sp),background .4s;}
.logo:hover .lhx{transform:rotate(60deg);}
.lnm{font-family:var(--mono);font-size:.54rem;letter-spacing:.3em;text-transform:uppercase;color:var(--td1);transition:color .4s;}
#SB.lm .lhx{background:var(--tl1);}
#SB.lm .lnm{color:var(--tl1);}

.nl{list-style:none;display:flex;flex-direction:column;gap:0;flex:1;justify-content:center;overflow:hidden;padding:14px 0;}
.ni{display:flex;align-items:center;gap:8px;padding:4px 0;cursor:none;transition:opacity .18s;}
.ni:not(.on){opacity:.28;}
.ni.on{opacity:1;}
.ni:hover:not(.on){opacity:.55;}
.nn{font-family:var(--mono);font-size:.4rem;letter-spacing:.15em;color:var(--td3);min-width:15px;transition:color .25s;}
.nb{width:0;height:1px;background:var(--y);transition:width .38s var(--E);flex-shrink:0;}
.nt{font-family:var(--sans);font-size:.63rem;font-weight:400;color:var(--td2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;transition:color .25s,font-weight .25s;}
.ni.on .nn{color:var(--y);}
.ni.on .nb{width:14px;}
.ni.on .nt{color:var(--td1);font-weight:500;}
#SB.lm .nn{color:var(--tl3);}
#SB.lm .ni.on .nn{color:var(--yd);}
#SB.lm .nt{color:var(--tl2);}
#SB.lm .ni.on .nt{color:var(--tl1);}
#SB.lm .nb{background:var(--yd);}

.sft{font-family:var(--mono);font-size:.4rem;letter-spacing:.11em;text-transform:uppercase;color:var(--td3);line-height:2.2;transition:color .4s;}
#SB.lm .sft{color:var(--tl3);}

/* ── TOP BAR ── */
#TB{position:fixed;top:0;right:0;z-index:600;left:var(--nav);height:56px;display:flex;align-items:center;justify-content:flex-end;padding:0 30px;gap:16px;pointer-events:none;}
#CT{font-family:var(--mono);font-size:.5rem;letter-spacing:.2em;color:var(--td2);transition:color .4s;}
#CT b{color:var(--td1);font-weight:400;transition:color .4s;}
#CT.lm{color:var(--tl2);}
#CT.lm b{color:var(--tl1);}
.ab{width:34px;height:34px;border-radius:50%;border:1px solid var(--bd2);display:flex;align-items:center;justify-content:center;cursor:none;pointer-events:all;color:var(--td2);background:transparent;transition:background .18s,border-color .18s,color .18s,transform .12s;}
.ab:hover{background:var(--bd1);border-color:var(--bd3);color:var(--td1);transform:scale(1.1);}
.ab.lm{border-color:var(--bl2);color:var(--tl2);}
.ab.lm:hover{background:var(--bl1);border-color:var(--bl3);color:var(--tl1);}

/* ── PROGRESS ── */
#PG{position:fixed;top:56px;left:var(--nav);right:0;height:1px;background:var(--bd1);z-index:600;transition:background .4s;}
#PG.lm{background:var(--bl1);}
#PF{height:100%;background:var(--y);width:0;transition:width .9s var(--E);}
#PG.lm #PF{background:var(--yd);}

/* ╔══════════════════════════════════════════════════════════════╗
   ║  STAGE & SLIDES                                              ║
   ╚══════════════════════════════════════════════════════════════╝ */
#ST{position:fixed;top:0;bottom:0;left:var(--nav);right:0;overflow:hidden;}
.slide{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;}
.slide.on{opacity:1;pointer-events:all;}
.slide.off{opacity:0;pointer-events:none;}

/* ── Scroll cue ── */
#CU{position:fixed;bottom:42px;left:calc(var(--nav) + (100vw - var(--nav))/2);transform:translateX(-50%);z-index:500;display:flex;flex-direction:column;align-items:center;gap:5px;transition:opacity .4s;}
#CU.gone{opacity:0;pointer-events:none;}
.cln{width:1px;height:26px;background:linear-gradient(var(--td2),transparent);animation:cA 2s ease infinite;}
@keyframes cA{0%{transform:scaleY(0);transform-origin:top;}48%{transform:scaleY(1);transform-origin:top;}50%{transform-origin:bottom;}100%{transform:scaleY(0);transform-origin:bottom;}}
.ctxt{font-family:var(--mono);font-size:.42rem;letter-spacing:.26em;text-transform:uppercase;color:var(--td2);}

/* ╔══════════════════════════════════════════════════════════════╗
   ║  6. MARQUEE TICKER                                           ║
   ╚══════════════════════════════════════════════════════════════╝ */
#TK{
  position:fixed;bottom:0;left:var(--nav);right:0;z-index:500;
  height:28px;display:flex;align-items:center;overflow:hidden;
  border-top:1px solid var(--bd1);
  background:rgba(6,6,11,.55);
  backdrop-filter:blur(10px);
  transition:border-color .4s,background .4s;
}
#TK.lm{border-top-color:var(--bl1);background:rgba(247,246,241,.55);}
.tk-track{display:flex;animation:tkM 36s linear infinite;white-space:nowrap;}
.tk-track:hover{animation-play-state:paused;}
.tk-i{font-family:var(--mono);font-size:.49rem;letter-spacing:.16em;text-transform:uppercase;color:var(--td3);padding:0 2.2rem;transition:color .4s;}
.tk-i.y{color:var(--y);}
#TK.lm .tk-i{color:var(--tl3);}
#TK.lm .tk-i.y{color:var(--yd);}
@keyframes tkM{from{transform:translateX(0);}to{transform:translateX(-50%);}}

/* ╔══════════════════════════════════════════════════════════════╗
   ║  3. LINE-BY-LINE REVEAL — the Awwwards "printing" effect     ║
   ║  .rl = reveal-line wrapper (overflow:hidden)                 ║
   ║  .ri = reveal-inner (clips left→right on activation)        ║
   ╚══════════════════════════════════════════════════════════════╝ */
.rl{overflow:hidden;display:block;}
.ri{display:block;clip-path:inset(0 100% 0 0);}
.ri.rev{animation:lRev .88s var(--E) both;}
@keyframes lRev{from{clip-path:inset(0 100% 0 0);}to{clip-path:inset(0 0% 0 0);}}

/* ╔══════════════════════════════════════════════════════════════╗
   ║  4. GHOST BACKGROUND NUMBERS                                 ║
   ╚══════════════════════════════════════════════════════════════╝ */
.gn{
  position:absolute;right:-1vw;bottom:-6vh;
  font-family:var(--serif);font-size:clamp(20rem,42vw,56rem);
  font-weight:900;font-style:italic;line-height:.78;
  letter-spacing:-.06em;color:currentColor;
  opacity:.024;pointer-events:none;user-select:none;z-index:0;
}

/* ═══════════════════════════════════════════════════════════════
   ELEMENT REVEAL SYSTEM  (data-r = rise, data-f = fade,
   data-w = wipe, data-p = pop)
═══════════════════════════════════════════════════════════════ */
[data-r]{opacity:0;}
.slide.on [data-r]{animation:eR .78s var(--S) both;}
.slide.on [data-r="0"]{animation-delay:.06s;} .slide.on [data-r="1"]{animation-delay:.18s;}
.slide.on [data-r="2"]{animation-delay:.30s;} .slide.on [data-r="3"]{animation-delay:.42s;}
.slide.on [data-r="4"]{animation-delay:.54s;} .slide.on [data-r="5"]{animation-delay:.66s;}
@keyframes eR{from{opacity:0;transform:translateY(14px);}to{opacity:1;transform:translateY(0);}}

[data-f]{opacity:0;}
.slide.on [data-f]{animation:eF .9s var(--E) both;}
.slide.on [data-f="0"]{animation-delay:.08s;} .slide.on [data-f="1"]{animation-delay:.22s;}
.slide.on [data-f="2"]{animation-delay:.36s;} .slide.on [data-f="3"]{animation-delay:.50s;}
.slide.on [data-f="4"]{animation-delay:.64s;} .slide.on [data-f="5"]{animation-delay:.78s;}
@keyframes eF{from{opacity:0;}to{opacity:1;}}

[data-w]{clip-path:inset(0 100% 0 0);}
.slide.on [data-w]{animation:eW .82s var(--E) both;}
.slide.on [data-w="0"]{animation-delay:.14s;} .slide.on [data-w="1"]{animation-delay:.30s;}
.slide.on [data-w="2"]{animation-delay:.46s;}
@keyframes eW{from{clip-path:inset(0 100% 0 0);}to{clip-path:inset(0 0% 0 0);}}

[data-p]{opacity:0;transform:scale(.68);}
.slide.on [data-p]{animation:eP .55s var(--Sp) both;}
.slide.on [data-p="0"]{animation-delay:.10s;} .slide.on [data-p="1"]{animation-delay:.24s;}
.slide.on [data-p="2"]{animation-delay:.38s;}
@keyframes eP{from{opacity:0;transform:scale(.66);}to{opacity:1;transform:scale(1);}}

/* ═══════════════════════════════════════════════════════════════
   TYPOGRAPHY SCALE
═══════════════════════════════════════════════════════════════ */
/* ── HERO — deliberately large, meant to bleed off right edge ── */
.th{
  font-family:var(--serif);
  font-size:clamp(6rem,17.5vw,22rem);
  font-weight:100;font-style:italic;
  line-height:.8;letter-spacing:-.042em;
  color:var(--td1);display:block;
  white-space:nowrap; /* allow intentional bleed */
}
.th em{font-style:normal;font-weight:900;color:var(--y);}

/* ── Section product name ── */
.tp{
  font-family:var(--serif);
  font-size:clamp(3.5rem,8.5vw,11rem);
  font-weight:900;line-height:.82;
  letter-spacing:-.028em;color:var(--td1);display:block;
}
.tp em{font-style:italic;color:var(--y);}
.tp.lm{color:var(--tl1);}
.tp.lm em{color:var(--yd);}

/* ── Contrast headline pair (Insight slide) ── */
.tdim{font-family:var(--serif);font-size:clamp(2rem,6vw,7.5rem);font-weight:100;font-style:italic;line-height:.95;color:var(--td3);letter-spacing:-.02em;display:block;}
.tlit{font-family:var(--serif);font-size:clamp(2rem,6vw,7.5rem);font-weight:900;line-height:.95;color:var(--td1);letter-spacing:-.03em;display:block;}
.tlit .hl{color:var(--y);font-style:italic;}

/* ── Section h2 ── */
.th2{font-family:var(--serif);font-size:clamp(2.5rem,5.5vw,6.5rem);font-weight:300;line-height:.9;letter-spacing:-.02em;color:var(--td1);display:block;}
.th2.lm{color:var(--tl1);}
.th2 em{font-style:italic;color:var(--y);}
.th2.lm em{color:var(--yd);}

/* ── Oversized stat ── */
.tstat{font-family:var(--serif);font-size:clamp(14rem,36vw,50rem);font-weight:100;line-height:.72;letter-spacing:-.06em;color:var(--td1);display:block;}
.tstat-sup{font-size:.22em;vertical-align:super;color:var(--y);}
.tstat-cap{font-family:var(--serif);font-size:clamp(.9rem,2vw,2.2rem);font-weight:300;font-style:italic;color:var(--td2);display:block;letter-spacing:-.01em;}

/* ── Body copy ── */
.tb{font-family:var(--sans);font-size:.86rem;font-weight:300;color:var(--td2);line-height:1.9;letter-spacing:.008em;display:block;}
.tb.lm{color:var(--tl2);}

/* ── Eyebrow ── */
.ey{display:block;font-family:var(--mono);font-size:.5rem;letter-spacing:.28em;text-transform:uppercase;color:var(--y);opacity:.7;}
.ey.lm{color:var(--yd);}

/* ── Badge ── */
.bdg{display:inline-flex;background:var(--y);color:var(--ydk);font-family:var(--mono);font-size:.44rem;letter-spacing:.1em;text-transform:uppercase;padding:.2rem .6rem;border-radius:2px;font-weight:500;}
.bdg.lm{background:var(--yd);color:var(--p0);}
.bdgo{display:inline-flex;border:1px solid var(--yln);color:var(--y);font-family:var(--mono);font-size:.44rem;letter-spacing:.1em;text-transform:uppercase;padding:.2rem .6rem;border-radius:2px;}
.bdgo.lm{border-color:rgba(200,168,0,.28);color:var(--yd);}

/* ── Rules ── */
.ry{display:block;height:1px;background:var(--y);opacity:.28;}
.rd{display:block;height:1px;background:var(--bd2);}
.rl2{display:block;height:1px;background:var(--bl2);}

/* ── Feature list ── */
.fl{list-style:none;display:flex;flex-direction:column;gap:.38rem;}
.fl li{display:flex;align-items:center;gap:.65rem;font-family:var(--sans);font-size:.84rem;font-weight:300;color:var(--td1);}
.fl li::before{content:'';width:11px;height:1px;background:var(--y);flex-shrink:0;}
.fl.lm li{color:var(--tl1);}
.fl.lm li::before{background:var(--yd);}

/* ── Pull quote ── */
.pq{position:relative;padding-left:1.2rem;}
.pq::before{content:'';position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--y);border-radius:1px;}
.pqt{font-family:var(--serif);font-size:clamp(.9rem,1.2vw,1.3rem);font-weight:300;font-style:italic;color:var(--td1);line-height:1.65;display:block;margin-bottom:.5rem;}
.pqa{font-family:var(--mono);font-size:.46rem;letter-spacing:.13em;text-transform:uppercase;color:var(--y);opacity:.65;display:block;}

/* ── Layouts ── */
.pw{width:100%;height:100%;padding:64px 5.5vw 46px;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden;}
/* Two-col grid */
.g2{display:grid;grid-template-columns:1fr 1fr;gap:5vw;align-items:center;width:100%;position:relative;z-index:1;}
/* Wider left */
.g21{display:grid;grid-template-columns:1.2fr 1fr;gap:5vw;align-items:center;width:100%;position:relative;z-index:1;}
/* Wider right */
.g12{display:grid;grid-template-columns:1fr 1.2fr;gap:5vw;align-items:center;width:100%;position:relative;z-index:1;}
.cx{display:flex;flex-direction:column;align-items:center;text-align:center;gap:.65rem;max-width:1000px;margin:0 auto;position:relative;z-index:1;}
.sk{display:flex;flex-direction:column;gap:.8rem;}

/* ═══════════════════════════════════════════════════════════════
   BACKGROUNDS & ATMOSPHERES
═══════════════════════════════════════════════════════════════ */
.bv{background:var(--v0);}
.bv2{background:var(--v1);}
.bp{background:var(--p0);}
.bp2{background:var(--p1);}

/* Hero: animated grid + parallax glow */
.hg{position:absolute;inset:-20%;background-image:radial-gradient(circle,rgba(255,214,0,.42) 1px,transparent 1px);background-size:52px 52px;opacity:.04;pointer-events:none;z-index:0;will-change:transform;}
.hgl{position:absolute;bottom:-18%;left:50%;transform:translateX(-50%);width:100vw;height:72vh;background:radial-gradient(ellipse,rgba(255,214,0,.058) 0%,transparent 58%);animation:gP 10s ease-in-out infinite alternate;pointer-events:none;z-index:0;will-change:transform;}
@keyframes gP{from{opacity:.48;}to{opacity:1;}}
/* Light slide faint grid */
.lg{position:absolute;inset:0;background-image:linear-gradient(rgba(0,0,0,.02) 1px,transparent 1px),linear-gradient(90deg,rgba(0,0,0,.02) 1px,transparent 1px);background-size:62px 62px;pointer-events:none;z-index:0;}
/* FutureGame glow */
.fgg{position:absolute;right:-5%;top:0;width:55vw;height:100%;background:radial-gradient(ellipse,rgba(255,214,0,.055) 0%,transparent 56%);pointer-events:none;z-index:0;}
/* Problem red tint */
.prb{position:absolute;inset:0;background:radial-gradient(ellipse 72% 58% at 18% 50%,rgba(200,25,25,.05) 0%,transparent 65%);pointer-events:none;z-index:0;}
/* CTA rings */
.cring{position:absolute;border-radius:50%;border:1px solid;pointer-events:none;animation:rP 7s ease-in-out infinite;}
.cr1{width:152vw;height:152vw;top:-62%;left:50%;transform:translateX(-50%);border-color:rgba(0,0,0,.044);}
.cr2{width:94vw;height:94vw;top:-32%;left:50%;transform:translateX(-50%);border-color:rgba(0,0,0,.036);animation-delay:.8s;}
@keyframes rP{0%,100%{transform:translateX(-50%) scale(1);}50%{transform:translateX(-50%) scale(1.024);}}

/* ═══════════════════════════════════════════════════════════════
   VISUAL COMPONENTS — per product
═══════════════════════════════════════════════════════════════ */

/* ── GAME BOARD (FutureGame) ── */
.gb{display:grid;grid-template-columns:repeat(8,1fr);grid-template-rows:repeat(6,1fr);gap:5px;height:100%;min-height:380px;width:100%;position:relative;z-index:1;}
.gc{border-radius:4px;background:var(--v2);border:1px solid rgba(255,214,0,.055);transition:background .5s,border-color .5s,box-shadow .5s;}
.gc.dim {background:rgba(255,214,0,.09);border-color:rgba(255,214,0,.2);}
.gc.warm{background:rgba(255,214,0,.2);border-color:rgba(255,214,0,.42);}
.gc.hot {background:rgba(255,214,0,.36);border-color:rgba(255,214,0,.62);box-shadow:0 0 14px rgba(255,214,0,.2);}
.gc.core{background:var(--y);border-color:var(--y);box-shadow:0 0 28px rgba(255,214,0,.42);}

/* ── HEX RINGS ── */
.hxs{position:relative;height:100%;min-height:380px;display:flex;align-items:center;justify-content:center;z-index:1;}
.hxr{position:absolute;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);border:1px solid;}
.hx1{width:90%;max-width:380px;aspect-ratio:1;border-color:var(--yln);}
.hx2{width:68%;max-width:272px;aspect-ratio:1;border-color:rgba(255,214,0,.22);animation:hR 26s linear infinite;}
.hx3{width:44%;max-width:176px;aspect-ratio:1;border-color:rgba(255,214,0,.38);animation:hR 16s linear infinite reverse;}
.hxc{width:12%;max-width:58px;aspect-ratio:1;}
.hxc.d{background:var(--y);}
.hxc.l{background:var(--yd);}
@keyframes hR{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}
.hxlb{position:absolute;font-family:var(--mono);font-size:.48rem;letter-spacing:.1em;text-transform:uppercase;}
.hxlt{top:5%;left:50%;transform:translateX(-50%);}
.hxlb2{bottom:12%;left:5%;}
.hxlb3{bottom:12%;right:5%;}

/* ── ISO BOX ── */
.bxs{position:relative;height:100%;min-height:380px;display:flex;align-items:center;justify-content:center;z-index:1;}
.iso{position:relative;width:260px;height:260px;}
.it{position:absolute;top:0;left:18%;width:64%;height:36%;background:var(--y);opacity:.92;clip-path:polygon(0 54%,50% 0,100% 54%,50% 100%);}
.il{position:absolute;bottom:0;left:0;width:50%;height:66%;background:rgba(255,214,0,.14);border:1px solid var(--yln);}
.ir{position:absolute;bottom:0;right:0;width:50%;height:66%;background:rgba(255,214,0,.05);border:1px solid rgba(255,214,0,.07);}
.bxl{position:absolute;font-family:var(--mono);font-size:.44rem;letter-spacing:.1em;text-transform:uppercase;color:var(--td2);}
.bxl1{top:20px;right:-8px;}.bxl2{bottom:90px;left:-36px;}.bxl3{bottom:46px;right:-36px;}

/* ── JOURNEY ── */
.jrn{position:relative;display:flex;flex-direction:column;flex-shrink:0;width:280px;z-index:1;}
.jrn::before{content:'';position:absolute;left:19px;top:28px;bottom:28px;width:1px;background:linear-gradient(var(--y),var(--td3));opacity:.28;}
.jst{display:flex;align-items:flex-start;gap:14px;padding:11px 0;position:relative;z-index:2;}
.jnd{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:.52rem;flex-shrink:0;}
.jnd.d{background:var(--y);color:var(--ydk);border:2px solid var(--y);}
.jnd.a{background:transparent;color:var(--y);border:2px solid var(--y);}
.jnd.n{background:var(--v2);color:var(--td3);border:1px solid var(--bd2);}
.ji{padding-top:9px;display:flex;flex-direction:column;gap:3px;}
.jit{font-family:var(--sans);font-size:.82rem;font-weight:400;color:var(--td1);}
.jis{font-family:var(--mono);font-size:.44rem;letter-spacing:.1em;text-transform:uppercase;color:var(--td2);}

/* ── PHONE ── */
.phs{position:relative;height:100%;min-height:380px;display:flex;align-items:center;justify-content:center;z-index:1;}
.ph{width:192px;height:388px;background:var(--v2);border:1px solid var(--yln);border-radius:22px;display:flex;flex-direction:column;padding:19px 12px 14px;gap:8px;position:relative;}
.ph::before{content:'';position:absolute;top:10px;left:50%;transform:translateX(-50%);width:34px;height:3px;background:var(--v1);border-radius:2px;}
.phb{width:100%;height:4px;background:var(--y);border-radius:2px;margin-top:9px;}
.phb.d{width:65%;background:var(--v1);}
.phc{background:var(--v1);border:1px solid var(--bd1);border-radius:6px;padding:7px 9px;}
.phct{font-family:var(--mono);font-size:.38rem;letter-spacing:.1em;text-transform:uppercase;color:var(--y);display:block;}
.phcn{font-family:var(--sans);font-size:.68rem;color:var(--td1);font-weight:400;margin-top:2px;display:block;}
.phcd{font-family:var(--mono);font-size:.38rem;color:var(--td2);margin-top:1px;display:block;}
.prw{display:flex;gap:3px;align-items:center;margin-top:auto;}
.ps{flex:1;height:2px;background:var(--v1);border-radius:1px;}
.ps.y{background:var(--y);}
.pp{font-family:var(--mono);font-size:.4rem;color:var(--y);margin-left:4px;}
.ft{position:absolute;background:var(--v2);border:1px solid var(--yln);border-radius:5px;padding:7px 10px;}
.fn{font-family:var(--mono);font-size:1.1rem;color:var(--y);letter-spacing:-.02em;line-height:1;display:block;}
.fa{font-family:var(--mono);font-size:.4rem;text-transform:uppercase;letter-spacing:.09em;color:var(--td2);margin-top:2px;display:block;}
.ft1{top:-8px;right:10px;}.ft2{bottom:52px;right:0;}.ft3{bottom:112px;left:-16px;}

/* ── PRODUCT GRID (all 9) ── */
.pgr{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--bl1);border:1px solid var(--bl1);border-radius:3px;overflow:hidden;}
.pi{background:var(--p0);padding:.95rem 1.2rem;position:relative;overflow:hidden;transition:background .18s;cursor:none;}
.pi:hover{background:var(--p1);}
.pi::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1.5px;background:var(--yd);transform:scaleX(0);transform-origin:left;transition:transform .26s var(--E);}
.pi:hover::after{transform:scaleX(1);}
.pin{font-family:var(--mono);font-size:.4rem;text-transform:uppercase;letter-spacing:.14em;color:var(--tl3);display:block;margin-bottom:.28rem;}
.piname{font-family:var(--serif);font-size:clamp(.8rem,1.2vw,1.3rem);font-weight:300;color:var(--tl1);line-height:1.18;}
.pi.star .piname{color:var(--yd);font-weight:700;}
.slide.on .pi{animation:piI .42s var(--S) both;}
.slide.on .pi:nth-child(1){animation-delay:.16s;}.slide.on .pi:nth-child(2){animation-delay:.19s;}
.slide.on .pi:nth-child(3){animation-delay:.22s;}.slide.on .pi:nth-child(4){animation-delay:.25s;}
.slide.on .pi:nth-child(5){animation-delay:.28s;}.slide.on .pi:nth-child(6){animation-delay:.31s;}
.slide.on .pi:nth-child(7){animation-delay:.34s;}.slide.on .pi:nth-child(8){animation-delay:.37s;}
.slide.on .pi:nth-child(9){animation-delay:.40s;}
@keyframes piI{from{opacity:0;transform:translateY(7px);}to{opacity:1;transform:translateY(0);}}

/* ── CLIENT CHIPS ── */
.cstrip{display:flex;flex-wrap:wrap;gap:5px;}
.cn{font-family:var(--mono);font-size:.44rem;letter-spacing:.08em;text-transform:uppercase;color:var(--tl2);padding:.26rem .7rem;border:1px solid var(--bl1);border-radius:2px;transition:border-color .18s,color .18s;opacity:0;cursor:none;}
.cn:hover{border-color:rgba(200,168,0,.32);color:var(--yd);}
.slide.on .cn{animation:cnI .36s var(--S) both;}
.slide.on .cn:nth-child(1){animation-delay:.50s;}.slide.on .cn:nth-child(2){animation-delay:.54s;}
.slide.on .cn:nth-child(3){animation-delay:.58s;}.slide.on .cn:nth-child(4){animation-delay:.62s;}
.slide.on .cn:nth-child(5){animation-delay:.66s;}.slide.on .cn:nth-child(6){animation-delay:.70s;}
.slide.on .cn:nth-child(7){animation-delay:.74s;}.slide.on .cn:nth-child(8){animation-delay:.78s;}
.slide.on .cn:nth-child(9){animation-delay:.82s;}.slide.on .cn:nth-child(10){animation-delay:.86s;}
.slide.on .cn:nth-child(11){animation-delay:.90s;}.slide.on .cn:nth-child(12){animation-delay:.94s;}
@keyframes cnI{from{opacity:0;transform:scale(.82);}to{opacity:1;transform:scale(1);}}

/* ── TESTIMONIALS ── */
.tc{background:var(--p0);border:1px solid var(--bl1);border-radius:5px;padding:1.4rem 1.6rem;border-left:2px solid var(--yd);}
.tq{font-family:var(--serif);font-size:clamp(.86rem,1.15vw,1.25rem);font-weight:300;font-style:italic;color:var(--tl1);line-height:1.72;display:block;margin-bottom:.8rem;}
.ta{font-family:var(--sans);font-size:.84rem;font-weight:500;color:var(--tl1);display:block;}
.tr{font-family:var(--mono);font-size:.44rem;letter-spacing:.09em;text-transform:uppercase;color:var(--tl2);margin-top:2px;display:block;}

/* ── PROCESS STEPS ── */
.pss{display:flex;flex-direction:column;gap:8px;z-index:1;}
.psi{background:var(--p1);border:1px solid var(--bl1);border-radius:5px;padding:13px 16px;display:flex;align-items:flex-start;gap:13px;transition:background .18s;cursor:none;}
.psi:hover{background:var(--p2);}
.psi.ft{background:rgba(200,168,0,.055);border-color:rgba(200,168,0,.16);}
.psn{font-family:var(--mono);font-size:.48rem;color:var(--yd);min-width:16px;padding-top:2px;letter-spacing:.11em;}
.pst{font-family:var(--sans);font-size:.84rem;font-weight:500;color:var(--tl1);display:block;}
.pss2{font-family:var(--sans);font-size:.76rem;font-weight:300;color:var(--tl2);margin-top:2px;display:block;}

/* ── GAMEPLAN ── */
.gpv{display:flex;flex-direction:column;gap:8px;z-index:1;}
.gpr{display:flex;gap:7px;align-items:center;}
.gpn{height:38px;border-radius:3px;display:flex;align-items:center;padding:0 10px;font-family:var(--mono);font-size:.46rem;letter-spacing:.09em;text-transform:uppercase;flex-shrink:0;}
.gpn.dk{background:var(--v2);color:var(--td2);border:1px solid var(--bd1);}
.gpn.ac{background:var(--y);color:var(--ydk);}
.gpn.dm{background:var(--ydim);color:var(--y);border:1px solid var(--yln);}
.gpl{flex:1;height:1px;background:var(--bd2);}

/* ── EVENTS ── */
.evg{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:8px;height:100%;min-height:360px;z-index:1;}
.evt{background:var(--p1);border:1px solid var(--bl1);border-radius:5px;padding:15px;display:flex;flex-direction:column;justify-content:flex-end;transition:background .18s;cursor:none;}
.evt:hover{background:var(--p2);}
.evt.ft{background:rgba(200,168,0,.055);border-color:rgba(200,168,0,.16);}
.evic{font-size:1.35rem;margin-bottom:7px;}
.evn{font-family:var(--serif);font-size:.92rem;color:var(--tl1);font-weight:400;display:block;}
.evs{font-family:var(--mono);font-size:.42rem;letter-spacing:.09em;text-transform:uppercase;color:var(--tl2);margin-top:2px;display:block;}

/* ── CTA ── */
.ctah{font-family:var(--serif);font-size:clamp(6.5rem,17vw,22rem);font-weight:100;font-style:italic;line-height:.8;color:var(--ydk);letter-spacing:-.04em;display:block;margin-bottom:2.5rem;white-space:nowrap;}
.ctabn{display:inline-flex;align-items:center;gap:.75rem;background:var(--ydk);color:var(--y);font-family:var(--sans);font-size:.95rem;font-weight:500;padding:.85rem 2.25rem;border-radius:3px;text-decoration:none;cursor:none;transition:background .18s,transform .18s,box-shadow .18s;position:relative;z-index:2;}
.ctabn:hover{background:#0a0920;transform:translateY(-3px);box-shadow:0 18px 44px rgba(0,0,0,.28);}
.ctabn svg{transition:transform .18s;}
.ctabn:hover svg{transform:translateX(7px);}
.ctaurl{font-family:var(--mono);font-size:.46rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(26,18,0,.32);display:block;margin-top:1.4rem;}
.ctag{font-family:var(--sans);font-size:.84rem;color:rgba(26,18,0,.42);font-weight:300;display:block;margin-bottom:1.6rem;}
</style>
</head>
<body>

<!-- ═══════════ CURSOR ═══════════ -->
<div id="CD"></div>
<div id="CR"></div>
<div id="CL"></div>

<!-- ═══════════ WIPE ═══════════ -->
<div id="WP"></div>

<!-- ═══════════ SIDEBAR ═══════════ -->
<nav id="SB">
  <a class="logo" href="#" id="HM">
    <div class="lhx"></div>
    <span class="lnm">HELDEN</span>
  </a>
  <ul class="nl" id="NL">
    <li class="ni on" data-i="0"><span class="nn">01</span><span class="nb"></span><span class="nt">Introduction</span></li>
    <li class="ni" data-i="1"><span class="nn">02</span><span class="nb"></span><span class="nt">Our Mission</span></li>
    <li class="ni" data-i="2"><span class="nn">03</span><span class="nb"></span><span class="nt">The Problem</span></li>
    <li class="ni" data-i="3"><span class="nn">04</span><span class="nb"></span><span class="nt">The Insight</span></li>
    <li class="ni" data-i="4"><span class="nn">05</span><span class="nb"></span><span class="nt">FutureGame</span></li>
    <li class="ni" data-i="5"><span class="nn">06</span><span class="nb"></span><span class="nt">Escape Room</span></li>
    <li class="ni" data-i="6"><span class="nn">07</span><span class="nb"></span><span class="nt">Escape Box</span></li>
    <li class="ni" data-i="7"><span class="nn">08</span><span class="nb"></span><span class="nt">Onboarding</span></li>
    <li class="ni" data-i="8"><span class="nn">09</span><span class="nb"></span><span class="nt">Micro Learning</span></li>
    <li class="ni" data-i="9"><span class="nn">10</span><span class="nb"></span><span class="nt">Custom Rooms</span></li>
    <li class="ni" data-i="10"><span class="nn">11</span><span class="nb"></span><span class="nt">GamePlan</span></li>
    <li class="ni" data-i="11"><span class="nn">12</span><span class="nb"></span><span class="nt">Events</span></li>
    <li class="ni" data-i="12"><span class="nn">13</span><span class="nb"></span><span class="nt">All Products</span></li>
    <li class="ni" data-i="13"><span class="nn">14</span><span class="nb"></span><span class="nt">Clients</span></li>
    <li class="ni" data-i="14"><span class="nn">15</span><span class="nb"></span><span class="nt">Get Started</span></li>
  </ul>
  <div class="sft">helden-inc.com<br>Haarlem · Netherlands<br>Game-Based Learning</div>
</nav>

<!-- ═══════════ TOP BAR ═══════════ -->
<div id="TB">
  <div id="CT"><b>01</b> / 15</div>
  <button class="ab" id="BU"><svg width="11" height="11" viewBox="0 0 11 11" fill="none"><path d="M8.5 7.5L5.5 4.5 2.5 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
  <button class="ab" id="BD"><svg width="11" height="11" viewBox="0 0 11 11" fill="none"><path d="M2.5 3.5l3 3 3-3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
</div>

<!-- ═══════════ PROGRESS ═══════════ -->
<div id="PG"><div id="PF"></div></div>

<!-- ═══════════ SCROLL CUE ═══════════ -->
<div id="CU"><div class="cln"></div><span class="ctxt">scroll</span></div>

<!-- ═══════════ MARQUEE ═══════════ -->
<div id="TK"><div class="tk-track" id="TKT"></div></div>

<!-- ══════════════════════════════════════════════════════════════
     15 SLIDES
══════════════════════════════════════════════════════════════ -->
<main id="ST">

<!-- ━━━━ S0 · HERO (dark) ━━━━ -->
<section class="slide on bv" id="s0">
  <div class="hg" id="HG"></div>
  <div class="hgl" id="HGL"></div>
  <span class="gn" style="color:var(--td1)">01</span>
  <div class="pw">
    <div style="position:relative;z-index:1;max-width:calc(100% + 8vw);">
      <span class="ey" data-f="0" style="margin-bottom:1.2rem;display:block;">
        Helden Inc. · Haarlem, Netherlands · Game-Based Learning Pioneers
      </span>
      <!-- 8. Line-by-line reveal — hero bleeds right intentionally -->
      <div class="rl" style="margin-bottom:-.04em;">
        <span class="ri th" style="animation-delay:.14s;">We don't</span>
      </div>
      <div class="rl">
        <span class="ri th" style="animation-delay:.28s;">do <em>boring</em>.</span>
      </div>
      <!-- Rule + copy row -->
      <div data-f="3" style="margin-top:2.2rem;display:flex;gap:1.5rem;align-items:flex-start;max-width:560px;">
        <span class="ry" data-w="0" style="width:40px;flex-shrink:0;margin-top:.55rem;"></span>
        <span class="tb">Game-based learning and internal communication for the world's most forward-thinking organisations. Heineken, KLM, Disney, EY — they chose Helden.</span>
      </div>
      <div data-f="4" style="margin-top:1.2rem;">
        <span style="font-family:var(--mono);font-size:.48rem;letter-spacing:.24em;text-transform:uppercase;color:var(--td2);">
          200+ Enterprise Clients &nbsp;·&nbsp; Benelux &amp; Beyond
        </span>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S1 · MISSION (light) ━━━━ -->
<section class="slide bp" id="s1">
  <div class="lg"></div>
  <span class="gn" style="color:var(--tl1)">02</span>
  <div class="pw">
    <div style="max-width:960px;position:relative;z-index:1;">
      <span class="ey lm" data-f="0" style="margin-bottom:1.4rem;display:block;">Our Mission</span>
      <!-- Line reveals on light slide -->
      <div class="rl">
        <span class="ri" data-r="1" style="font-family:var(--serif);font-size:clamp(1.6rem,4vw,4.8rem);font-weight:100;font-style:italic;line-height:1.04;color:var(--tl2);letter-spacing:-.015em;display:block;">
          Endless PowerPoints, passive workshops, forgotten messages —
        </span>
      </div>
      <div class="rl" style="margin-top:.3rem;">
        <span class="ri" data-r="2" style="font-family:var(--serif);font-size:clamp(1.6rem,4vw,4.8rem);font-weight:900;line-height:1.0;color:var(--tl1);letter-spacing:-.02em;display:block;">
          We replace all of it with games<br>people <em style="color:var(--yd);font-style:italic;">actually remember</em>.
        </span>
      </div>
      <span class="rl2" data-w="0" style="width:100%;display:block;margin:1.5rem 0;"></span>
      <span class="tb lm" data-f="3" style="max-width:600px;">
        We help HR teams and communications professionals make serious topics — strategy, change management, compliance, onboarding — fun, visual, and immovably memorable. Always through a game.
      </span>
    </div>
  </div>
</section>

<!-- ━━━━ S2 · PROBLEM (dark) ━━━━ -->
<section class="slide bv" id="s2">
  <div class="prb"></div>
  <span class="gn" style="color:var(--td1)">03</span>
  <div class="pw">
    <div class="g2" style="gap:4vw;align-items:flex-end;padding-bottom:8vh;">
      <div>
        <span class="ey" data-f="0" style="margin-bottom:1rem;display:block;">The Problem</span>
        <!-- 7. Stat counter — fills from 0 to 10 -->
        <span class="tstat"><span class="cnt" data-to="10" data-sfx="%">10%</span></span>
      </div>
      <div style="padding-bottom:4.5rem;">
        <span class="ry" data-w="0" style="display:block;width:100%;margin-bottom:1.4rem;"></span>
        <div class="rl">
          <span class="ri th2" data-r="2" style="font-size:clamp(1.4rem,3vw,3.5rem);">
            That's how much your team retains after a typical presentation.
          </span>
        </div>
        <span class="tb" data-f="3" style="margin-top:.9rem;max-width:370px;">
          The other 90% is gone within 48 hours. Your strategy, your culture, your message — evaporated. There is a fundamentally better way.
        </span>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S3 · INSIGHT (dark) ━━━━ -->
<section class="slide bv2" id="s3">
  <span class="gn" style="color:var(--td1)">04</span>
  <div class="pw">
    <div class="cx" style="max-width:1000px;">
      <span class="ey" data-f="0">The Insight</span>
      <div class="rl" style="width:100%;">
        <span class="ri tdim" data-r="1" style="text-align:center;">People don't learn by watching.</span>
      </div>
      <div class="rl" style="width:100%;">
        <span class="ri tlit" data-r="2" style="text-align:center;">People learn by <span class="hl">playing</span>.</span>
      </div>
      <span class="ry" data-w="0" style="width:32px;margin:.5rem 0;"></span>
      <span data-f="3" style="font-family:var(--mono);font-size:.54rem;letter-spacing:.2em;text-transform:uppercase;color:var(--td2);text-align:center;display:block;line-height:2.2;">
        <span style="color:var(--y);">3× higher</span> retention &nbsp;·&nbsp;
        <span style="color:var(--y);">100%</span> active participation &nbsp;·&nbsp;
        <span style="color:var(--y);">−60%</span> change resistance
      </span>
    </div>
  </div>
</section>

<!-- ━━━━ S4 · FUTUREGAME (dark) ━━━━ -->
<section class="slide bv" id="s4">
  <div class="fgg"></div>
  <span class="gn" style="color:var(--td1)">05</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g2">
      <div class="sk" style="z-index:1;">
        <span class="bdg" data-p="0">🏆 Bestseller</span>
        <div class="rl"><span class="ri tp" data-r="1">Future<br>Game</span></div>
        <span class="tb" data-f="2" style="max-width:350px;">An interactive strategic simulation. Your team experiences future scenarios — not just discusses them. Design thinking meets game mechanics. Built around omdenken methodology.</span>
        <ul class="fl" data-f="3">
          <li>Strategy, change management &amp; new policy</li>
          <li>4–200 participants · Online or on location</li>
          <li>Fully automated · Concept within 48 hours</li>
          <li>Max 2 new clients per month by design</li>
        </ul>
        <div class="pq" data-f="4">
          <span class="pqt">"Holy Sh*t, the game is amazing!"</span>
          <span class="pqa">Verified client · Helden Inc.</span>
        </div>
      </div>
      <!-- Animated game board right -->
      <div class="gb" data-f="2" id="GB"></div>
    </div>
  </div>
</section>

<!-- ━━━━ S5 · ESCAPE ROOM (light) ━━━━ -->
<section class="slide bp" id="s5">
  <div class="lg"></div>
  <span class="gn" style="color:var(--tl1)">06</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g12">
      <div class="sk" style="z-index:1;">
        <span class="bdg lm" data-p="0">On Location</span>
        <div class="rl"><span class="ri tp lm" data-r="1">Escape Room<br><em>on Location</em></span></div>
        <span class="tb lm" data-f="2" style="max-width:370px;">A fully produced escape room delivered to your office. We handle everything: concept, build-up, professional hosts from theater and film, teardown. Your story in every puzzle.</span>
        <ul class="fl lm" data-f="3">
          <li>20–120 participants simultaneously</li>
          <li>45–90 min · App-guided with live leaderboard</li>
          <li>Custom themes — culture, compliance, change</li>
          <li>Available throughout Benelux &amp; internationally</li>
        </ul>
      </div>
      <div class="hxs" data-f="1">
        <div class="hxr hx1"></div>
        <div class="hxr hx2"></div>
        <div class="hxr hx3"></div>
        <div class="hxr hxc l"></div>
        <span class="hxlb hxlt" style="color:var(--tl2);">Up to 120 players</span>
        <span class="hxlb hxlb2" style="color:var(--tl2);">45–90 min</span>
        <span class="hxlb hxlb3" style="color:var(--tl2);">All locations</span>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S6 · ESCAPE BOX (dark) ━━━━ -->
<section class="slide bv2" id="s6">
  <span class="gn" style="color:var(--td1)">07</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g21">
      <div class="bxs" data-f="0">
        <div class="iso"><div class="it"></div><div class="il"></div><div class="ir"></div></div>
        <span class="bxl bxl1">4–6 per box</span>
        <span class="bxl bxl2">30/60/90 min</span>
        <span class="bxl bxl3">Up to 300</span>
      </div>
      <div class="sk" style="z-index:1;">
        <span class="bdg" data-p="0">Portable</span>
        <div class="rl"><span class="ri tp" data-r="1">Escape<br><em>Box</em></span></div>
        <span class="tb" data-f="2" style="max-width:360px;">A complete escape room in a portable box. Teams of 4–6 solve physical puzzles and riddles. Multiple boxes run in parallel for groups up to 300. Not breaking out — breaking <em>in</em>.</span>
        <ul class="fl" data-f="3">
          <li>Groups of 20 to 300 participants</li>
          <li>Standard or 100% personalised content</li>
          <li>Dutch &amp; English · Indoor &amp; outdoor</li>
          <li>Full build-up &amp; teardown handled</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S7 · ONBOARDING (light) ━━━━ -->
<section class="slide bp2" id="s7">
  <div class="lg"></div>
  <span class="gn" style="color:var(--tl1)">08</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g2">
      <div class="sk" style="z-index:1;">
        <span class="bdg lm" data-p="0">Day One</span>
        <div class="rl"><span class="ri tp lm" data-r="1">Onboarding<br><em>Game</em></span></div>
        <span class="tb lm" data-f="2" style="max-width:360px;">Your first day is exciting and nerve-wracking. By playing together, new employees break the ice from minute one — experiencing culture, values, and colleagues playfully.</span>
        <ul class="fl lm" data-f="3">
          <li>Culture, values &amp; organisational structure</li>
          <li>Scalable for large new-hire cohorts</li>
          <li>Reusable — adapt for every intake</li>
          <li>Developed with UMC Utrecht &amp; DSM</li>
        </ul>
        <span class="bdgo lm" data-p="1" style="width:fit-content;">"Highly recommended!" — Nicole Blom, UMC Utrecht</span>
      </div>
      <div class="jrn" data-f="1">
        <div class="jst"><div class="jnd d">✓</div><div class="ji"><span class="jit">Welcome &amp; context</span><span class="jis">Company intro · Culture brief</span></div></div>
        <div class="jst"><div class="jnd d">✓</div><div class="ji"><span class="jit">Game begins</span><span class="jis">Puzzles · Challenges · Team</span></div></div>
        <div class="jst"><div class="jnd a">3</div><div class="ji"><span class="jit">Culture discovery</span><span class="jis">Values · People · Stories</span></div></div>
        <div class="jst"><div class="jnd n">4</div><div class="ji"><span class="jit">Debrief &amp; connect</span><span class="jis">Insights · First connections</span></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S8 · MICRO LEARNING (dark) ━━━━ -->
<section class="slide bv" id="s8">
  <span class="gn" style="color:var(--td1)">09</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g21">
      <div class="phs" data-f="0">
        <div class="ph">
          <div class="phb"></div><div class="phb d"></div>
          <div class="phc"><span class="phct">Module 4 of 9</span><span class="phcn">Sustainability Policy 2025</span><span class="phcd">⏱ 8 min · Escape format</span></div>
          <div class="phc"><span class="phct">Monthly Challenge</span><span class="phcn">New HR Regulation</span><span class="phcd">⏱ 5 min · Quiz + puzzle</span></div>
          <div class="phc"><span class="phct">Compliance ✓</span><span class="phcn">GDPR Refresher</span><span class="phcd">⏱ 3 min · Done</span></div>
          <div class="prw"><div class="ps y"></div><div class="ps y"></div><div class="ps y"></div><div class="ps"></div><div class="ps"></div><span class="pp">62%</span></div>
        </div>
        <div class="ft ft1"><span class="fn">2–15</span><span class="fa">min/module</span></div>
        <div class="ft ft2"><span class="fn">3×</span><span class="fa">retention</span></div>
        <div class="ft ft3"><span class="fn">∞</span><span class="fa">reusable</span></div>
      </div>
      <div class="sk" style="z-index:1;">
        <span class="bdg" data-p="0">Always On</span>
        <div class="rl"><span class="ri tp" data-r="1">Micro<br><em>Learning</em></span></div>
        <span class="tb" data-f="2" style="max-width:350px;">Monthly escape-room-style knowledge challenges delivered in your browser. No download. No install. The right knowledge at the right moment — compliance, culture, policy, skills.</span>
        <ul class="fl" data-f="3">
          <li>2–15 minute bite-sized modules</li>
          <li>Monthly game-based knowledge challenges</li>
          <li>Integrates with existing LMS platforms</li>
          <li>Developed with RVKO · Custom per dept.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S9 · CUSTOM ESCAPE ROOM (light) ━━━━ -->
<section class="slide bp" id="s9">
  <div class="lg"></div>
  <span class="gn" style="color:var(--tl1)">10</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g2">
      <div class="sk" style="z-index:1;">
        <span class="bdg lm" data-p="0">Tailor-Made</span>
        <div class="rl"><span class="ri tp lm" data-r="1" style="font-size:clamp(2.5rem,5.2vw,7rem);">Custom<br><em>Escape<br>Room</em></span></div>
        <span class="tb lm" data-f="2" style="max-width:370px;">A standard escape room says: I didn't make an effort. We build experiences where every puzzle reflects your specific story. Mercedes, KLM, Disney — they chose premium.</span>
        <ul class="fl lm" data-f="3">
          <li>Free concept — pay only when satisfied</li>
          <li>Full script, props &amp; production handled</li>
          <li>Professional actors &amp; live bands available</li>
          <li>Events for 20 to 3,000 participants</li>
        </ul>
      </div>
      <div class="pss" data-f="1">
        <div class="psi ft"><span class="psn">01</span><div><span class="pst">Free concept consultation</span><span class="pss2">Questionnaire · Immediate results</span></div></div>
        <div class="psi"><span class="psn">02</span><div><span class="pst">Script + quote in 48h</span><span class="pss2">Single point of contact throughout</span></div></div>
        <div class="psi"><span class="psn">03</span><div><span class="pst">Unforgettable experience delivered</span><span class="pss2">Build-up, hosting &amp; teardown</span></div></div>
        <div class="psi"><span class="psn">04</span><div><span class="pst">Reusable game library</span><span class="pss2">Modular · Adaptable · Lasting value</span></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S10 · GAMEPLAN (dark) ━━━━ -->
<section class="slide bv2" id="s10">
  <span class="gn" style="color:var(--td1)">11</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g12">
      <div class="sk" style="z-index:1;">
        <span class="bdg" data-p="0">Strategy Tool</span>
        <div class="rl"><span class="ri tp" data-r="1">Game<br><em>Plan</em></span></div>
        <span class="tb" data-f="2" style="max-width:350px;">Turn strategy sessions into interactive game experiences. Every voice is heard. Abstract plans become concrete actions everyone believes in.</span>
        <ul class="fl" data-f="3">
          <li>Strategic planning &amp; team alignment</li>
          <li>Decision-making under realistic pressure</li>
          <li>All insights automatically captured</li>
          <li>Leadership teams to large departments</li>
        </ul>
      </div>
      <div class="gpv" data-f="1">
        <div class="gpr"><div class="gpn ac">Strategy Session</div><div class="gpl"></div><div class="gpn dm">Input Phase</div></div>
        <div class="gpr" style="padding-left:14px;"><div class="gpl" style="max-width:14px;flex:none;"></div><div class="gpn dk">Group A</div><div class="gpl"></div><div class="gpn dk">Group B</div></div>
        <div class="gpr"><div class="gpn dm">Synthesis</div><div class="gpl"></div><div class="gpn ac">Action Plan</div></div>
        <div class="gpr"><div class="gpn dk">Implement</div><div class="gpl"></div><div class="gpn dk">Review</div><div class="gpl"></div><div class="gpn dm">Iterate</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S11 · EVENTS (light) ━━━━ -->
<section class="slide bp" id="s11">
  <div class="lg"></div>
  <span class="gn" style="color:var(--tl1)">12</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g2">
      <div class="sk" style="z-index:1;">
        <span class="bdg lm" data-p="0">Large Scale</span>
        <div class="rl"><span class="ri tp lm" data-r="1">Learning<br><em>Events</em></span></div>
        <span class="tb lm" data-f="2" style="max-width:360px;">From 50 to 3,000 people. We design experiences that make your entire organisation feel a message simultaneously. Original musicals, live games, theatrical scenarios in extraordinary venues.</span>
        <ul class="fl lm" data-f="3">
          <li>Events for 50 to 3,000 participants</li>
          <li>Theaters, warehouses, churches as venues</li>
          <li>Original musicals &amp; live concerts</li>
          <li>Professional actors throughout</li>
        </ul>
      </div>
      <div class="evg" data-f="1">
        <div class="evt ft"><span class="evic">🎭</span><span class="evn">Theatre Experience</span><span class="evs">Actors · Live performance</span></div>
        <div class="evt"><span class="evic">🎵</span><span class="evn">Musical Production</span><span class="evs">Live band · Original score</span></div>
        <div class="evt"><span class="evic">🔐</span><span class="evn">Live Escape Game</span><span class="evs">Real-life · Large groups</span></div>
        <div class="evt"><span class="evic">🏆</span><span class="evn">Game Championship</span><span class="evs">Competition · Leaderboard</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S12 · ALL PRODUCTS (light) ━━━━ -->
<section class="slide bp2" id="s12">
  <div class="lg"></div>
  <span class="gn" style="color:var(--tl1)">13</span>
  <div class="pw">
    <div style="width:100%;position:relative;z-index:1;">
      <div style="display:flex;align-items:baseline;justify-content:space-between;padding-bottom:.85rem;border-bottom:1px solid var(--bl1);margin-bottom:1px;">
        <div class="rl"><span class="ri" data-r="0" style="font-family:var(--serif);font-size:clamp(2rem,4.5vw,5.5rem);font-weight:300;line-height:.9;color:var(--tl1);letter-spacing:-.018em;display:block;">Nine ways to<br>make them <em style="color:var(--yd);font-style:italic;">remember</em>.</span></div>
        <span data-f="1" style="font-family:var(--mono);font-size:.48rem;letter-spacing:.16em;text-transform:uppercase;color:var(--tl2);flex-shrink:0;margin-left:1rem;">09 products</span>
      </div>
      <div class="pgr">
        <div class="pi star"><span class="pin">01</span><span class="piname">FutureGame</span></div>
        <div class="pi"><span class="pin">02</span><span class="piname">Escape Room on Location</span></div>
        <div class="pi"><span class="pin">03</span><span class="piname">Custom Escape Room</span></div>
        <div class="pi"><span class="pin">04</span><span class="piname">Escape Box</span></div>
        <div class="pi"><span class="pin">05</span><span class="piname">In-Company Training Box</span></div>
        <div class="pi"><span class="pin">06</span><span class="piname">Onboarding Game</span></div>
        <div class="pi"><span class="pin">07</span><span class="piname">GamePlan</span></div>
        <div class="pi"><span class="pin">08</span><span class="piname">Micro Learning</span></div>
        <div class="pi"><span class="pin">09</span><span class="piname">Learning Events</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S13 · CLIENTS (light) ━━━━ -->
<section class="slide bp" id="s13">
  <div class="lg"></div>
  <span class="gn" style="color:var(--tl1)">14</span>
  <div class="pw" style="padding:64px 5.5vw 46px;">
    <div class="g2" style="gap:5vw;align-items:start;">
      <div class="sk" style="z-index:1;">
        <span class="ey lm" data-f="0">Trusted by</span>
        <!-- Stat counter: 200+ -->
        <span data-p="0" style="font-family:var(--serif);font-size:clamp(7rem,17vw,22rem);font-weight:100;line-height:.76;letter-spacing:-.05em;color:var(--tl1);display:block;">
          <span class="cnt" data-to="200" data-sfx="+">200+</span>
        </span>
        <span data-f="1" style="font-family:var(--serif);font-size:clamp(.9rem,1.6vw,1.8rem);font-weight:100;font-style:italic;color:var(--tl2);display:block;margin-bottom:1.2rem;">enterprise organisations</span>
        <div class="cstrip">
          <span class="cn">Heineken</span><span class="cn">KLM</span><span class="cn">ING</span><span class="cn">ABN AMRO</span>
          <span class="cn">EY</span><span class="cn">Schiphol</span><span class="cn">L'Oréal</span><span class="cn">Disney</span>
          <span class="cn">BMW</span><span class="cn">Deloitte</span><span class="cn">ArboNed</span><span class="cn">UMC Utrecht</span>
        </div>
      </div>
      <div class="sk" style="gap:10px;z-index:1;">
        <span class="ey lm" data-f="1">What they say</span>
        <div class="tc" data-r="2"><span class="tq">"Holy Sh*t, the game is amazing! The students were so busy with the puzzles they didn't have time to ask anything."</span><span class="ta">Eva Kleine</span><span class="tr">Company Doctor · ArboNed</span></div>
        <div class="tc" data-r="3"><span class="tq">"Together with Helden Inc. we developed a great game for our onboarding. Our team was very enthusiastic — highly recommended!"</span><span class="ta">Nicole Blom</span><span class="tr">L&amp;D Manager · UMC Utrecht</span></div>
        <div class="tc" data-r="4"><span class="tq">"Your commitment, creativity and energy contributed to a very successful event enjoyed by almost everyone."</span><span class="ta">Jeroen Kluytman</span><span class="tr">Manager Employability · DSM</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ━━━━ S14 · CTA (yellow) ━━━━ -->
<section class="slide" id="s14" style="background:var(--y);">
  <div class="cring cr1"></div>
  <div class="cring cr2"></div>
  <div class="pw" style="position:relative;z-index:2;overflow:hidden;">
    <div class="cx">
      <div class="rl" style="width:100%;">
        <span class="ri ctah" data-r="0">Make them<br>remember.</span>
      </div>
      <span class="ctag" data-f="1">Free consultation · Concept within 48 hours · No commitment</span>
      <a class="ctabn" data-p="0" href="https://helden-inc.com/en/" target="_blank" rel="noopener">
        Plan your free demo
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M2.5 7h9M8 3.5L11.5 7 8 10.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <span class="ctaurl" data-f="2">helden-inc.com · Haarlem, Netherlands</span>
    </div>
  </div>
</section>

</main>

<!-- ══════════════════════════════════════════════════════════════════
     JAVASCRIPT ENGINE
══════════════════════════════════════════════════════════════════ -->
<script>
(function(){
'use strict';
const N=15, CTA=14, WIPE=580, HALF=275;
const LIGHT=new Set([1,5,7,9,11,12,13]);

/* DOM */
const WP  = document.getElementById('WP');
const SB  = document.getElementById('SB');
const NIs = document.querySelectorAll('.ni');
const CT  = document.getElementById('CT');
const PF  = document.getElementById('PF');
const PG  = document.getElementById('PG');
const CU  = document.getElementById('CU');
const TK  = document.getElementById('TK');
const BU  = document.getElementById('BU');
const BD  = document.getElementById('BD');
const ABs = document.querySelectorAll('.ab');
const SLs = document.querySelectorAll('.slide');
const HG  = document.getElementById('HG');
const HGL = document.getElementById('HGL');
const CD  = document.getElementById('CD');
const CR  = document.getElementById('CR');
const CL  = document.getElementById('CL');

let cur=0, busy=false;

/* ━━━━━━━━━━━━━━━━━━━━━━━
   CUSTOM CURSOR
━━━━━━━━━━━━━━━━━━━━━━━ */
let mx=window.innerWidth/2, my=window.innerHeight/2;
let rx=mx, ry=my;

document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  CD.style.left = mx+'px'; CD.style.top = my+'px';
  // Parallax on hero
  if(cur===0){
    const dx=(mx/window.innerWidth -.5);
    const dy=(my/window.innerHeight-.5);
    if(HG)  HG.style.transform  = `translate(${dx*18}px,${dy*14}px)`;
    if(HGL) HGL.style.transform = `translate(calc(-50% + ${dx*12}px),${dy*9}px)`;
  }
});

// Ring follows with lag
(function raf(){
  rx += (mx-rx)*.09;
  ry += (my-ry)*.09;
  CR.style.left = rx+'px'; CR.style.top = ry+'px';
  CL.style.left = rx+'px'; CL.style.top = ry+'px';
  requestAnimationFrame(raf);
})();

// Hover expansion
document.querySelectorAll('a,button,.ni,.pi,.psi,.evt,.ab,.logo').forEach(el=>{
  el.addEventListener('mouseenter',()=>{
    document.body.classList.add('chov');
    const t=el.dataset.lbl||(el.tagName==='A'?'open ↗':'');
    CL.textContent=t;
  });
  el.addEventListener('mouseleave',()=>{
    document.body.classList.remove('chov');
    CL.textContent='';
  });
});

/* ━━━━━━━━━━━━━━━━━━━━━━━
   MARQUEE
━━━━━━━━━━━━━━━━━━━━━━━ */
(function(){
  const T=document.getElementById('TKT');
  if(!T) return;
  const items=[
    {t:'FutureGame',y:true},{t:'Escape Room on Location'},{t:'Custom Escape Rooms'},{t:'Escape Box',y:true},
    {t:'In-Company Training'},{t:'Onboarding Game'},{t:'GamePlan',y:true},{t:'Micro Learning'},{t:'Learning Events'},
    {t:'FutureGame',y:true},{t:'Escape Room on Location'},{t:'Custom Escape Rooms'},{t:'Escape Box',y:true},
    {t:'In-Company Training'},{t:'Onboarding Game'},{t:'GamePlan',y:true},{t:'Micro Learning'},{t:'Learning Events'},
  ];
  [...items,...items].forEach(it=>{
    const s=document.createElement('span');
    s.className='tk-i'+(it.y?' y':'');
    s.textContent=it.t;
    T.appendChild(s);
  });
})();

/* ━━━━━━━━━━━━━━━━━━━━━━━
   GAME BOARD
━━━━━━━━━━━━━━━━━━━━━━━ */
(function(){
  const b=document.getElementById('GB');
  if(!b) return;
  const LIT=new Set([1,2,3,8,9,10,11,16,17,18,19,24,25,26,32,33,34]);
  const WM =new Set([9,10,17,18,25,26]);
  const HT =new Set([17,18]);
  const CR =new Set([18]);
  for(let i=0;i<48;i++){
    const c=document.createElement('div');
    c.className='gc'+(CR.has(i)?' core':HT.has(i)?' hot':WM.has(i)?' warm':LIT.has(i)?' dim':'');
    b.appendChild(c);
  }
})();
let bTimer=null;
const WAVES=[[0,1,8,9],[1,2,9,10],[2,3,10,11],[9,10,17,18],[17,18,25,26],[25,26,33,34],
             [18,19,26,27],[8,16,24,32],[4,12,20,28],[5,13,21,29],[6,14,22,30]];
let wi=0;
function bStart(){
  clearInterval(bTimer);
  bTimer=setInterval(()=>{
    document.querySelectorAll('.gc.hot').forEach(c=>c.classList.remove('hot'));
    WAVES[wi%WAVES.length].forEach(i=>{
      const c=document.querySelectorAll('.gc')[i];
      if(c&&!c.classList.contains('core')) c.classList.add('hot');
    });
    wi++;
  },760);
}
function bStop(){
  clearInterval(bTimer);
  document.querySelectorAll('.gc.hot').forEach(c=>c.classList.remove('hot'));
}

/* ━━━━━━━━━━━━━━━━━━━━━━━
   LINE-BY-LINE REVEAL
━━━━━━━━━━━━━━━━━━━━━━━ */
function revealLines(sl){
  // Reset first
  sl.querySelectorAll('.ri').forEach(el=>{
    el.style.animation='none';
    el.classList.remove('rev');
  });
  void sl.offsetHeight;
  // Apply with stagger
  sl.querySelectorAll('.ri').forEach((el,i)=>{
    const base = parseFloat(el.style.animationDelay)||0;
    el.style.animationDelay = (base || (0.14 + i*0.14))+'s';
    el.classList.add('rev');
  });
}

/* ━━━━━━━━━━━━━━━━━━━━━━━
   STAT COUNTERS
━━━━━━━━━━━━━━━━━━━━━━━ */
function runCounters(sl){
  sl.querySelectorAll('.cnt[data-to]').forEach(el=>{
    const target=parseInt(el.dataset.to);
    const sfx=el.dataset.sfx||'';
    const dur=1100;
    const t0=performance.now();
    function tick(now){
      const p=Math.min((now-t0)/dur,1);
      const ep=1-(1-p)*(1-p)*(1-p); // ease-out-cubic
      el.textContent=Math.round(ep*target)+sfx;
      if(p<1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  });
}

/* ━━━━━━━━━━━━━━━━━━━━━━━
   RESET ANIMATIONS
━━━━━━━━━━━━━━━━━━━━━━━ */
function resetAnims(sl){
  sl.querySelectorAll('[data-r],[data-f],[data-w],[data-p],.pi,.cn').forEach(e=>{
    e.style.animation='none'; e.style.opacity='';
  });
  sl.querySelectorAll('.ri').forEach(e=>{
    e.style.animation='none'; e.classList.remove('rev');
  });
  void sl.offsetHeight;
  sl.querySelectorAll('[data-r],[data-f],[data-w],[data-p],.pi,.cn').forEach(e=>{
    e.style.animation='';
  });
}

/* ━━━━━━━━━━━━━━━━━━━━━━━
   CHROME
━━━━━━━━━━━━━━━━━━━━━━━ */
function chrome(i){
  const lm=LIGHT.has(i), cta=i===CTA;
  SB.classList.toggle('lm',lm);
  NIs.forEach((n,j)=>n.classList.toggle('on',j===i));
  CT.innerHTML='<b>'+String(i+1).padStart(2,'0')+'</b> / 15';
  CT.classList.toggle('lm',lm);
  ABs.forEach(b=>b.classList.toggle('lm',lm));
  PF.style.width=((i+1)/N*100)+'%';
  PF.style.opacity=cta?'0':'1';
  PG.classList.toggle('lm',lm);
  TK.classList.toggle('lm',lm);
  CU.classList.toggle('gone',i!==0);
  if(i!==0){
    if(HG)  HG.style.transform='';
    if(HGL) HGL.style.transform='';
  }
}

/* ━━━━━━━━━━━━━━━━━━━━━━━
   NAVIGATION — diagonal wipe
━━━━━━━━━━━━━━━━━━━━━━━ */
function go(nx){
  if(busy||nx===cur||nx<0||nx>=N) return;
  busy=true;
  const fwd=nx>cur;

  // Fire wipe
  WP.className='';
  void WP.offsetWidth;
  WP.classList.add(fwd?'fwd':'bwd');

  // Swap at midpoint
  setTimeout(()=>{
    SLs[cur].classList.remove('on');
    SLs[cur].classList.add('off');
    const nxt=SLs[nx];
    resetAnims(nxt);
    nxt.classList.remove('off');
    nxt.classList.add('on');
    if(nx===4) bStart(); else bStop();
    chrome(nx);
    revealLines(nxt);
    runCounters(nxt);
    cur=nx;
  }, HALF);

  // Clean up
  setTimeout(()=>{
    WP.className='';
    SLs.forEach(s=>s.classList.remove('off'));
    busy=false;
  }, WIPE+120);
}

// Boot
chrome(0);
revealLines(SLs[0]);

/* ━━━━━━━━━━━━━━━━━━━━━━━
   INPUT EVENTS
━━━━━━━━━━━━━━━━━━━━━━━ */
let wa=0, wt=null;
window.addEventListener('wheel', e=>{
  e.preventDefault();
  wa+=Math.abs(e.deltaY);
  clearTimeout(wt); wt=setTimeout(()=>wa=0,240);
  if(wa>52){ wa=0; go(cur+(e.deltaY>0?1:-1)); }
},{passive:false});

window.addEventListener('keydown',e=>{
  if(['ArrowDown','PageDown','Space','ArrowRight'].includes(e.key)){e.preventDefault();go(cur+1);}
  if(['ArrowUp','PageUp','ArrowLeft'].includes(e.key)){e.preventDefault();go(cur-1);}
  if(e.key==='Home') go(0);
  if(e.key==='End')  go(N-1);
});

let ty=0;
window.addEventListener('touchstart',e=>{ty=e.touches[0].clientY;},{passive:true});
window.addEventListener('touchend',e=>{const d=ty-e.changedTouches[0].clientY;if(Math.abs(d)>44)go(cur+(d>0?1:-1));},{passive:true});

NIs.forEach(n=>n.addEventListener('click',()=>go(+n.dataset.i)));
BU.addEventListener('click',()=>go(cur-1));
BD.addEventListener('click',()=>go(cur+1));
CU.addEventListener('click',()=>go(1));
document.getElementById('HM').addEventListener('click',e=>{e.preventDefault();go(0);});

// Streamlit height sync
function sh(){try{window.parent.postMessage({isStreamlitMessage:true,type:'streamlit:setFrameHeight',height:Math.max(window.innerHeight,700)},'*');}catch(_){}}
sh(); window.addEventListener('resize',sh);

})();
</script>
</body>
</html>"""

components.html(HTML, height=900, scrolling=False)
