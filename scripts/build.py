"""Generate the Hyperframes composition (index.html) for the stepper ad."""
import json, sys, html

TRANSCRIPT, OUT = sys.argv[1], sys.argv[2]
TOTAL = 34.2

# ---------------------------------------------------------------- edit plan
# (output_start, output_end, source, media_start)
CUTS = [
    (0.00, 0.50, "f4", 7.0),    # hook montage
    (0.50, 1.00, "f3", 2.0),
    (1.00, 1.55, "f2", 0.5),
    (1.55, 4.20, "f1", 1.5),    # 30 minit setiap hari
    (4.20, 5.35, "f3", 0.0),    # nampak mudah
    (5.35, 7.75, "f2", 2.0),    # 5 minit berpeluh
    (7.75, 9.20, "f3", 3.0),    # bukan kaki je
    (9.20, 11.55, "f4", 0.0),   # satu badan
    (11.55, 13.85, "f4", 2.6),  # total body workout
    (13.85, 15.05, "f2", 4.6),  # efektif gila
    (15.05, 18.20, "f3", 11.6), # product shot: counter
    (18.20, 21.10, "f2", 6.0),  # track steps & kalori
    (21.10, 24.40, "f1", 4.4),  # bilik / depan TV
    (24.40, 26.15, "f4", 5.2),  # kat luar
    (26.15, 28.75, "f2", 9.2),  # harga murah
    (28.75, 30.45, "f3", 5.0),  # harga naik
    (30.45, TOTAL, "f1", 8.0),  # CTA
]

# ---------------------------------------------------------------- captions
FIX = {"meraya": "raya", "bed": "beg"}
KEY = {"trim", "raya", "30", "minit", "mudah", "berpeluh", "gila", "kaki", "badan",
       "total", "body", "workout", "efektif", "multifunction", "counter", "steps",
       "kalori", "bilik", "tv", "luar", "murah", "rugi", "grab", "naik", "sekarang",
       "beg", "kuning", "5", "stepper"}
words = []
for seg in json.load(open(TRANSCRIPT)):
    for w in seg["words"]:
        txt = w["w"].strip()
        core = txt.strip(",.?!").lower()
        if core in FIX:
            txt = txt.lower().replace(core, FIX[core])
        words.append({"t": txt, "s": round(w["s"], 2), "e": round(w["e"], 2),
                      "k": txt.strip(",.?!").lower() in KEY})
# Fix zero-length "Eh," (27.64-27.64)
for i, w in enumerate(words):
    if w["e"] - w["s"] < 0.06:
        w["e"] = round(w["s"] + 0.1, 2)
        if i + 1 < len(words) and words[i + 1]["s"] < w["e"]:
            words[i + 1]["s"] = w["e"]

chunks, cur = [], []
for i, w in enumerate(words):
    cur.append(w)
    nxt = words[i + 1] if i + 1 < len(words) else None
    end_punct = w["t"][-1] in ",.?!"
    if nxt is None or end_punct or len(cur) >= 3 or nxt["s"] - w["e"] > 0.25:
        chunks.append(cur); cur = []

# hook (first sentence) is rendered as the big hook title instead of a caption
HOOK_END = 1.4
cap_html, cap_js = [], []
for ci, ch in enumerate(chunks):
    if ch[-1]["e"] <= HOOK_END + 0.01:
        continue
    start = ch[0]["s"]
    nxt_start = chunks[ci + 1][0]["s"] if ci + 1 < len(chunks) else TOTAL
    end = min(max(ch[-1]["e"] + 0.15, start + 0.4), nxt_start)
    if ci + 1 == len(chunks):
        end = TOTAL - 0.05
    cid = f"cap{ci}"
    spans = []
    for wi, w in enumerate(ch):
        t = html.escape(w["t"].upper().rstrip(","))
        cls = "w key" if w["k"] else "w"
        spans.append(f'<span class="{cls}" id="{cid}w{wi}">{t}</span>')
        cap_js.append(f'tl.set("#{cid}w{wi}",{{className:"{cls} on"}},{w["s"]:.2f});')
    cap_html.append(
        f'<div class="cap clip" id="{cid}" data-start="{start:.2f}" data-duration="{end-start:.2f}" '
        f'data-track-index="20">{" ".join(spans)}</div>')
    cap_js.append(f'tl.fromTo("#{cid}",{{scale:0.6,y:30,opacity:0}},{{scale:1,y:0,opacity:1,duration:0.18,ease:"back.out(2.5)"}},{start:.2f});')

