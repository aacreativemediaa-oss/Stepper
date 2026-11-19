"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 30.0
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f17", 1.5),    # HOOK: 10 minit latihan stepper
    (3.5, 6.5, "f19", 0.0),    # EDU: kalori ikut berat badan
    (6.5, 10.8, "f2", 2.0),    # EDU: jadual kalori
    (10.8, 15.0, "f9", 0.0),   # EDU: jadual kalori (sambung)
    (15.0, 19.0, "f5", 50.9),  # USP: pasang bateri counter (muted: ada muzik)
    (19.0, 22.5, "f5", 68.6),  # USP: tekan counter (muted)
    (22.5, 26.0, "f15", 0.5),  # CTA: nak badan fit 2027
    (26.0, TOTAL, "f1", 8.0),  # CTA: grab stepper kat beg kuning
]
MUTED = {"f5"}

SFX = [
    (0.00, "whoosh", 0.35), (0.20, "tick", 0.5), (0.30, "impact", 0.55), (0.95, "pop", 0.4), (1.80, "swoosh", 0.35),
    (3.50, "whoosh", 0.35), (3.85, "impact", 0.4), (4.40, "pop", 0.4),
    (6.50, "whoosh", 0.35), (6.80, "pop", 0.4),
    (7.20, "pop", 0.35), (8.10, "pop", 0.35), (9.00, "pop", 0.35), (9.90, "pop", 0.35), (10.80, "pop", 0.35), (11.70, "ding", 0.3),
    (15.00, "whoosh", 0.35), (15.35, "ding", 0.3),
    (19.00, "swoosh", 0.35), (19.20, "pop", 0.4), (19.90, "pop", 0.4), (20.60, "pop", 0.4),
    (22.50, "whoosh", 0.35), (23.00, "swoosh", 0.35), (23.80, "impact", 0.45),
    (26.00, "whoosh", 0.35), (26.10, "pop", 0.4), (26.80, "ding", 0.3), (27.00, "pop", 0.4),
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
