"""Task 9: 3 Tips Latihan V-Stepper. Built from Task 8 template (USP + CTA reused, shifted +2s)."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t = open(S + '/template8.html').read()
SHIFT = 2.0

t = t.replace('    </style>', '''      .tipttl { display: flex; align-items: center; justify-content: center; gap: 18px; }
      .tipttl .num { margin-bottom: 0; width: 130px; height: 130px; font-size: 86px; }
      .ill { display: block; margin: 18px auto 0; }
      #shoe { width: 560px; height: 300px; }
      #steps3 { display: flex; justify-content: center; align-items: flex-end; gap: 26px; height: 430px; margin-top: 26px; }
      .col { width: 230px; text-align: center; }
      .col .bar { border: 6px solid #000; border-radius: 22px 22px 8px 8px; box-shadow: 0 12px 0 #000; transform-origin: 50% 100%;
                  display: flex; flex-direction: column; justify-content: flex-start; padding-top: 14px; }
      .col .bar b { font-weight: 400; font-size: 76px; line-height: 1; color: #000; }
      .col .bar i { font-style: normal; font-family: var(--font-ui); font-weight: 900; font-size: 26px; color: #000; }
      .col .wk { font-family: var(--font-ui); font-weight: 900; font-size: 30px; letter-spacing: 0.06em; color: #fff; margin-top: 14px;
                 background: rgba(0,0,0,0.75); border-radius: 999px; padding: 6px 0; }
      #db { width: 520px; height: 230px; }
    </style>''', 1)

CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SHOE = '''<svg id="shoe" class="ill" viewBox="0 0 280 150">
  <g id="ripples" fill="none" stroke="#ff3b30" stroke-width="6" stroke-linecap="round">
    <path id="rp1" d="M18 136 Q48 150 78 136"/><path id="rp2" d="M8 146 Q48 166 88 146" opacity="0.7"/></g>
  <path d="M12 118 H246 Q262 118 258 102 L250 96 H18 Q8 100 12 118 Z" fill="#fff" stroke="#000" stroke-width="7" stroke-linejoin="round"/>
  <path d="M18 96 Q16 58 52 46 L108 30 Q128 62 172 66 L226 74 Q254 80 250 96 Z" fill="#c6ff00" stroke="#000" stroke-width="7" stroke-linejoin="round"/>
  <path d="M112 40 L104 58 M126 50 L118 66 M140 56 L134 70" stroke="#000" stroke-width="6" stroke-linecap="round"/>
  <path id="heel" d="M14 118 H74 V96 H18 Q8 100 14 118 Z" fill="#ff2e7e" stroke="#000" stroke-width="6" stroke-linejoin="round"/>
</svg>'''
DUMB = '''<svg id="db" class="ill" viewBox="0 0 260 115">
  <rect x="70" y="48" width="120" height="20" rx="8" fill="#888" stroke="#000" stroke-width="6"/>
  <rect x="16" y="14" width="58" height="88" rx="18" fill="#ff2e7e" stroke="#000" stroke-width="7"/>
  <rect x="186" y="14" width="58" height="88" rx="18" fill="#ff2e7e" stroke="#000" stroke-width="7"/>
  <text id="dbkg" x="130" y="42" text-anchor="middle" font-family="Anton" font-size="36" fill="#fff" stroke="#000" stroke-width="6" paint-order="stroke">1KG</text>
</svg>'''
cols = [("MINGGU 1", "10", "MINIT", 180, "var(--lime)"), ("MINGGU 2", "15", "MINIT", 270, "var(--yellow)"), ("MINGGU 3+", "↑", "TAMBAH LAGI", 360, "var(--pink)")]
COLS = ''.join(f'<div class="col" id="col{i}"><div class="bar" id="bar{i}" style="height:{h}px;background:{c}"><b>{n}</b><i>{u}</i></div><div class="wk">{w}</div></div>'
               for i, (w, n, u, h, c) in enumerate(cols))

NEW_HTML = f'''      <!-- HOOK -->
      <div id="hook" class="g clip" data-start="0" data-duration="3.5" data-track-index="10" style="top:400px">
        <span class="big" id="h1" style="font-size:250px;color:var(--lime)">3 TIPS</span>
        <span class="blk" id="h2">LATIHAN V-STEPPER</span>
      </div>

      <!-- TIP 1 -->
      <div id="tip1" class="g clip" data-start="3.55" data-duration="6.45" data-track-index="10" style="top:240px">
        <div class="tipttl"><div class="num" id="t1n">1</div><span class="blk" id="t1t">PAKAI KASUT</span></div>
        {SHOE}
        <span class="mid" id="t1a" style="margin-top:20px">ELAK IMPAK BERTERUSAN</span>
        <span class="blk pink" id="t1b" style="font-size:80px">PADA TUMIT</span>
      </div>

      <!-- TIP 2 -->
      <div id="tip2" class="g clip" data-start="10.05" data-duration="6.95" data-track-index="10" style="top:240px">
        <div class="tipttl"><div class="num" id="t2n">2</div><span class="blk" id="t2t" style="font-size:78px">KONSISTEN SETIAP HARI</span></div>
        <div id="steps3">{COLS}</div>
      </div>

      <!-- TIP 3 -->
      <div id="tip3" class="g clip" data-start="17.05" data-duration="6.45" data-track-index="10" style="top:240px">
        <div class="tipttl"><div class="num" id="t3n">3</div><span class="blk" id="t3t" style="font-size:66px">GABUNG LATIHAN UPPER BODY</span></div>
        {DUMB}
        <span class="mid" id="t3a">MULA DENGAN DUMBBELL 1KG</span>
        <div style="margin-top:20px"><span class="pill yellow" id="t3b">{CHECK("#000","#ffd400")}TAMBAH BERAT SECARA BERPERINGKAT</span></div>
      </div>

'''
a = t.index('      <!-- HOOK -->'); b = t.index('      <!-- USP -->')
t = t[:a] + NEW_HTML + t[b:]

# shift USP/CTA html blocks
def shift_html(m):
    return f'data-start="{float(m.group(1)) + SHIFT:.2f}"'
a = t.index('      <!-- USP -->'); b = t.index('<div id="flash"')
seg = re.sub(r'data-start="([0-9.]+)"', shift_html, t[a:b])
t = t[:a] + seg + t[b:]

NEW_JS = '''      // hook
      tl.fromTo("#h1", { scale: 3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }, 0.05);
      tl.to("#root", { keyframes: { x: [0, -14, 12, -8, 6, 0] }, duration: 0.25 }, 0.3);
      tl.fromTo("#h2", { scale: 0, rotation: -20 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 0.9);
      tl.to("#h1", { scale: 1.06, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, 1.4);

      // tip 1
      tl.fromTo("#t1n", { scale: 0, rotation: -180 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 3.6);
      tl.fromTo("#t1t", { x: 1100 }, { x: 0, duration: 0.3, ease: "power4.out" }, 3.9);
      tl.fromTo("#shoe", { y: -400, rotation: -10 }, { y: 0, rotation: 0, duration: 0.45, ease: "bounce.out" }, 4.3);
      tl.fromTo("#ripples path", { scale: 0.4, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1.2, opacity: 1, duration: 0.5, stagger: 0.12, repeat: 5, ease: "power1.out" }, 4.75);
      tl.fromTo("#heel", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 9 }, 4.75);
      tl.fromTo("#t1a", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 5.6);
      tl.fromTo("#t1b", { scale: 0, rotation: 15 }, { scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }, 6.1);

      // tip 2
      tl.fromTo("#t2n", { scale: 0, rotation: -180 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 10.1);
      tl.fromTo("#t2t", { x: 1100 }, { x: 0, duration: 0.3, ease: "power4.out" }, 10.4);
      tl.fromTo("#bar0", { scaleY: 0 }, { scaleY: 1, duration: 0.45, ease: "back.out(1.6)" }, 11.2);
      tl.fromTo("#bar1", { scaleY: 0 }, { scaleY: 1, duration: 0.45, ease: "back.out(1.6)" }, 12.4);
      tl.fromTo("#bar2", { scaleY: 0 }, { scaleY: 1, duration: 0.45, ease: "back.out(1.6)" }, 13.6);
      tl.fromTo(["#col0 .wk", "#col1 .wk", "#col2 .wk"], { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.25, stagger: 1.2 }, 11.2);
      tl.to("#bar2", { y: -16, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, 14.2);

      // tip 3
      tl.fromTo("#t3n", { scale: 0, rotation: -180 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 17.1);
      tl.fromTo("#t3t", { x: 1100 }, { x: 0, duration: 0.3, ease: "power4.out" }, 17.4);
      tl.fromTo("#db", { scale: 0, rotation: -30 }, { scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }, 18.0);
      tl.to("#db", { y: -30, duration: 0.35, yoyo: true, repeat: 7, ease: "sine.inOut" }, 18.5);
      tl.fromTo("#t3a", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 0.25 }, 18.6);
      tl.fromTo("#t3b", { x: -1100 }, { x: 0, duration: 0.35, ease: "back.out(1.6)" }, 19.8);
      const dbk = { v: 1 };
      tl.fromTo(dbk, { v: 1 }, { v: 3, duration: 2.0, ease: "steps(2)", onUpdate: () => { document.getElementById("dbkg").textContent = Math.round(dbk.v) + "KG"; } }, 20.1);

'''
a = t.index('      // hook'); b = t.index('      // usp counter')
tail = t[b:]
end = tail.index('      window.__timelines')
shifted = re.sub(r', ([0-9.]+)\);', lambda m: f', {float(m.group(1)) + SHIFT:.2f});', tail[:end])
t = t[:a] + NEW_JS + shifted + tail[end:]

body = t[t.index('<body>'):]
o, c = len(re.findall(r'<div\b', body)), body.count('</div>')
print('div open', o, 'close', c); assert o == c
for need in ['id="hook"', 'id="tip1"', 'id="tip2"', 'id="tip3"', 'id="usp"', 'id="u1ring"', 'id="c1"', 'id="cta"', 'id="arrows"', 'GELEBEH?', 'KAT BEG KUNING']:
    assert need in t, need
print(re.findall(r'id="(usp|u1|u1ring|u1low|c1|cta|arrows)" class="g clip" data-start="([0-9.]+)"', t))
open(S + '/template9.html', 'w').write(t)

bsrc = open(S + '/build8.py').read()
bsrc = bsrc.replace('TOTAL = 36.0', 'TOTAL = 38.0')
bsrc, n = re.subn(r'CUTS = \[.*?\nMUTED = \{"f5"\}', '''CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f13", 2.0),    # HOOK: 3 tips
    (3.5, 10.0, "f17", 1.5),   # TIP 1: pakai kasut (close-up kasut)
    (10.0, 13.5, "f19", 0.0),  # TIP 2: konsisten setiap hari
    (13.5, 17.0, "f9", 0.0),   # TIP 2 (sambung)
    (17.0, 20.5, "f2", 2.0),   # TIP 3: dumbbell (upper body)
    (20.5, 23.5, "f18", 5.0),  # TIP 3 (sambung, dumbbell)
    (23.5, 27.0, "f5", 50.9),  # USP: multifunction counter (muted: ada muzik)
    (27.0, 31.0, "f16", 2.9),  # USP: timbang stepper 5.90kg
    (31.0, 34.0, "f15", 0.5),  # CTA: nak kecilkan gelebeh?
    (34.0, TOTAL, "f1", 8.0),  # CTA: grab stepper kat beg kuning
]
MUTED = {"f5"}''', bsrc, flags=re.S); assert n == 1
bsrc, n = re.subn(r'SFX = \[\n.*?\n\]', '''SFX = [
    (0.05, "impact", 0.55), (0.05, "whoosh", 0.35), (0.90, "pop", 0.4),
    (3.50, "whoosh", 0.35), (3.60, "impact", 0.4), (4.75, "impact", 0.35), (5.60, "pop", 0.4), (6.10, "pop", 0.4),
    (10.00, "whoosh", 0.35), (10.10, "impact", 0.4), (11.20, "pop", 0.4), (12.40, "pop", 0.4), (13.60, "riser", 0.25), (14.20, "ding", 0.3),
    (17.00, "whoosh", 0.35), (17.10, "impact", 0.4), (18.00, "pop", 0.4), (19.80, "swoosh", 0.35), (20.60, "tick", 0.5), (21.60, "tick", 0.5),
    (23.50, "whoosh", 0.35), (23.85, "ding", 0.3),
    (27.00, "whoosh", 0.35), (27.20, "pop", 0.4), (27.80, "ding", 0.3), (28.55, "swoosh", 0.35),
    (31.00, "whoosh", 0.35), (31.45, "impact", 0.45),
    (34.00, "whoosh", 0.35), (34.10, "pop", 0.4), (34.80, "ding", 0.3), (35.00, "pop", 0.4),
]''', bsrc, flags=re.S); assert n == 1
open(S + '/build9.py', 'w').write(bsrc)
print('ok')
