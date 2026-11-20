"""Task 3: text-driven V-Stepper ad (no voiceover). Footage keeps its own sound at 30%."""
import re, sys

TEMPLATE, OUT = sys.argv[1], sys.argv[2]
TOTAL = 38.0
FOOTAGE_VOL = 0.3
SFX_GAIN = 0.15

CUTS = [  # (start, end, file, media_start) -- shots not used in earlier videos
    (0.0, 3.5, "f3", 1.0),     # HOOK: kaki + kettlebell atas stepper
    (3.5, 10.0, "f12", 0.0),   # K1: tak pakai kasut (bilik gelap, kasut putih)
    (10.0, 13.5, "f11", 2.0),  # K2: terlalu laju (bilik gelap, tali)
    (13.5, 17.0, "f6", 6.0),   # K2 (sambung): trek luar (muted: bunyi bermuzik)
    (17.0, 20.5, "f8", 3.0),   # K3: tak konsisten (trek luar, topi)
    (20.5, 23.5, "f10", 4.0),  # K3 (sambung): bilik gelap
    (23.5, 27.0, "f5", 54.0),  # USP: skrin counter dipegang (muted: ada muzik)
    (27.0, 31.0, "f16", 4.0),  # USP: timbang stepper 5.90kg (bahagian lain klip)
    (31.0, 34.0, "f14", 6.0),  # CTA: azam tahun baru (ruang tamu, baju merah)
    (34.0, TOTAL, "f7", 11.0), # CTA: luar, tali rintangan diangkat
]
MUTED = {"f5", "f6"}

SFX = [
    (0.00, "whoosh", 0.35), (0.05, "zap", 0.4), (0.30, "impact", 0.55), (1.00, "pop", 0.4),
    (3.50, "whoosh", 0.35), (3.60, "impact", 0.4), (4.75, "impact", 0.35), (5.00, "zap", 0.35), (6.30, "pop", 0.4), (8.00, "ding", 0.3),
    (10.00, "whoosh", 0.35), (10.10, "impact", 0.4), (11.10, "riser", 0.3), (12.20, "zap", 0.4), (13.30, "swoosh", 0.35), (15.00, "ding", 0.3),
    (17.00, "whoosh", 0.35), (17.10, "impact", 0.4), (17.90, "pop", 0.3), (18.26, "pop", 0.3), (18.62, "pop", 0.3), (18.98, "pop", 0.3), (19.60, "zap", 0.35), (21.20, "ding", 0.3),
    (23.50, "whoosh", 0.35), (23.85, "ding", 0.3),
    (27.00, "whoosh", 0.35), (27.20, "pop", 0.4), (27.80, "ding", 0.3), (28.55, "swoosh", 0.35),
    (31.00, "whoosh", 0.35), (31.45, "impact", 0.45),
    (34.00, "whoosh", 0.35), (34.10, "pop", 0.4), (34.80, "ding", 0.3), (35.00, "pop", 0.4),
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
