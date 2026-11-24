"""Task 18: 10 minit latihan V-Stepper. Starts on calorie table (55..115kg, 7 rows, one by one, 10s),
muscles (seluruh badan + fakta), USP counter + <6kg, CTA 2027 upgrade body. Infographics scaled to 90%."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t = open(S + '/template14.html').read()
t16 = open(S + '/template16.html').read()

def R(o, n, cnt=1):
    global t
    assert o in t, o[:90]
    t = t.replace(o, n, cnt)
def block(src, bid):
    i = src.index(f'<div id="{bid}"'); d = 0
    for m in re.finditer(r'<div\b|</div>', src[i:]):
        d += 1 if m.group(0).startswith('<div') else -1
        if d == 0: return src[i:i + m.end()]

# ---- hook text
R('>15 MINIT</span>', '>10 MINIT</span>')
R('id="hk2" style="font-size:47px">LATIHAN STEPPER', 'id="hk2" style="font-size:47px">LATIHAN V-STEPPER')
R('*Anggaran untuk 15 minit latihan', '*Anggaran untuk 10 minit latihan')

# ---- table rows: 55..115kg (extrapolated from user's 10-min reference ~2.0-2.1 kcal/kg)
KG = [55, 65, 75, 85, 95, 105, 115]
KC = [110, 130, 150, 170, 190, 220, 240]
rows = ''.join(f'<div class="trow{" top" if k == 115 else ""}" id="r{i}"><span class="kg">{k}KG</span><span class="bar"><i id="b{i}" style="width:{c/240*100:.1f}%"></i></span><span class="kc">±{c}<small>KAL</small></span></div>'
               for i, (k, c) in enumerate(zip(KG, KC)))
tb = block(t, 'table')
new_tb = re.sub(r'(<div class="hdr">.*?</div>\n\s*).*?(\n\s*</div>)$', lambda m: m.group(1) + rows + m.group(2), tb, flags=re.S)
assert new_tb.count('class="trow') == 7
t = t.replace(tb, new_tb.replace('style="top:520px"', 'style="top:470px"'))
# row animations: one by one every 1.0s
js_rows = '\n'.join(f'      tl.fromTo("#r{i}", {{ x: -900, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {0.3 + i*1.0:.2f});\n'
                    f'      tl.fromTo("#b{i}", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.5, ease: "power2.out" }}, {0.45 + i*1.0:.2f});' for i in range(1, 7))
t, n = re.subn(r'      tl\.fromTo\("#r0".*?tl\.fromTo\("#b5"[^\n]*\n', lambda m: js_rows + '\n', t, count=1, flags=re.S); assert n == 1
R('tl.to("#r5", { scale: 1.04, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut" }, 7.4);',
  'tl.to("#r6", { scale: 1.04, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut" }, 7.3);')
R('<div id="vs" class="g clip" data-start="7.8" data-duration="2.2" data-track-index="12" style="top:1335px">',
  '<div id="vs" class="g clip" data-start="7.8" data-duration="2.2" data-track-index="12" style="top:1310px">')
R('<div id="note" class="g clip" data-start="8.2" data-duration="1.8" data-track-index="12" style="top:1440px">',
  '<div id="note" class="g clip" data-start="8.2" data-duration="1.8" data-track-index="12" style="top:1405px">')

# ---- infographics at 90%: table + muscles CSS
def scale_rule(rule):
    return re.sub(r'(\d+(?:\.\d+)?)px', lambda m: f'{round(float(m.group(1)) * 0.9)}px', rule)
css_a = t.index('<style>'); css_b = t.index('</style>')
css = t[css_a:css_b]
def scale_selectors(css, prefixes):
    out = []
    for line in css.split('\n'):
        s = line.strip()
        if any(s.startswith(p) for p in prefixes):
            line = scale_rule(line)
        out.append(line)
    return '\n'.join(out)
# multi-line #table rule: join first
css = css.replace('border-radius: 34px;\n               box-shadow: 0 16px 0 #000; padding: 26px 34px 20px; text-align: left; }',
                  'border-radius: 34px; box-shadow: 0 16px 0 #000; padding: 26px 34px 20px; text-align: left; }')
css = scale_selectors(css, ['#table', '.trow', '#muscles', '#mpills'])
css = re.sub(r'#table \{ left: \d+px; right: \d+px; top: \d+px;', '#table { left: 108px; right: 108px; top: 470px;', css)
css = re.sub(r'#muscles \{ left: \d+px; right: \d+px; top: \d+px;', '#muscles { left: 99px; right: 99px; top: 400px;', css)
assert '#table { left: 108px' in css and '#muscles { left: 99px' in css and 'height: 101px' in css
t = t[:css_a] + css + t[css_b:]

# ---- muscles: seluruh badan + fakta
R('>OTOT YANG DILATIH</span>', '>LATIH OTOT SELURUH BADAN</span>')
R('style="font-size:84px">LATIH OTOT SELURUH BADAN', 'style="font-size:76px">LATIH OTOT SELURUH BADAN')
mus = block(t, 'muscles')
FACT = ('<div class="src" id="msrc">Fakta: stepper melatih quadriceps, hamstring, glutes &amp; betis; core bekerja untuk imbangan; '
        'tali resistance libatkan bahu &amp; lengan. (Well+Good, Chron, Women\'s Health)</div>')
t = t.replace(mus, mus[:-len('</div>')] + '  ' + FACT + '\n      </div>')
R('    </style>', '      .src { margin-top: 12px; font-family: var(--font-ui); font-weight: 800; font-size: 20px; color: #fff; opacity: 0.85; text-shadow: 0 2px 0 #000; }\n    </style>')
R('      // usp counter', '      tl.fromTo("#msrc", { opacity: 0 }, { opacity: 0.85, duration: 0.4 }, 14.6);\n      // usp counter')

# ---- USP 1: counter instead of 100kg
ctr = block(t16, 'ctr')
ctr = re.sub(r'data-start="[0-9.]+" data-duration="[0-9.]+"', 'data-start="16.55" data-duration="3.45"', ctr, count=1)
t = t.replace(block(t, 'kg'), ctr)
t, n = re.subn(r'      tl\.fromTo\("#kgc".*?tl\.fromTo\("#kgp"[^\n]*\n',
               lambda m: '      tl.fromTo("#cc", { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 16.60);\n'
                         '      tl.fromTo("#cb", { scale: 0.4, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }, 16.85);\n'
                         '      tl.fromTo(["#cp1","#cp2","#cp3"], { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.4 }, 17.80);\n',
               t, count=1, flags=re.S); assert n == 1
# ---- USP 2: < 6kg
R('<span class="mid" id="la">MUDAH NAK ALIH</span>', '<span class="mid" id="la">BERAT TAK SAMPAI 6KG</span>')
t = t.replace(block(t, 'lightlow'), '')
t = re.sub(r'\n\s*tl\.fromTo\("#lb"[^\n]*', '', t)
# ---- CTA
R('<span class="mid" id="c1a" style="margin-top:34px">2027 NAK BADAN FIT?</span>',
  '<span class="mid" id="c1a" style="margin-top:34px">TAHUN 2027</span>\n        <span class="blk" id="c1b" style="font-size:80px">NAK UPGRADE BODY?</span>')
R('      tl.to("#root", { keyframes: { y: [0, 12, -10, 6, 0] }, duration: 0.22 }, 25.40);',
  '      tl.fromTo("#c1b", { scale: 0, rotation: 15 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 25.30);\n'
  '      tl.to("#root", { keyframes: { y: [0, 12, -10, 6, 0] }, duration: 0.22 }, 25.40);')

t = re.sub(r'(font-size: ?)(\d+)px', lambda m: f'{m.group(1)}{min(int(m.group(2)), 100)}px', t)
assert not [x for x in re.findall(r'font-size: ?(\d+)px', t) if int(x) > 100]
b = t[t.index('<body>'):]
o, c = len(re.findall(r'<div\b', b)), b.count('</div>')
print('div open', o, 'close', c); assert o == c
ids = re.findall(r'\bid="([^"]+)"', b); dup = {i for i in ids if ids.count(i) > 1}; assert not dup, dup
for need in ['id="r6"', '±240', 'id="ctr"', 'id="ring6"', 'NAK UPGRADE BODY?', 'START STEPPER', 'id="msrc"']:
    assert need in t, need
open(S + '/template18.html', 'w').write(t)

src = open(S + '/build14.py').read()
src, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 10.0, "f11", 0.5),   # HOOK + jadual kalori 10 minit (bilik, tali)
    (10.0, 13.2, "f4", 2.0),   # otot: luar, tali (baju putih)
    (13.2, 16.5, "f17", 2.0),  # otot: close-up lutut
    (16.5, 20.0, "f5", 68.6),  # USP counter: tekan counter (muted: ada muzik)
    (20.0, 24.0, "f16", 2.9),  # USP <6kg: timbang 5.9kg
    (24.0, 27.5, "f14", 6.0),  # CTA tahun 2027
    (27.5, TOTAL, "f19", 9.0), # CTA start stepper sekarang
]
MUTED = {"f5"}''', src, flags=re.S); assert n == 1
src = re.sub(r'\(0\.30, "pop", 0\.35\), \(1\.50, "pop", 0\.35\).*?\(6\.30, "pop", 0\.35\),',
             ', '.join(f'({0.3 + i*1.0:.2f}, "pop", 0.35)' for i in range(1, 7)) + ',', src, count=1, flags=re.S)
src = src.replace('(16.75, "riser", 0.25), (17.75, "impact", 0.45), (18.30, "pop", 0.4),',
                  '(16.85, "ding", 0.3), (17.80, "pop", 0.35), (18.20, "pop", 0.35), (18.60, "pop", 0.35),')
src = src.replace('(21.55, "swoosh", 0.35),', '')
assert '(6.30, "pop", 0.35)' in src and '(17.80, "pop", 0.35)' in src
open(S + '/build18.py', 'w').write(src)
print('ok')
