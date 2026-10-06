# Buku Catatan Kesalahan (Mistake Book)

Status: **kosong** — belum ada sesi latihan yang tercatat.

Buku ini diisi otomatis oleh `study-quiz` setiap kali soal dijawab salah
(`internal/state/mistakes.md`, kontrak skill `study-quiz`). Tidak ada data
pembelajaran yang boleh diisi secara manual atau diasumsikan.

## Skema entri

Setiap entri adalah satu blok dengan field wajib berikut:

| Field | Isi |
|---|---|
| `date` | Tanggal latihan (YYYY-MM-DD) |
| `question_id` | ID butir pada bank soal, mis. `OSL-P08-PG-001` |
| `point_id` | Poin konsep, mis. `8.3.1` |
| `your_answer` | Jawaban yang dipilih |
| `correct_answer` | Kunci jawaban |
| `root_cause` | Analisis akar kesalahan (bukan sekadar "salah") |
| `status` | `belum-diperbaiki` → `diperbaiki` (re-do benar = `复盘通过`) |

## Aturan

1. **Jangan pernah mengarang entri.** Jumlah entri di bawah ini nol.
2. Entri hanya dibuat setelah learner benar-benar menjawab soal.
3. Sebuah kesalahan ditandai selesai (`diperaktif`) hanya bila learner
   menjawab ulang pertanyaan yang disamarkan dengan benar (teknik disguise).
4. Bila `mastery <= 2`, `study-quiz` wajib menyarankan materi diulang
   sebelum lanjut ke bab berikutnya.

## Entri

_(kosong — belum ada kesalahan yang tercatat)_
