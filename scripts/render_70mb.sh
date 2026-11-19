#!/usr/bin/env bash
# Render a Hyperframes project at 1080x1920 60fps with the output file at most 70 MB.
# Usage: render_70mb.sh PROJECT_DIR OUTPUT.mp4 [TARGET_MB]
# The video bitrate is computed from the duration so the file lands just under the target
# (3% headroom for the container). If the encoder still overshoots, the video is re-encoded
# with a 2-pass x264 at the exact bitrate, keeping the audio untouched.
set -euo pipefail
PROJ="$1"; OUT="$2"; TARGET_MB="${3:-70}"
AUDIO_KBPS=192
LIMIT=$((TARGET_MB * 1000 * 1000))

DUR=$(grep -o 'data-composition-id="main"[^>]*data-duration="[0-9.]*"' "$PROJ/index.html" | grep -o 'data-duration="[0-9.]*"' | grep -o '[0-9.]*')
VKBPS=$(python3 -c "print(int(${TARGET_MB}*8000*0.97/${DUR} - ${AUDIO_KBPS}))")
echo "duration ${DUR}s -> video ${VKBPS} kbps (target ${TARGET_MB} MB)"

(cd "$PROJ" && npx hyperframes render --fps 60 --quality delivery --workers 4 \
   --video-bitrate "${VKBPS}k" --max-bitrate "$((VKBPS * 12 / 10))k" -o "$OUT")

SIZE=$(stat -c %s "$OUT")
if [ "$SIZE" -gt "$LIMIT" ]; then
  echo "render is $SIZE bytes (> $LIMIT); 2-pass re-encode to ${VKBPS} kbps"
  TMP="$(dirname "$OUT")/.2pass_$$"; mkdir -p "$TMP"
  ffmpeg -v error -y -i "$OUT" -c:v libx264 -preset slow -b:v "${VKBPS}k" -pass 1 -passlogfile "$TMP/log" -an -f mp4 /dev/null
  ffmpeg -v error -y -i "$OUT" -c:v libx264 -preset slow -b:v "${VKBPS}k" -pass 2 -passlogfile "$TMP/log" \
         -pix_fmt yuv420p -r 60 -c:a copy -movflags +faststart "$TMP/out.mp4"
  mv "$TMP/out.mp4" "$OUT"; rm -rf "$TMP"
fi
SIZE=$(stat -c %s "$OUT")
echo "final: $OUT  $(python3 -c "print(round($SIZE/1e6,1))") MB"
[ "$SIZE" -le "$LIMIT" ] || { echo "ERROR: still over ${TARGET_MB} MB" >&2; exit 1; }
