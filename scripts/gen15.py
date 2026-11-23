"""Task 15: VO (52.8s) almost the same script as Task 11. Reuse Task 11 template/builder,
remap all times sentence-by-sentence, apply the new text sizes (headline 100, sub 47, caption 40, max 100)."""
import json, re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'

# ---- 1. corrected transcript (approved by user)
segs = json.load(open(S + '/t15/transcript.json'))
for seg in segs:
    ws, out, i = seg['words'], [], 0
    while i < len(ws):
        w = dict(ws[i]); core = w['w'].strip().strip(',.?!').lower()
        nxt = ws[i + 1]['w'].strip().lower() if i + 1 < len(ws) else ''
        if core == 'bliss' and nxt.startswith('walk'):
            w['w'] = ' briskwalk'; w['e'] = ws[i + 1]['e']; i += 1
        elif core == 'sah' and nxt.startswith('-sahaja'):
            w['w'] = ' saja-saja'; w['e'] = ws[i + 1]['e']; i += 1
        else:
            rep = {'mana': 'badan', 'virus': 'viral', 'bit': 'beg', 'kompak': 'compact', 'gelebi': 'gelebeh'}
            if core in rep:
                w['w'] = w['w'].replace(w['w'].strip().strip(',.?!'), rep[core])
        out.append(w); i += 1
    for j, w in enumerate(out):
        c = w['w'].strip().lower(); nx = out[j + 1]['w'].strip().lower() if j + 1 < len(out) else ''
        if c == 'so,': w['w'] = w['w'].replace('So,', 'So')            # join "So" to its clause
        if c == 'risau' and nx == 'sebab': w['w'] += ','                 # caption split: badan besar / 100kg
        if c == 'ni' and j > 0 and out[j-1]['w'].strip().lower() == 'ringan': w['w'] += ','  # compact & ringan ni / tak pakai ruang
        if c == 'ni' and nx == 'memang' and j > 0 and out[j-1]['w'].strip().lower() == 'stepper' and out[0]['w'].strip().lower() == 'dulu': w['w'] += ','
    seg['words'] = out
    seg['text'] = ''.join(x['w'] for x in out)
json.dump(segs, open(S + '/t15/transcript_fixed.json', 'w'), ensure_ascii=False, indent=1)

# ---- 2. time map Task 11 -> Task 15 (sentence anchors)
A = [(0, 0), (3.72, 4.2), (4.76, 5.16), (7.68, 7.82), (9.48, 10.72), (12.54, 13.94), (14.52, 16.64),
     (17.58, 20.38), (19.44, 22.16), (22.1, 25.48), (23.16, 26.6), (25.34, 30.0), (27.76, 32.48),
     (29.16, 34.92), (31.28, 38.1), (33.12, 41.06), (34.40, 42.70), (36.96, 42.82), (38.9, 44.94),
     (39.76, 46.3), (41.1, 47.52), (42.14, 48.68), (43.82, 50.54), (46.3, 53.2)]
def f(x):
    for (a0, b0), (a1, b1) in zip(A, A[1:]):
        if x <= a1:
            return b0 + (x - a0) * (b1 - b0) / (a1 - a0)
    return A[-1][1] + (x - A[-1][0])

t = open(S + '/template11.html').read()
# drop the feedback scene (no such sentence in this VO)
for bid in ['fb', 'hearts']:
    i = t.index(f'id="{bid}"'); i = t.rindex('<div', 0, i)
    depth = 0
    for m in re.finditer(r'<div\b|</div>', t[i:]):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            t = t[:i] + t[i + m.end():]; break
t = re.sub(r'\n\s*tl\.[^\n]*#(fbc|fbt|thumb|hearts)[^\n]*', '', t)
# price: "DULU LEBIH RM100"
assert 'BERATUS RINGGIT' in t
t = t.replace('>BERATUS RINGGIT<', '>LEBIH RM100<')
t = t.replace('TRIM GELEBEH KAT RUMAH', 'TRIM GELEBEH DALAM RUMAH')
i = t.index('<div id="u1ring"'); depth = 0
for m in re.finditer(r'<div\b|</div>', t[i:]):
    depth += 1 if m.group(0).startswith('<div') else -1
    if depth == 0:
        t = t[:i] + t[i + m.end():]; break
t = re.sub(r'\n\s*tl\.[^\n]*#(ring6|kgtag)[^\n]*', '', t)
assert 'ring6' not in t and 'kgtag' not in t
# remap times
t = re.sub(r'data-start="([0-9.]+)" data-duration="([0-9.]+)"',
           lambda m: f'data-start="{f(float(m.group(1))):.2f}" data-duration="{f(float(m.group(1)) + float(m.group(2))) - f(float(m.group(1))):.2f}"', t)
