"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 35.0
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start)
    (0.0, 3.5, "f13", 2.0),    # HOOK: 3 cara
    (3.5, 5.5, "f19", 0.0),    # MINI HOOK: save video
    (5.5, 10.5, "f2", 2.0),    # EDU 1: bakar kalori cepat
    (10.5, 13.3, "f9", 0.0),   # EDU 2: total body (badan penuh)
    (13.3, 16.5, "f17", 3.0),  # EDU 2: punggung/peha/betis close-up
    (16.5, 21.0, "f14", 1.0),  # EDU 3: low intensity, dalam rumah
    (21.0, 25.0, "f16", 2.9),  # USP: timbang stepper, penimbang 5.90kg
    (25.0, 28.5, "f5", 68.6),  # USP: multifunction counter (muted: ada muzik)
    (28.5, 31.5, "f15", 0.5),  # CTA: trim gelebeh sebelum raya
    (31.5, TOTAL, "f1", 8.0),  # CTA: start workout sekarang
]
MUTED = {"f5"}

SFX = [
    (0.05, "impact", 0.55), (0.05, "whoosh", 0.35), (0.75, "pop", 0.4), (1.20, "impact", 0.4),
    (3.50, "whoosh", 0.35), (3.60, "pop", 0.4), (4.50, "ding", 0.3),
    (5.50, "whoosh", 0.35), (5.60, "impact", 0.4), (6.50, "pop", 0.4), (8.50, "ding", 0.3),
    (10.50, "whoosh", 0.35), (10.60, "impact", 0.4), (11.30, "pop", 0.4),
    (12.40, "pop", 0.35), (12.95, "pop", 0.35), (13.50, "pop", 0.35), (14.05, "pop", 0.35), (14.60, "pop", 0.35),
    (16.50, "whoosh", 0.35), (16.60, "impact", 0.4), (17.60, "pop", 0.4), (18.40, "pop", 0.4),
    (21.00, "whoosh", 0.35), (21.20, "pop", 0.4), (21.80, "ding", 0.3), (22.60, "swoosh", 0.35),
    (25.00, "whoosh", 0.35), (25.35, "ding", 0.3),
    (28.50, "whoosh", 0.35), (29.00, "pop", 0.4),
    (31.50, "whoosh", 0.35), (31.60, "impact", 0.45), (32.30, "pop", 0.4), (33.00, "ding", 0.3),
]
DUR = {"impact": .9, "whoosh": .45, "swoosh": .35, "pop": .12, "ding": 1.2, "tick": .03,
       "riser": 1.2, "cash": 1.0, "zap": .35}

vid_html, vid_js = [], []
for i, (a, b, src, ms) in enumerate(CUTS):
    vid_html.append(
        (f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" muted playsinline ' if src in MUTED else
         f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" playsinline data-has-audio="true" data-volume="{FOOTAGE_VOL}" ') +
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
