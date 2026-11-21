"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 27.5
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start)
    (0.0, 6.0, "f8", 0.0),     # HOOK + jadual kalori (trek luar)
    (6.0, 9.2, "f7", 2.0),     # otot: badan penuh, tali rintangan (luar)
    (9.2, 12.5, "f17", 6.0),   # otot: close-up kaki
    (12.5, 16.0, "f5", 60.0),  # USP: pasang counter pada stepper (muted: ada muzik)
    (16.0, 20.0, "f16", 3.0),  # USP: ringan, timbang 5.9kg
    (20.0, 23.5, "f13", 5.0),  # CTA: fit 2027 (close-up kasut)
    (23.5, TOTAL, "f2", 9.0),  # CTA: grab kat beg kuning
]
MUTED = {"f5"}

SFX = [
    (0.00, "impact", 0.55), (0.05, "whoosh", 0.35), (1.00, "pop", 0.4), (2.00, "ding", 0.3),
    (6.00, "whoosh", 0.35), (6.10, "impact", 0.4), (6.80, "riser", 0.25),
    (8.40, "pop", 0.35), (8.95, "pop", 0.35), (9.50, "pop", 0.35), (10.05, "pop", 0.35), (10.60, "pop", 0.35),
    (12.50, "whoosh", 0.35), (12.85, "ding", 0.3), (14.00, "pop", 0.35), (14.40, "pop", 0.35), (14.80, "pop", 0.35),
    (16.00, "whoosh", 0.35), (16.30, "pop", 0.4), (16.80, "ding", 0.3), (17.55, "swoosh", 0.35),
    (20.00, "whoosh", 0.35), (20.50, "swoosh", 0.35), (21.30, "impact", 0.45),
    (23.50, "whoosh", 0.35), (23.60, "pop", 0.4), (24.20, "ding", 0.3), (24.30, "pop", 0.4),
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
