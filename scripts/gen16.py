"""Task 16: 3 Kesilapan Guna V-Stepper v2 (laju / kasut sukan / konsisten) + USP 6kg, counter, otot.
Format terkini: headline 100px, sub-headline 47px, tiada tulisan >100px."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t10 = open(S + '/template10.html').read()
t8 = open(S + '/template8.html').read()
t7 = open(S + '/template7.html').read()

def block(src, bid):
    i = src.index(f'<div id="{bid}"'); d = 0
    for m in re.finditer(r'<div\b|</div>', src[i:]):
        d += 1 if m.group(0).startswith('<div') else -1
        if d == 0: return src[i:i + m.end()]
def timed(h, s, d):
    return re.sub(r'data-start="[0-9.]+" data-duration="[0-9.]+"', f'data-start="{s:.2f}" data-duration="{d:.2f}"', h, count=1)
def svg(h, idx=0):
    return re.findall(r'<svg.*?</svg>', h, re.S)[idx]

head = t10[:t10.index('    </style>')]
head += '''      .bignum { display: block; font-size: 100px; line-height: 1; color: var(--lime); -webkit-text-stroke: 7px #000; paint-order: stroke fill; text-shadow: 0 10px 0 #000; }
      .src { margin-top: 14px; font-family: var(--font-ui); font-weight: 800; font-size: 22px; color: #fff; opacity: 0.85; text-shadow: 0 2px 0 #000; }
'''
CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
m1, m2, m3 = block(t10, 'm1'), block(t10, 'm2'), block(t10, 'm3')
WARN = svg(block(t10, 'hook'))
WARNI = svg(m1, 1)
FOOT, GAUGE = svg(m1, 0), svg(m2, 0)
WEEK = re.search(r'<div id="week">.*?</div></div>', m3, re.S).group(0)
RING = block(t10, 'u1ring')
MUS = block(t8, 'muscles')
CAL = re.search(r'<div id="cal">.*?2026</div></div></div>', t7, re.S).group(0)

T = dict(k1=3.5, k2=10.0, k3=17.0, ctr=23.5, kg=27.0, mus=31.0, cal=37.5, card=40.5, end=44.5)
html = f'''      <!-- HOOK: headline 100px, sub-headline 47px -->
      <div id="hook" class="g clip" data-start="0" data-duration="3.5" data-track-index="10" style="top:420px">
        {WARN}
        <span class="big" id="h1" style="font-size:100px;color:var(--yellow)">3 KESILAPAN</span>
        <span class="blk pink" id="h2" style="font-size:47px">GUNA V-STEPPER</span>
      </div>

      <!-- K1: laju -->
      <div id="k1" class="g clip" data-start="{T['k1']+0.05:.2f}" data-duration="{T['k2']-T['k1']-0.05:.2f}" data-track-index="10" style="top:230px">
        <div class="tipttl"><div class="num red" id="k1n">1</div><span class="blk" id="k1t" style="font-size:80px">STEP LAJU SANGAT</span></div>
        {GAUGE}
        <span class="blk pink" id="k1a" style="font-size:80px">HILANG KAWALAN</span>
        <span class="mid" id="k1b" style="margin-top:14px;font-size:62px">BADAN TAK STABIL</span>
        <div style="margin-top:16px"><span class="pill" id="k1c" style="background:var(--red);color:#fff">{WARNI}RISIKO TERJATUH</span></div>
        <div class="fix"><span class="pill lime" id="k1f">{CHECK("#000","#c6ff00")}KAWAL RENTAK</span></div>
      </div>

      <!-- K2: kasut sukan -->
      <div id="k2" class="g clip" data-start="{T['k2']+0.05:.2f}" data-duration="{T['k3']-T['k2']-0.05:.2f}" data-track-index="10" style="top:230px">
        <div class="tipttl"><div class="num red" id="k2n">2</div><span class="blk" id="k2t" style="font-size:74px">TAK PAKAI KASUT SUKAN</span></div>
        {FOOT}
        <span class="mid" id="k2a" style="margin-top:14px;font-size:54px">IMPAK BERTERUSAN PADA TAPAK KAKI</span>
        <div style="margin-top:16px"><span class="pill" id="k2b" style="background:var(--red);color:#fff">{WARNI}RISIKO KECEDERAAN MENINGKAT</span></div>
        <div class="fix"><span class="pill lime" id="k2f">{CHECK("#000","#c6ff00")}PAKAI KASUT SUKAN</span></div>
      </div>

      <!-- K3: konsisten -->
      <div id="k3" class="g clip" data-start="{T['k3']+0.05:.2f}" data-duration="{T['ctr']-T['k3']-0.05:.2f}" data-track-index="10" style="top:230px">
        <div class="tipttl"><div class="num red" id="k3n">3</div><span class="blk" id="k3t">TAK KONSISTEN</span></div>
        {WEEK}
        <div id="prog"><i id="progi"></i></div>
        <div style="margin-top:22px"><span class="blk" id="k3a" style="font-size:72px">MIN. 10 MINIT SETIAP HARI</span></div>
        <div class="fix"><span class="pill lime" id="k3f">{CHECK("#000","#c6ff00")}UNTUK KESAN EFEKTIF</span></div>
      </div>

      <!-- USP 1: counter -->
      <div id="ctr" class="g clip" data-start="{T['ctr']+0.05:.2f}" data-duration="{T['kg']-T['ctr']-0.05:.2f}" data-track-index="10" style="top:250px">
        <div class="cara" id="cc">ADA SEKALI</div>
        <span class="big" id="cb" style="font-size:98px">MULTIFUNCTION<br>COUNTER</span>
        <div class="row" style="margin-top:18px"><span class="pill lime" id="cp1">{CHECK("#000","#c6ff00")}STEPS</span><span class="pill yellow" id="cp2">{CHECK("#000","#ffd400")}MASA</span><span class="pill pink" id="cp3">{CHECK("#c6ff00","#000")}KALORI</span></div>
      </div>

      <!-- USP 2: < 6kg -->
      <div id="wt" class="g clip" data-start="{T['kg']+0.05:.2f}" data-duration="{T['mus']-T['kg']-0.05:.2f}" data-track-index="10" style="top:230px">
        <div class="cara" id="wc">RINGAN</div>
        <span class="mid" id="wa">BERAT TAK SAMPAI 6KG</span>
      </div>
      {timed(RING, T['kg']+0.6, T['mus']-T['kg']-0.6)}

      <!-- USP 3: otot seluruh badan -->
      <div id="mtitle" class="g clip" data-start="{T['mus']+0.05:.2f}" data-duration="{T['cal']-T['mus']-0.05:.2f}" data-track-index="10" style="top:250px">
        <span class="blk pink" id="mt1" style="font-size:80px">LATIH OTOT SELURUH BADAN</span>
      </div>
      {timed(MUS, T['mus']+0.25, T['cal']-T['mus']-0.25).replace('</div>\n      </div>', '</div>\n        <div class="src" id="msrc">Fakta: stepper melatih quadriceps, hamstring, glutes &amp; betis; core bekerja untuk imbangan; tali resistance libatkan bahu &amp; lengan.</div>\n      </div>', 1)}

      <!-- CTA -->
      <div id="c1" class="g clip" data-start="{T['cal']+0.05:.2f}" data-duration="{T['card']-T['cal']-0.05:.2f}" data-track-index="10" style="top:230px">
        {CAL}
        <span class="mid" id="c1a" style="margin-top:34px">TAHUN 2027</span>
        <span class="blk" id="c1b" style="font-size:80px">NAK UPGRADE BODY?</span>
      </div>
      <div id="cta" class="g clip" data-start="{T['card']+0.05:.2f}" data-duration="{T['end']-T['card']-0.05:.2f}" data-track-index="10" style="top:330px">
        <div class="card" id="ctacard"><div class="b" style="font-size:100px">START STEPPER<br>SEKARANG!</div></div>
      </div>
'''
k1, k2, k3, c, kg, mu, ca, cd = (T[x] for x in ['k1', 'k2', 'k3', 'ctr', 'kg', 'mus', 'cal', 'card'])
js = f'''      // hook
      tl.fromTo("#warn", {{ scale: 0, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }}, 0.0);
      tl.to("#warn", {{ scale: 1.1, duration: 0.2, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 0.5);
      tl.fromTo("#h1", {{ scale: 3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }}, 0.3);
      tl.to("#root", {{ keyframes: {{ x: [0, -14, 12, -8, 6, 0] }}, duration: 0.25 }}, 0.55);
      tl.fromTo("#h2", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 1.0);

      // K1 laju
      tl.fromTo("#k1n", {{ scale: 0, rotation: -180 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }}, {k1+0.1:.2f});
      tl.fromTo("#k1t", {{ x: 1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, {k1+0.4:.2f});
      tl.fromTo("#gauge", {{ scale: 0 }}, {{ scale: 1, duration: 0.35, ease: "back.out(2)" }}, {k1+0.8:.2f});
      tl.fromTo("#needle", {{ rotation: -80 }}, {{ rotation: 72, duration: 1.0, ease: "power2.in" }}, {k1+1.1:.2f});
      tl.to("#needle", {{ rotation: 62, duration: 0.08, yoyo: true, repeat: 15, ease: "none" }}, {k1+2.1:.2f});
      tl.fromTo("#k1a", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, {k1+2.2:.2f});
      tl.fromTo("#k1b", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {k1+2.9:.2f});
      tl.to("#k1b", {{ keyframes: {{ rotation: [0, -4, 4, -3, 3, 0], x: [0, -12, 12, -8, 8, 0] }}, duration: 0.6, repeat: 1 }}, {k1+3.2:.2f});
      tl.fromTo("#k1c", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, {k1+3.8:.2f});
      tl.fromTo("#k1f", {{ x: -1100 }}, {{ x: 0, duration: 0.35, ease: "back.out(1.6)" }}, {k1+4.9:.2f});

      // K2 kasut
      tl.fromTo("#k2n", {{ scale: 0, rotation: -180 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }}, {k2+0.1:.2f});
      tl.fromTo("#k2t", {{ x: 1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, {k2+0.4:.2f});
      tl.fromTo("#foot", {{ y: -400 }}, {{ y: 0, duration: 0.45, ease: "bounce.out" }}, {k2+0.8:.2f});
      tl.fromTo("#fripple path", {{ scale: 0.4, opacity: 0, transformOrigin: "50% 50%" }}, {{ scale: 1.2, opacity: 1, duration: 0.5, stagger: 0.12, repeat: 5, ease: "power1.out" }}, {k2+1.25:.2f});
      tl.fromTo("#heelhit", {{ opacity: 0.2 }}, {{ opacity: 0.9, duration: 0.25, yoyo: true, repeat: 9 }}, {k2+1.25:.2f});
      tl.fromTo("#xmark", {{ scale: 0, transformOrigin: "231px 49px" }}, {{ scale: 1, duration: 0.3, ease: "back.out(3)" }}, {k2+1.5:.2f});
      tl.fromTo("#k2a", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {k2+2.0:.2f});
      tl.fromTo("#k2b", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, {k2+2.9:.2f});
      tl.fromTo("#k2f", {{ x: -1100 }}, {{ x: 0, duration: 0.35, ease: "back.out(1.6)" }}, {k2+4.6:.2f});

      // K3 konsisten
      tl.fromTo("#k3n", {{ scale: 0, rotation: -180 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }}, {k3+0.1:.2f});
      tl.fromTo("#k3t", {{ x: 1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, {k3+0.4:.2f});
      tl.fromTo(["#d0","#d1","#d2","#d3","#d4","#d5","#d6"], {{ scale: 0 }}, {{ scale: 1, duration: 0.25, ease: "back.out(2.5)", stagger: 0.18 }}, {k3+0.9:.2f});
      tl.fromTo("#progi", {{ scaleX: 0 }}, {{ scaleX: 0.22, duration: 2.0, ease: "power1.out" }}, {k3+2.2:.2f});
      tl.fromTo("#k3a", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, {k3+2.8:.2f});
      tl.fromTo("#k3f", {{ x: -1100 }}, {{ x: 0, duration: 0.35, ease: "back.out(1.6)" }}, {k3+4.0:.2f});

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
      // USP otot
      tl.fromTo("#mt1", {{ scale: 0, rotation: -15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, {mu+0.1:.2f});
      tl.fromTo("#muscles", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {mu+0.3:.2f});
      tl.fromTo("#fg1 .mf > *", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.12 }}, {mu+0.8:.2f});
      tl.fromTo("#fg2 .mb > *", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.12 }}, {mu+1.4:.2f});
      tl.to(["#fg1 .mf", "#fg2 .mb"], {{ opacity: 0.55, duration: 0.3, yoyo: true, repeat: 7, ease: "sine.inOut" }}, {mu+2.6:.2f});
      tl.fromTo(["#mp0","#mp1","#mp2","#mp3","#mp4"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.45 }}, {mu+2.2:.2f});
      tl.fromTo("#msrc", {{ opacity: 0 }}, {{ opacity: 0.85, duration: 0.4 }}, {mu+4.6:.2f});

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
for need in ['id="warn"', 'id="gauge"', 'id="foot"', 'id="week"', 'id="ring6"', 'id="muscles"', 'id="msrc"', 'id="cal"', 'id="ctacard"']:
    assert need in t, need
ids = re.findall(r'\bid="([^"]+)"', b)
dup = {i for i in ids if ids.count(i) > 1}; assert not dup, dup
open(S + '/template16.html', 'w').write(t)

src = open(S + '/build9.py').read()
src = src.replace('TOTAL = 38.0', f'TOTAL = {T["end"]}')
src, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f13", 6.0),    # HOOK: close-up kasut
    (3.5, 10.0, "f7", 1.0),    # K1 laju: luar, tali (baju putih)
    (10.0, 17.0, "f17", 4.0),  # K2 kasut sukan: close-up kaki/kasut
    (17.0, 23.5, "f19", 3.0),  # K3 konsisten: dumbbell depan TV
    (23.5, 27.0, "f5", 68.6),  # USP counter: tekan counter (muted: ada muzik)
    (27.0, 31.0, "f16", 2.9),  # USP <6kg: timbang 5.9kg
    (31.0, 37.5, "f2", 2.0),   # USP otot seluruh badan: dumbbell depan TV
    (37.5, 40.5, "f15", 2.0),  # CTA 2027 upgrade body
    (40.5, TOTAL, "f18", 10.0),# CTA start stepper sekarang
]
MUTED = {"f5"}''', src, flags=re.S); assert n == 1
sfx = ['(0.00, "whoosh", 0.35)', '(0.05, "zap", 0.4)', '(0.30, "impact", 0.55)', '(1.00, "pop", 0.4)']
for s0 in (k1, k2, k3):
    sfx += [f'({s0:.2f}, "whoosh", 0.35)', f'({s0+0.1:.2f}, "impact", 0.4)']
sfx += [f'({k1+1.1:.2f}, "riser", 0.3)', f'({k1+2.2:.2f}, "zap", 0.4)', f'({k1+3.8:.2f}, "impact", 0.35)', f'({k1+4.9:.2f}, "ding", 0.3)',
        f'({k2+1.25:.2f}, "impact", 0.35)', f'({k2+1.5:.2f}, "zap", 0.35)', f'({k2+2.9:.2f}, "pop", 0.4)', f'({k2+4.6:.2f}, "ding", 0.3)',
        f'({k3+0.9:.2f}, "pop", 0.3)', f'({k3+1.26:.2f}, "pop", 0.3)', f'({k3+1.62:.2f}, "pop", 0.3)', f'({k3+1.98:.2f}, "pop", 0.3)', f'({k3+2.8:.2f}, "impact", 0.4)', f'({k3+4.0:.2f}, "ding", 0.3)',
        f'({c:.2f}, "whoosh", 0.35)', f'({c+0.35:.2f}, "ding", 0.3)', f'({c+1.3:.2f}, "pop", 0.35)', f'({c+1.7:.2f}, "pop", 0.35)', f'({c+2.1:.2f}, "pop", 0.35)',
        f'({kg:.2f}, "whoosh", 0.35)', f'({kg+0.25:.2f}, "pop", 0.4)', f'({kg+0.8:.2f}, "ding", 0.3)',
        f'({mu:.2f}, "whoosh", 0.35)', f'({mu+0.1:.2f}, "impact", 0.4)', f'({mu+0.8:.2f}, "riser", 0.25)'] + \
       [f'({mu+2.2+j*0.45:.2f}, "pop", 0.35)' for j in range(5)] + \
       [f'({ca:.2f}, "whoosh", 0.35)', f'({ca+0.5:.2f}, "swoosh", 0.35)', f'({ca+1.3:.2f}, "impact", 0.45)',
        f'({cd:.2f}, "whoosh", 0.35)', f'({cd+0.1:.2f}, "pop", 0.4)', f'({cd+0.7:.2f}, "ding", 0.3)']
src, n = re.subn(r'SFX = \[\n.*?\n\]', 'SFX = [\n    ' + ', '.join(sfx) + ',\n]', src, flags=re.S); assert n == 1
open(S + '/build16.py', 'w').write(src)
print('ok')
