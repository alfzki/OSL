#!/usr/bin/env python3
"""Bangun Obsidian study vault OSL dari sumber materi terverifikasi.

Sumber kebenaran (grounding):
  - internal/state/knowledge.json      -> urutan bab, judul, dan seksi
  - internal/lessons/chapter-XX/*.json -> isi konsep, rumus, contoh, jebakan

Keluar (kontrak exam-sprint-builder, deliverables-catalog §1):
  <out>/_MOC.md
  <out>/chapters/NN-<slug>.md
  <out>/_glossary.md
  <out>/_formulas.md

Vault murni Markdown: tanpa CSS, tanpa referensi remote, portabel antar tema.
Tidak ada konten yang dikarang; setiap baris diturunkan dari JSON sumber.
"""
import argparse
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
MOC_LINK = "[[_MOC|← Back to MOC]]"

IMPORTANCE_ID = {"高": "Tinggi", "中": "Sedang", "低": "Rendah"}


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-zA-Z0-9]+", "-", ascii_only).strip("-").lower()


def strip_meeting_prefix(title: str) -> str:
    return re.sub(r"^Pertemuan\s+\d+\s*:\s*", "", title).strip()


def load_knowledge() -> list:
    path = ROOT / "internal" / "state" / "knowledge.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return sorted(data["chapters"], key=lambda c: c["id"])


def load_lessons() -> list:
    units = []
    for path in sorted((ROOT / "internal" / "lessons").glob("chapter-*/*.json")):
        if path.name.startswith("chapter-"):
            continue
        units.append(json.loads(path.read_text(encoding="utf-8")))
    units.sort(key=lambda u: u["point_id"])
    return units


def citation(unit: dict) -> str:
    parts = []
    for src in unit.get("grounding", {}).get("primary_sources", []):
        parts.append(f"[{src['file']}, slide/hal. {src['slide_or_page']}]")
    for src in unit.get("grounding", {}).get("supplemental_sources", []):
        label = src.get("label", src.get("file", "suplemen"))
        parts.append(f"[SUPLEMEN: {label}]")
    return " ".join(parts) if parts else "TIDAK ADA DI MATERI"


def render_chapter(chapter: dict, units: list, prev_link: str, next_link: str) -> str:
    chapter_id = chapter["id"]
    section_titles = {
        point_id: sec.get("title", "")
        for sec in chapter.get("sections", [])
        for point_id in [p["id"] for p in sec.get("points", [])]
    }

    lines = [
        "---",
        f"tags: [osl, ppt-{chapter_id}, universitas]",
        f"chapter: {chapter_id}",
        "status: draft",
        f"points: {len(units)}",
        "---",
        "",
        f"# {chapter['title']}",
        "",
        "> Modul ini diturunkan dari `internal/lessons/chapter-%02d/*.json`." % chapter_id,
        "> `status: draft` karena belum ada sesi belajar yang tercatat pada `progress/tracker.json`.",
        "",
        "## Konsep",
        "",
    ]

    for unit in units:
        point = (unit.get("points") or [{}])[0]
        theory = unit.get("theory", {})
        importance = IMPORTANCE_ID.get(unit.get("importance", ""), unit.get("importance", "-"))
        section = section_titles.get(unit["point_id"], unit.get("section", ""))

        lines += [
            f"### {unit['point_id']} {unit['title']}",
            "",
            f"- **Seksi**: {section}",
            f"- **Prioritas**: {importance}",
            f"- **Rujukan**: {citation(unit)}",
            f"- **Cakupan**: {unit.get('grounding', {}).get('coverage_status', '-')}",
            "",
        ]
        if point.get("exam_focus"):
            lines += [f"**Fokus ujian** — {point['exam_focus']}", ""]
        for key, label in (("intuition", "Intuisi"), ("bps_definition", "Definisi BPS"),
                           ("boundary_conditions", "Syarat & batas")):
            if theory.get(key):
                lines += [f"**{label}** — {theory[key]}", ""]
        if theory.get("formula_latex"):
            fl = theory["formula_latex"].strip()
            if fl.startswith("`") and fl.endswith("`"):
                fl = fl[1:-1].strip()
            lines += [f"**Rumus** — {fl}", ""]

    lines += ["## Contoh Hitung", ""]
    for unit in units:
        example = unit.get("numerical_example", {})
        if not example:
            continue
        lines += [f"### {unit['point_id']} — {unit['title']}", ""]
        if example.get("problem_statement"):
            lines += [example["problem_statement"], ""]
        if example.get("data_table"):
            lines += [example["data_table"], ""]
        if example.get("step_by_step_solution"):
            lines += ["**Penyelesaian**", "", example["step_by_step_solution"], ""]
        if example.get("expected_output"):
            lines += [f"**Hasil verifikasi** — `{example['expected_output']}`", ""]

    lines += ["## Jebakan Ujian", ""]
    for unit in units:
        for pitfall in unit.get("exam_pitfalls", []):
            lines += [
                f"**{unit['point_id']} — {pitfall['trap_description']}**",
                "",
                f"- Jebakan: {pitfall['common_mistake']}",
                f"- Strategi aman: {pitfall['safe_strategy']}",
                "",
            ]

    lines += [
        "## Navigasi",
        "",
        f"- {prev_link}",
        f"- {next_link}",
        f"- [[_formulas|Rumus lengkap OSL]]",
        f"- [[_glossary|Glosarium istilah]]",
        "",
        "---",
        "",
        MOC_LINK,
        "",
    ]
    return "\n".join(lines)


