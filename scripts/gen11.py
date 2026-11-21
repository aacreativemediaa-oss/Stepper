"""Task 11 (VO, 46s): template11.html + build11.py."""
import re
S = '/tmp/claude-0/-home-user-Stepper/b8f74fb8-acd7-52a4-8d66-0e297ed9c05d/scratchpad'
t10 = open(S + '/template10.html').read()
head = t10[:t10.index('    </style>')]
t5 = open(S + '/template5.html').read()
capcss = re.search(r'      /\* captions \(65px\) \*/.*?\.cap \.w\.key\.on \{[^\n]*\n', t5, re.S).group(0)
assert 'font-size: 60px' in capcss
head += capcss + '''
      #sweat { top: 240px; } #sweat .watch { display: inline-flex; align-items: center; gap: 20px; }
      .drop { position: absolute; width: 60px; height: 84px; }
      .stack { left: 70px; right: auto; display: flex; flex-direction: column; gap: 22px; align-items: flex-start; }
      #cmp .stat .box { min-width: 300px; }
      #mcard { left: 60px; right: 60px; top: 380px; background: rgba(10,10,12,0.86); border: 6px solid #000; border-radius: 34px; box-shadow: 0 16px 0 #000;
               padding: 18px; display: flex; align-items: center; gap: 24px; }
      #mcard svg.fig { width: 250px; height: 430px; flex: none; }
      #mcard .mp { display: flex; flex-direction: column; gap: 18px; align-items: flex-start; }
      .bignum { display: block; font-size: 190px; line-height: 1; color: var(--lime); -webkit-text-stroke: 9px #000; paint-order: stroke fill; text-shadow: 0 12px 0 #000; font-variant-numeric: tabular-nums; }
      .strike { position: relative; display: inline-block; }
      .strike::after { content: ""; }
      #strk { position: absolute; left: -10px; top: 50%; height: 18px; width: 0; background: var(--red); border-radius: 9px; transform: rotate(-6deg); box-shadow: 0 6px 0 #000; }
      #thumb { width: 220px; height: 220px; display: block; margin: 0 auto 10px; }
      .heart { position: absolute; width: 70px; height: 64px; }
      #rugi { top: 560px; } #rugi span { display: inline-block; font-family: var(--font-display); font-size: 110px; color: #fff; background: var(--red); padding: 0 40px; transform: rotate(-5deg); box-shadow: 0 14px 0 #000; }
'''
CHECK = lambda fill, stroke: f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{fill}"/><path d="M18 33 L28 43 L47 22" fill="none" stroke="{stroke}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
HOUSE = '<svg viewBox="0 0 64 64"><path d="M6 30 L32 8 L58 30" fill="none" stroke="#ff2e7e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/><rect x="14" y="28" width="36" height="28" fill="#ff2e7e"/><rect x="27" y="40" width="10" height="16" fill="#fff"/></svg>'
TV = '<svg viewBox="0 0 64 64"><rect x="4" y="10" width="56" height="36" rx="5" fill="#000"/><rect x="10" y="16" width="44" height="24" fill="#5ad1ff"/><path d="M22 56 L42 56 M32 46 L32 56" stroke="#000" stroke-width="6" stroke-linecap="round"/></svg>'
BAG = '<svg viewBox="0 0 80 80"><path d="M14 26 H66 L62 72 H18 Z" fill="#ffd400" stroke="#000" stroke-width="6" stroke-linejoin="round"/><path d="M28 30 V20 A12 12 0 0 1 52 20 V30" fill="none" stroke="#000" stroke-width="6" stroke-linecap="round"/></svg>'
ARROW = '<svg viewBox="0 0 150 90"><path d="M15 15 L75 75 L135 15" fill="none" stroke="#ffd400" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DROP = '<svg class="drop" style="left:{x}px;top:{y}px" viewBox="0 0 60 84"><path d="M30 0 C30 0 0 40 0 56 A30 28 0 0 0 60 56 C60 40 30 0 30 0Z" fill="#5ad1ff" stroke="#000" stroke-width="5"/></svg>'
FLAME = '<svg id="hflame" viewBox="0 0 190 170" style="width:170px;height:150px;display:block;margin:0 auto 8px"><path d="M95 165 C45 165 25 130 30 100 C35 70 60 55 62 25 C85 40 95 60 92 80 C105 70 110 55 108 40 C140 65 165 95 160 125 C155 150 130 165 95 165 Z" fill="#ff3b30" stroke="#000" stroke-width="6" stroke-linejoin="round"/><path d="M95 160 C70 160 60 140 65 122 C70 105 85 98 88 80 C105 95 118 110 120 128 C122 148 112 160 95 160 Z" fill="#ffd400" stroke="#000" stroke-width="5" stroke-linejoin="round"/></svg>'
HEART = '<svg class="heart" style="left:{x}px;top:{y}px" viewBox="0 0 70 64"><path d="M35 60 C10 42 2 30 2 18 A16 16 0 0 1 35 12 A16 16 0 0 1 68 18 C68 30 60 42 35 60 Z" fill="#ff2e7e" stroke="#000" stroke-width="5"/></svg>'
THUMB = '<svg id="thumb" viewBox="0 0 220 220"><circle cx="110" cy="110" r="104" fill="#c6ff00" stroke="#000" stroke-width="8"/><path d="M62 104 H92 V170 H62 Z" fill="#fff" stroke="#000" stroke-width="7" stroke-linejoin="round"/><path d="M92 104 L118 52 Q132 46 134 62 L128 96 H160 Q174 98 170 114 L160 160 Q156 172 142 170 H92 Z" fill="#fff" stroke="#000" stroke-width="7" stroke-linejoin="round"/></svg>'
g8 = open(S + '/gen8.py').read()
BASE = re.search(r"BASE = '''(.*?)'''", g8, re.S).group(1)
FRONT = re.search(r"FRONT = f'''(.*?)'''", g8, re.S).group(1).replace('{BASE}', BASE).replace('<svg viewBox="0 0 200 420">', '<svg class="fig" viewBox="0 0 200 420">')

