"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 27.0
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start)
    (0.0, 3.4, "f13", 2.0),    # HOOK: close-up kaki atas stepper
    (3.4, 6.6, "f2", 2.0),     # EDUCATE: total body workout
    (6.6, 9.4, "f17", 2.0),    # EDUCATE: bukan otot kaki je
    (9.4, 13.0, "f9", 0.0),    # EDUCATE: satu badan bekerja serentak
    (13.0, 17.0, "f19", 3.0),  # USP: support lebih 100kg
    (17.0, 20.2, "f14", 2.0),  # USP: home workout
    (20.2, 23.2, "f15", 2.0),  # CTA: harga murah
    (23.2, TOTAL, "f1", 8.0),  # CTA: grab sekarang, beg kuning
]

SFX = [
    (0.05, "impact", 0.55), (0.05, "whoosh", 0.35), (0.95, "impact", 0.45),
    (3.40, "whoosh", 0.35), (3.55, "pop", 0.4), (4.20, "ding", 0.3),
    (6.60, "swoosh", 0.35), (6.90, "impact", 0.4),
    (9.40, "whoosh", 0.35), (10.40, "pop", 0.4), (10.90, "pop", 0.4), (11.40, "pop", 0.4),
    (13.00, "whoosh", 0.35), (13.20, "riser", 0.3), (14.80, "impact", 0.5),
    (17.00, "swoosh", 0.35), (17.20, "pop", 0.4), (17.70, "ding", 0.3),
    (20.20, "whoosh", 0.35), (20.35, "cash", 0.45),
    (23.20, "whoosh", 0.35), (23.40, "pop", 0.4), (24.40, "ding", 0.3), (25.00, "pop", 0.4),
]
DUR = {"impact": .9, "whoosh": .45, "swoosh": .35, "pop": .12, "ding": 1.2, "tick": .03,
       "riser": 1.2, "cash": 1.0, "zap": .35}

vid_html, vid_js = [], []
for i, (a, b, src, ms) in enumerate(CUTS):
    vid_html.append(
        f'<video class="clip bg" id="v{i}" src="assets/video/{src}.mp4" playsinline data-has-audio="true" '
        f'data-volume="{FOOTAGE_VOL}" data-start="{a:.2f}" data-duration="{b-a:.2f}" '
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