def render_moc(chapters: list, chapter_notes: list) -> str:
    lines = [
        "---",
        "tags: [moc, osl]",
        "subject: Official Statistics Lanjutan",
        "status: draft",
        "---",
        "",
        "# OSL — Map of Contents",
        "",
        "Vault belajar untuk mata kuliah **Official Statistics Lanjutan (OSL)**.",
        "Seluruh isi diturunkan dari materi terverifikasi di repositori;",
        "entri bertanda `TIDAK ADA DI MATERI` berarti tidak dibahas dalam materi kuliah.",
        "",
        "## Bab",
        "",
    ]
    for chapter, note in zip(chapters, chapter_notes):
        lines.append(f"- {note} — {chapter['title']}")
    lines += [
        "",
        "## Berkas Pendukung",
        "",
        "- [[_formulas]] — Kumpulan rumus seluruh bab",
        "- [[_glossary]] — Glosarium istilah statistik",
        "",
        "## Materi Asli (di luar vault)",
        "",
        "- Modul ajar per bab: `internal/lessons/chapter-XX/`",
        "- Modul gabungan: `open/chapters/chapter-XX.html`",
        "- Kuis interaktif: `open/quizzes/`, `output/kuis_interaktif_uas.html`",
        "- Cheat sheet A4: `output/cheat_sheet_rumus_a4.html`",
        "- Bank soal terverifikasi: `bank/soal.json`",
        "",
    ]
    return "\n".join(lines)


def render_glossary(units: list) -> str:
    lines = [
        "---",
        "tags: [osl, glossary]",
        "status: draft",
        "---",
        "",
        "# Glosarium Istilah OSL",
        "",
        "Definisi diturunkan dari `theory.bps_definition` pada tiap modul ajar.",
        "",
        "| Istilah | Definisi |",
        "|---|---|",
    ]
    for unit in units:
        raw_def = (unit.get("theory", {}) or {}).get("bps_definition", "")
        if not raw_def:
            continue
        definition = raw_def.replace("\r\n", "\n").replace("\n", "<br>").replace("|", "\\|")
        lines.append(f"| {unit['title']} | {definition} |")
    lines += ["", "---", "", MOC_LINK, ""]
    return "\n".join(lines)


def render_formulas(units: list) -> str:
    lines = [
        "---",
        "tags: [osl, formulas]",
        "status: draft",
        "---",
        "",
        "# Rumus OSL",
        "",
        "Kumpulan rumus seluruh bab OSL dalam format LaTeX/MathJax.",
        "Dapat dirender langsung di Obsidian atau aplikasi Markdown dengan dukungan KaTeX/MathJax.",
        "",
    ]
    current_chapter = None
    for unit in units:
        formula = (unit.get("theory", {}) or {}).get("formula_latex", "").strip()
        if not formula:
            continue
        if formula.startswith("`") and formula.endswith("`"):
            formula = formula[1:-1].strip()
        chapter_id = unit.get("chapter_id")
        if chapter_id != current_chapter:
            current_chapter = chapter_id
            lines += [f"## {unit.get('chapter_title', 'Bab ' + str(chapter_id))}", ""]
        lines += [
            f"### {unit['point_id']} {unit['title']}",
            "",
            formula,
            "",
            f"Rujukan: {citation(unit)}",
            "",
        ]
    lines += ["---", "", MOC_LINK, ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default=["output/OSL"],
        nargs="+",
        help="vault root(s) (default: output/OSL)",
    )
    args = parser.parse_args()

    knowledge = load_knowledge()
    lessons = load_lessons()
    by_chapter = {}
    for unit in lessons:
        by_chapter.setdefault(unit["chapter_id"], []).append(unit)

    vault_chapters = [
        (chapter, f"{index:02d}-{slugify(strip_meeting_prefix(chapter['title']))}")
        for index, chapter in enumerate(knowledge, start=1)
        if by_chapter.get(chapter["id"])
    ]
    notes = [note for _, note in vault_chapters]
    titles = {note: chapter["title"] for chapter, note in vault_chapters}

    for out_arg in args.out:
        out_root = pathlib.Path(out_arg)
        if not out_root.is_absolute():
            out_root = ROOT / out_root
        chapters_dir = out_root / "chapters"
        chapters_dir.mkdir(parents=True, exist_ok=True)

        for position, (chapter, note) in enumerate(vault_chapters):
            prev_note = notes[position - 1] if position > 0 else None
            next_note = notes[position + 1] if position < len(notes) - 1 else None
            prev_link = f"[[{prev_note}|← {titles[prev_note]}]]" if prev_note else "← (bab pertama)"
            next_link = f"[[{next_note}|→ {titles[next_note]}]]" if next_note else "→ (bab terakhir)"

            (chapters_dir / f"{note}.md").write_text(
                render_chapter(chapter, by_chapter[chapter["id"]], prev_link, next_link),
                encoding="utf-8",
            )

        (out_root / "_MOC.md").write_text(
            render_moc([chapter for chapter, _ in vault_chapters], notes), encoding="utf-8"
        )
        (out_root / "_glossary.md").write_text(render_glossary(lessons), encoding="utf-8")
        (out_root / "_formulas.md").write_text(render_formulas(lessons), encoding="utf-8")

        total = len(notes) + 3
        print(f"[OK] Vault ditulis ke {out_root}/")
        print(f"     {len(notes)} catatan bab + _MOC + _glossary + _formulas = {total} berkas")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
