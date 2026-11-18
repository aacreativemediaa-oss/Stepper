# Style edit video (rujukan tetap)

Style yang diluluskan untuk video stepper (Task 1). Guna semula untuk video seterusnya.

## Format
- 1080×1920 menegak, 60fps, Hyperframes (`hyperframes/`), render `--quality delivery`.
- Tiada muzik latar. Voiceover asal **tidak diubah** (volume 1, tiada potongan).
- Bunyi asal footage: 30%. Footage yang bunyinya ada muzik (lv_0_20250521120347, video_20260531_203850) dimatikan/dielakkan.
- Sebelum render akhir: tunjuk draf caption kepada pengguna untuk disemak.

## Potongan
- Maksimum ~10 klip setiap video (~3–4 saat setiap klip). Intro: satu shot sahaja, jangan tukar laju.
- Setiap klip: punch-in zoom 1.18→1.04 (0.35s) kemudian push perlahan ke 1.0; kilatan putih ringkas di setiap potongan (bukan di frame pertama).
- Bunyi asal footage pada 30% (lihat atas), kecuali footage bermuzik dimatikan.
- Babak produk/fitur: guna footage sebenar yang tunjuk fitur tu (cth. pasang bateri counter), bukan grafik palsu.

## Teks
- Font: Anton (tajuk/caption), Montserrat 800/900 (label/pill). Saiz font = 70% daripada versi pertama.
- **Caption/subtitle: 60px** (mulai Task 5; Task 4 = 65px), stroke hitam 5px.
- **Jangan bertindih:** kalau grafik besar dah tunjuk ayat yang sama, sembunyikan caption untuk ayat tu (guna grafik sahaja). Automatik dalam `scripts/build4.py` (GFX + dup_of_graphic). Keputusan ikut klausa penuh (dipapar semua atau disembunyi semua), sembunyi jika ≥1/3 perkataan utama ada dalam grafik — lihat `scripts/build5.py`.
- Ilustrasi (kalendar, muscle, tapak kaki, api kalori) dilukis sendiri sebagai SVG dalam template bila tiada gambar dalam folder.
- Caption: huruf besar, stroke hitam, perkataan aktif jadi kuning, kata kunci jadi hijau neon; 1–3 perkataan setiap paparan, di tengah (top 1150px).
- Hook: tajuk besar 3 baris, baris akhir atas blok hijau neon condong, dengan bunyi impact + gegar.
- Ejaan pembetulan: "gelebeh" (bukan kelebihan), "raya", "beg kuning".

## Warna
- Pink `#ff2e7e`, hijau neon `#c6ff00`, kuning `#ffd400`, merah `#ff3b30`, putih, hitam.

## Grafik & overlay
- Pill label dengan ikon (✓, rumah, TV, pokok), sticker condong, cop merah, tag harga kuning, graf naik merah, kad CTA putih + pill "beg kuning" + anak panah ke bawah.
- Overlay: vignette, bar progres pink→hijau di atas.
- Tiada nombor/data palsu.

## Sound effect
- Disintesis sendiri (`scripts/sfx.py`): whoosh, swoosh, pop, ding, impact, cha-ching, zap, riser.
- Volume SFX = 0.15 × nilai asas (di bawah voiceover).

## Dua jenis video
- **A. Ada voiceover** (Task 1, 2, 4, 5): transkrip VO → draf caption untuk disemak → grafik ikut masa VO → caption disembunyi bila sama dengan grafik.
- **B. Tiada voiceover, ikut brief** (Task 3, 6): Hook / Mini hook / Education / USP / CTA disampaikan sebagai teks motion graphics; setiap mesej ≥2.5–3 saat supaya sempat dibaca.

## Aliran kerja
1. Muat turun VO + footage dari Drive (folder perlu "Anyone with the link").
2. Transkrip (Whisper large-v3, bahasa Melayu) + semak footage (contact sheet, bunyi, spektrogram untuk kesan muzik).
3. Jenis A: tunjuk draf caption, tunggu "ok".
4. Pilih ≤10 klip ikut ayat/mesej; babak fitur guna footage sebenar (pasang bateri counter, timbang stepper 5.90kg).
5. Bina, lint, snapshot setiap babak dan semak visual.
6. Render 60fps; semak VO masih selari, dan semak frame akhir untuk **setiap** blok grafik (terutama CTA) sebelum hantar.