# ---------------------------------------------------------------- video
vid_html, vid_js = [], []
for i, (a, b, src, ms) in enumerate(CUTS):
    vid_html.append(
        f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" muted playsinline '
        f'data-start="{a:.2f}" data-duration="{b-a:.2f}" data-media-start="{ms:.2f}" data-track-index="1"></video>')
    # punch-in at the cut, then a slow push
    vid_js.append(f'tl.fromTo("#v{i}",{{scale:1.18}},{{scale:1.04,duration:0.35,ease:"power3.out"}},{a:.2f});')
    vid_js.append(f'tl.to("#v{i}",{{scale:1.0,duration:{max(b-a-0.35,0.1):.2f},ease:"none"}},{a+0.35:.2f});')
    if i > 0:
        vid_js.append(f'tl.fromTo("#flash",{{opacity:0.75}},{{opacity:0,duration:0.14,ease:"power1.out"}},{a:.2f});')

# ---------------------------------------------------------------- sfx
SFX = [  # (time, file, volume)
    (0.00, "impact", 0.55), (0.02, "whoosh", 0.35), (0.50, "whoosh", 0.35), (1.00, "whoosh", 0.35),
    (1.55, "swoosh", 0.35), (1.70, "pop", 0.4), (2.96, "ding", 0.25),
    (4.20, "swoosh", 0.35), (4.40, "pop", 0.4),
    (5.35, "whoosh", 0.35), (5.80, "tick", 0.5), (6.78, "pop", 0.4),
    (7.75, "swoosh", 0.35), (8.10, "pop", 0.4), (9.20, "whoosh", 0.3), (9.90, "pop", 0.4),
    (11.55, "whoosh", 0.35), (12.70, "impact", 0.4),
    (13.85, "swoosh", 0.3), (14.00, "impact", 0.45),
    (15.05, "whoosh", 0.35), (15.30, "riser", 0.3), (16.75, "ding", 0.3),
    (18.20, "swoosh", 0.35), (18.40, "pop", 0.4),
    (21.10, "whoosh", 0.35), (21.30, "pop", 0.4), (22.50, "pop", 0.4),
    (24.40, "whoosh", 0.35), (24.70, "pop", 0.4),
    (26.15, "whoosh", 0.35), (26.30, "cash", 0.4), (27.70, "impact", 0.45),
    (28.75, "swoosh", 0.35), (29.10, "zap", 0.35),
    (30.45, "whoosh", 0.35), (30.90, "riser", 0.3), (32.10, "ding", 0.3), (32.90, "pop", 0.4),
]
# counter ticks while the LCD counts up
t = 18.75
while t < 20.9:
    SFX.append((round(t, 2), "tick", 0.25)); t += 0.16
DUR = {"impact": .9, "whoosh": .45, "swoosh": .35, "pop": .12, "ding": 1.2, "tick": .03,
       "riser": 1.2, "cash": 1.0, "zap": .35}
sfx_html = []
for i, (s, f, v) in enumerate(SFX):
    d = min(DUR[f], TOTAL - s)
    sfx_html.append(f'<audio class="sfx" id="s{i}" src="assets/sfx/{f}.wav" data-start="{s:.2f}" '
                    f'data-duration="{d:.2f}" data-volume="{round(v*0.15,4)}" data-track-index="{30 + i % 4}"></audio>')

tpl = open(sys.argv[3]).read()
out = (tpl.replace("{{TOTAL}}", f"{TOTAL}")
          .replace("{{VIDEOS}}", "\n      ".join(vid_html))
          .replace("{{CAPTIONS}}", "\n      ".join(cap_html))
          .replace("{{SFX}}", "\n      ".join(sfx_html))
          .replace("/*{{VIDJS}}*/", "\n      ".join(vid_js))
          .replace("/*{{CAPJS}}*/", "\n      ".join(cap_js)))
open(OUT, "w").write(out)
print("chunks", len(cap_html), "sfx", len(SFX))