s0 = t.index('<script>')
t = t[:s0] + re.sub(r', ([0-9]+\.[0-9]+|[0-9]+)\);', lambda m: f', {f(float(m.group(1))):.2f});', t[s0:]) + ''
t = re.sub(r'(<audio id="vo" src="assets/vo.wav" data-start=")[0-9.]+(" data-duration=")[0-9.]+"', r'\g<1>0\g<2>52.85"', t)
t = re.sub(r'(<div id="hook" class="g clip" data-start="0.00" data-duration=")[0-9.]+"', r'\g<1>4.15"', t)
# ---- 3. new text sizes
t = t.replace('style="font-size:150px;color:var(--lime)">200 KALORI', 'style="font-size:100px;color:var(--lime)">200 KALORI')
t = t.replace('id="h2" style="font-size:70px">15 MINIT STEPPER', 'id="h2" style="font-size:47px">15 MINIT STEPPER')
t = t.replace('font-size: 60px; line-height: 1.05;', 'font-size: 40px; line-height: 1.05;')
t = t.replace('-webkit-text-stroke: 5px #000; paint-order: stroke fill;\n                text-shadow: 0 6px 0', '-webkit-text-stroke: 3.5px #000; paint-order: stroke fill;\n                text-shadow: 0 4px 0')
for need in ['font-size:100px;color:var(--lime)">200 KALORI', 'font-size:47px">15 MINIT STEPPER', 'font-size: 40px; line-height: 1.05;', 'stroke: 3.5px']:
    assert need in t, need
t = re.sub(r'(font-size: ?)(\d+)px', lambda m: f'{m.group(1)}{min(int(m.group(2)), 100)}px', t)
assert not [x for x in re.findall(r'font-size: ?(\d+)px', t) if int(x) > 100]
b = t[t.index('<body>'):]
assert len(re.findall(r'<div\b', b)) == b.count('</div>')
open(S + '/template15.html', 'w').write(t)

# ---- 4. builder
src = open(S + '/build11.py').read()
def R(o, n):
    global src
    assert o in src, o[:60]; src = src.replace(o, n, 1)
R('TOTAL = 46.3', 'TOTAL = 53.2')
src, n = re.subn(r'CUTS = \[.*?\n\]\nMUTED', '''CUTS = [
    (0.00, 4.15, "f13", 4.0),   # hook: 200 kalori (close-up kasut atas stepper)
    (4.15, 10.60, "f17", 1.0),  # briskwalk 30 minit / total body (close-up lutut)
    (10.60, 16.55, "f8", 5.0),  # otot lengan, perut, kaki + berpeluh (trek luar, tali)
    (16.55, 20.30, "f3", 1.0),  # trim gelebeh dalam rumah (kettlebell)
    (20.30, 26.55, "f10", 3.0), # badan besar, tampung 100kg+, selamat (bilik, tali)
    (26.55, 29.90, "f5", 17.0), # compact & ringan: angkat stepper keluar kotak (muted)
    (29.90, 32.40, "f19", 7.0), # depan TV / dalam bilik
    (32.40, 37.95, "f5", 50.9), # digital counter: pasang bateri (muted)
    (37.95, 44.85, "f6", 8.0),  # 400,000 terjual / viral / dulu mahal (trek luar; muted: muzik)
    (44.85, TOTAL, "f9", 0.5),  # lebih RM100 -> murah / rugi / CTA beg kuning (tali)
]
MUTED''', src, flags=re.S); assert n == 1
R('FIX = {"gelebi": "gelebeh", "beresuap": "briskwalk", "latih": "dilatih", "virus": "viral", "bekon": "beg kuning"}', 'FIX = {}')
R('HOOK_END = 3.6', 'HOOK_END = 4.15')
R('MUTED = {"f5"}', 'MUTED = {"f5", "f6"}')
# GFX: remap Task 11 list, drop feedback, price text
g0 = re.search(r'GFX = \[.*?\n\]', src, re.S)
items = re.findall(r'\(([0-9.]+), ([0-9.]+), "([^"]+)"\)', g0.group(0))
new = []
for a, b_, txt in items:
    if 'FEEDBACK' in txt: continue
    txt = txt.replace('DULU BERATUS RINGGIT', 'DULU HARGA LEBIH RM100').replace('15 MINIT STEPPER SETARA 30 MINIT BRISKWALK BIASA', '15 MINIT STEPPER MACAM 30 MINIT BRISKWALK') \
             .replace('TAMPUNG LEBIH 100KG', 'TAMPUNG BERAT LEBIH DARIPADA 100KG').replace('COMPACT RINGAN', 'SAIZ COMPACT RINGAN') \
             .replace('TRIM GELEBEH KAT RUMAH', 'TRIM GELEBEH DALAM RUMAH').replace('PILIH WARNA BEG KUNING BAWAH', 'PILIH WARNA BEG KUNING BAWAH SEKARANG') \
             .replace('ADA DIGITAL COUNTER SEKALI KALORI STEPS TRACK JUMLAH', 'DATANG SEKALI DIGITAL COUNTER KALORI STEPS TRACK JUMLAH MUDAH')
    new.append(f'({f(float(a)):.2f}, {f(float(b_)):.2f}, "{txt}")')
src = src[:g0.start()] + 'GFX = [\n    ' + ', '.join(new) + ',\n]' + src[g0.end():]
s1 = re.search(r'SFX = \[  # \(time, file, volume\)\n(.*?)\n\]', src, re.S)
sfx = re.sub(r'\(([0-9.]+), "', lambda m: f'({f(float(m.group(1))):.2f}, "', s1.group(1))
sfx = re.sub(r'\(42\.\d\d, "pop", 0\.4\), \(42\.\d\d, "ding", 0\.25\),', '', sfx)  # feedback sfx
src = src[:s1.start(1)] + sfx + src[s1.end(1):]
open(S + '/build15.py', 'w').write(src)
print('ok')