body = f'''    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{{{{TOTAL}}}}" data-width="1080" data-height="1920">
      {{{{VIDEOS}}}}
      <!-- voiceover: original audio, untouched -->
      <audio id="vo" src="assets/vo.wav" data-start="0" data-duration="45.97" data-volume="1" data-track-index="2"></audio>
      {{{{SFX}}}}
      <div id="vignette" class="layer"></div>

      <!-- HOOK: headline 150px, sub headline 70px -->
      <div id="hook" class="g clip" data-start="0" data-duration="3.6" data-track-index="10" style="top:400px">
        {FLAME}
        <span class="big" id="h1" style="font-size:150px;color:var(--lime)">200 KALORI</span>
        <span class="blk pink" id="h2" style="font-size:70px">15 MINIT STEPPER</span>
      </div>

      <div id="cmp" class="g clip" data-start="5.3" data-duration="2.35" data-track-index="10" style="top:300px">
        <div class="cara" id="cmpc">SETARA DENGAN</div>
        <div class="stat" id="cmps"><div class="box"><b>15</b><i>MINIT STEPPER</i></div><div class="eq">≈</div><div class="box" style="border-color:var(--yellow)"><b style="color:var(--yellow)">30</b><i>MINIT BRISKWALK</i></div></div>
      </div>

      <div id="total" class="g clip" data-start="8.5" data-duration="0.95" data-track-index="10" style="top:330px"><span class="blk" id="tw">TOTAL BODY WORKOUT</span></div>

      <div id="mcard" class="g clip" data-start="9.5" data-duration="3.0" data-track-index="10">
        {FRONT}
        <div class="mp">
          <span class="pill pink" id="mp1">{CHECK("#c6ff00","#000")}LENGAN</span>
          <span class="pill pink" id="mp2">{CHECK("#c6ff00","#000")}PERUT</span>
          <span class="pill pink" id="mp3">{CHECK("#c6ff00","#000")}KAKI</span>
          <span class="blk" id="mp4" style="font-size:70px">SERENTAK!</span>
        </div>
      </div>

      <div id="sweat" class="g clip" data-start="12.8" data-duration="1.7" data-track-index="10">
        <div class="watch">
          <svg width="110" height="128" viewBox="0 0 130 150"><rect x="50" y="0" width="30" height="18" rx="4" fill="#fff"/><circle cx="65" cy="85" r="56" fill="#fff" stroke="#000" stroke-width="8"/>
            <line id="hand" x1="65" y1="85" x2="65" y2="42" stroke="#ff2e7e" stroke-width="10" stroke-linecap="round" style="transform-origin:65px 85px"/></svg>
          <span class="big">5 MINIT</span>
        </div>
        <div><span class="blk pink" id="sweattag">BERPELUH LENCUN!</span></div>
      </div>
      <div class="g clip" id="drops" data-start="13.6" data-duration="0.9" data-track-index="11" style="left:0;top:0;width:1080px;height:1000px">
        {DROP.format(x=150,y=200)}{DROP.format(x=870,y=240)}{DROP.format(x=910,y=520)}{DROP.format(x=110,y=560)}
      </div>

      <div id="rumah" class="g clip" data-start="16.2" data-duration="1.35" data-track-index="10" style="top:330px">
        <span class="pill yellow" id="rm">{HOUSE}TRIM GELEBEH KAT RUMAH</span>
      </div>

      <div id="kg" class="g clip" data-start="20.1" data-duration="2.0" data-track-index="10" style="top:300px">
        <div class="cara" id="kgc">TAMPUNG LEBIH</div>
        <span class="bignum" id="kgn">0KG+</span>
      </div>
      <div id="safe" class="g clip" data-start="22.1" data-duration="1.0" data-track-index="10" style="top:330px">
        <span class="pill lime" id="sf">{CHECK("#000","#c6ff00")}SELAMAT</span>
      </div>

      <div id="cpt" class="g clip" data-start="23.15" data-duration="2.15" data-track-index="10" style="top:250px">
        <span class="blk" id="cp1" style="font-size:80px">COMPACT &amp; RINGAN</span>
      </div>
      <div id="u1ring" class="g clip" data-start="23.5" data-duration="1.8" data-track-index="11" style="left:0;top:0;width:1080px;height:1920px">
        <svg width="1080" height="1920" style="position:absolute;inset:0"><circle id="ring6" cx="735" cy="770" r="125" fill="none" stroke="#c6ff00" stroke-width="14"/></svg>
        <span class="blk" id="kgtag" style="position:absolute;left:600px;top:560px;font-size:90px">5.9KG</span>
      </div>

      <div id="places" class="g clip stack" data-start="25.9" data-duration="1.8" data-track-index="10" style="top:300px">
        <div class="pill lime" id="pl1">{TV}DEPAN TV</div>
        <div class="pill yellow" id="pl2">{HOUSE}DALAM BILIK</div>
      </div>

      <div id="ctr" class="g clip" data-start="27.8" data-duration="3.4" data-track-index="10" style="top:250px">
        <div class="cara" id="ctc">ADA SEKALI</div>
        <span class="big" id="ctb" style="font-size:100px">DIGITAL COUNTER</span>
        <div class="row" style="margin-top:18px"><span class="pill lime" id="ct1">{CHECK("#000","#c6ff00")}KALORI</span><span class="pill pink" id="ct2">{CHECK("#c6ff00","#000")}STEPS</span></div>
      </div>

      <div id="sold" class="g clip" data-start="31.3" data-duration="1.85" data-track-index="10" style="top:300px">
        <div class="cara" id="soc">HAMPIR</div>
        <span class="bignum" id="son" style="font-size:150px">0</span>
        <span class="blk pink" id="sob" style="font-size:80px">UNIT TERJUAL</span>
      </div>

      <div id="fb" class="g clip" data-start="34.4" data-duration="2.3" data-track-index="10" style="top:260px">
        {THUMB}
        <div class="cara" id="fbc">RAMAI DAH BAGI</div>
        <span class="blk" id="fbt" style="font-size:80px">FEEDBACK POSITIF</span>
      </div>
      <div class="g clip" id="hearts" data-start="35.2" data-duration="1.7" data-track-index="11" style="left:0;top:0;width:1080px;height:1000px">
        {HEART.format(x=180,y=330)}{HEART.format(x=820,y=300)}{HEART.format(x=860,y=560)}{HEART.format(x=140,y=600)}
      </div>

      <div id="price" class="g clip" data-start="37.0" data-duration="4.1" data-track-index="10" style="top:250px">
        <div class="cara" id="pd">DULU</div>
        <span class="strike"><span class="big" id="pr1" style="font-size:110px">BERATUS RINGGIT</span><i id="strk"></i></span>
        <div style="margin-top:30px"><div class="tagbox" id="tagbox"><div class="s">SEKARANG</div><div class="m">MURAH!</div></div></div>
      </div>
      <div id="rugi" class="g clip" data-start="41.1" data-duration="1.05" data-track-index="11"><span>RUGI TAK GRAB!</span></div>

      <div id="cta" class="g clip" data-start="42.2" data-duration="4.1" data-track-index="10">
        <div class="card" id="ctacard"><div class="a">PILIH WARNA KORANG</div><div class="b">GRAB<br>SEKARANG!</div></div>
        <div><div class="bag" id="ctabag">{BAG}BEG KUNING BAWAH NI</div></div>
      </div>
      <div id="arrows" class="g clip" data-start="42.9" data-duration="3.4" data-track-index="11">{ARROW}{ARROW}{ARROW}</div>

      {{{{CAPTIONS}}}}
      <div id="flash" class="layer"></div>
      <div id="progress"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      /*{{{{VIDJS}}}}*/
      tl.fromTo("#progress", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {{{{TOTAL}}}}, ease: "none" }}, 0);
      const set = (id, v) => {{ document.getElementById(id).textContent = v; }};

      tl.fromTo("#hflame", {{ scale: 0, transformOrigin: "50% 100%" }}, {{ scale: 1, duration: 0.35, ease: "back.out(2)" }}, 0.0);
      tl.to("#hflame", {{ scaleY: 1.12, duration: 0.18, yoyo: true, repeat: 9, ease: "sine.inOut", transformOrigin: "50% 100%" }}, 0.4);
      tl.fromTo("#h1", {{ scale: 3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }}, 0.15);
      tl.to("#root", {{ keyframes: {{ x: [0, -14, 12, -8, 6, 0] }}, duration: 0.25 }}, 0.4);
      tl.fromTo("#h2", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 0.7);

      tl.fromTo("#cmpc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 5.3);
      tl.fromTo("#cmps .box", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2)", stagger: 0.9 }}, 5.4);
      tl.fromTo("#cmps .eq", {{ scale: 0 }}, {{ scale: 1, duration: 0.25, ease: "back.out(3)" }}, 6.0);

      tl.fromTo("#tw", {{ scale: 3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.22, ease: "power4.out" }}, 8.55);
      tl.to("#root", {{ keyframes: {{ y: [0, 12, -10, 6, 0] }}, duration: 0.22 }}, 8.77);

      tl.fromTo("#mcard", {{ y: 400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, 9.5);
      tl.fromTo("#mcard .mf > *", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.1 }}, 9.8);
      tl.fromTo("#mp1", {{ x: 700 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)" }}, 9.9);
      tl.fromTo("#mp2", {{ x: 700 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)" }}, 10.35);
      tl.fromTo("#mp3", {{ x: 700 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)" }}, 10.8);
      tl.fromTo("#mp4", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 11.8);
      tl.to("#mcard .mf", {{ opacity: 0.55, duration: 0.25, yoyo: true, repeat: 5 }}, 11.0);

      tl.fromTo("#sweat .watch", {{ y: -200, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, 12.85);
      tl.fromTo("#hand", {{ rotation: 0 }}, {{ rotation: 720, duration: 1.2, ease: "power1.inOut" }}, 13.0);
      tl.fromTo("#sweattag", {{ scale: 0 }}, {{ scale: 1, duration: 0.28, ease: "back.out(3)" }}, 13.8);
      tl.fromTo("#drops .drop", {{ y: -120, opacity: 0, scale: 0.4 }}, {{ y: 120, opacity: 1, scale: 1, duration: 0.85, ease: "power2.in", stagger: 0.06 }}, 13.6);

      tl.fromTo("#rm", {{ scale: 0, rotation: -10 }}, {{ scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2)" }}, 16.25);

      tl.fromTo("#kgc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 20.1);
      const kk = {{ v: 0 }};
      tl.fromTo(kk, {{ v: 0 }}, {{ v: 100, duration: 0.9, ease: "power2.in", onUpdate: () => set("kgn", Math.round(kk.v) + "KG+") }}, 20.2);
      tl.to("#kgn", {{ scale: 1.12, duration: 0.15, yoyo: true, repeat: 1 }}, 21.1);
      tl.to("#root", {{ keyframes: {{ x: [0, 14, -12, 8, 0] }}, duration: 0.22 }}, 21.1);
      tl.fromTo("#sf", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, 22.1);

      tl.fromTo("#cp1", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 23.2);
      tl.fromTo("#ring6", {{ scale: 2.5, opacity: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, 23.5);
      tl.fromTo("#kgtag", {{ scale: 0, rotation: 20 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.5)" }}, 23.7);
      tl.to("#ring6", {{ scale: 1.08, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut", transformOrigin: "50% 50%" }}, 24.0);

      tl.fromTo("#pl1", {{ x: -800 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)" }}, 25.95);
      tl.fromTo("#pl2", {{ x: -800 }}, {{ x: 0, duration: 0.3, ease: "back.out(1.6)" }}, 26.9);

      tl.fromTo("#ctc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 27.8);
      tl.fromTo("#ctb", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, 28.0);
      tl.fromTo("#ct1", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, 29.95);
      tl.fromTo("#ct2", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, 30.85);

      tl.fromTo("#soc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 31.3);
      const so = {{ v: 0 }};
      tl.fromTo(so, {{ v: 0 }}, {{ v: 400000, duration: 1.0, ease: "power2.out", onUpdate: () => set("son", Math.round(so.v).toLocaleString("en-US")) }}, 31.45);
      tl.fromTo("#sob", {{ scale: 0, rotation: 15 }}, {{ scale: 1, rotation: -3, duration: 0.3, ease: "back.out(2.2)" }}, 32.5);

      tl.fromTo("#thumb", {{ scale: 0, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }}, 34.6);
      tl.fromTo("#fbc", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 34.45);
      tl.fromTo("#fbt", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.2)" }}, 35.1);
      tl.fromTo("#hearts .heart", {{ y: 60, opacity: 0, scale: 0.3 }}, {{ y: -80, opacity: 1, scale: 1, duration: 0.9, ease: "power2.out", stagger: 0.12 }}, 35.2);

      tl.fromTo("#pd", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, 37.0);
      tl.fromTo("#pr1", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, 37.35);
      tl.fromTo("#strk", {{ width: 0 }}, {{ width: 900, duration: 0.3, ease: "power2.inOut" }}, 39.75);
      tl.fromTo("#tagbox", {{ y: -400, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, 40.25);
      tl.fromTo("#tagbox", {{ rotation: 12 }}, {{ rotation: 0, duration: 0.7, ease: "elastic.out(1.2,0.25)", immediateRender: false }}, 40.55);
      tl.fromTo("#rugi span", {{ scale: 3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.2, ease: "power4.in" }}, 41.05);
      tl.to("#root", {{ keyframes: {{ x: [0, -12, 10, -6, 0] }}, duration: 0.22 }}, 41.25);

      tl.fromTo("#ctacard", {{ scale: 0, rotation: -8 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2)" }}, 42.2);
      tl.fromTo("#ctabag", {{ y: 300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, 42.85);
      tl.to("#ctabag", {{ scale: 1.08, duration: 0.25, yoyo: true, repeat: 9, ease: "sine.inOut" }}, 43.3);
      tl.fromTo("#arrows svg", {{ y: -30, opacity: 0 }}, {{ y: 20, opacity: 1, duration: 0.4, stagger: 0.12, repeat: 5, yoyo: true, ease: "sine.inOut" }}, 42.9);

      /*{{{{CAPJS}}}}*/
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
t = head + body
for css_need in ['.tagbox', '#rugi', '.card', '.bag', '#arrows', '.stat', '.cara', '.row']:
    assert css_need in t, css_need
b = t[t.index('<body>'):]
o, c = len(re.findall(r'<div\b', b)), b.count('</div>')
print('div open', o, 'close', c); assert o == c
open(S + '/template11.html', 'w').write(t)

# ---------------- builder
src = open(S + '/build5.py').read()
def R(old, new, cnt=1):
    global src
    assert old in src, old[:60]
    src = src.replace(old, new, cnt)
src = src.replace('TOTAL = 35.8', 'TOTAL = 46.3')
src, n = re.subn(r'CUTS = \[.*?\n\]\nMUTED = \{"f5"\}\nFOOTAGE_VOL = 0.3', '''CUTS = [
    (0.00, 3.70, "f15", 6.0),   # hook: kasut pink/hijau (offset baru)
    (3.70, 9.40, "f2", 5.0),    # 200 kalori / briskwalk / total body
    (9.40, 14.50, "f7", 5.0),   # otot lengan, perut, kaki + berpeluh (luar, tali)
    (14.50, 19.40, "f14", 3.0), # trim gelebeh kat rumah / badan besar jangan risau
    (19.40, 23.10, "f12", 4.0), # tampung 100kg+, selamat
    (23.10, 25.30, "f16", 4.2), # compact & ringan (timbang 5.9kg)
    (25.30, 27.70, "f18", 1.0), # depan TV / dalam bilik
    (27.70, 31.20, "f5", 68.6), # digital counter (muted: ada muzik)
    (31.20, 38.90, "f4", 1.0),  # 400,000 terjual / viral / feedback / dulu mahal
    (38.90, TOTAL, "f1", 5.5),  # murah / rugi / CTA beg kuning
]
MUTED = {"f5"}
VO_PATH = OUT.rsplit("/", 1)[0] + "/assets/vo.wav"''', src, flags=re.S); assert n == 1
R('FIX = {"gelebi": "gelebeh"}', 'FIX = {"gelebi": "gelebeh", "beresuap": "briskwalk", "latih": "dilatih", "virus": "viral", "bekon": "beg kuning"}')
# "sahaja je." -> "saja-saja."
R('''    if words: words[-1]["segend"] = True''', '''    if words: words[-1]["segend"] = True
for i, w in enumerate(words):
    if w["t"].lower() == "sahaja" and i + 1 < len(words) and words[i + 1]["t"].lower().startswith("je"):
        w["t"] = "saja-saja."; w["e"] = words[i + 1]["e"]; w["segend"] = words[i + 1].get("segend"); del words[i + 1]; break''')
R('HOOK_END = 3.75', 'HOOK_END = 3.6')
src, n = re.subn(r'GFX = \[.*?\n\]', '''GFX = [
    (5.3, 7.65, "15 MINIT STEPPER SETARA 30 MINIT BRISKWALK BIASA"), (8.5, 9.45, "TOTAL BODY WORKOUT"),
    (9.5, 12.5, "OTOT LENGAN PERUT KAKI SERENTAK DILATIH"), (12.8, 14.5, "5 MINIT BERPELUH LENCUN"),
    (16.2, 17.55, "TRIM GELEBEH KAT RUMAH"), (20.1, 22.1, "TAMPUNG LEBIH 100KG"), (22.1, 23.1, "SELAMAT"),
    (23.15, 25.3, "COMPACT RINGAN"), (25.9, 27.7, "DEPAN TV DALAM BILIK"),
    (27.8, 31.2, "ADA DIGITAL COUNTER SEKALI KALORI STEPS TRACK JUMLAH"), (31.3, 33.15, "HAMPIR 400,000 UNIT TERJUAL"),
    (34.4, 36.9, "RAMAI BAGI FEEDBACK POSITIF BILA LATIHAN STEPPER"), (37.0, 39.75, "DULU BERATUS RINGGIT"), (39.75, 41.1, "SEKARANG MURAH"),
    (41.1, 42.15, "RUGI TAK GRAB"), (42.2, 43.8, "PILIH WARNA BEG KUNING BAWAH"),
]''', src, flags=re.S); assert n == 1
R('''vid_html, vid_js = [], []''', '''sys.path.insert(0, "/home/user/Stepper/scripts")
from footage_gain import clip_volumes, print_report
VOLS, _rows, _t, _vo = clip_volumes(CUTS, OUT.rsplit("/", 1)[0] + "/assets/video", VO_PATH, MUTED)
print_report(_rows, _t, _vo)
vid_html, vid_js = [], []''')
R('data-volume="{FOOTAGE_VOL}" \')', 'data-volume="{VOLS[i]}" \')')
src, n = re.subn(r'SFX = \[  # \(time, file, volume\)\n.*?\n\]', '''SFX = [  # (time, file, volume)
    (0.00, "whoosh", 0.35), (0.15, "impact", 0.5), (0.70, "pop", 0.4),
    (3.70, "whoosh", 0.35), (5.40, "pop", 0.4), (6.00, "ding", 0.25), (6.30, "pop", 0.4),
    (8.55, "impact", 0.4), (9.40, "whoosh", 0.35), (9.90, "pop", 0.35), (10.35, "pop", 0.35), (10.80, "pop", 0.35), (11.80, "impact", 0.35),
    (12.85, "tick", 0.5), (13.80, "pop", 0.4), (14.50, "whoosh", 0.35), (16.25, "pop", 0.4),
    (19.40, "whoosh", 0.35), (20.20, "riser", 0.25), (21.10, "impact", 0.45), (22.10, "ding", 0.25),
    (23.10, "whoosh", 0.35), (23.70, "pop", 0.4), (25.30, "swoosh", 0.35), (25.95, "pop", 0.4), (26.90, "pop", 0.4),
    (27.70, "whoosh", 0.35), (28.00, "ding", 0.25), (29.95, "pop", 0.4), (30.85, "pop", 0.4),
    (31.20, "whoosh", 0.35), (31.45, "riser", 0.2), (32.50, "impact", 0.4), (34.60, "pop", 0.4), (35.20, "ding", 0.25),
    (37.35, "pop", 0.4), (39.75, "zap", 0.35), (40.25, "cash", 0.4), (41.05, "impact", 0.45),
    (42.20, "whoosh", 0.35), (42.85, "pop", 0.4), (43.30, "ding", 0.25),
]''', src, flags=re.S); assert n == 1
open(S + '/build11.py', 'w').write(src)
print('ok')
