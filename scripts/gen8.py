"""Generate template8.html + build8.py for Task 8 (15 minit) from Task 7 files."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t = open(S + '/template7_15.html').read()   # Task 7 template with table already x1.5
t = t.replace('>10 MINIT<', '>15 MINIT<').replace('STEPPER 10 MINIT', 'STEPPER 15 MINIT') \
     .replace('*Anggaran untuk 10 minit latihan', '*Anggaran untuk 15 minit latihan')
assert t.count('15 MINIT') >= 3
# hook stopwatch: quarter turn for 15 min
t = t.replace('{ rotation: 360, duration: 1.6', '{ rotation: 90, duration: 1.6') \
     .replace('{ attr: { "stroke-dashoffset": 0 }, duration: 1.6', '{ attr: { "stroke-dashoffset": 188 }, duration: 1.6')

t = t.replace('    </style>', '''      #muscles { left: 50px; right: 50px; top: 400px; background: rgba(10,10,12,0.86); border: 6px solid #000; border-radius: 34px; box-shadow: 0 16px 0 #000; padding: 22px 20px 26px; }
      #muscles .figs { display: flex; justify-content: space-around; }
      #muscles .fig { text-align: center; font-family: var(--font-ui); font-weight: 900; font-size: 28px; letter-spacing: 0.12em; color: #9aa; }
      #muscles .fig svg { width: 300px; height: 520px; display: block; }
      #mpills { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin-top: 18px; }
      #mpills .pill { font-size: 36px; padding: 12px 24px; }
    </style>''', 1)

BASE = '''<g fill="#3d3d44" stroke="#000" stroke-width="5" stroke-linejoin="round">
  <circle cx="100" cy="40" r="28"/><rect x="88" y="64" width="24" height="18"/>
  <path d="M55 85 Q100 74 145 85 L140 215 Q100 230 60 215 Z"/>
  <path d="M55 90 L32 100 L20 210 L36 214 L52 122 Z"/><path d="M145 90 L168 100 L180 210 L164 214 L148 122 Z"/>
  <path d="M20 210 L14 292 L30 294 L36 214 Z"/><path d="M180 210 L186 292 L170 294 L164 214 Z"/>
  <path d="M60 215 Q100 232 140 215 L142 252 L58 252 Z"/>
  <path d="M58 252 L98 252 L95 340 L92 412 L68 412 L63 340 Z"/><path d="M102 252 L142 252 L137 340 L132 412 L108 412 L105 340 Z"/>
</g>'''
FRONT = f'''<svg viewBox="0 0 200 420">{BASE}<g class="mf" fill="#ff2e7e" stroke="#000" stroke-width="3">
  <ellipse cx="54" cy="99" rx="15" ry="13"/><ellipse cx="146" cy="99" rx="15" ry="13"/>
  <ellipse cx="38" cy="152" rx="9" ry="26" transform="rotate(8 38 152)"/><ellipse cx="162" cy="152" rx="9" ry="26" transform="rotate(-8 162 152)"/>
  <rect x="80" y="112" width="40" height="92" rx="12"/><path d="M80 140 H120 M80 168 H120 M100 112 V204" stroke="#000" stroke-width="3" fill="none"/>
  <ellipse cx="80" cy="292" rx="15" ry="38"/><ellipse cx="121" cy="292" rx="15" ry="38"/></g></svg>'''
BACK = f'''<svg viewBox="0 0 200 420">{BASE}<g class="mb" fill="#c6ff00" stroke="#000" stroke-width="3">
  <ellipse cx="38" cy="152" rx="9" ry="26" transform="rotate(8 38 152)"/><ellipse cx="162" cy="152" rx="9" ry="26" transform="rotate(-8 162 152)"/>
  <ellipse cx="81" cy="238" rx="19" ry="16"/><ellipse cx="119" cy="238" rx="19" ry="16"/>
  <ellipse cx="80" cy="298" rx="14" ry="32"/><ellipse cx="121" cy="298" rx="14" ry="32"/>
  <ellipse cx="79" cy="370" rx="10" ry="26"/><ellipse cx="120" cy="370" rx="10" ry="26"/></g></svg>'''
CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
pills = [("lime", "PUNGGUNG"), ("lime", "PEHA"), ("lime", "BETIS"), ("pink", "CORE"), ("pink", "LENGAN &amp; BAHU")]
ph = ''.join(f'<span class="pill {c}" id="mp{i}">{CHECK("#000","#c6ff00") if c=="lime" else CHECK("#c6ff00","#000")}{n}</span>' for i, (c, n) in enumerate(pills))
MUS = f'''
      <!-- EDU: otot yang bekerja -->
      <div id="mtitle" class="g clip" data-start="15.05" data-duration="6.45" data-track-index="10" style="top:250px">
        <span class="blk pink" id="mt1" style="font-size:84px">OTOT YANG BEKERJA</span>
      </div>
      <div id="muscles" class="g clip" data-start="15.3" data-duration="6.2" data-track-index="11">
        <div class="figs"><div class="fig" id="fg1">{FRONT}DEPAN</div><div class="fig" id="fg2">{BACK}BELAKANG</div></div>
        <div id="mpills">{ph}</div>
      </div>
'''
assert '      <!-- USP -->' in t
t = t.replace('      <!-- USP -->', MUS + '      <!-- USP -->', 1)
t = t.replace('<div id="usp" class="g clip" data-start="15.05" data-duration="3.95"', '<div id="usp" class="g clip" data-start="21.55" data-duration="3.45"')
t, n = re.subn(r'      <div id="track" class="g clip stack".*?\n      </div>\n', '''      <div id="u1" class="g clip" data-start="25.05" data-duration="3.95" data-track-index="10" style="top:230px">
        <div class="cara" id="u1c">RINGAN GILA</div>
        <span class="mid" id="u1a">BERAT TAK SAMPAI 6KG</span>
      </div>
      <div id="u1ring" class="g clip" data-start="25.6" data-duration="3.4" data-track-index="11" style="left:0;top:0;width:1080px;height:1920px">
        <svg width="1080" height="1920" style="position:absolute;inset:0"><circle id="ring6" cx="735" cy="770" r="125" fill="none" stroke="#c6ff00" stroke-width="14"/></svg>
        <span class="blk" id="kgtag" style="position:absolute;left:600px;top:560px;font-size:90px">5.9KG</span>
      </div>
      <div id="u1low" class="g clip" data-start="26.5" data-duration="2.5" data-track-index="10" style="top:1330px">
        <span class="blk pink" id="u1b" style="font-size:72px">SENANG ALIH KE MANA-MANA</span>
      </div>
''', t, count=1, flags=re.S)
assert n == 1
old_c1 = '<div id="c1" class="g clip" data-start="22.55" data-duration="3.45" data-track-index="10" style="top:230px">'
assert old_c1 in t
t = t.replace(old_c1, '<div id="c1" class="g clip" data-start="29.05" data-duration="2.95" data-track-index="10" style="top:330px">')
t, n = re.subn(r'<div id="cal">.*?2026</div></div></div>\s*', '', t, count=1, flags=re.S); assert n == 1
old = '<span class="mid" id="c1a" style="margin-top:34px">NAK BADAN FIT</span>\n        <span class="blk" id="c1b">2027?</span>'
assert old in t
t = t.replace(old, '<span class="mid" id="c1a">NAK KECILKAN</span>\n        <span class="blk pink" id="c1b">GELEBEH?</span>')
for o, nw in [('<div id="cta" class="g clip" data-start="26.05" data-duration="3.95"', '<div id="cta" class="g clip" data-start="32.05" data-duration="3.95"'),
              ('<div id="arrows" class="g clip" data-start="27.0" data-duration="3.0"', '<div id="arrows" class="g clip" data-start="33.0" data-duration="3.0"')]:
    assert o in t; t = t.replace(o, nw)
js_new = '''      // otot
      tl.fromTo("#mt1", { scale: 0, rotation: -15 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 15.1);
      tl.fromTo("#muscles", { y: 400, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }, 15.3);
      tl.fromTo("#fg1 .mf > *", { opacity: 0 }, { opacity: 1, duration: 0.2, stagger: 0.12 }, 15.8);
      tl.fromTo("#fg2 .mb > *", { opacity: 0 }, { opacity: 1, duration: 0.2, stagger: 0.12 }, 16.4);
      tl.to(["#fg1 .mf", "#fg2 .mb"], { opacity: 0.55, duration: 0.3, yoyo: true, repeat: 7, ease: "sine.inOut" }, 17.6);
      tl.fromTo(["#mp0", "#mp1", "#mp2", "#mp3", "#mp4"], { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.6 }, 17.4);

      // usp counter
      tl.fromTo("#u0", { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 21.6);
      tl.fromTo("#u1", { scale: 0.4, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }, 21.85);
      // usp weight
      tl.fromTo("#u1c", { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 25.1);
      tl.fromTo("#u1a", { scale: 0.4, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }, 25.25);
      tl.fromTo("#ring6", { scale: 2.5, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }, 25.6);
      tl.to("#ring6", { scale: 1.08, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 50%" }, 26.0);
      tl.fromTo("#kgtag", { scale: 0, rotation: 20 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.5)" }, 25.8);
      tl.fromTo("#u1b", { x: 1100 }, { x: 0, duration: 0.3, ease: "power4.out" }, 26.55);

      // cta
      tl.fromTo("#c1a", { y: -60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 29.1);
      tl.fromTo("#c1b", { scale: 0, rotation: 15 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 29.45);
      tl.to("#root", { keyframes: { y: [0, 12, -10, 6, 0] }, duration: 0.22 }, 29.6);
      tl.fromTo("#ctacard", { scale: 0, rotation: -8 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 32.1);
      tl.fromTo("#ctabag", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }, 32.8);
      tl.to("#ctabag", { scale: 1.08, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut" }, 33.2);
      tl.fromTo("#arrows svg", { y: -30, opacity: 0 }, { y: 20, opacity: 1, duration: 0.4, stagger: 0.12, repeat: 4, yoyo: true, ease: "sine.inOut" }, 33.0);

'''
t, n = re.subn(r'      // usp\n.*?\n      window.__timelines', lambda m: js_new + '      window.__timelines', t, count=1, flags=re.S)
assert n == 1
body = t[t.index('<body>'):]
o, c = len(re.findall(r'<div\b', body)), body.count('</div>')
print('div open', o, 'close', c); assert o == c
for need in ['id="mtitle"', 'id="muscles"', 'id="usp"', 'id="u1ring"', 'id="c1"', 'id="cta"', 'id="arrows"', 'id="table"', 'id="hook"']:
    assert need in t, need
open(S + '/template8.html', 'w').write(t)

b = open(S + '/build7.py').read()
b = b.replace('TOTAL = 30.0', 'TOTAL = 36.0')
b, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f13", 2.0),    # HOOK: 15 minit latihan stepper
    (3.5, 6.5, "f18", 5.0),    # EDU: kalori ikut berat badan
    (6.5, 10.8, "f2", 2.0),    # EDU: jadual kalori
    (10.8, 15.0, "f9", 0.0),   # EDU: jadual kalori (sambung)
    (15.0, 18.2, "f17", 3.0),  # EDU: otot kaki (close-up)
    (18.2, 21.5, "f4", 0.0),   # EDU: otot lengan/bahu (tali rintangan)
    (21.5, 25.0, "f5", 50.9),  # USP: multifunction counter (muted: ada muzik)
    (25.0, 29.0, "f16", 2.9),  # USP: timbang stepper 5.90kg
    (29.0, 32.0, "f15", 0.5),  # CTA: nak kecilkan gelebeh?
    (32.0, TOTAL, "f1", 8.0),  # CTA: grab stepper kat beg kuning
]
MUTED = {"f5"}''', b, flags=re.S); assert n == 1
b, n = re.subn(r'SFX = \[\n.*?\n\]', '''SFX = [
    (0.00, "whoosh", 0.35), (0.20, "tick", 0.5), (0.30, "impact", 0.55), (0.95, "pop", 0.4), (1.80, "swoosh", 0.35),
    (3.50, "whoosh", 0.35), (3.85, "impact", 0.4), (4.40, "pop", 0.4),
    (6.50, "whoosh", 0.35), (6.80, "pop", 0.4),
    (7.20, "pop", 0.35), (8.10, "pop", 0.35), (9.00, "pop", 0.35), (9.90, "pop", 0.35), (10.80, "pop", 0.35), (11.70, "ding", 0.3),
    (15.00, "whoosh", 0.35), (15.10, "impact", 0.4), (15.80, "riser", 0.25),
    (17.40, "pop", 0.35), (18.00, "pop", 0.35), (18.60, "pop", 0.35), (19.20, "pop", 0.35), (19.80, "pop", 0.35),
    (21.50, "whoosh", 0.35), (21.85, "ding", 0.3),
    (25.00, "whoosh", 0.35), (25.20, "pop", 0.4), (25.80, "ding", 0.3), (26.55, "swoosh", 0.35),
    (29.00, "whoosh", 0.35), (29.45, "impact", 0.45),
    (32.00, "whoosh", 0.35), (32.10, "pop", 0.4), (32.80, "ding", 0.3), (33.00, "pop", 0.4),
]''', b, flags=re.S); assert n == 1
open(S + '/build8.py', 'w').write(b)
print('ok')
