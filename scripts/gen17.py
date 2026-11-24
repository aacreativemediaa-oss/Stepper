"""Task 17: Briskwalk VS Stepper. Format terkini (headline 100px, sub-headline 47px, max 100px)."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t16 = open(S + '/template16.html').read()
g8 = open(S + '/gen8.py').read()
BASE = re.search(r"BASE = '''(.*?)'''", g8, re.S).group(1)

def block(src, bid):
    i = src.index(f'<div id="{bid}"'); d = 0
    for m in re.finditer(r'<div\b|</div>', src[i:]):
        d += 1 if m.group(0).startswith('<div') else -1
        if d == 0: return src[i:i + m.end()]
def timed(h, s, d):
    return re.sub(r'data-start="[0-9.]+" data-duration="[0-9.]+"', f'data-start="{s:.2f}" data-duration="{d:.2f}"', h, count=1)

head = t16[:t16.index('    </style>')]
head += '''      .panel { left: 40px; right: 40px; background: rgba(10,10,12,0.88); border: 6px solid #000; border-radius: 34px; box-shadow: 0 16px 0 #000; padding: 24px 22px; }
      .cols { display: flex; gap: 18px; }
      .col2 { flex: 1; text-align: center; }
      .col2 h3 { font-family: var(--font-display); font-weight: 400; font-size: 56px; line-height: 1; margin-bottom: 10px; -webkit-text-stroke: 4px #000; paint-order: stroke fill; }
      .col2 .ic { width: 230px; height: 230px; display: block; margin: 0 auto 10px; }
      .col2 .pl { display: flex; flex-direction: column; gap: 10px; align-items: center; }
      .col2 .pill { font-size: 27px; padding: 10px 18px; gap: 10px; }
      .col2 .pill svg { width: 32px; height: 32px; }
      .vsb { align-self: center; width: 96px; height: 96px; border-radius: 50%; background: var(--red); border: 6px solid #000; box-shadow: 0 8px 0 #000;
             display: flex; align-items: center; justify-content: center; font-size: 50px; color: #fff; -webkit-text-stroke: 4px #000; paint-order: stroke fill; flex: none; }
      .thead { display: flex; font-family: var(--font-ui); font-weight: 900; font-size: 24px; letter-spacing: 0.08em; color: #9aa; padding: 0 6px 10px; border-bottom: 3px solid #333; }
      .thead span:nth-child(1) { width: 150px; } .thead span:nth-child(2), .thead span:nth-child(3) { flex: 1; text-align: center; }
      .crow { display: flex; align-items: center; height: 104px; border-bottom: 3px dashed #2a2a2a; padding: 0 6px; }
      .crow:last-child { border-bottom: 0; }
      .crow .kg { width: 150px; font-size: 58px; color: #fff; }
      .crow .c { flex: 1; display: flex; align-items: center; gap: 10px; padding: 0 8px; }
      .crow .bar { flex: 1; height: 30px; background: #222; border-radius: 15px; border: 3px solid #000; overflow: hidden; }
      .crow .bar i { display: block; height: 100%; border-radius: 15px; transform-origin: 0 50%; }
      .crow .v { width: 88px; text-align: right; font-size: 50px; line-height: 1; }
      .note { margin-top: 12px; font-family: var(--font-ui); font-weight: 800; font-size: 20px; color: #ccc; text-align: center; }
      .figs4 { display: flex; justify-content: space-around; }
      .figs4 svg { width: 200px; height: 420px; display: block; }
      .figlab { font-family: var(--font-ui); font-weight: 900; font-size: 22px; letter-spacing: 0.1em; color: #9aa; text-align: center; }
'''
CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CROSS = '<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#000"/><path d="M20 20 L44 44 M44 20 L20 44" stroke="#ff3b30" stroke-width="8" stroke-linecap="round"/></svg>'
WALKER = '''<svg class="ic" id="walker" viewBox="0 0 230 230"><circle cx="115" cy="115" r="108" fill="#2a2a30" stroke="#000" stroke-width="6"/>
  <g stroke="#fff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <circle cx="122" cy="48" r="16" fill="#fff" stroke="none"/>
    <path d="M118 72 L108 124"/><path d="M114 84 L86 104 M114 84 L140 106"/>
    <path id="wlegA" d="M108 124 L90 168 L76 192"/><path id="wlegB" d="M108 124 L128 162 L150 180"/></g>
  <path id="warr" d="M40 214 H190 M172 200 L190 214 L172 228" stroke="#ffd400" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
STEPI = '''<svg class="ic" id="stepi" viewBox="0 0 230 230"><circle cx="115" cy="115" r="108" fill="#2a2a30" stroke="#000" stroke-width="6"/>
  <g id="pedL"><rect x="40" y="118" width="64" height="18" rx="5" fill="#ff3b30" stroke="#000" stroke-width="4"/></g>
  <g id="pedR"><rect x="126" y="118" width="64" height="18" rx="5" fill="#ff3b30" stroke="#000" stroke-width="4"/></g>
  <path d="M72 136 L115 176 L158 136" stroke="#888" stroke-width="10" fill="none"/><rect x="60" y="172" width="110" height="16" rx="6" fill="#000"/>
  <g stroke="#c6ff00" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M115 36 V96"/><path d="M98 52 L115 36 L132 52"/><path d="M98 80 L115 96 L132 80"/></g></svg>'''

def fig(front, parts, color, fid):
    P = {'shoulders': '<ellipse cx="54" cy="99" rx="15" ry="13"/><ellipse cx="146" cy="99" rx="15" ry="13"/>',
         'arms': '<ellipse cx="38" cy="152" rx="9" ry="26" transform="rotate(8 38 152)"/><ellipse cx="162" cy="152" rx="9" ry="26" transform="rotate(-8 162 152)"/>',
         'core': '<rect x="80" y="112" width="40" height="92" rx="12"/>',
         'quads': '<ellipse cx="80" cy="292" rx="15" ry="38"/><ellipse cx="121" cy="292" rx="15" ry="38"/>',
         'glutes': '<ellipse cx="81" cy="238" rx="19" ry="16"/><ellipse cx="119" cy="238" rx="19" ry="16"/>',
         'hams': '<ellipse cx="80" cy="298" rx="14" ry="32"/><ellipse cx="121" cy="298" rx="14" ry="32"/>',
         'calves': '<ellipse cx="79" cy="370" rx="10" ry="26"/><ellipse cx="120" cy="370" rx="10" ry="26"/>'}
    hl = ''.join(P[p] for p in parts)
    return f'<div><svg viewBox="0 0 200 420">{BASE}<g class="hl" id="{fid}" fill="{color}" stroke="#000" stroke-width="3">{hl}</g></svg><div class="figlab">{"DEPAN" if front else "BELAKANG"}</div></div>'

W = [50, 60, 70, 80, 90, 100]
BW = [round(4.8 * 3.5 * k / 200 * 10) for k in W]   # brisk walk 10 min, MET 4.8 (Compendium 2024, 3.5-3.9 mph)
ST = [100, 120, 140, 160, 180, 210]                  # stepper 10 min (rujukan pengguna, Task 7)
rows = ''.join(f'''<div class="crow" id="cr{i}"><span class="kg">{k}KG</span>
          <span class="c"><span class="bar"><i id="bb{i}" style="width:{b/210*100:.1f}%;background:#9aa"></i></span><span class="v" style="color:#ddd">{b}</span></span>
          <span class="c"><span class="bar"><i id="sb{i}" style="width:{s/210*100:.1f}%;background:linear-gradient(90deg,var(--lime),var(--yellow))"></i></span><span class="v" style="color:var(--lime)">{s}</span></span></div>'''
               for i, (k, b, s) in enumerate(zip(W, BW, ST)))

T = dict(e1=3.5, e2=10.0, e3=18.0, ctr=25.0, kg=28.5, cal=32.5, card=35.5, end=39.5)
ctr = timed(block(t16, 'ctr'), T['ctr'] + 0.05, T['kg'] - T['ctr'] - 0.05)
wt = timed(block(t16, 'wt'), T['kg'] + 0.05, T['cal'] - T['kg'] - 0.05)
ring = timed(block(t16, 'u1ring'), T['kg'] + 0.6, T['cal'] - T['kg'] - 0.6)
c1 = timed(block(t16, 'c1'), T['cal'] + 0.05, T['card'] - T['cal'] - 0.05)
cta = timed(block(t16, 'cta'), T['card'] + 0.05, T['end'] - T['card'] - 0.05)

html = f'''      <!-- HOOK: headline 100px, sub-headline 47px -->
      <div id="hook" class="g clip" data-start="0" data-duration="3.5" data-track-index="10" style="top:400px">
        <span class="big" id="h1" style="font-size:100px;color:#fff">BRISKWALK</span>
        <div class="vsb" id="hvs" style="margin:14px auto">VS</div>
        <span class="big" id="h1b" style="font-size:100px;color:var(--lime)">STEPPER</span>
        <span class="blk pink" id="h2" style="font-size:47px;margin-top:22px">MANA LAGI BERKESAN?</span>
      </div>

      <!-- EDU 1: jenis pergerakan -->
      <div id="e1t" class="g clip" data-start="{T['e1']+0.05:.2f}" data-duration="{T['e2']-T['e1']-0.05:.2f}" data-track-index="10" style="top:200px">
        <span class="blk" id="e1h" style="font-size:47px">① JENIS PERGERAKAN</span>
      </div>
      <div id="e1" class="g clip panel" data-start="{T['e1']+0.2:.2f}" data-duration="{T['e2']-T['e1']-0.2:.2f}" data-track-index="11" style="top:310px">
        <div class="cols">
          <div class="col2" id="e1l"><h3 style="color:#fff">BRISKWALK</h3>{WALKER}
            <div class="pl"><span class="pill" id="bl1">{CHECK("#fff","#000")}JALAN KE DEPAN</span><span class="pill" id="bl2" style="background:#ffd5d0">{CROSS}IMPAK PADA TUMIT</span><span class="pill" id="bl3">{CHECK("#fff","#000")}PERLU LALUAN</span></div></div>
          <div class="vsb" id="e1vs">VS</div>
          <div class="col2" id="e1r"><h3 style="color:var(--lime)">STEPPER</h3>{STEPI}
            <div class="pl"><span class="pill lime" id="sl1">{CHECK("#000","#c6ff00")}NAIK-TURUN</span><span class="pill lime" id="sl2">{CHECK("#000","#c6ff00")}LOW IMPACT</span><span class="pill lime" id="sl3">{CHECK("#000","#c6ff00")}DI TEMPAT SENDIRI</span></div></div>
        </div>
      </div>

      <!-- EDU 2: kalori 10 minit -->
      <div id="e2t" class="g clip" data-start="{T['e2']+0.05:.2f}" data-duration="{T['e3']-T['e2']-0.05:.2f}" data-track-index="10" style="top:200px">
        <span class="blk" id="e2h" style="font-size:47px">② KALORI DALAM 10 MINIT</span>
      </div>
      <div id="e2" class="g clip panel" data-start="{T['e2']+0.2:.2f}" data-duration="{T['e3']-T['e2']-0.2:.2f}" data-track-index="11" style="top:310px">
        <div class="thead"><span>BERAT</span><span>BRISKWALK</span><span style="color:var(--lime)">STEPPER</span></div>
        {rows}
        <div class="note" id="e2n">*Anggaran. Briskwalk: MET 4.8 (Compendium 2024). Stepper: jadual rujukan.</div>
      </div>
      <div id="e2c" class="g clip" data-start="{T['e2']+6.0:.2f}" data-duration="{T['e3']-T['e2']-6.0:.2f}" data-track-index="12" style="top:1290px">
        <span class="blk pink" id="e2x" style="font-size:66px">STEPPER ±2.4X LEBIH BANYAK!</span>
      </div>

      <!-- EDU 3: otot -->
      <div id="e3t" class="g clip" data-start="{T['e3']+0.05:.2f}" data-duration="{T['ctr']-T['e3']-0.05:.2f}" data-track-index="10" style="top:200px">
        <span class="blk" id="e3h" style="font-size:47px">③ OTOT YANG DILATIH</span>
      </div>
      <div id="e3" class="g clip panel" data-start="{T['e3']+0.2:.2f}" data-duration="{T['ctr']-T['e3']-0.2:.2f}" data-track-index="11" style="top:310px">
        <div class="cols">
          <div class="col2"><h3 style="color:#fff">BRISKWALK</h3>
            <div class="figs4">{fig(True, ['quads'], '#ffd400', 'b1')}{fig(False, ['calves'], '#ffd400', 'b2')}</div>
            <div class="pl" style="margin-top:12px"><span class="pill yellow" id="bm1">{CHECK("#000","#ffd400")}PEHA DEPAN</span><span class="pill yellow" id="bm2">{CHECK("#000","#ffd400")}BETIS</span></div></div>
          <div class="col2"><h3 style="color:var(--lime)">STEPPER</h3>
            <div class="figs4">{fig(True, ['shoulders', 'arms', 'core', 'quads'], '#c6ff00', 's1')}{fig(False, ['arms', 'glutes', 'hams', 'calves'], '#c6ff00', 's2')}</div>
            <div class="pl" style="margin-top:12px"><span class="pill lime" id="sm1">{CHECK("#000","#c6ff00")}PUNGGUNG &amp; PEHA</span><span class="pill lime" id="sm2">{CHECK("#000","#c6ff00")}BETIS &amp; CORE</span><span class="pill lime" id="sm3">{CHECK("#000","#c6ff00")}LENGAN*</span></div></div>
        </div>
        <div class="note" id="e3n">*Lengan &amp; bahu bila guna tali resistance. Sumber: Women's Health, Peloton, Well+Good.</div>
      </div>

      <!-- USP -->
      {ctr}
      {wt}
      {ring}

      <!-- CTA -->
      {c1}
      {cta}
'''
e1, e2, e3, c, kg, ca, cd = (T[x] for x in ['e1', 'e2', 'e3', 'ctr', 'kg', 'cal', 'card'])
rjs = '\n'.join(f'''      tl.fromTo("#cr{i}", {{ x: -900, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {e2+0.6+i*0.8:.2f});
      tl.fromTo(["#bb{i}", "#sb{i}"], {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.5, ease: "power2.out", stagger: 0.15 }}, {e2+0.75+i*0.8:.2f});''' for i in range(6))
js = f'''      // hook
      tl.fromTo("#h1", {{ x: -1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, 0.05);
      tl.fromTo("#h1b", {{ x: 1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, 0.35);
      tl.fromTo("#hvs", {{ scale: 0, rotation: -180 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2.5)" }}, 0.65);
      tl.to("#root", {{ keyframes: {{ x: [0, -14, 12, -8, 6, 0] }}, duration: 0.25 }}, 0.75);
      tl.to("#hvs", {{ scale: 1.15, duration: 0.2, yoyo: true, repeat: 5, ease: "sine.inOut" }}, 1.2);
      tl.fromTo("#h2", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 1.2);

      // edu 1
      tl.fromTo("#e1h", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, {e1+0.05:.2f});
      tl.fromTo("#e1", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {e1+0.2:.2f});
      tl.fromTo("#e1vs", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, {e1+0.5:.2f});
      tl.to(["#wlegA"], {{ rotation: 18, transformOrigin: "108px 124px", duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e1+0.6:.2f});
      tl.to(["#wlegB"], {{ rotation: -18, transformOrigin: "108px 124px", duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e1+0.6:.2f});
      tl.fromTo("#warr", {{ x: -30 }}, {{ x: 10, duration: 0.6, yoyo: true, repeat: 4, ease: "sine.inOut" }}, {e1+0.6:.2f});
      tl.to("#pedL", {{ y: 24, duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e1+0.6:.2f});
      tl.fromTo("#pedR", {{ y: 24 }}, {{ y: 0, duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e1+0.6:.2f});
      tl.fromTo(["#bl1", "#sl1", "#bl2", "#sl2", "#bl3", "#sl3"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.55 }}, {e1+1.4:.2f});

      // edu 2
      tl.fromTo("#e2h", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, {e2+0.05:.2f});
      tl.fromTo("#e2", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {e2+0.2:.2f});
{rjs}
      tl.fromTo("#e2n", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {e2+5.6:.2f});
      tl.fromTo("#e2x", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, {e2+6.0:.2f});
      tl.to("#root", {{ keyframes: {{ x: [0, 12, -10, 6, 0] }}, duration: 0.22 }}, {e2+6.1:.2f});

      // edu 3
      tl.fromTo("#e3h", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, {e3+0.05:.2f});
      tl.fromTo("#e3", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {e3+0.2:.2f});
      tl.fromTo(["#b1 > *", "#b2 > *"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.12 }}, {e3+0.8:.2f});
      tl.fromTo(["#s1 > *", "#s2 > *"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.1 }}, {e3+1.6:.2f});
      tl.to(["#b1", "#b2", "#s1", "#s2"], {{ opacity: 0.55, duration: 0.3, yoyo: true, repeat: 7, ease: "sine.inOut" }}, {e3+3.0:.2f});
      tl.fromTo(["#bm1", "#bm2"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.3 }}, {e3+1.2:.2f});
      tl.fromTo(["#sm1", "#sm2", "#sm3"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.4 }}, {e3+2.6:.2f});
      tl.fromTo("#e3n", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {e3+4.2:.2f});

      // USP counter
      tl.fromTo("#cc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {c+0.1:.2f});
      tl.fromTo("#cb", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {c+0.35:.2f});
      tl.fromTo(["#cp1","#cp2","#cp3"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.4 }}, {c+1.3:.2f});
      // USP 6kg
      tl.fromTo("#wc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {kg+0.1:.2f});
      tl.fromTo("#wa", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {kg+0.25:.2f});
      tl.fromTo("#ring6", {{ scale: 2.5, opacity: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {kg+0.6:.2f});
      tl.to("#ring6", {{ scale: 1.08, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 50%" }}, {kg+1.0:.2f});
      tl.fromTo("#kgtag", {{ scale: 0, rotation: 20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.5)" }}, {kg+0.8:.2f});

      // CTA
      tl.fromTo("#cal", {{ y: -500, rotation: -8 }}, {{ y: 0, rotation: 0, duration: 0.4, ease: "back.out(1.6)" }}, {ca+0.05:.2f});
      tl.fromTo("#calold", {{ rotationX: 0 }}, {{ rotationX: -100, opacity: 0, duration: 0.45, ease: "power2.in" }}, {ca+0.5:.2f});
      tl.fromTo("#c1a", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {ca+1.0:.2f});
      tl.fromTo("#c1b", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, {ca+1.3:.2f});
      tl.to("#root", {{ keyframes: {{ y: [0, 12, -10, 6, 0] }}, duration: 0.22 }}, {ca+1.4:.2f});
      tl.fromTo("#ctacard", {{ scale: 0, rotation: -8 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }}, {cd+0.1:.2f});
      tl.to("#ctacard", {{ scale: 1.06, duration: 0.25, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {cd+0.7:.2f});
'''
body = f'''    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{{{{TOTAL}}}}" data-width="1080" data-height="1920">
      {{{{VIDEOS}}}}
      {{{{SFX}}}}
      <div id="vignette" class="layer"></div>

{html}
      <div id="flash" class="layer"></div>
      <div id="progress"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      /*{{{{VIDJS}}}}*/
      tl.fromTo("#progress", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {{{{TOTAL}}}}, ease: "none" }}, 0);

{js}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
t = head + body
t = re.sub(r'(font-size: ?)(\d+)px', lambda m: f'{m.group(1)}{min(int(m.group(2)), 100)}px', t)
assert not [x for x in re.findall(r'font-size: ?(\d+)px', t) if int(x) > 100]
b = t[t.index('<body>'):]
o, cc = len(re.findall(r'<div\b', b)), b.count('</div>')
print('div open', o, 'close', cc); assert o == cc
ids = re.findall(r'\bid="([^"]+)"', b); dup = {i for i in ids if ids.count(i) > 1}; assert not dup, dup
for need in ['id="ctr"', 'id="wt"', 'id="ring6"', 'id="cal"', 'id="ctacard"', 'NAK UPGRADE BODY?', 'START STEPPER']:
    assert need in t, need
open(S + '/template17.html', 'w').write(t)
print('BW', BW)

src = open(S + '/build9.py').read()
src = src.replace('TOTAL = 38.0', f'TOTAL = {T["end"]}')
src, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f6", 6.0),     # HOOK: trek luar, berjalan (muted: muzik)
    (3.5, 10.0, "f13", 2.0),   # EDU1 jenis pergerakan: close-up langkah stepper
    (10.0, 18.0, "f12", 1.0),  # EDU2 kalori: bilik, tali
    (18.0, 25.0, "f9", 1.0),   # EDU3 otot: tali resistance
    (25.0, 28.5, "f5", 54.0),  # USP counter: counter dipegang (muted: ada muzik)
    (28.5, 32.5, "f16", 2.9),  # USP <6kg: timbang 5.9kg
    (32.5, 35.5, "f14", 3.0),  # CTA 2027 upgrade body
    (35.5, TOTAL, "f1", 6.0),  # CTA start stepper sekarang
]
MUTED = {"f5", "f6"}''', src, flags=re.S); assert n == 1
sfx = ['(0.05, "whoosh", 0.35)', '(0.35, "swoosh", 0.35)', '(0.65, "impact", 0.55)', '(1.20, "pop", 0.4)']
for s0 in (e1, e2, e3):
    sfx += [f'({s0:.2f}, "whoosh", 0.35)', f'({s0+0.05:.2f}, "pop", 0.4)', f'({s0+0.2:.2f}, "swoosh", 0.3)']
sfx += [f'({e1+0.5:.2f}, "impact", 0.35)'] + [f'({e1+1.4+j*0.55:.2f}, "pop", 0.3)' for j in range(6)]
sfx += [f'({e2+0.6+j*0.8:.2f}, "pop", 0.3)' for j in range(6)] + [f'({e2+6.0:.2f}, "impact", 0.45)', f'({e2+6.1:.2f}, "ding", 0.3)']
sfx += [f'({e3+0.8:.2f}, "riser", 0.25)', f'({e3+1.2:.2f}, "pop", 0.3)', f'({e3+1.5:.2f}, "pop", 0.3)'] + [f'({e3+2.6+j*0.4:.2f}, "pop", 0.3)' for j in range(3)]
sfx += [f'({c:.2f}, "whoosh", 0.35)', f'({c+0.35:.2f}, "ding", 0.3)', f'({c+1.3:.2f}, "pop", 0.35)', f'({c+1.7:.2f}, "pop", 0.35)', f'({c+2.1:.2f}, "pop", 0.35)',
        f'({kg:.2f}, "whoosh", 0.35)', f'({kg+0.25:.2f}, "pop", 0.4)', f'({kg+0.8:.2f}, "ding", 0.3)',
        f'({ca:.2f}, "whoosh", 0.35)', f'({ca+0.5:.2f}, "swoosh", 0.35)', f'({ca+1.3:.2f}, "impact", 0.45)',
        f'({cd:.2f}, "whoosh", 0.35)', f'({cd+0.1:.2f}, "pop", 0.4)', f'({cd+0.7:.2f}, "ding", 0.3)']
src, n = re.subn(r'SFX = \[\n.*?\n\]', 'SFX = [\n    ' + ', '.join(sfx) + ',\n]', src, flags=re.S); assert n == 1
open(S + '/build17.py', 'w').write(src)
print('ok')
