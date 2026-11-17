"""Generate the Hyperframes composition (index.html) for the stepper ad."""
import json, sys, html

TRANSCRIPT, OUT = sys.argv[1], sys.argv[2]
TOTAL = 33.4

# ---------------------------------------------------------------- edit plan
# (output_start, output_end, source, media_start)
CUTS = [
    (0.00, 3.40, "f13", 2.0),   # hook
    (3.40, 7.50, "f19", 0.0),   # start + total body
    (7.50, 11.80, "f9", 0.0),   # kaki + satu badan serentak
    (11.80, 16.20, "f2", 2.0),  # 5 minit berpeluh lencun
    (16.20, 19.40, "f5", 50.9), # pasang bateri counter (bunyi asal dimatikan: ada muzik)
    (19.40, 20.85, "f16", 2.5), # counter atas stepper
    (20.85, 23.60, "f14", 1.0), # beginners / kat rumah
    (23.60, 26.20, "f7", 2.0),  # 10,000 langkah
    (26.20, 30.10, "f15", 0.5), # harga murah / rugi
    (30.10, TOTAL, "f1", 8.0),  # CTA
]
MUTED = {"f5"}
FOOTAGE_VOL = 0.3

# ---------------------------------------------------------------- captions
FIX = {"gelebi": "gelebeh"}
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
        if txt.startswith(",") and words:
            words[-1]["t"] += txt; words[-1]["e"] = round(w["e"], 2); continue
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
        if len(cur) == 1 and chunks and len(chunks[-1]) <= 3 and cur[0]["s"] - chunks[-1][-1]["e"] < 0.3:
            chunks[-1].extend(cur)
        else:
            chunks.append(cur)
        cur = []


# On-screen graphics (start, end, text). A caption chunk that overlaps a graphic in time and
# repeats >=50% of its content words is dropped, so the same sentence never shows twice.
GFX = [
    (3.9, 5.35, "START JE"), (6.2, 7.6, "TOTAL BODY WORKOUT"),
    (8.2, 11.8, "KAKI SATU BADAN SERENTAK"),
    (12.8, 16.2, "5 MINIT BERPELUH LENCUN KALORI BANYAK TERBAKAR"),
    (16.3, 17.5, "PALING BEST"), (17.5, 19.45, "SIAP ADA MULTIFUNCTION COUNTER"),
    (19.5, 20.85, "TRACK STEPS KALORI BURN"),
    (21.3, 23.65, "SESUAI UNTUK BEGINNERS BERSENAM KAT RUMAH"),
    (24.6, 26.2, "10,000 LANGKAH SEHARI"), (27.4, 28.85, "HARGA TENGAH MURAH"),
    (28.85, 30.1, "RUGI TAK GRAB"), (30.2, 33.4, "SEBELUM STOCK HABIS CHECK OUT SEKARANG LINK KAT BAWAH NI"),
]
STOP = {"DAN","YANG","NAK","KORANG","JE","TAU","PUN","SO","TU","DIA","NI","SANGAT","BETTER","ATAUPUN","SEBAB","AKU","DAH","KAN","TAPI","BUAT"}
def _norm(s): return s.upper().strip(",.?!")
def dup_of_graphic(ch, start, end):
    words = [_norm(w["t"]) for w in ch]
    content = [w for w in words if w not in STOP]
    if not content: return False
    for gs, ge, gt in GFX:
        if start < ge and end > gs:
            g = set(_norm(x) for x in gt.split())
            if sum(w in g for w in content) / len(content) >= 0.5:
                return True
    return False

# hook (first sentence) is rendered as the big hook title instead of a caption
HOOK_END = 3.3
cap_html, cap_js = [], []
prev_dropped = False
for ci, ch in enumerate(chunks):
    if ch[-1]["e"] <= HOOK_END + 0.01:
        continue
    start = ch[0]["s"]
    nxt_start = chunks[ci + 1][0]["s"] if ci + 1 < len(chunks) else TOTAL
    end = min(max(ch[-1]["e"] + 0.15, start + 0.4), nxt_start)
    if ci + 1 == len(chunks):
        end = TOTAL - 0.05
    content_n = len([w for w in ch if _norm(w["t"]) not in STOP])
    if dup_of_graphic(ch, start, end) or (prev_dropped and content_n <= 1):
        print("drop caption:", " ".join(w["t"] for w in ch)); prev_dropped = True; continue
    prev_dropped = False
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
        (f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" muted playsinline ' if src in MUTED else
         f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" playsinline data-has-audio="true" data-volume="{FOOTAGE_VOL}" ')
        +
        f'data-start="{a:.2f}" data-duration="{b-a:.2f}" data-media-start="{ms:.2f}" data-track-index="1"></video>')
    # punch-in at the cut, then a slow push
    vid_js.append(f'tl.fromTo("#v{i}",{{scale:1.18}},{{scale:1.04,duration:0.35,ease:"power3.out"}},{a:.2f});')
    vid_js.append(f'tl.to("#v{i}",{{scale:1.0,duration:{max(b-a-0.35,0.1):.2f},ease:"none"}},{a+0.35:.2f});')
    if i > 0:
        vid_js.append(f'tl.fromTo("#flash",{{opacity:0.75}},{{opacity:0,duration:0.14,ease:"power1.out",immediateRender:false}},{a:.2f});')

# ---------------------------------------------------------------- sfx
SFX = [  # (time, file, volume)
    (0.05, "impact", 0.55), (0.05, "whoosh", 0.35), (0.75, "impact", 0.4), (1.55, "swoosh", 0.35), (2.30, "pop", 0.4), (2.70, "pop", 0.4),
    (3.40, "whoosh", 0.35), (3.90, "pop", 0.4), (6.20, "swoosh", 0.3), (6.68, "impact", 0.4),
    (7.50, "whoosh", 0.35), (8.25, "pop", 0.4), (9.95, "pop", 0.4), (11.10, "pop", 0.4),
    (11.80, "swoosh", 0.35), (12.85, "tick", 0.5), (13.80, "pop", 0.4), (14.65, "ding", 0.25),
    (16.20, "whoosh", 0.35), (16.40, "impact", 0.45), (17.70, "ding", 0.3),
    (19.40, "swoosh", 0.35), (19.70, "pop", 0.4), (20.20, "pop", 0.4),
    (20.85, "whoosh", 0.35), (21.35, "pop", 0.4), (22.75, "pop", 0.4),
    (23.60, "whoosh", 0.35), (24.60, "riser", 0.25), (25.35, "ding", 0.3),
    (26.20, "whoosh", 0.35), (27.45, "cash", 0.4), (28.80, "impact", 0.45),
    (30.10, "whoosh", 0.35), (30.30, "pop", 0.4), (31.50, "ding", 0.3), (31.60, "pop", 0.4),
]
# counter ticks while the LCD counts up
t = 18.75
while t < 20.9:
    t += 99
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
