"""Per-clip loudness matching for original footage sound.

Rule (STYLE.md): each clip's original sound is set to -57 LUFS, or 27 dB below the
voiceover when the VO is not at the usual ~-30 LUFS. Louder clips are turned down;
quieter clips are turned up, but never by more than +12 dB, so background hiss does
not get pushed up too far. Clips listed as muted (they contain music) stay muted.

Usage as a module:
    from footage_gain import clip_volumes
    vols = clip_volumes(cuts, video_dir, vo_path=None)   # {index: data-volume}

Usage from the shell (prints a table):
    python3 footage_gain.py VIDEO_DIR [VO_PATH] FILE:MEDIA_START:DURATION ...
"""
import math
import re
import subprocess
import sys

TARGET_LUFS = -57.0
VO_GAP_DB = 27.0
USUAL_VO_LUFS = -30.0
VO_TOLERANCE_LU = 1.0
MAX_BOOST_DB = 12.0
SILENT_LUFS = -70.0  # ffmpeg's absolute gate: anything at/below this reads as silence


def integrated_lufs(path, start=None, duration=None):
    cmd = ["ffmpeg", "-nostats", "-hide_banner"]
    if start is not None:
        cmd += ["-ss", f"{start}"]
    if duration is not None:
        cmd += ["-t", f"{duration}"]
    cmd += ["-i", path, "-vn", "-af", "ebur128", "-f", "null", "-"]
    err = subprocess.run(cmd, capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[0-9.]+|-inf)\s+LUFS", err)
    if not m:
        return None  # no audio stream
    v = m[-1]
    return -math.inf if v == "-inf" else float(v)


def target_lufs(vo_path=None):
    if not vo_path:
        return TARGET_LUFS, None
    vo = integrated_lufs(vo_path)
    if vo is None or not math.isfinite(vo) or abs(vo - USUAL_VO_LUFS) <= VO_TOLERANCE_LU:
        return TARGET_LUFS, vo
    return vo - VO_GAP_DB, vo


def gain_db(measured, target):
    if measured is None or not math.isfinite(measured) or measured <= SILENT_LUFS:
        return MAX_BOOST_DB  # (near) silent clip: allow the capped boost only
    return min(target - measured, MAX_BOOST_DB)


def clip_volumes(cuts, video_dir, vo_path=None, muted=()):
    """cuts: [(start, end, file_stem, media_start), ...] -> ({i: volume}, report rows)."""
    target, vo = target_lufs(vo_path)
    vols, rows = {}, []
    for i, (a, b, src, ms) in enumerate(cuts):
        if src in muted:
            rows.append((i, src, ms, b - a, None, None, 0.0))
            continue
        lufs = integrated_lufs(f"{video_dir}/{src}.mp4", ms, b - a)
        g = gain_db(lufs, target)
        vol = round(10 ** (g / 20), 4)
        vols[i] = vol
        rows.append((i, src, ms, b - a, lufs, g, vol))
    return vols, rows, target, vo


def print_report(rows, target, vo):
    print(f"VO: {vo if vo is not None else '-'} LUFS  ->  footage target {target:.1f} LUFS")
    for i, src, ms, d, lufs, g, vol in rows:
        if lufs is None and g is None:
            print(f"  #{i:<2} {src:<4} @{ms:>5.1f} {d:4.1f}s  MUTED (music)")
        else:
            lv = "silent" if lufs is None or not math.isfinite(lufs) else f"{lufs:6.1f}"
            print(f"  #{i:<2} {src:<4} @{ms:>5.1f} {d:4.1f}s  {lv} LUFS  gain {g:+5.1f} dB  volume {vol}")


if __name__ == "__main__":
    vdir, rest = sys.argv[1], sys.argv[2:]
    vo = rest.pop(0) if rest and ":" not in rest[0] else None
    cuts, t = [], 0.0
    for spec in rest:
        f, ms, d = spec.split(":")
        cuts.append((t, t + float(d), f, float(ms))); t += float(d)
    _, rows, target, vo_l = clip_volumes(cuts, vdir, vo)
    print_report(rows, target, vo_l)
