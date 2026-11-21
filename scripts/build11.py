"""Generate the Hyperframes composition (index.html) for the stepper ad."""
import json, sys, html

TRANSCRIPT, OUT = sys.argv[1], sys.argv[2]
TOTAL = 46.3

# ---------------------------------------------------------------- edit plan
# (output_start, output_end, source, media_start)
CUTS = [
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
VO_PATH = OUT.rsplit("/", 1)[0] + "/assets/vo.wav"

# ---------------------------------------------------------------- captions
FIX = {"gelebi": "gelebeh", "beresuap": "briskwalk", "latih": "dilatih", "virus": "viral", "bekon": "beg kuning"}
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
    (5.3, 7.65, "15 MINIT STEPPER SETARA 30 MINIT BRISKWALK BIASA"), (8.5, 9.45, "TOTAL BODY WORKOUT"),
    (9.5, 12.5, "OTOT LENGAN PERUT KAKI SERENTAK DILATIH"), (12.8, 14.5, "5 MINIT BERPELUH LENCUN"),
    (16.2, 17.55, "TRIM GELEBEH KAT RUMAH"), (20.1, 22.1, "TAMPUNG LEBIH 100KG"), (22.1, 23.1, "SELAMAT"),
    (23.15, 25.3, "COMPACT RINGAN"), (25.9, 27.7, "DEPAN TV DALAM BILIK"),
    (27.8, 31.2, "ADA DIGITAL COUNTER SEKALI KALORI STEPS TRACK JUMLAH"), (31.3, 33.15, "HAMPIR 400,000 UNIT TERJUAL"),
    (34.4, 36.9, "RAMAI BAGI FEEDBACK POSITIF BILA LATIHAN STEPPER"), (37.0, 39.75, "DULU BERATUS RINGGIT"), (39.75, 41.1, "SEKARANG MURAH"),
    (41.1, 42.15, "RUGI TAK GRAB"), (42.2, 43.8, "PILIH WARNA BEG KUNING BAWAH"),
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
HOOK_END = 3.6
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
