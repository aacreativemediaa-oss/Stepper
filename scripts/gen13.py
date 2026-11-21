"""Task 13: Level 1-4 senaman stepper (8s each), hook 'LEVEL MANA KORANG?', CTA repost."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t3 = open(S + '/template3.html').read()
head = t3[:t3.index('    </style>')]
head += '''
      .lvtop { left: 0; right: 0; top: 190px; text-align: center; }
      .lvl { display: inline-block; font-size: 150px; line-height: 0.95; -webkit-text-stroke: 9px #000; paint-order: stroke fill; text-shadow: 0 12px 0 #000; }
      .meter { display: flex; justify-content: center; gap: 14px; margin-top: 14px; }
      .meter i { width: 120px; height: 34px; border-radius: 10px; border: 5px solid #000; background: rgba(0,0,0,0.55); box-shadow: 0 6px 0 #000; transform-origin: 0 50%; }
      .lvrow { display: flex; justify-content: center; gap: 16px; margin-top: 22px; flex-wrap: wrap; padding: 0 40px; }
      .lvbot { left: 0; right: 0; top: 1180px; text-align: center; }
      .ben { display: inline-block; font-size: 72px; line-height: 1; padding: 10px 30px 4px; color: #000; background: #fff; border: 6px solid #000; border-radius: 20px; box-shadow: 0 12px 0 #000; transform: rotate(-2deg); }
      .slabel { margin-top: 30px; font-family: var(--font-ui); font-weight: 900; font-size: 32px; letter-spacing: 0.14em; color: #fff; text-shadow: 0 3px 0 #000, 0 0 12px rgba(0,0,0,0.8); }
      .spills { display: flex; flex-direction: column; align-items: center; gap: 16px; margin-top: 14px; }
      .spills .pill { font-size: 40px; }
      #hmeter { display: flex; justify-content: center; gap: 16px; margin-top: 30px; }
      #hmeter i { width: 150px; height: 44px; border-radius: 12px; border: 6px solid #000; box-shadow: 0 8px 0 #000; transform-origin: 0 50%; }
      #rp { width: 230px; height: 230px; display: block; margin: 0 auto 18px; }
'''
CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SHOE = '<svg viewBox="0 0 64 64"><path d="M6 44 H56 Q62 44 60 38 L56 34 H8 Q4 38 6 44 Z" fill="#fff" stroke="#000" stroke-width="4"/><path d="M8 34 Q8 20 20 16 L34 12 Q40 22 50 24 L56 26 Q60 30 56 34 Z" fill="#c6ff00" stroke="#000" stroke-width="4" stroke-linejoin="round"/></svg>'
BAND = '<svg viewBox="0 0 64 64"><path d="M14 10 Q32 40 50 10" fill="none" stroke="#000" stroke-width="5"/><rect x="6" y="4" width="16" height="12" rx="4" fill="#ff2e7e" stroke="#000" stroke-width="4"/><rect x="42" y="4" width="16" height="12" rx="4" fill="#ff2e7e" stroke="#000" stroke-width="4"/><path d="M32 38 V60" stroke="#000" stroke-width="5"/></svg>'
DB = '<svg viewBox="0 0 64 64"><rect x="18" y="28" width="28" height="8" fill="#888" stroke="#000" stroke-width="3"/><rect x="4" y="16" width="16" height="32" rx="6" fill="#ff2e7e" stroke="#000" stroke-width="4"/><rect x="44" y="16" width="16" height="32" rx="6" fill="#ff2e7e" stroke="#000" stroke-width="4"/></svg>'
SPEED = '<svg viewBox="0 0 64 64"><path d="M8 48 A26 26 0 0 1 56 48" fill="none" stroke="#000" stroke-width="7"/><path d="M32 48 L{nx} {ny}" stroke="#ff3b30" stroke-width="6" stroke-linecap="round"/><circle cx="32" cy="48" r="6" fill="#000"/></svg>'
FIRE = '<svg viewBox="0 0 64 64"><path d="M32 60 C14 60 8 46 10 36 C12 26 20 20 21 9 C29 14 32 22 31 28 C36 24 38 18 37 13 C48 22 56 33 54 44 C52 53 44 60 32 60 Z" fill="#ff3b30" stroke="#000" stroke-width="4"/></svg>'
COLORS = ['#c6ff00', '#ffd400', '#ff8a00', '#ff2e7e']
LEVELS = [
    dict(pace='PACE PERLAHAN', needle=(14, 32), tool=('KAKI SAHAJA', SHOE), ben='BAKAR KALORI = BRISKWALK',
         lab='SESUAI UNTUK', pills=['PEMULA', 'OVERWEIGHT &amp; OBESE', 'SAKIT LUTUT']),
    dict(pace='PACE SEDERHANA', needle=(32, 24), tool=('KAKI SAHAJA', SHOE), ben='BAKAR KALORI LEBIH BANYAK',
         lab='SESUAI UNTUK', pills=['TAK ADA MASA NAK JOGGING KAT LUAR']),
    dict(pace='PACE LAJU', needle=(50, 32), tool=('+ TALI RESISTANCE', BAND), ben='BAKAR KALORI SANGAT BANYAK',
         lab='SESUAI UNTUK', pills=['TRIM GELEBEH LENGAN &amp; PEHA SERENTAK']),
    dict(pace='PACE LAJU', needle=(50, 32), tool=('+ DUMBBELL', DB), ben='TONING LENGAN, PERUT &amp; PEHA',
         lab='HASILNYA', pills=['BADAN NAMPAK KEMAS &amp; CURVY', '10 MINIT = 150+ KALORI']),
]
T0, LEN = 3.0, 8.0
html, js = [], []
for k, L in enumerate(LEVELS):
    s = T0 + k * LEN; n = k + 1; col = COLORS[k]
    meter = ''.join(f'<i id="m{n}_{j}" style="background:{COLORS[j] if j < n else "rgba(0,0,0,0.55)"}"></i>' for j in range(4))
    sp = SPEED.replace('{nx}', str(L['needle'][0])).replace('{ny}', str(L['needle'][1]))
    pills = ''.join(f'<span class="pill" id="p{n}_{j}" style="background:{col}">{CHECK("#000", col)}{p}</span>' for j, p in enumerate(L['pills']))
    html.append(f'''      <!-- LEVEL {n} -->
      <div id="lt{n}" class="lvtop clip" data-start="{s+0.05:.2f}" data-duration="{LEN-0.05:.2f}" data-track-index="10">
        <span class="lvl" id="lv{n}" style="color:{col}">LEVEL {n}</span>
        <div class="meter">{meter}</div>
        <div class="lvrow"><span class="pill" id="pc{n}">{sp}{L['pace']}</span><span class="pill" id="tl{n}" style="background:{col}">{L['tool'][1]}{L['tool'][0]}</span></div>
      </div>
      <div id="lb{n}" class="lvbot clip" data-start="{s+2.3:.2f}" data-duration="{LEN-2.3:.2f}" data-track-index="10">
        <span class="ben" id="bn{n}"><svg viewBox="0 0 64 64" style="width:58px;height:58px;vertical-align:-6px;margin-right:10px">{FIRE[FIRE.index('<path'):FIRE.rindex('</svg>')]}</svg>{L['ben']}</span>
        <div class="slabel" id="sl{n}">{L['lab']}</div>
        <div class="spills">{pills}</div>
      </div>''')
    js.append(f'''      // level {n}
      tl.fromTo("#lv{n}", {{ scale: 2.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }}, {s+0.05:.2f});
      tl.to("#root", {{ keyframes: {{ x: [0, -12, 10, -6, 0] }}, duration: 0.22 }}, {s+0.3:.2f});
      tl.fromTo(["{'","'.join(f'#m{n}_{j}' for j in range(4))}"], {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.25, ease: "back.out(2)", stagger: 0.12 }}, {s+0.4:.2f});
      tl.to("#m{n}_{n-1}", {{ scale: 1.15, duration: 0.2, yoyo: true, repeat: 3, ease: "sine.inOut" }}, {s+1.0:.2f});
      tl.fromTo("#pc{n}", {{ x: -900 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)" }}, {s+0.9:.2f});
      tl.fromTo("#tl{n}", {{ x: 900 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)" }}, {s+1.4:.2f});
      tl.fromTo("#bn{n}", {{ scale: 0, rotation: 10 }}, {{ scale: 1, rotation: -2, duration: 0.35, ease: "back.out(2.2)" }}, {s+2.35:.2f});
      tl.fromTo("#sl{n}", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {s+3.8:.2f});
      tl.fromTo([{", ".join(f'"#p{n}_{j}"' for j in range(len(L['pills'])))}], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.6 }}, {s+4.1:.2f});''')

TOTAL = T0 + 4 * LEN + 4.5
REPOST = '''<svg id="rp" viewBox="0 0 230 230"><circle cx="115" cy="115" r="108" fill="#c6ff00" stroke="#000" stroke-width="8"/>
  <g id="rpa" style="transform-origin:115px 115px" fill="none" stroke="#000" stroke-width="16" stroke-linecap="round" stroke-linejoin="round">
    <path d="M60 100 Q60 66 96 66 H160"/><path d="M142 46 L162 66 L142 86"/>
    <path d="M170 130 Q170 164 134 164 H70"/><path d="M88 144 L68 164 L88 184"/></g></svg>'''
hmeter = ''.join(f'<i id="hm{j}" style="background:{COLORS[j]}"></i>' for j in range(4))
body = f'''    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{{{{TOTAL}}}}" data-width="1080" data-height="1920">
      {{{{VIDEOS}}}}
      {{{{SFX}}}}
      <div id="vignette" class="layer"></div>

      <!-- HOOK: headline 150px, sub headline 70px -->
      <div id="hook" class="g clip" data-start="0" data-duration="3.0" data-track-index="10" style="top:380px">
        <span class="big" id="h1" style="font-size:150px;color:var(--lime)">LEVEL MANA</span>
        <span class="big" id="h1b" style="font-size:150px;color:var(--lime)">KORANG?</span>
        <span class="blk pink" id="h2" style="font-size:70px">SENAMAN STEPPER</span>
        <div id="hmeter">{hmeter}</div>
      </div>

{chr(10).join(html)}

      <!-- CTA -->
      <div id="cta" class="g clip" data-start="{T0+4*LEN+0.05:.2f}" data-duration="{TOTAL-(T0+4*LEN+0.05):.2f}" data-track-index="10" style="top:300px">
        {REPOST}
        <div class="card" id="ctacard"><div class="b" style="font-size:110px">REPOST<br>VIDEO NI!</div></div>
        <div style="margin-top:28px"><span class="pill yellow" id="ctap" style="font-size:42px;white-space:normal;max-width:760px;text-align:center;line-height:1.2;border-radius:34px;justify-content:center">SUPAYA KAWAN-KAWAN PUN<br>BOLEH SENAM JUGAK!</span></div>
      </div>

      <div id="flash" class="layer"></div>
      <div id="progress"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      /*{{{{VIDJS}}}}*/
      tl.fromTo("#progress", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {{{{TOTAL}}}}, ease: "none" }}, 0);

      // hook
      tl.fromTo("#h1", {{ scale: 3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }}, 0.05);
      tl.fromTo("#h1b", {{ scale: 3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }}, 0.35);
      tl.to("#root", {{ keyframes: {{ x: [0, -14, 12, -8, 6, 0] }}, duration: 0.25 }}, 0.6);
      tl.fromTo("#h2", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 0.9);
      tl.fromTo(["#hm0", "#hm1", "#hm2", "#hm3"], {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.25, ease: "back.out(2)", stagger: 0.25 }}, 1.4);

{chr(10).join(js)}

      // cta
      tl.fromTo("#rp", {{ scale: 0 }}, {{ scale: 1, duration: 0.4, ease: "back.out(2.5)" }}, {T0+4*LEN+0.1:.2f});
      tl.fromTo("#rpa", {{ rotation: 0 }}, {{ rotation: 360, duration: 1.2, ease: "power2.inOut", repeat: 2 }}, {T0+4*LEN+0.4:.2f});
      tl.fromTo("#ctacard", {{ scale: 0, rotation: -8 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }}, {T0+4*LEN+0.4:.2f});
      tl.to("#ctacard", {{ scale: 1.05, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut" }}, {T0+4*LEN+1.0:.2f});
      tl.fromTo("#ctap", {{ y: 80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {T0+4*LEN+1.0:.2f});

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
t = head + body
b = t[t.index('<body>'):]
o, c = len(re.findall(r'<div\b', b)), b.count('</div>')
print('div open', o, 'close', c, 'TOTAL', TOTAL); assert o == c
open(S + '/template13.html', 'w').write(t)

src = open(S + '/build9.py').read()
src = src.replace('TOTAL = 38.0', f'TOTAL = {TOTAL}')
src, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 3.0, "f8", 0.0),     # HOOK: muka, trek luar
    (3.0, 11.0, "f17", 2.0),   # LEVEL 1: perlahan, kaki sahaja (close-up lutut)
    (11.0, 19.0, "f13", 1.0),  # LEVEL 2: sederhana, kaki sahaja (close-up kasut)
    (19.0, 27.0, "f12", 1.5),  # LEVEL 3: laju + tali resistance
    (27.0, 35.0, "f18", 6.0),  # LEVEL 4: laju + dumbbell
    (35.0, TOTAL, "f2", 4.0),  # CTA: repost
]
MUTED = {"f5"}''', src, flags=re.S); assert n == 1
sfx = ['(0.05, "impact", 0.55)', '(0.05, "whoosh", 0.35)', '(0.35, "impact", 0.4)', '(0.90, "pop", 0.4)',
       '(1.40, "pop", 0.3)', '(1.65, "pop", 0.3)', '(1.90, "pop", 0.3)', '(2.15, "ding", 0.3)']
for k in range(4):
    s = T0 + k * LEN
    sfx += [f'({s:.2f}, "whoosh", 0.35)', f'({s+0.3:.2f}, "impact", 0.45)', f'({s+0.9:.2f}, "swoosh", 0.3)', f'({s+1.4:.2f}, "pop", 0.4)',
            f'({s+2.35:.2f}, "ding", 0.3)', f'({s+4.1:.2f}, "pop", 0.35)']
    if k == 0: sfx += [f'({s+4.7:.2f}, "pop", 0.35)', f'({s+5.3:.2f}, "pop", 0.35)']
    if k == 3: sfx += [f'({s+4.7:.2f}, "cash", 0.35)']
c0 = T0 + 4 * LEN
sfx += [f'({c0:.2f}, "whoosh", 0.35)', f'({c0+0.1:.2f}, "pop", 0.4)', f'({c0+0.4:.2f}, "swoosh", 0.35)', f'({c0+1.0:.2f}, "ding", 0.3)']
src, n = re.subn(r'SFX = \[\n.*?\n\]', 'SFX = [\n    ' + ', '.join(sfx) + ',\n]', src, flags=re.S); assert n == 1
open(S + '/build13.py', 'w').write(src)
print('ok')
