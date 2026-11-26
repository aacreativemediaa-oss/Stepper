"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 44.0
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f8", 3.0),     # HOOK: trek luar, topi
    (3.5, 11.5, "f19", 1.0),   # EDU1 kalori 15 minit: dumbbell depan TV
    (11.5, 18.5, "f7", 3.0),   # EDU2 otot & koordinasi: luar, tali resistance
    (18.5, 24.5, "f3", 2.0),   # EDU3 ruang & peralatan: dalam bilik, kettlebell
    (24.5, 29.5, "f13", 1.0),  # TIPS kasut: close-up kasut atas stepper
    (29.5, 33.0, "f5", 50.9),  # USP digital counter: pasang bateri (muted: ada muzik)
    (33.0, 37.0, "f16", 2.9),  # USP tak berat: timbang 5.9kg
    (37.0, 40.0, "f15", 2.0),  # CTA raya 2027
    (40.0, TOTAL, "f18", 4.0), # CTA start stepper sekarang
]
MUTED = {"f5"}

SFX = [
    (0.05, "whoosh", 0.35), (0.35, "swoosh", 0.35), (0.65, "impact", 0.55), (1.20, "pop", 0.4), (3.50, "whoosh", 0.35), (3.55, "pop", 0.4), (11.50, "whoosh", 0.35), (11.55, "pop", 0.4), (18.50, "whoosh", 0.35), (18.55, "pop", 0.4), (24.50, "whoosh", 0.35), (24.55, "pop", 0.4), (4.10, "pop", 0.3), (4.90, "pop", 0.3), (5.70, "pop", 0.3), (6.50, "pop", 0.3), (7.30, "pop", 0.3), (8.10, "pop", 0.3), (9.50, "impact", 0.45), (9.60, "ding", 0.3), (12.30, "riser", 0.25), (12.90, "pop", 0.3), (13.30, "pop", 0.3), (13.90, "pop", 0.3), (14.30, "pop", 0.3), (14.90, "ding", 0.25), (19.00, "impact", 0.35), (19.70, "pop", 0.3), (20.25, "pop", 0.3), (20.80, "pop", 0.3), (21.35, "pop", 0.3), (21.90, "pop", 0.3), (22.45, "pop", 0.3), (25.20, "swoosh", 0.3), (25.65, "impact", 0.35), (26.80, "pop", 0.4), (29.50, "whoosh", 0.35), (29.85, "ding", 0.3), (30.80, "pop", 0.35), (31.20, "pop", 0.35), (31.60, "pop", 0.35), (33.00, "whoosh", 0.35), (33.25, "pop", 0.4), (33.80, "ding", 0.3), (37.00, "whoosh", 0.35), (37.50, "swoosh", 0.35), (38.30, "impact", 0.45), (40.00, "whoosh", 0.35), (40.10, "pop", 0.4), (40.70, "ding", 0.3),
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
