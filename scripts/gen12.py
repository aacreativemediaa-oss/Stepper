"""Task 12: opens straight on the calorie table (10 min), then muscles, USP, CTA."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t7 = open(S + '/template7.html').read()   # 10-min table, calendar, counter
t8 = open(S + '/template8.html').read()   # muscles, scale ring
head = t8[:t8.index('    </style>')]
cal_css = re.search(r'      #cal \{.*?#cal \.rings i \{[^\n]*\n', t7, re.S).group(0)
if '#cal {' not in head:
    head += cal_css
head += '''      #rugi { top: 560px; }
'''

def block(src, bid):
    """Return the full <div id="bid" ...>...</div> element (balanced)."""
    i = src.index(f'<div id="{bid}"')
    depth, j = 0, i
    for m in re.finditer(r'<div\b|</div>', src[i:]):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            return src[i:i + m.end()]
    raise ValueError(bid)

def timed(html, start, dur):
    return re.sub(r'data-start="[0-9.]+" data-duration="[0-9.]+"', f'data-start="{start}" data-duration="{dur}"', html, count=1)

table = timed(block(t7, 'table'), 0, 6.0).replace('top: 520px', '')
assert '±100<small>' in table and '±210<small>' in table
muscles = timed(block(t8, 'muscles'), 6.25, 6.25)
usp = timed(block(t8, 'usp'), 12.55, 3.45).replace('>SIAP ADA<', '>ADA SEKALI<')
ring = timed(block(t8, 'u1ring'), 16.6, 3.4)
cal = re.search(r'<div id="cal">.*?2026</div></div></div>', t7, re.S).group(0)
ctacard = block(t7, 'cta')
assert 'GRAB<br>STEPPER!' in ctacard
cta = timed(ctacard, 23.55, 3.95).replace('<div class="a">JANGAN TUNGGU</div>', '<div class="a">SEKARANG!</div>') \
                                .replace('KAT BEG KUNING</div>', 'KAT BEG KUNING SEKARANG!</div>', 1)
cta = cta.replace('<div class="a">SEKARANG!</div>', '')
arrows = timed(block(t7, 'arrows'), 24.3, 3.2)
CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

body = f'''    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{{{{TOTAL}}}}" data-width="1080" data-height="1920">
      {{{{VIDEOS}}}}
      {{{{SFX}}}}
      <div id="vignette" class="layer"></div>

      <!-- HOOK + EDU 1: straight into the table (0-6s). Headline 150px, sub headline 70px -->
      <div id="ttitle" class="g clip" data-start="0" data-duration="6.0" data-track-index="10" style="top:110px">
        <span class="big" id="hk1" style="font-size:150px;color:var(--lime)">10 MINIT</span>
        <span class="blk pink" id="hk2" style="font-size:70px">LATIHAN STEPPER</span>
      </div>
      {table.replace('<div id="table" class="g clip"', '<div id="table" class="g clip" style="top:520px"')}
      <div id="vs" class="g clip" data-start="0" data-duration="6.0" data-track-index="12" style="top:1335px">
        <span class="blk" id="vs1" style="font-size:66px">BERAT BADAN VS KALORI</span>
      </div>

      <!-- EDU 2: otot -->
      <div id="mtitle" class="g clip" data-start="6.05" data-duration="6.45" data-track-index="10" style="top:250px">
        <span class="blk pink" id="mt1" style="font-size:84px">OTOT YANG DILATIH</span>
      </div>
      {muscles}

      <!-- USP -->
      {usp}
      <div id="ctp" class="g clip stack" data-start="14.0" data-duration="2.0" data-track-index="11" style="top:640px">
        <div class="pill lime" id="cp1">{CHECK("#000","#c6ff00")}STEPS</div>
        <div class="pill yellow" id="cp2">{CHECK("#000","#ffd400")}MASA</div>
        <div class="pill pink" id="cp3">{CHECK("#c6ff00","#000")}KALORI</div>
      </div>
      <div id="light" class="g clip" data-start="16.05" data-duration="3.95" data-track-index="10" style="top:230px">
        <div class="cara" id="lc">RINGAN</div>
        <span class="mid" id="la">MUDAH NAK ALIH</span>
      </div>
      {ring}
      <div id="lightlow" class="g clip" data-start="17.5" data-duration="2.5" data-track-index="10" style="top:1330px">
        <span class="blk pink" id="lb" style="font-size:72px">BAWA KE MANA-MANA</span>
      </div>

      <!-- CTA -->
      <div id="c1" class="g clip" data-start="20.05" data-duration="3.45" data-track-index="10" style="top:230px">
        {cal}
        <span class="mid" id="c1a" style="margin-top:34px">NAK BADAN FIT</span>
        <span class="blk" id="c1b">2027?</span>
      </div>
      {cta}
      {arrows}

      <div id="flash" class="layer"></div>
      <div id="progress"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      /*{{{{VIDJS}}}}*/
      tl.fromTo("#progress", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {{{{TOTAL}}}}, ease: "none" }}, 0);

      // table from frame 0 (already on screen), rows + bars race in fast
      tl.fromTo("#hk1", {{ scale: 1.25 }}, {{ scale: 1, duration: 0.3, ease: "power3.out" }}, 0);
      tl.to("#root", {{ keyframes: {{ x: [0, -12, 10, -6, 0] }}, duration: 0.22 }}, 0.05);
      tl.fromTo("#hk2", {{ rotation: -10, scale: 0.8 }}, {{ rotation: -3, scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, 0.1);
{chr(10).join(f'      tl.to("#b{i}", {{ scaleX: 1.04, duration: 0.18, yoyo: true, repeat: 1, ease: "sine.inOut" }}, {0.3 + i*0.15:.2f});' for i in range(6))}
      tl.to("#r5", {{ scale: 1.04, duration: 0.25, yoyo: true, repeat: 5, ease: "sine.inOut" }}, 2.0);
      tl.fromTo("#vs1", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 1.0);
      tl.fromTo("#note span", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, 1.6);

      // otot
      tl.fromTo("#mt1", {{ scale: 0, rotation: -15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 6.1);
      tl.fromTo("#muscles", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, 6.3);
      tl.fromTo("#fg1 .mf > *", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.12 }}, 6.8);
      tl.fromTo("#fg2 .mb > *", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.12 }}, 7.4);
      tl.to(["#fg1 .mf", "#fg2 .mb"], {{ opacity: 0.55, duration: 0.3, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 8.6);
      tl.fromTo(["#mp0", "#mp1", "#mp2", "#mp3", "#mp4"], {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.55 }}, 8.4);

      // usp counter
      tl.fromTo("#u0", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 12.6);
      tl.fromTo("#u1", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, 12.85);
      tl.fromTo(["#cp1", "#cp2", "#cp3"], {{ x: -800 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)", stagger: 0.4 }}, 14.0);
      // ringan
      tl.fromTo("#lc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 16.1);
      tl.fromTo("#la", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, 16.3);
      tl.fromTo("#ring6", {{ scale: 2.5, opacity: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, 16.6);
      tl.to("#ring6", {{ scale: 1.08, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 50%" }}, 17.0);
      tl.fromTo("#kgtag", {{ scale: 0, rotation: 20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.5)" }}, 16.8);
      tl.fromTo("#lb", {{ x: 1100 }}, {{ x: 0, duration: 0.3, ease: "power4.out" }}, 17.55);

      // cta
      tl.fromTo("#cal", {{ y: -500, rotation: -8 }}, {{ y: 0, rotation: 0, duration: 0.4, ease: "back.out(1.6)" }}, 20.05);
      tl.fromTo("#calold", {{ rotationX: 0 }}, {{ rotationX: -100, opacity: 0, duration: 0.45, ease: "power2.in" }}, 20.5);
      tl.fromTo("#c1a", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 21.0);
      tl.fromTo("#c1b", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 21.3);
      tl.to("#root", {{ keyframes: {{ y: [0, 12, -10, 6, 0] }}, duration: 0.22 }}, 21.4);
      tl.fromTo("#ctacard", {{ scale: 0, rotation: -8 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }}, 23.6);
      tl.fromTo("#ctabag", {{ y: 300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, 24.2);
      tl.to("#ctabag", {{ scale: 1.08, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 24.6);
      tl.fromTo("#arrows svg", {{ y: -30, opacity: 0 }}, {{ y: 20, opacity: 1, duration: 0.4, stagger: 0.12, repeat: 4, yoyo: true, ease: "sine.inOut" }}, 24.3);

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
# note under table
note = '<div id="note" class="g clip" data-start="1.6" data-duration="4.4" data-track-index="12" style="top:1440px"><span>*Anggaran untuk 10 minit latihan</span></div>'
body = body.replace('      <!-- EDU 2: otot -->', '      ' + note + '\n\n      <!-- EDU 2: otot -->', 1)
t = head + body
# the table's own header row already says BERAT BADAN / KALORI TERBAKAR; table title block from t7 is not used
b = t[t.index('<body>'):]
o, c = len(re.findall(r'<div\b', b)), b.count('</div>')
print('div open', o, 'close', c); assert o == c
for need in ['id="table"', 'id="muscles"', 'id="usp"', 'id="u1ring"', 'id="cal"', 'id="cta"', 'id="arrows"', 'KAT BEG KUNING SEKARANG!', '#note']:
    assert need in t, need
open(S + '/template12.html', 'w').write(t)

bsrc = open(S + '/build9.py').read()
bsrc = bsrc.replace('TOTAL = 38.0', 'TOTAL = 27.5')
bsrc, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 6.0, "f8", 0.0),     # HOOK + jadual kalori (trek luar)
    (6.0, 9.2, "f7", 2.0),     # otot: badan penuh, tali rintangan (luar)
    (9.2, 12.5, "f17", 6.0),   # otot: close-up kaki
    (12.5, 16.0, "f5", 60.0),  # USP: pasang counter pada stepper (muted: ada muzik)
    (16.0, 20.0, "f16", 3.0),  # USP: ringan, timbang 5.9kg
    (20.0, 23.5, "f13", 5.0),  # CTA: fit 2027 (close-up kasut)
    (23.5, TOTAL, "f2", 9.0),  # CTA: grab kat beg kuning
]
MUTED = {"f5"}''', bsrc, flags=re.S); assert n == 1
bsrc, n = re.subn(r'SFX = \[\n.*?\n\]', '''SFX = [
    (0.00, "impact", 0.55), (0.05, "whoosh", 0.35), (1.00, "pop", 0.4), (2.00, "ding", 0.3),
    (6.00, "whoosh", 0.35), (6.10, "impact", 0.4), (6.80, "riser", 0.25),
    (8.40, "pop", 0.35), (8.95, "pop", 0.35), (9.50, "pop", 0.35), (10.05, "pop", 0.35), (10.60, "pop", 0.35),
    (12.50, "whoosh", 0.35), (12.85, "ding", 0.3), (14.00, "pop", 0.35), (14.40, "pop", 0.35), (14.80, "pop", 0.35),
    (16.00, "whoosh", 0.35), (16.30, "pop", 0.4), (16.80, "ding", 0.3), (17.55, "swoosh", 0.35),
    (20.00, "whoosh", 0.35), (20.50, "swoosh", 0.35), (21.30, "impact", 0.45),
    (23.50, "whoosh", 0.35), (23.60, "pop", 0.4), (24.20, "ding", 0.3), (24.30, "pop", 0.4),
]''', bsrc, flags=re.S); assert n == 1
open(S + '/build12.py', 'w').write(bsrc)
print('ok')
