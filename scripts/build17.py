"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 39.5
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f6", 6.0),     # HOOK: trek luar, berjalan (muted: muzik)
    (3.5, 10.0, "f13", 2.0),   # EDU1 jenis pergerakan: close-up langkah stepper
    (10.0, 18.0, "f12", 1.0),  # EDU2 kalori: bilik, tali
    (18.0, 25.0, "f9", 1.0),   # EDU3 otot: tali resistance
    (25.0, 28.5, "f5", 54.0),  # USP counter: counter dipegang (muted: ada muzik)
    (28.5, 32.5, "f16", 2.9),  # USP <6kg: timbang 5.9kg
    (32.5, 35.5, "f14", 3.0),  # CTA 2027 upgrade body
    (35.5, TOTAL, "f1", 6.0),  # CTA start stepper sekarang
]
MUTED = {"f5", "f6"}

SFX = [
    (0.05, "whoosh", 0.35), (0.35, "swoosh", 0.35), (0.65, "impact", 0.55), (1.20, "pop", 0.4), (3.50, "whoosh", 0.35), (3.55, "pop", 0.4), (3.70, "swoosh", 0.3), (10.00, "whoosh", 0.35), (10.05, "pop", 0.4), (10.20, "swoosh", 0.3), (18.00, "whoosh", 0.35), (18.05, "pop", 0.4), (18.20, "swoosh", 0.3), (4.00, "impact", 0.35), (4.90, "pop", 0.3), (5.45, "pop", 0.3), (6.00, "pop", 0.3), (6.55, "pop", 0.3), (7.10, "pop", 0.3), (7.65, "pop", 0.3), (10.60, "pop", 0.3), (11.40, "pop", 0.3), (12.20, "pop", 0.3), (13.00, "pop", 0.3), (13.80, "pop", 0.3), (14.60, "pop", 0.3), (16.00, "impact", 0.45), (16.10, "ding", 0.3), (18.80, "riser", 0.25), (19.20, "pop", 0.3), (19.50, "pop", 0.3), (20.60, "pop", 0.3), (21.00, "pop", 0.3), (21.40, "pop", 0.3), (25.00, "whoosh", 0.35), (25.35, "ding", 0.3), (26.30, "pop", 0.35), (26.70, "pop", 0.35), (27.10, "pop", 0.35), (28.50, "whoosh", 0.35), (28.75, "pop", 0.4), (29.30, "ding", 0.3), (32.50, "whoosh", 0.35), (33.00, "swoosh", 0.35), (33.80, "impact", 0.45), (35.50, "whoosh", 0.35), (35.60, "pop", 0.4), (36.20, "ding", 0.3),
]
DUR = {"impact": .9, "whoosh": .45, "swoosh": .35, "pop": .12, "ding": 1.2, "tick": .03,
       "riser": 1.2, "cash": 1.0, "zap": .35}

sys.path.insert(0, "/home/user/Stepper/scripts")
from footage_gain import clip_volumes, print_report
VIDEO_DIR = OUT.rsplit("/", 1)[0] + "/assets/video"
VOLS, _rows, _t, _vo = clip_volumes(CUTS, VIDEO_DIR, None, MUTED)
print_report(_rows, _t, _vo)
vid_html, vid_js = [], []
for i, (a, b, src, ms) in enumerate(CUTS):
    vid_html.append(
        (f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" muted playsinline ' if src in MUTED else
         f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" playsinline data-has-audio="true" data-volume="{VOLS[i]}" ') +
        f'data-start="{a:.2f}" data-duration="{b-a:.2f}" '
        f'data-media-start="{ms:.2f}" data-track-index="1"></video>')
    vid_js.append(f'tl.fromTo("#v{i}",{{scale:1.18}},{{scale:1.04,duration:0.35,ease:"power3.out"}},{a:.2f});')
    vid_js.append(f'tl.to("#v{i}",{{scale:1.0,duration:{max(b-a-0.35,0.1):.2f},ease:"none"}},{a+0.35:.2f});')
    if i > 0:
        vid_js.append(f'tl.fromTo("#flash",{{opacity:0.75}},{{opacity:0,duration:0.14,ease:"power1.out",immediateRender:false}},{a:.2f});')

sfx_html = []
for i, (s, f, v) in enumerate(SFX):
    d = min(DUR[f], TOTAL - s)
    sfx_html.append(f'<audio class="sfx" id="s{i}" src="assets/sfx/{f}.wav" data-start="{s:.2f}" '
                    f'data-duration="{d:.2f}" data-volume="{round(v*SFX_GAIN,4)}" data-track-index="{30 + i % 4}"></audio>')

t = open(TEMPLATE).read()
t = (t.replace("{{TOTAL}}", f"{TOTAL}")
      .replace("{{VIDEOS}}", "\n      ".join(vid_html))
      .replace("{{SFX}}", "\n      ".join(sfx_html))
      .replace("/*{{VIDJS}}*/", "\n      ".join(vid_js)))
open(OUT, "w").write(t)
print("clips", len(CUTS), "sfx", len(SFX))
