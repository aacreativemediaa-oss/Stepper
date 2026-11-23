"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 44.5
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f13", 6.0),    # HOOK: close-up kasut
    (3.5, 10.0, "f7", 1.0),    # K1 laju: luar, tali (baju putih)
    (10.0, 17.0, "f17", 4.0),  # K2 kasut sukan: close-up kaki/kasut
    (17.0, 23.5, "f19", 3.0),  # K3 konsisten: dumbbell depan TV
    (23.5, 27.0, "f5", 68.6),  # USP counter: tekan counter (muted: ada muzik)
    (27.0, 31.0, "f16", 2.9),  # USP <6kg: timbang 5.9kg
    (31.0, 37.5, "f2", 2.0),   # USP otot seluruh badan: dumbbell depan TV
    (37.5, 40.5, "f15", 2.0),  # CTA 2027 upgrade body
    (40.5, TOTAL, "f18", 10.0),# CTA start stepper sekarang
]
MUTED = {"f5"}

SFX = [
    (0.00, "whoosh", 0.35), (0.05, "zap", 0.4), (0.30, "impact", 0.55), (1.00, "pop", 0.4), (3.50, "whoosh", 0.35), (3.60, "impact", 0.4), (10.00, "whoosh", 0.35), (10.10, "impact", 0.4), (17.00, "whoosh", 0.35), (17.10, "impact", 0.4), (4.60, "riser", 0.3), (5.70, "zap", 0.4), (7.30, "impact", 0.35), (8.40, "ding", 0.3), (11.25, "impact", 0.35), (11.50, "zap", 0.35), (12.90, "pop", 0.4), (14.60, "ding", 0.3), (17.90, "pop", 0.3), (18.26, "pop", 0.3), (18.62, "pop", 0.3), (18.98, "pop", 0.3), (19.80, "impact", 0.4), (21.00, "ding", 0.3), (23.50, "whoosh", 0.35), (23.85, "ding", 0.3), (24.80, "pop", 0.35), (25.20, "pop", 0.35), (25.60, "pop", 0.35), (27.00, "whoosh", 0.35), (27.25, "pop", 0.4), (27.80, "ding", 0.3), (31.00, "whoosh", 0.35), (31.10, "impact", 0.4), (31.80, "riser", 0.25), (33.20, "pop", 0.35), (33.65, "pop", 0.35), (34.10, "pop", 0.35), (34.55, "pop", 0.35), (35.00, "pop", 0.35), (37.50, "whoosh", 0.35), (38.00, "swoosh", 0.35), (38.80, "impact", 0.45), (40.50, "whoosh", 0.35), (40.60, "pop", 0.4), (41.20, "ding", 0.3),
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
