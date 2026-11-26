"""Task 19: Stepper VS Briskwalk (15 minit) + otot & koordinasi + ruang & peralatan + tips kasut,
USP digital counter & tak berat, CTA Raya 2027. Reuses helpers/CSS/icons from gen17."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
g17 = open(S + '/gen17.py').read()
exec(g17[:g17.index('W = [50, 60, 70, 80, 90, 100]')])          # block, timed, head, CHECK, CROSS, WALKER, STEPI, fig, t16
SHOE = re.search(r"SHOE = '''(.*?)'''", open(S + '/gen9.py').read(), re.S).group(1)

head += '''      .tipbadge { display: inline-block; font-family: var(--font-ui); font-weight: 900; font-size: 34px; letter-spacing: 0.14em; color: #000; background: var(--yellow);
                  padding: 8px 26px; border-radius: 999px; border: 5px solid #000; box-shadow: 0 8px 0 #000; }
      #shoe { width: 520px; height: 280px; }
'''
W = [50, 60, 70, 80, 90, 100]
ST = [150, 180, 210, 240, 270, 315]                                  # stepper 15 min = rujukan 10 min x 1.5
BW = [round(4.8 * 3.5 * k / 200 * 15) for k in W]                  # briskwalk 15 min, MET 4.8 (Compendium 2024)
MX = 315
rows = ''.join(f'''<div class="crow" id="cr{i}"><span class="kg">{k}KG</span>
          <span class="c"><span class="bar"><i id="sb{i}" style="width:{s/MX*100:.1f}%;background:linear-gradient(90deg,var(--lime),var(--yellow))"></i></span><span class="v" style="color:var(--lime)">{s}</span></span>
          <span class="c"><span class="bar"><i id="bb{i}" style="width:{b/MX*100:.1f}%;background:#9aa"></i></span><span class="v" style="color:#ddd">{b}</span></span></div>'''
               for i, (k, s, b) in enumerate(zip(W, ST, BW)))
ratio = sum(ST) / sum(BW)

T = dict(e1=3.5, e2=11.5, e3=18.5, tip=24.5, ctr=29.5, kg=33.0, cal=37.0, card=40.0, end=44.0)
ctr = timed(block(t16, 'ctr'), T['ctr'] + 0.05, T['kg'] - T['ctr'] - 0.05).replace('MULTIFUNCTION<br>COUNTER', 'DIGITAL<br>COUNTER')
wt = timed(block(t16, 'wt'), T['kg'] + 0.05, T['cal'] - T['kg'] - 0.05) \
    .replace('<div class="cara" id="wc">RINGAN</div>', '<div class="cara" id="wc">TAK BERAT</div>') \
    .replace('BERAT TAK SAMPAI 6KG', 'RINGAN, MUDAH ALIH')
ring = timed(block(t16, 'u1ring'), T['kg'] + 0.6, T['cal'] - T['kg'] - 0.6)
c1 = timed(block(t16, 'c1'), T['cal'] + 0.05, T['card'] - T['cal'] - 0.05) \
    .replace('>TAHUN 2027</span>', '>RAYA 2027</span>').replace('>NAK UPGRADE BODY?</span>', '>NAK BADAN FIT?</span>')
cta = timed(block(t16, 'cta'), T['card'] + 0.05, T['end'] - T['card'] - 0.05)
assert 'DIGITAL<br>COUNTER' in ctr and 'TAK BERAT' in wt and 'RAYA 2027' in c1 and 'NAK BADAN FIT?' in c1 and 'START STEPPER' in cta

WALKER2 = WALKER.replace('id="walker"', 'id="walker2"').replace('id="wlegA"', 'id="wlegA2"').replace('id="wlegB"', 'id="wlegB2"').replace('id="warr"', 'id="warr2"')
STEPI2 = STEPI.replace('id="stepi"', 'id="stepi2"').replace('id="pedL"', 'id="pedL2"').replace('id="pedR"', 'id="pedR2"')

html = f'''      <!-- HOOK: headline 100px, sub-headline 47px -->
      <div id="hook" class="g clip" data-start="0" data-duration="3.5" data-track-index="10" style="top:400px">
        <span class="big" id="h1" style="font-size:100px;color:var(--lime)">STEPPER</span>
        <div class="vsb" id="hvs" style="margin:14px auto">VS</div>
        <span class="big" id="h1b" style="font-size:100px;color:#fff">BRISKWALK</span>
        <span class="blk pink" id="h2" style="font-size:47px;margin-top:22px">MANA LAGI BERKESAN?</span>
      </div>

      <!-- EDU 1: kalori 15 minit -->
      <div id="e1t" class="g clip" data-start="{T['e1']+0.05:.2f}" data-duration="{T['e2']-T['e1']-0.05:.2f}" data-track-index="10" style="top:200px">
        <span class="blk" id="e1h" style="font-size:47px">① KALORI DALAM 15 MINIT</span>
      </div>
      <div id="e1" class="g clip panel" data-start="{T['e1']+0.2:.2f}" data-duration="{T['e2']-T['e1']-0.2:.2f}" data-track-index="11" style="top:310px">
        <div class="thead"><span>BERAT</span><span style="color:var(--lime)">STEPPER</span><span>BRISKWALK</span></div>
        {rows}
        <div class="note" id="e1n">*Anggaran. Stepper: jadual rujukan ×1.5. Briskwalk: MET 4.8 (Compendium 2024).</div>
      </div>
      <div id="e1c" class="g clip" data-start="{T['e1']+6.0:.2f}" data-duration="{T['e2']-T['e1']-6.0:.2f}" data-track-index="12" style="top:1290px">
        <span class="blk pink" id="e1x" style="font-size:66px">STEPPER ±{ratio:.1f}X LEBIH BANYAK!</span>
      </div>

      <!-- EDU 2: otot & koordinasi -->
      <div id="e2t" class="g clip" data-start="{T['e2']+0.05:.2f}" data-duration="{T['e3']-T['e2']-0.05:.2f}" data-track-index="10" style="top:200px">
        <span class="blk" id="e2h" style="font-size:47px">② OTOT &amp; KOORDINASI</span>
      </div>
      <div id="e2" class="g clip panel" data-start="{T['e2']+0.2:.2f}" data-duration="{T['e3']-T['e2']-0.2:.2f}" data-track-index="11" style="top:310px">
        <div class="cols">
          <div class="col2"><h3 style="color:var(--lime)">STEPPER</h3>
            <div class="figs4">{fig(True, ['shoulders', 'arms', 'core', 'quads'], '#c6ff00', 's1')}{fig(False, ['arms', 'glutes', 'hams', 'calves'], '#c6ff00', 's2')}</div>
            <div class="pl" style="margin-top:12px"><span class="pill lime" id="sm1">{CHECK("#000","#c6ff00")}PUNGGUNG, PEHA, BETIS</span><span class="pill lime" id="sm2">{CHECK("#000","#c6ff00")}CORE &amp; LENGAN*</span><span class="pill pink" id="sm3">{CHECK("#c6ff00","#000")}KOORDINASI TANGAN–KAKI*</span><span class="pill pink" id="sm4">{CHECK("#c6ff00","#000")}IMBANGAN BADAN</span></div></div>
          <div class="col2"><h3 style="color:#fff">BRISKWALK</h3>
            <div class="figs4">{fig(True, ['quads'], '#ffd400', 'b1')}{fig(False, ['calves'], '#ffd400', 'b2')}</div>
            <div class="pl" style="margin-top:12px"><span class="pill yellow" id="bm1">{CHECK("#000","#ffd400")}PEHA DEPAN &amp; BETIS</span><span class="pill" id="bm2">{CHECK("#fff","#000")}AYUNAN TANGAN BIASA</span></div></div>
        </div>
        <div class="note" id="e2n">*Bila guna tali resistance. Sumber: Women's Health, Peloton, Well+Good.</div>
      </div>

      <!-- EDU 3: ruang & peralatan -->
      <div id="e3t" class="g clip" data-start="{T['e3']+0.05:.2f}" data-duration="{T['tip']-T['e3']-0.05:.2f}" data-track-index="10" style="top:200px">
        <span class="blk" id="e3h" style="font-size:47px">③ RUANG &amp; PERALATAN</span>
      </div>
      <div id="e3" class="g clip panel" data-start="{T['e3']+0.2:.2f}" data-duration="{T['tip']-T['e3']-0.2:.2f}" data-track-index="11" style="top:310px">
        <div class="cols">
          <div class="col2"><h3 style="color:var(--lime)">STEPPER</h3>{STEPI2}
            <div class="pl"><span class="pill lime" id="sr1">{CHECK("#000","#c6ff00")}MUAT DALAM BILIK</span><span class="pill lime" id="sr2">{CHECK("#000","#c6ff00")}TAK KIRA CUACA</span><span class="pill lime" id="sr3">{CHECK("#000","#c6ff00")}STEPPER + KASUT</span></div></div>
          <div class="vsb" id="e3vs">VS</div>
          <div class="col2"><h3 style="color:#fff">BRISKWALK</h3>{WALKER2}
            <div class="pl"><span class="pill" id="br1">{CHECK("#fff","#000")}PERLU LALUAN / TREK</span><span class="pill" id="br2" style="background:#ffd5d0">{CROSS}IKUT CUACA</span><span class="pill" id="br3">{CHECK("#fff","#000")}KASUT SUKAN</span></div></div>
        </div>
      </div>

      <!-- TIPS -->
      <div id="tip" class="g clip" data-start="{T['tip']+0.05:.2f}" data-duration="{T['ctr']-T['tip']-0.05:.2f}" data-track-index="10" style="top:240px">
        <span class="tipbadge" id="tb">TIPS</span>
        <span class="blk" id="tt" style="font-size:66px;margin-top:22px">PAKAI KASUT BILA GUNA STEPPER</span>
        {SHOE}
        <span class="mid" id="ta" style="margin-top:16px;font-size:56px">ELAK IMPAK BERTERUSAN</span>
        <span class="blk pink" id="tb2" style="font-size:66px">PADA TAPAK KAKI</span>
      </div>

      <!-- USP -->
      {ctr}
      {wt}
      {ring}

      <!-- CTA -->
      {c1}
      {cta}
'''
e1, e2, e3, tp, c, kg, ca, cd = (T[x] for x in ['e1', 'e2', 'e3', 'tip', 'ctr', 'kg', 'cal', 'card'])
rjs = '\n'.join(f'''      tl.fromTo("#cr{i}", {{ x: -900, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {e1+0.6+i*0.8:.2f});
      tl.fromTo(["#sb{i}", "#bb{i}"], {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.5, ease: "power2.out", stagger: 0.15 }}, {e1+0.75+i*0.8:.2f});''' for i in range(6))
js = f'''      // hook
      tl.fromTo("#h1", {{ x: -1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, 0.05);
      tl.fromTo("#h1b", {{ x: 1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, 0.35);
      tl.fromTo("#hvs", {{ scale: 0, rotation: -180 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2.5)" }}, 0.65);
      tl.to("#root", {{ keyframes: {{ x: [0, -14, 12, -8, 6, 0] }}, duration: 0.25 }}, 0.75);
      tl.to("#hvs", {{ scale: 1.15, duration: 0.2, yoyo: true, repeat: 5, ease: "sine.inOut" }}, 1.2);
      tl.fromTo("#h2", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 1.2);

      // edu 1 kalori
      tl.fromTo("#e1h", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, {e1+0.05:.2f});
      tl.fromTo("#e1", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {e1+0.2:.2f});
{rjs}
      tl.fromTo("#e1n", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {e1+5.6:.2f});
      tl.fromTo("#e1x", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, {e1+6.0:.2f});
      tl.to("#root", {{ keyframes: {{ x: [0, 12, -10, 6, 0] }}, duration: 0.22 }}, {e1+6.1:.2f});

      // edu 2 otot & koordinasi
      tl.fromTo("#e2h", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, {e2+0.05:.2f});
      tl.fromTo("#e2", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {e2+0.2:.2f});
      tl.fromTo(["#s1 > *", "#s2 > *"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.1 }}, {e2+0.8:.2f});
      tl.fromTo(["#b1 > *", "#b2 > *"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.12 }}, {e2+1.6:.2f});
      tl.to(["#b1", "#b2", "#s1", "#s2"], {{ opacity: 0.55, duration: 0.3, yoyo: true, repeat: 7, ease: "sine.inOut" }}, {e2+3.4:.2f});
      tl.fromTo(["#sm1", "#sm2"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.4 }}, {e2+1.4:.2f});
      tl.fromTo(["#bm1", "#bm2"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.4 }}, {e2+2.4:.2f});
      tl.fromTo(["#sm3", "#sm4"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.5 }}, {e2+3.4:.2f});
      tl.fromTo("#e2n", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {e2+4.6:.2f});

      // edu 3 ruang & peralatan
      tl.fromTo("#e3h", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, {e3+0.05:.2f});
      tl.fromTo("#e3", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {e3+0.2:.2f});
      tl.fromTo("#e3vs", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, {e3+0.5:.2f});
      tl.to("#pedL2", {{ y: 24, duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e3+0.6:.2f});
      tl.fromTo("#pedR2", {{ y: 24 }}, {{ y: 0, duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e3+0.6:.2f});
      tl.to("#wlegA2", {{ rotation: 18, transformOrigin: "108px 124px", duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e3+0.6:.2f});
      tl.to("#wlegB2", {{ rotation: -18, transformOrigin: "108px 124px", duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }}, {e3+0.6:.2f});
      tl.fromTo("#warr2", {{ x: -30 }}, {{ x: 10, duration: 0.6, yoyo: true, repeat: 4, ease: "sine.inOut" }}, {e3+0.6:.2f});
      tl.fromTo(["#sr1", "#br1", "#sr2", "#br2", "#sr3", "#br3"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.55 }}, {e3+1.2:.2f});

      // tips
      tl.fromTo("#tb", {{ scale: 0, rotation: -15 }}, {{ scale: 1, rotation: 0, duration: 0.3, ease: "back.out(2.5)" }}, {tp+0.05:.2f});
      tl.fromTo("#tt", {{ x: 1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, {tp+0.3:.2f});
      tl.fromTo("#shoe", {{ y: -400, rotation: -10 }}, {{ y: 0, rotation: 0, duration: 0.45, ease: "bounce.out" }}, {tp+0.7:.2f});
      tl.fromTo("#ripples path", {{ scale: 0.4, opacity: 0, transformOrigin: "50% 50%" }}, {{ scale: 1.2, opacity: 1, duration: 0.5, stagger: 0.12, repeat: 4, ease: "power1.out" }}, {tp+1.15:.2f});
      tl.fromTo("#heel", {{ opacity: 0.3 }}, {{ opacity: 1, duration: 0.25, yoyo: true, repeat: 7 }}, {tp+1.15:.2f});
      tl.fromTo("#ta", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {tp+1.8:.2f});
      tl.fromTo("#tb2", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, {tp+2.3:.2f});

      // USP digital counter
      tl.fromTo("#cc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {c+0.1:.2f});
      tl.fromTo("#cb", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {c+0.35:.2f});
      tl.fromTo(["#cp1","#cp2","#cp3"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.4 }}, {c+1.3:.2f});
      // USP tak berat
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
open(S + '/template19.html', 'w').write(t)
print('ST', ST, 'BW', BW, 'ratio', round(ratio, 2))

src = open(S + '/build9.py').read()
src = src.replace('TOTAL = 38.0', f'TOTAL = {T["end"]}')
src, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f8", 3.0),     # HOOK: trek luar, topi
    (3.5, 11.5, "f19", 1.0),   # EDU1 kalori 15 minit: dumbbell depan TV
    (11.5, 18.5, "f7", 3.0),   # EDU2 otot & koordinasi: luar, tali resistance
    (18.5, 24.5, "f3", 2.0),   # EDU3 ruang & peralatan: dalam bilik, kettlebell
    (24.5, 29.5, "f13", 1.0),  # TIPS kasut: close-up kasut atas stepper
    (29.5, 33.0, "f5", 50.9),  # USP digital counter: pasang bateri (muted: ada muzik)
    (33.0, 37.0, "f16", 2.9),  # USP tak berat: timbang 5.9kg
    (37.0, 40.0, "f15", 2.0),  # CTA raya 2027
    (40.0, TOTAL, "f18", 4.0), # CTA start stepper sekarang
]
MUTED = {"f5"}''', src, flags=re.S); assert n == 1
sfx = ['(0.05, "whoosh", 0.35)', '(0.35, "swoosh", 0.35)', '(0.65, "impact", 0.55)', '(1.20, "pop", 0.4)']
for s0 in (e1, e2, e3, tp):
    sfx += [f'({s0:.2f}, "whoosh", 0.35)', f'({s0+0.05:.2f}, "pop", 0.4)']
sfx += [f'({e1+0.6+j*0.8:.2f}, "pop", 0.3)' for j in range(6)] + [f'({e1+6.0:.2f}, "impact", 0.45)', f'({e1+6.1:.2f}, "ding", 0.3)']
sfx += [f'({e2+0.8:.2f}, "riser", 0.25)', f'({e2+1.4:.2f}, "pop", 0.3)', f'({e2+1.8:.2f}, "pop", 0.3)', f'({e2+2.4:.2f}, "pop", 0.3)', f'({e2+2.8:.2f}, "pop", 0.3)', f'({e2+3.4:.2f}, "ding", 0.25)']
sfx += [f'({e3+0.5:.2f}, "impact", 0.35)'] + [f'({e3+1.2+j*0.55:.2f}, "pop", 0.3)' for j in range(6)]
sfx += [f'({tp+0.7:.2f}, "swoosh", 0.3)', f'({tp+1.15:.2f}, "impact", 0.35)', f'({tp+2.3:.2f}, "pop", 0.4)']
sfx += [f'({c:.2f}, "whoosh", 0.35)', f'({c+0.35:.2f}, "ding", 0.3)', f'({c+1.3:.2f}, "pop", 0.35)', f'({c+1.7:.2f}, "pop", 0.35)', f'({c+2.1:.2f}, "pop", 0.35)',
        f'({kg:.2f}, "whoosh", 0.35)', f'({kg+0.25:.2f}, "pop", 0.4)', f'({kg+0.8:.2f}, "ding", 0.3)',
        f'({ca:.2f}, "whoosh", 0.35)', f'({ca+0.5:.2f}, "swoosh", 0.35)', f'({ca+1.3:.2f}, "impact", 0.45)',
        f'({cd:.2f}, "whoosh", 0.35)', f'({cd+0.1:.2f}, "pop", 0.4)', f'({cd+0.7:.2f}, "ding", 0.3)']
src, n = re.subn(r'SFX = \[\n.*?\n\]', 'SFX = [\n    ' + ', '.join(sfx) + ',\n]', src, flags=re.S); assert n == 1
open(S + '/build19.py', 'w').write(src)
print('ok')
