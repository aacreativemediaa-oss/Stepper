"""Task 14: same opening as Task 12 (table first, rows one by one, 10s) with 15-min values,
new text sizes (headline 100px, sub-headline 47px), USP 100kg+ & ringan, CTA 'start stepper sekarang'."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
g = open(S + '/gen12.py').read()

def R(old, new, count=1):
    global g
    assert old in g, old[:80]
    g = g.replace(old, new, count)

# 15-minute table values (Task 8 = Task 7 x 1.5)
R("table = timed(block(t7, 'table'), 0, 10.0)", "table = timed(block(open(S + '/template7_15.html').read(), 'table'), 0, 10.0)")
R('*Anggaran untuk 10 minit latihan', '*Anggaran untuk 15 minit latihan')
R("assert '±100<small>' in table and '±210<small>' in table", "assert '±150<small>' in table and '±315<small>' in table")
# new sizes
R('<span class="big" id="hk1" style="font-size:150px;color:var(--lime)">10 MINIT</span>',
  '<span class="big" id="hk1" style="font-size:100px;color:var(--lime)">15 MINIT</span>')
R('<span class="blk pink" id="hk2" style="font-size:70px">LATIHAN STEPPER</span>',
  '<span class="blk pink" id="hk2" style="font-size:47px">LATIHAN STEPPER</span>')
R('<span class="blk" id="vs1" style="font-size:66px">BERAT BADAN VS KALORI</span>',
  '<span class="blk" id="vs1" style="font-size:47px">BERAT BADAN VS KALORI</span>')
R('style="top:110px">\n        <span class="big" id="hk1"', 'style="top:150px">\n        <span class="big" id="hk1"')
# USP 1: 100kg+ instead of counter
R("""      {usp}
      <div id="ctp" class="g clip stack" data-start="14.0" data-duration="2.0" data-track-index="11" style="top:640px">
        <div class="pill lime" id="cp1">{CHECK("#000","#c6ff00")}STEPS</div>
        <div class="pill yellow" id="cp2">{CHECK("#000","#ffd400")}MASA</div>
        <div class="pill pink" id="cp3">{CHECK("#c6ff00","#000")}KALORI</div>
      </div>""", """      <div id="kg" class="g clip" data-start="12.55" data-duration="3.45" data-track-index="10" style="top:300px">
        <div class="cara" id="kgc">BOLEH TAMPUNG BERAT</div>
        <span class="bignum" id="kgn">0KG+</span>
        <div style="margin-top:20px"><span class="pill lime" id="kgp">{CHECK("#000","#c6ff00")}KUAT &amp; STABIL</span></div>
      </div>""")
R("""      tl.fromTo("#u0", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 12.6);
      tl.fromTo("#u1", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, 12.85);
      tl.fromTo(["#cp1", "#cp2", "#cp3"], {{ x: -800 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)", stagger: 0.4 }}, 14.0);""",
  """      tl.fromTo("#kgc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 12.6);
      const kk = {{ v: 0 }};
      tl.fromTo(kk, {{ v: 0 }}, {{ v: 100, duration: 1.0, ease: "power2.in", onUpdate: () => {{ document.getElementById("kgn").textContent = Math.round(kk.v) + "KG+"; }} }}, 12.75);
      tl.to("#kgn", {{ scale: 1.12, duration: 0.15, yoyo: true, repeat: 1 }}, 13.75);
      tl.to("#root", {{ keyframes: {{ x: [0, 14, -12, 8, 0] }}, duration: 0.22 }}, 13.75);
      tl.fromTo("#kgp", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, 14.3);""")
R("usp = timed(block(t8, 'usp'), 12.55, 3.45).replace('>SIAP ADA<', '>ADA SEKALI<')", "")
R("'id=\"usp\"', ", "'id=\"kg\"', ")
# CTA
R("""        <span class="mid" id="c1a" style="margin-top:34px">NAK BADAN FIT</span>
        <span class="blk" id="c1b">2027?</span>""", """        <span class="mid" id="c1a" style="margin-top:34px">2027 NAK BADAN FIT?</span>""")
R("""      tl.fromTo("#c1b", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 21.3);\n""", "")
R("cta = cta.replace('<div class=\"a\">SEKARANG!</div>', '')",
  "cta = cta.replace('<div class=\"a\">SEKARANG!</div>', '').replace('GRAB<br>STEPPER!', 'START STEPPER<br>SEKARANG!')\n"
  "cta = re.sub(r'<div><div class=\"bag\".*?</div></div>', '', cta, flags=re.S)")
R("      {arrows}\n", "")
R("""      tl.fromTo("#ctabag", {{ y: 300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, 24.2);
      tl.to("#ctabag", {{ scale: 1.08, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut" }}, 24.6);
      tl.fromTo("#arrows svg", {{ y: -30, opacity: 0 }}, {{ y: 20, opacity: 1, duration: 0.4, stagger: 0.12, repeat: 4, yoyo: true, ease: "sine.inOut" }}, 24.3);""",
  """      tl.to("#ctacard", {{ scale: 1.06, duration: 0.25, yoyo: true, repeat: 9, ease: "sine.inOut" }}, 24.2);""")
R("'id=\"arrows\"', 'KAT BEG KUNING SEKARANG!', ", "'START STEPPER<br>SEKARANG!', ")
# bignum css
R("head += '''      #rugi { top: 560px; }\n'''",
  "head += '''      #rugi { top: 560px; }\n      .bignum { display: block; font-size: 120px; line-height: 1; color: var(--lime); -webkit-text-stroke: 7px #000; paint-order: stroke fill; text-shadow: 0 10px 0 #000; font-variant-numeric: tabular-nums; }\n'''")
# outputs
R("open(S + '/template12.html', 'w')", "open(S + '/template14.html', 'w')")
R("open(S + '/build12.py', 'w')", "open(S + '/build14.py', 'w')")
# clips
R('''    (0.0, 10.0, "f8", 0.0),    # HOOK + jadual kalori (trek luar), 10s
    (10.0, 13.2, "f7", 2.0),   # otot: badan penuh, tali rintangan (luar)
    (13.2, 16.5, "f17", 6.0),  # otot: close-up kaki
    (16.5, 20.0, "f5", 60.0),  # USP: pasang counter pada stepper (muted: ada muzik)
    (20.0, 24.0, "f16", 3.0),  # USP: ringan, timbang 5.9kg
    (24.0, 27.5, "f13", 5.0),  # CTA: fit 2027 (close-up kasut)
    (27.5, TOTAL, "f2", 9.0),  # CTA: grab kat beg kuning''', '''    (0.0, 10.0, "f18", 8.0),   # HOOK + jadual kalori 15 minit (dumbbell depan TV), 10s
    (10.0, 13.2, "f9", 0.0),   # otot: badan penuh, tali rintangan
    (13.2, 16.5, "f17", 9.0),  # otot: close-up kaki
    (16.5, 20.0, "f12", 4.0),  # USP: tampung 100kg+ (bilik gelap)
    (20.0, 24.0, "f16", 3.0),  # USP: ringan, timbang 5.9kg
    (24.0, 27.5, "f15", 6.0),  # CTA: 2027 nak badan fit
    (27.5, TOTAL, "f1", 5.5),  # CTA: start stepper sekarang''')
R('(16.50, "whoosh", 0.35), (16.85, "ding", 0.3), (18.00, "pop", 0.35), (18.40, "pop", 0.35), (18.80, "pop", 0.35),',
  '(16.50, "whoosh", 0.35), (16.75, "riser", 0.25), (17.75, "impact", 0.45), (18.30, "pop", 0.4),') if '(16.85, "ding", 0.3)' in g else None
exec(compile(g, 'gen12-as-14', 'exec'))

# ---- format: largest text 100px; "15 MINIT" block moved lower
t14 = open(S + '/template14.html').read()
t14 = t14.replace('style="top:150px">\n        <span class="big" id="hk1"', 'style="top:250px">\n        <span class="big" id="hk1"')
assert 'style="top:250px">\n        <span class="big" id="hk1"' in t14
def cap(m):
    v = int(m.group(2))
    return f'{m.group(1)}{min(v, 100)}px'
t14 = re.sub(r'(font-size: ?)(\d+)px', cap, t14)
t14 = re.sub(r'(font-size=")(\d+)(")', lambda m: f'{m.group(1)}{min(int(m.group(2)),100)}{m.group(3)}', t14)
over = [int(x) for x in re.findall(r'font-size: ?(\d+)px', t14) if int(x) > 100]
assert not over, over
open(S + '/template14.html', 'w').write(t14)
print('capped to 100px; hook moved to top 250px')
