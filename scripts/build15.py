"""Generate the Hyperframes composition (index.html) for the stepper ad."""
import json, sys, html

TRANSCRIPT, OUT = sys.argv[1], sys.argv[2]
TOTAL = 53.2

# ---------------------------------------------------------------- edit plan
# (output_start, output_end, source, media_start)
CUTS = [
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
MUTED = {"f5", "f6"}
VO_PATH = OUT.rsplit("/", 1)[0] + "/assets/vo.wav"

# ---------------------------------------------------------------- captions
FIX = {}
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
        if (txt.startswith(",") or txt.startswith("-")) and words:
            words[-1]["t"] += txt.replace("gelebi", "gelebeh"); words[-1]["e"] = round(w["e"], 2); continue
        words.append({"t": txt, "s": round(w["s"], 2), "e": round(w["e"], 2),
                      "k": txt.strip(",.?!").lower() in KEY})
    if words: words[-1]["segend"] = True
for i, w in enumerate(words):
    if w["t"].lower() == "sahaja" and i + 1 < len(words) and words[i + 1]["t"].lower().startswith("je"):
        w["t"] = "saja-saja."; w["e"] = words[i + 1]["e"]; w["segend"] = words[i + 1].get("segend"); del words[i + 1]; break
# clause ids: a clause ends at punctuation or at the end of a VO segment
cl = 0
for w in words:
    w["cl"] = cl
    if w["t"][-1] in ",.?!" or w.get("segend"): cl += 1
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
    end_punct = w["t"][-1] in ",.?!" or w.get("segend")
    if nxt is None or end_punct or len(cur) >= 3 or nxt["s"] - w["e"] > 0.25:
        if len(cur) == 1 and chunks and len(chunks[-1]) <= 3 and cur[0]["s"] - chunks[-1][-1]["e"] < 0.3 and chunks[-1][-1]["cl"] == cur[0]["cl"]:
            chunks[-1].extend(cur)
        else:
            chunks.append(cur)
        cur = []


# On-screen graphics (start, end, text). A caption chunk that overlaps a graphic in time and
# repeats >=50% of its content words is dropped, so the same sentence never shows twice.
GFX = [
    (5.65, 7.79, "15 MINIT STEPPER MACAM 30 MINIT BRISKWALK"), (9.14, 10.67, "TOTAL BODY WORKOUT"), (10.74, 13.90, "OTOT LENGAN PERUT KAKI SERENTAK DILATIH"), (14.29, 16.61, "5 MINIT BERPELUH LENCUN"), (18.69, 20.34, "TRIM GELEBEH DALAM RUMAH"), (22.98, 25.48, "TAMPUNG BERAT LEBIH DARIPADA 100KG"), (25.48, 26.54, "SELAMAT"), (26.59, 29.94, "SAIZ COMPACT RINGAN"), (30.57, 32.42, "DEPAN TV DALAM BILIK"), (32.55, 37.98, "DATANG SEKALI DIGITAL COUNTER KALORI STEPS TRACK JUMLAH MUDAH"), (38.13, 41.10, "HAMPIR 400,000 UNIT TERJUAL"), (42.86, 46.28, "DULU HARGA LEBIH RM100"), (46.28, 47.52, "SEKARANG MURAH"), (47.52, 48.69, "RUGI TAK GRAB"), (48.75, 50.52, "PILIH WARNA BEG KUNING BAWAH SEKARANG"),
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
            if sum(w in g for w in content) / len(content) >= 1/3:
                return True
    return False

# hook (first sentence) is rendered as the big hook title instead of a caption
HOOK_END = 4.15
cap_html, cap_js = [], []
# decide per clause: hide the whole clause if >=1/3 of its content words are already on an overlapping graphic
DROPPED = set()
for c in sorted(set(w["cl"] for w in words)):
    cw = [w for w in words if w["cl"] == c]
    if dup_of_graphic(cw, cw[0]["s"], cw[-1]["e"]): DROPPED.add(c)
for ci, ch in enumerate(chunks):
    if ch[-1]["e"] <= HOOK_END + 0.01:
        continue
    start = ch[0]["s"]
    nxt_start = chunks[ci + 1][0]["s"] if ci + 1 < len(chunks) else TOTAL
    end = min(max(ch[-1]["e"] + 0.15, start + 0.4), nxt_start)
    if ci + 1 == len(chunks):
        end = TOTAL - 0.05
    if ch[0]["cl"] in DROPPED:
        print("drop caption:", " ".join(w["t"] for w in ch)); continue
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
sys.path.insert(0, "/home/user/Stepper/scripts")
from footage_gain import clip_volumes, print_report
VOLS, _rows, _t, _vo = clip_volumes(CUTS, OUT.rsplit("/", 1)[0] + "/assets/video", VO_PATH, MUTED)
print_report(_rows, _t, _vo)
vid_html, vid_js = [], []
for i, (a, b, src, ms) in enumerate(CUTS):
    vid_html.append(
        (f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" muted playsinline ' if src in MUTED else
         f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" playsinline data-has-audio="true" data-volume="{VOLS[i]}" ')
        +
        f'data-start="{a:.2f}" data-duration="{b-a:.2f}" data-media-start="{ms:.2f}" data-track-index="1"></video>')
    # punch-in at the cut, then a slow push
    vid_js.append(f'tl.fromTo("#v{i}",{{scale:1.18}},{{scale:1.04,duration:0.35,ease:"power3.out"}},{a:.2f});')
    vid_js.append(f'tl.to("#v{i}",{{scale:1.0,duration:{max(b-a-0.35,0.1):.2f},ease:"none"}},{a+0.35:.2f});')
    if i > 0:
        vid_js.append(f'tl.fromTo("#flash",{{opacity:0.75}},{{opacity:0,duration:0.14,ease:"power1.out",immediateRender:false}},{a:.2f});')

# ---------------------------------------------------------------- sfx
SFX = [  # (time, file, volume)
    (0.00, "whoosh", 0.35), (0.17, "impact", 0.5), (0.79, "pop", 0.4),
    (4.18, "whoosh", 0.35), (5.74, "pop", 0.4), (6.29, "ding", 0.25), (6.56, "pop", 0.4),
    (9.22, "impact", 0.4), (10.59, "whoosh", 0.35), (11.16, "pop", 0.35), (11.64, "pop", 0.35), (12.11, "pop", 0.35), (13.16, "impact", 0.35),
    (14.36, "tick", 0.5), (15.66, "pop", 0.4), (16.61, "whoosh", 0.35), (18.75, "pop", 0.4),
    (22.12, "whoosh", 0.35), (23.11, "riser", 0.25), (24.23, "impact", 0.45), (25.48, "ding", 0.25),
    (26.54, "whoosh", 0.35), (27.44, "pop", 0.4), (29.94, "swoosh", 0.35), (30.63, "pop", 0.4), (31.60, "pop", 0.4),
    (32.42, "whoosh", 0.35), (32.90, "ding", 0.25), (36.10, "pop", 0.4), (37.46, "pop", 0.4),
    (37.98, "whoosh", 0.35), (38.37, "riser", 0.2), (40.06, "impact", 0.4), 
    (43.25, "pop", 0.4), (46.28, "zap", 0.35), (46.75, "cash", 0.4), (47.47, "impact", 0.45),
    (48.75, "whoosh", 0.35), (49.47, "pop", 0.4), (49.96, "ding", 0.25),
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
