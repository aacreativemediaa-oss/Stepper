# Format edit video stepper (terkini)

Rujukan tetap untuk setiap video baru. Kemas kini terakhir: sebelum Task 14.

## Output
- 1080×1920 menegak, **60fps**, dibina dengan Hyperframes.
- **Saiz fail ≤70MB**: render dengan `scripts/render_70mb.sh` (bitrate ikut durasi; kalau masih lebih, encode semula 2-pass, audio tak disentuh).
- **Tiada muzik latar.**

## Bunyi
- **Voiceover asal tidak diubah** (volume 100%, tiada potongan).
- **Bunyi asal footage: setiap klip diselaraskan ke −57 LUFS**, atau 27 dB di bawah VO kalau VO bukan sekitar −30 LUFS.
  - Klip yang kuat diperlahankan; klip yang perlahan dikuatkan, **had +12 dB**.
  - Dikira automatik oleh `scripts/footage_gain.py` (ukur segmen yang digunakan sahaja).
- Footage yang bunyinya ada muzik dimatikan: `lv_0_20250521120347`, `video_20260531_203850`.
- Sound effect disintesis sendiri (whoosh, swoosh, pop, ding, impact, cha-ching, zap, riser, tick), volume rendah di bawah VO (0.15 × nilai asas).

## Potongan
- **Maksimum 10 klip.** Intro satu shot sahaja, jangan tukar laju.
- Setiap klip: zoom masuk ringkas (1.18→1.04) + push perlahan; kilatan putih pada setiap potongan.
- Babak fitur guna **footage sebenar** (pasang bateri counter, tekan counter, timbang stepper 5.90kg).
- Bila diminta, **ubah shot** berbanding video sebelum ini.
- Bila diminta "terus mula dengan visual", frame pertama terus tunjuk grafik itu (tiada intro).

## Saiz tulisan (mulai Task 14)
| Tulisan | Saiz |
|---|---|
| Headline | **100px** |
| Sub-headline / pelekat save | **47px** |
| Caption | **40px** (stroke hitam ~3–4px), kedudukan **y = 1450px** (mulai Task 20) |
| Nombor heart rate | **64px** |
| Chip, nama warna, label zon | **19px** |

**Tulisan paling besar 100px sahaja** — tiada tulisan lain (nombor, kalendar, kad CTA, dll.) melebihi 100px. Tulisan lain yang tak disenaraikan kekal saiz sedia ada jika ≤100px.
Saiz lama (Task 4–13): headline 150px, sub headline 70px, caption 65px → 60px.

## Teks & caption
- Font: **Anton** (headline/caption), **Montserrat** 800/900 (label/pill).
- Caption: huruf besar, 2–3 perkataan setiap paparan, perkataan aktif jadi **kuning**, kata kunci jadi **hijau neon**, di tengah, **y = 1450px** dari atas (dulu 1150px).
- **Jangan bertindih:** kalau grafik dah tunjuk klausa yang sama, caption untuk klausa itu disembunyikan (ikut klausa penuh; sembunyi jika ≥1/3 perkataan utama ada dalam grafik).
- Ejaan tetap: **gelebeh**, **beg kuning**, **raya**, **briskwalk**.
- Hook: headline besar + sub-headline atas blok berwarna, dengan bunyi impact + gegar skrin.

## Warna
- Pink `#ff2e7e`, hijau neon `#c6ff00`, kuning `#ffd400`, merah `#ff3b30`, oren `#ff8a00`, putih, hitam.

## Grafik & overlay
- Pill ✓ dengan ikon, sticker condong, cop merah, tag harga kuning, lencana nombor ①②③, kad CTA putih + pill beg kuning + anak panah.
- Jadual/senarai: baris keluar **satu demi satu** (cth. jadual berat badan vs kalori 50kg → 100kg).
- Ilustrasi SVG dilukis sendiri bila folder tiada gambar (kalendar 2027, muscle, rajah otot depan/belakang, tapak kaki, api, kasut, dumbbell, meter laju, ikon repost, dll.).
- Overlay: vignette + bar progres pink→hijau di atas.
- **Tiada nombor atau data palsu.** Angka hanya dari VO, brief atau footage; anggaran ditanda "*Anggaran".

## Dua jenis video
- **A. Ada voiceover:** transkrip → **draf caption dihantar untuk disemak, tunggu "ok"** → grafik ikut masa VO.
- **B. Tiada voiceover (ikut brief):** Hook / Mini hook / Education / USP / CTA sebagai teks motion graphics; setiap mesej ≥2.5–3 saat (atau ikut durasi yang diminta).

## Aliran kerja
1. Muat turun VO + footage dari Drive (folder "Anyone with the link").
2. Transkrip (Whisper large-v3, Bahasa Melayu); semak footage (contact sheet, bunyi, kesan muzik).
3. Jenis A: hantar draf caption, tunggu "ok". Kalau brief tak jelas (cth. bilangan level), tanya dulu.
4. Pilih ≤10 klip; bina, lint, snapshot setiap babak dan semak visual.
5. Render dengan `scripts/render_70mb.sh`; semak VO masih selari dan **frame akhir setiap blok grafik (terutama CTA)** sebelum hantar.
