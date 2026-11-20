"""Task 10: 3 Kesilapan Guna V-Stepper. Built from Task 9 template (USP + CTA reused, same times)."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t = open(S + '/template9.html').read()

t = t.replace('    </style>', '''      .num.red { background: var(--red); }
      #warn { width: 230px; height: 200px; display: block; margin: 0 auto 10px; }
      #foot { width: 420px; height: 300px; }
      #gauge { width: 470px; height: 290px; }
      #week { display: flex; justify-content: center; gap: 12px; margin-top: 28px; }
      .day { width: 118px; text-align: center; background: rgba(0,0,0,0.78); border: 5px solid #000; border-radius: 18px; padding: 8px 0 6px; }
      .day i { display: block; font-style: normal; font-family: var(--font-ui); font-weight: 900; font-size: 24px; color: #9aa; }
      .day b { display: block; font-weight: 400; font-size: 66px; line-height: 1.1; }
      .day.ok b { color: var(--lime); } .day.no b { color: var(--red); }
      #prog { width: 760px; height: 46px; margin: 26px auto 0; background: rgba(0,0,0,0.75); border: 5px solid #000; border-radius: 23px; overflow: hidden; }
      #prog i { display: block; height: 100%; width: 100%; background: linear-gradient(90deg, var(--red), var(--yellow)); transform-origin: 0 50%; }
      .fix { margin-top: 22px; }
    </style>''', 1)

CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
WARNI = '<svg viewBox="0 0 64 64"><path d="M32 5 L61 57 H3 Z" fill="#ffd400" stroke="#000" stroke-width="5" stroke-linejoin="round"/><path d="M32 24 V40" stroke="#000" stroke-width="7" stroke-linecap="round"/><circle cx="32" cy="49" r="4" fill="#000"/></svg>'
WARN = '<svg id="warn" viewBox="0 0 230 200"><path d="M115 10 L222 192 H8 Z" fill="#ff3b30" stroke="#000" stroke-width="10" stroke-linejoin="round"/><path d="M115 70 V130" stroke="#fff" stroke-width="22" stroke-linecap="round"/><circle cx="115" cy="162" r="13" fill="#fff"/></svg>'
FOOT = '''<svg id="foot" class="ill" viewBox="0 0 280 200">
  <g id="fripple" fill="none" stroke="#ff3b30" stroke-width="7" stroke-linecap="round"><path d="M60 190 Q110 210 160 190"/><path d="M40 200 Q110 228 180 200" opacity="0.7"/></g>
  <path d="M70 180 C40 175 30 130 45 95 C60 60 100 55 115 75 C135 100 150 120 190 128 C230 136 250 150 245 168 C240 186 200 186 160 182 Z" fill="#ffb07c" stroke="#000" stroke-width="8" stroke-linejoin="round"/>
  <g fill="#ffb07c" stroke="#000" stroke-width="6"><circle cx="232" cy="140" r="12"/><circle cx="214" cy="128" r="10"/><circle cx="197" cy="122" r="9"/><circle cx="181" cy="118" r="8"/></g>
  <ellipse id="heelhit" cx="78" cy="168" rx="34" ry="14" fill="#ff3b30" opacity="0.85"/>
  <g id="xmark" stroke="#ff3b30" stroke-width="20" stroke-linecap="round"><path d="M200 18 L262 80"/><path d="M262 18 L200 80"/></g>
</svg>'''
GAUGE = '''<svg id="gauge" class="ill" viewBox="0 0 470 290">
  <path d="M45 260 A190 190 0 0 1 145 95" fill="none" stroke="#c6ff00" stroke-width="40"/>
  <path d="M150 92 A190 190 0 0 1 320 92" fill="none" stroke="#ffd400" stroke-width="40"/>
  <path d="M325 95 A190 190 0 0 1 425 260" fill="none" stroke="#ff3b30" stroke-width="40"/>
  <path d="M45 260 A190 190 0 0 1 425 260" fill="none" stroke="#000" stroke-width="6"/>
  <g id="needle" style="transform-origin:235px 260px"><path d="M229 260 L235 92 L241 260 Z" fill="#fff" stroke="#000" stroke-width="5"/></g>
  <circle cx="235" cy="260" r="22" fill="#fff" stroke="#000" stroke-width="7"/>
  <text x="400" y="80" text-anchor="middle" font-family="Anton" font-size="44" fill="#ff3b30" stroke="#000" stroke-width="5" paint-order="stroke">LAJU!</text>
</svg>'''
DAYS = [("ISN", "✓", "ok"), ("SEL", "✗", "no"), ("RAB", "✗", "no"), ("KHA", "✓", "ok"), ("JUM", "✗", "no"), ("SAB", "✗", "no"), ("AHD", "✓", "ok")]
WEEK = ''.join(f'<div class="day {c}" id="d{i}"><i>{d}</i><b>{m}</b></div>' for i, (d, m, c) in enumerate(DAYS))

NEW_HTML = f'''      <!-- HOOK -->
      <div id="hook" class="g clip" data-start="0" data-duration="3.5" data-track-index="10" style="top:330px">
        {WARN}
        <span class="big" id="h1" style="font-size:200px;color:var(--yellow)">3 KESILAPAN</span>
        <span class="blk pink" id="h2">GUNA V-STEPPER</span>
      </div>

      <!-- KESILAPAN 1 -->
      <div id="m1" class="g clip" data-start="3.55" data-duration="6.45" data-track-index="10" style="top:230px">
        <div class="tipttl"><div class="num red" id="m1n">1</div><span class="blk" id="m1t">TAK PAKAI KASUT</span></div>
        {FOOT}
        <span class="mid" id="m1a" style="margin-top:14px;font-size:62px">IMPAK BERTERUSAN PADA TAPAK KAKI</span>
        <div style="margin-top:18px"><span class="pill" id="m1b" style="background:var(--red);color:#fff">{WARNI}RISIKO INJURY MENINGKAT</span></div>
        <div class="fix"><span class="pill lime" id="m1f">{CHECK("#000","#c6ff00")}PAKAI KASUT</span></div>
      </div>

      <!-- KESILAPAN 2 -->
      <div id="m2" class="g clip" data-start="10.05" data-duration="6.95" data-track-index="10" style="top:230px">
        <div class="tipttl"><div class="num red" id="m2n">2</div><span class="blk" id="m2t">TERLALU LAJU</span></div>
        {GAUGE}
        <span class="blk pink" id="m2a" style="font-size:84px">HILANG KAWALAN</span>
        <span class="mid" id="m2b" style="margin-top:18px">BADAN JADI TAK STABIL</span>
        <div class="fix"><span class="pill lime" id="m2f">{CHECK("#000","#c6ff00")}KAWAL RENTAK</span></div>
      </div>

      <!-- KESILAPAN 3 -->
      <div id="m3" class="g clip" data-start="17.05" data-duration="6.45" data-track-index="10" style="top:230px">
        <div class="tipttl"><div class="num red" id="m3n">3</div><span class="blk" id="m3t">TAK KONSISTEN</span></div>
        <div id="week">{WEEK}</div>
        <div id="prog"><i id="progi"></i></div>
        <div style="margin-top:22px"><span class="blk pink" id="m3a" style="font-size:84px">LAMBAT NAMPAK HASIL</span></div>
        <div class="fix"><span class="pill lime" id="m3f">{CHECK("#000","#c6ff00")}BUAT SETIAP HARI</span></div>
      </div>

'''
a = t.index('      <!-- HOOK -->'); b = t.index('      <!-- USP -->')
t = t[:a] + NEW_HTML + t[b:]

old = '<span class="mid" id="c1a">NAK KECILKAN</span>'
assert old in t
t = t.replace(old, '<div class="cara" id="c1z">AZAM TAHUN BARU</div>\n        <span class="mid" id="c1a">NAK KECILKAN</span>')

NEW_JS = '''      // hook
      tl.fromTo("#warn", { scale: 0, rotation: -30 }, { scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, 0.0);
      tl.to("#warn", { scale: 1.1, duration: 0.2, yoyo: true, repeat: 7, ease: "sine.inOut" }, 0.5);
      tl.fromTo("#h1", { scale: 3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }, 0.3);
      tl.to("#root", { keyframes: { x: [0, -14, 12, -8, 6, 0] }, duration: 0.25 }, 0.55);
      tl.fromTo("#h2", { scale: 0, rotation: -20 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 1.0);

      // kesilapan 1
      tl.fromTo("#m1n", { scale: 0, rotation: -180 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 3.6);
      tl.fromTo("#m1t", { x: 1100 }, { x: 0, duration: 0.3, ease: "power4.out" }, 3.9);
      tl.fromTo("#foot", { y: -400 }, { y: 0, duration: 0.45, ease: "bounce.out" }, 4.3);
      tl.fromTo("#fripple path", { scale: 0.4, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1.2, opacity: 1, duration: 0.5, stagger: 0.12, repeat: 5, ease: "power1.out" }, 4.75);
      tl.fromTo("#heelhit", { opacity: 0.2 }, { opacity: 0.9, duration: 0.25, yoyo: true, repeat: 9 }, 4.75);
      tl.fromTo("#xmark", { scale: 0, transformOrigin: "231px 49px" }, { scale: 1, duration: 0.3, ease: "back.out(3)" }, 5.0);
      tl.fromTo("#m1a", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 5.5);
      tl.fromTo("#m1b", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(2.5)" }, 6.3);
      tl.fromTo("#m1f", { x: -1100 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, 8.0);

      // kesilapan 2
      tl.fromTo("#m2n", { scale: 0, rotation: -180 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 10.1);
      tl.fromTo("#m2t", { x: 1100 }, { x: 0, duration: 0.3, ease: "power4.out" }, 10.4);
      tl.fromTo("#gauge", { scale: 0 }, { scale: 1, duration: 0.35, ease: "back.out(2)" }, 10.8);
      tl.fromTo("#needle", { rotation: -80 }, { rotation: 72, duration: 1.0, ease: "power2.in" }, 11.1);
      tl.to("#needle", { rotation: 62, duration: 0.08, yoyo: true, repeat: 15, ease: "none" }, 12.1);
      tl.fromTo("#m2a", { scale: 0, rotation: 15 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 12.2);
      tl.fromTo("#m2b", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 13.0);
      tl.to("#m2b", { keyframes: { rotation: [0, -4, 4, -3, 3, 0], x: [0, -12, 12, -8, 8, 0] }, duration: 0.6, repeat: 2 }, 13.3);
      tl.fromTo("#m2f", { x: -1100 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, 15.0);

      // kesilapan 3
      tl.fromTo("#m3n", { scale: 0, rotation: -180 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 17.1);
      tl.fromTo("#m3t", { x: 1100 }, { x: 0, duration: 0.3, ease: "power4.out" }, 17.4);
      tl.fromTo(["#d0","#d1","#d2","#d3","#d4","#d5","#d6"], { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2.5)", stagger: 0.18 }, 17.9);
      tl.fromTo("#progi", { scaleX: 0 }, { scaleX: 0.22, duration: 2.4, ease: "power1.out" }, 19.2);
      tl.fromTo("#m3a", { scale: 0, rotation: 15 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 19.6);
      tl.fromTo("#m3f", { x: -1100 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, 21.2);

'''
a = t.index('      // hook'); b = t.index('      // usp counter')
t = t[:a] + NEW_JS + t[b:]
t = t.replace('      tl.fromTo("#c1a", { y: -60, opacity: 0 }', '      tl.fromTo("#c1z", { y: -40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 31.05);\n      tl.fromTo("#c1a", { y: -60, opacity: 0 }', 1)
assert '#c1z' in t.split('<script>')[1]

body = t[t.index('<body>'):]
o, c = len(re.findall(r'<div\b', body)), body.count('</div>')
print('div open', o, 'close', c); assert o == c
for need in ['id="hook"', 'id="m1"', 'id="m2"', 'id="m3"', 'id="usp"', 'id="u1ring"', 'id="c1"', 'AZAM TAHUN BARU', 'id="cta"', 'id="arrows"', 'KAT BEG KUNING']:
    assert need in t, need
open(S + '/template10.html', 'w').write(t)

bsrc = open(S + '/build9.py').read()
bsrc, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start) -- shots not used in earlier videos
    (0.0, 3.5, "f3", 1.0),     # HOOK: kaki + kettlebell atas stepper
    (3.5, 10.0, "f12", 0.0),   # K1: tak pakai kasut (bilik gelap, kasut putih)
    (10.0, 13.5, "f11", 2.0),  # K2: terlalu laju (bilik gelap, tali)
    (13.5, 17.0, "f6", 6.0),   # K2 (sambung): trek luar (muted: bunyi bermuzik)
    (17.0, 20.5, "f8", 3.0),   # K3: tak konsisten (trek luar, topi)
    (20.5, 23.5, "f10", 4.0),  # K3 (sambung): bilik gelap
    (23.5, 27.0, "f5", 54.0),  # USP: skrin counter dipegang (muted: ada muzik)
    (27.0, 31.0, "f16", 4.0),  # USP: timbang stepper 5.90kg (bahagian lain klip)
    (31.0, 34.0, "f14", 6.0),  # CTA: azam tahun baru (ruang tamu, baju merah)
    (34.0, TOTAL, "f7", 11.0), # CTA: luar, tali rintangan diangkat
]
MUTED = {"f5", "f6"}''', bsrc, flags=re.S); assert n == 1
bsrc, n = re.subn(r'SFX = \[\n.*?\n\]', '''SFX = [
    (0.00, "whoosh", 0.35), (0.05, "zap", 0.4), (0.30, "impact", 0.55), (1.00, "pop", 0.4),
    (3.50, "whoosh", 0.35), (3.60, "impact", 0.4), (4.75, "impact", 0.35), (5.00, "zap", 0.35), (6.30, "pop", 0.4), (8.00, "ding", 0.3),
    (10.00, "whoosh", 0.35), (10.10, "impact", 0.4), (11.10, "riser", 0.3), (12.20, "zap", 0.4), (13.30, "swoosh", 0.35), (15.00, "ding", 0.3),
    (17.00, "whoosh", 0.35), (17.10, "impact", 0.4), (17.90, "pop", 0.3), (18.26, "pop", 0.3), (18.62, "pop", 0.3), (18.98, "pop", 0.3), (19.60, "zap", 0.35), (21.20, "ding", 0.3),
    (23.50, "whoosh", 0.35), (23.85, "ding", 0.3),
    (27.00, "whoosh", 0.35), (27.20, "pop", 0.4), (27.80, "ding", 0.3), (28.55, "swoosh", 0.35),
    (31.00, "whoosh", 0.35), (31.45, "impact", 0.45),
    (34.00, "whoosh", 0.35), (34.10, "pop", 0.4), (34.80, "ding", 0.3), (35.00, "pop", 0.4),
]''', bsrc, flags=re.S); assert n == 1
open(S + '/build10.py', 'w').write(bsrc)
print('ok')
