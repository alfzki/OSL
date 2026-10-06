#!/usr/bin/env python3
"""Localize quiz HTML user-facing UI labels into standard Bahasa Indonesia."""

import re
from pathlib import Path

files_to_update = [
    Path("output/kuis_interaktif_uas.html"),
    Path("open/quizzes/2026-09-29-uas-lengkap.html"),
    Path("internal/quizzes/2026-09-29-uas-lengkap.html")
]

replacements = [
    ('lang="zh-CN"', 'lang="id"'),
    ('生成于 2026-09-29 · 共 <span id="total"></span> 题 · 做完一题立即显示答案与解析', 'Dibuat pada 2026-09-29 · Total <span id="total"></span> Soal · Selesai satu butir langsung tampil pembahasan'),
    ('公式渲染组件未加载，数学公式将以 LaTeX 源码显示。', 'Mode Offline: Rumus matematika disajikan dalam format LaTeX.'),
    ('⚠️ 离线模式：本测验不加载任何远程资源，公式以 LaTeX 源码呈现，含义不受影响。', '⚠️ Mode Offline: Kuis ini mandiri tanpa dependensi eksternal, rumus disajikan dalam format LaTeX.'),
    ('/* 归一化：judge 转成两选项；multi 答案排序 */', '/* Normalisasi tipe soal */'),
    ('q._opts = ["正确", "错误"];', 'q._opts = ["Benar", "Salah"];'),
    ('["完全正确", 1.0], ["大部分正确", 0.75], ["对了一半", 0.5], ["少部分正确", 0.25], ["基本不会", 0]', '["Benar Sempurna", 1.0], ["Sebagian Besar Benar", 0.75], ["Benar Separuh", 0.5], ["Sebagian Kecil Benar", 0.25], ["Belum Menguasai", 0]'),
    ('`已完成 ${done} / ${QS.length} 题 ｜ 当前得分 ${round1(earned())} / ${fullScore()} 分`', '`Selesai ${done} / ${QS.length} Soal ｜ Skor Saat Ini ${round1(earned())} / ${fullScore()} Poin`'),
    ('第 ${idx + 1} / ${QS.length} 题 · ${esc(q.qtype_label || q.type)}', 'Soal ${idx + 1} / ${QS.length} · ${esc(q.qtype_label || q.type)}'),
    ('知识点：${esc(q.point_name)}', 'Materi: ${esc(q.point_name)}'),
    ('${st.correct ? "✓ 回答正确" : "✗ 回答错误"} ｜ 正确答案：${ansLabel} ｜ 得分 ${round1(st.earned)}/${q.score}', '${st.correct ? "✓ Jawaban Benar" : "✗ Jawaban Salah"} ｜ Kunci Jawaban: ${ansLabel} ｜ Skor: ${round1(st.earned)}/${q.score}'),
    ('多选题：选出所有正确项后点确认${q.partial ? "（漏选且无错选得一半分）" : "（错选、漏选均不得分）"}', 'Pilihan Ganda Kompleks: Pilih semua opsi yang benar lalu klik konfirmasi${q.partial ? " (kurang lengkap tanpa salah pilih mendapat setengah poin)" : " (salah pilih atau kurang lengkap tidak mendapat poin)"}'),
    ('确认作答', 'Konfirmasi Jawaban'),
    ('const head = st.correct ? "✓ 完全正确" : (st.earned > 0 ? "◐ 漏选（得一半分）" : "✗ 回答错误");', 'const head = st.correct ? "✓ Benar Sempurna" : (st.earned > 0 ? "◐ Kurang Lengkap (Mendapat Setengah Poin)" : "✗ Jawaban Salah");'),
    ('${head} ｜ 正确答案：${letters(q._ansArr)} ｜ 你的选择：${letters([...sel].sort((a, b) => a - b))} ｜ 得分 ${round1(st.earned)}/${q.score}', '${head} ｜ Kunci Jawaban: ${letters(q._ansArr)} ｜ Pilihan Anda: ${letters([...sel].sort((a, b) => a - b))} ｜ Skor: ${round1(st.earned)}/${q.score}'),
    ('/* text 主观题 */', '/* text soal esai/hitungan */'),
    ('在这里写下你的答案（计算题请写出关键步骤）', 'Tuliskan jawaban Anda di sini (soal hitungan sertakan tahapan perhitungan kunci)...'),
    ('提交并查看参考答案', 'Kirim & Lihat Kunci Pembahasan'),
    ('📖 参考答案与得分点（满分 ${q.score} 分）', '📖 Kunci Jawaban & Rubrik Penilaian (Maksimal ${q.score} Poin)'),
    ('【易错提醒】', '【Catatan Penting & Pembahasan】'),
    ('对照得分点给自己打分：', 'Evaluasi mandiri berdasarkan rubrik penilaian di atas:'),
    ('分）</button>`', ' poin)</button>`'),
    ('← 上一题', '← Soal Sebelumnya'),
    ('请先自评打分', 'Silakan evaluasi mandiri terlebih dahulu'),
    ('作答后才能进入下一题', 'Jawab terlebih dahulu sebelum lanjut'),
    ('查看成绩单 →', 'Lihat Rekap Nilai →'),
    ('下一题 →', 'Soal Berikutnya →'),
    ('自评：${st.selfLabel || "—"}', 'Evaluasi Mandiri: ${st.selfLabel || "—"}'),
    ('✓ 正确', '✓ Benar'),
    ('◐ 漏选', '◐ Kurang Lengkap'),
    ('✗ 错误', '✗ Salah'),
    ('（选了 ', '(Memilih '),
    ('未作答', 'Belum Menjawab'),
    ('未自评', 'Belum Evaluasi'),
    ('（未作答）', '(Belum Menjawab)'),
    ('<span class="chip">成绩单</span>', '<span class="chip">Rekap Hasil Latihan</span>'),
    ('${got} / ${total} 分（${pct}%）', '${got} / ${total} Poin (${pct}%)'),
    ('红色行为失分题，建议复盘后让老师把它们记入错题本。', 'Baris merah menandakan butir yang belum sempurna, pelajari pembahasannya dan catat di buku evaluasi kesalahan.'),
    ('全部正确，太棒了！', 'Seluruh jawaban benar, pemahaman materi sangat baik!'),
    ('<th>#</th><th>题型</th><th>知识点</th><th>得分</th><th>结果</th>', '<th>#</th><th>Tipe Soal</th><th>Materi / Indikator</th><th>Skor</th><th>Hasil</th>'),
    ('导出作答记录（贴回对话给老师批改）', 'Salin Riwayat Latihan (Format Teks)'),
    ('← 回看题目', '← Tinjau Kembali Soal'),
    ('已复制到剪贴板，直接粘贴到对话里即可。', 'Riwayat latihan berhasil disalin ke clipboard!'),
    ('请手动全选复制上面的文本，粘贴到对话里。', 'Silakan salin teks di atas secara manual.'),
    ('【作答记录】${DATA.title} ｜ ${new Date().toLocaleString("zh-CN")}', '【Riwayat Latihan UAS OSL】${DATA.title} ｜ ${new Date().toLocaleString("id-ID")}'),
    ('总分：${round1(earned())} / ${fullScore()}', 'Total Skor: ${round1(earned())} / ${fullScore()} Poin'),
    ('Q${i + 1} ｜ ${q.qtype_label || q.type} ｜ 知识点：${q.point_id || ""} ${q.point_name || ""} ｜ 得分 ${round1(st.earned)}/${q.score}', 'Q${i + 1} ｜ ${q.qtype_label || q.type} ｜ Materi: ${q.point_id || ""} ${q.point_name || ""} ｜ Skor: ${round1(st.earned)}/${q.score} Poin'),
    ('我的选择：${letters(st.userAnswer)}（正确答案 ${letters(q._ansArr)}，${st.correct ? "正确" : st.earned > 0 ? "漏选" : "错误"}）', 'Pilihan Saya: ${letters(st.userAnswer)} (Kunci: ${letters(q._ansArr)}, ${st.correct ? "Benar" : st.earned > 0 ? "Kurang Lengkap" : "Salah"})'),
    ('我的选择：${pick}（正确答案 ${ans}，${st.correct ? "正确" : "错误"}）', 'Pilihan Saya: ${pick} (Kunci: ${ans}, ${st.correct ? "Benar" : "Salah"})'),
    ('自评：${st.selfLabel || "未自评"}', 'Evaluasi Mandiri: ${st.selfLabel || "Belum Evaluasi"}'),
    ('自评：${st.selfLabel || "Belum Evaluasi"}', 'Evaluasi Mandiri: ${st.selfLabel || "Belum Evaluasi"}'),
    ('我的答案：${(st.userAnswer || "（未作答）").trim()}', 'Jawaban Saya: ${(st.userAnswer || "(Belum Menjawab)").trim()}'),
    ('我的答案：${(st.userAnswer || "（Belum Menjawab）").trim()}', 'Jawaban Saya: ${(st.userAnswer || "(Belum Menjawab)").trim()}'),
    ('（Belum Menjawab）', '(Belum Menjawab)'),
]

for fp in files_to_update:
    if not fp.exists():
        continue
    content = fp.read_text(encoding="utf-8")
    for src, dst in replacements:
        content = content.replace(src, dst)
    fp.write_text(content, encoding="utf-8")
    rem_chinese = len(re.findall(r'[\u4e00-\u9fff]', content))
    print(f"{fp}: remaining Chinese chars = {rem_chinese}")
