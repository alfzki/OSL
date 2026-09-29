---
name: exam-forecast
description: >-
  Analyze past exams, professor patterns, and previous exam papers to surface patterns — subject weighting, recurring problem types and traps, question style, theory vs practical ratio — and forecast likely emphases for the upcoming final exam (UAS/Ujian Akhir Semester). Use when the user asks "what's on the exam", "analisis soal tahun lalu", "prediksi materi UAS", "analyze past exams", "forecast exam topics", or provides past exam papers.
---

# Exam Forecast (Analisis Pola & Prediksi Soal UAS)

## Purpose

Every professor and course curriculum leaves fingerprints in their exams. Recurring question structures, consistent point distributions, favored problem-solving frameworks, and typical conceptual traps repeat across years. Students who analyze past exams study with laser focus.

This skill conducts a systematic longitudinal analysis of past university exams (UAS / UTS / past papers) and current course syllabi to forecast high-probability topics and exam structures.

> **Confidence Discipline & Framing:**
> A forecast is a probabilistic weighting heuristic for study time allocation, NOT a psychic guarantee. Always maintain calibration:
> - **Sample Size Discipline**:
>   - *Thin Sample (<3 past exams)*: Flag that pattern inference is weak/noisy.
>   - *Moderate Sample (3-5 past exams)*: Reliable for core topic weighting and format tendencies.
>   - *Strong Sample (6+ past exams)*: High confidence on stable vs. rotational topic patterns.
> - **Professor Factor**: Exams from the same lecturer/dosen carry the highest signal. Multi-lecturer courses or changed professors must be treated with lower confidence.
> - Never advise skipping syllabus topics entirely. Use this skill to weight study hours (e.g., 50% / 35% / 15%), not eliminate topics.

---

## Intake & Context Gathering

Collect whatever materials the student has available:
1. **Course & Instructor**: Course title, lecturer/dosen name (crucial for pattern matching).
2. **Upcoming Exam Format**: Duration, total points/marks, allowed materials (open book, closed book, cheat sheet / formula sheet allowed, calculator).
3. **Past Exams (Bank Soal)**: PDFs, images, text, or file paths of past UAS papers (note years/semesters).
4. **Current Syllabus / RPS / Lecture Outline**: Topics taught this semester, especially any newly introduced or removed modules.

---

## Analysis Workflow

### Step 1: Individual Exam Inspection
For each available past exam paper, analyze:
- **Structure & Breakdown**: Total questions, section weights (e.g. Part A Multiple Choice 30%, Part B Essay/Computation 70%), time-per-question estimate.
- **Subject Coverage & Point Allocation**: Map every question to specific course chapters/topics and record exact marks/percentages.
- **Question Style & Cognitive Depth**:
  - Theory & Definition (Bloom: Remember/Understand)
  - Formula & Computation / Coding (Bloom: Apply)
  - Case Study / Architecture / Problem Diagnosis (Bloom: Analyze/Evaluate)
- **Trap Patterns & Distractors**: Common edge cases, tricky unit conversions, deceptive assumptions, or subtle boundary conditions the professor frequently inserts.

### Step 2: Cross-Exam Longitudinal Pattern Analysis
Compare all exams to categorize topics:
- **Anchors (Stable Every Year)**: Topics that appear in 80-100% of past exams and consistently command major points (e.g. "Dynamic Programming always appears as a 25-point problem").
- **Rotators (Cyclical Patterns)**: Topics that alternate every year or every two semesters.
- **Professor Hobby Horses**: Niche or favorite concepts emphasized in lectures that receive disproportionately high exam points relative to textbook pages.
- **Dormant / Deprecated Topics**: Topics appearing in very old exams that have been phased out of the modern syllabus.

### Step 3: Synthesis & Forecast Generation
Combine historical patterns with the **current semester's progress**:
- If a topic was heavily covered in lecture or mentioned as "perhatikan ini untuk UAS", bump its priority.
- If new materials/tools were introduced this semester, treat them as high-probability new additions.

Generate the structured forecast report using the template below.

---

## Forecast Output Format

When generating the forecast (in chat and saved to `forecasts/[Course-Name]/uas-forecast-[YYYY].md`):

```markdown
# 🎯 UAS Exam Forecast — [Course Name]
*Dosen / Instructor:* [Name] | *Date of Forecast:* [YYYY-MM-DD]
*Past Exams Analyzed:* [N] years | *Sample Confidence:* [Thin / Moderate / Strong]

---

### 1. Format & Blueprint Prediction
- **Estimated Structure:** [e.g., 5 Essay Problems / 40 MCQs + 3 Computation Problems]
- **Style Expectation:** [e.g., Heavy case-study computation with partial credit]
- **Time Pressure Index:** [High / Moderate / Manageable]

### 2. Topic Weighting Matrix

| Topic / Chapter | Historical Weight (%) | In Current Syllabus? | Forecast Probability | Expected Format |
|---|---|---|---|---|
| [Topic A] | ~30% | Yes (Lectures 9-10) | 🔴 HIGH (90%) | Multi-part derivation / problem |
| [Topic B] | ~25% | Yes (Lectures 11-12) | 🔴 HIGH (85%) | Comprehensive analysis |
| [Topic C] | ~20% | Yes (Lecture 13) | 🟡 MEDIUM (60%) | Short answer / conceptual |
| [Topic D] | ~15% | Yes | 🟢 ROTATIONAL (40%) | Alternating topic |
| [Topic E] | ~10% | Mentioned briefly | ⚪ LOW (20%) | Quick question / bonus |

### 3. Key Traps & Professor "Hobby Horses"
- ⚠️ **Trap 1:** [Specific tricky aspect frequently tested]
- 💡 **Special Emphasis:** [Concept the professor loves repeating]

### 4. Recommended Study Allocation (Resource Strategy)
- **Heavy Priority (45-50% study time):** [Top anchor topics] — Practice full problems end-to-end.
- **Moderate Priority (35-40% study time):** [Supporting core topics] — Review formulas, diagrams, and standard examples.
- **Safety Review (10-15% study time):** [Edge cases and rotational topics] — Prepare quick summary notes / formula sheet entries.

---
*Disclaimer: This forecast is based on pattern analysis of historical exam papers and syllabus weighting. It serves as a study prioritization guide, not an official exam disclosure.*
```

---

## Integration with Other Skills

- Feed forecast weights directly into `exam-sprint-builder` to configure mock exam questions and A4 cheat sheet density.
- Feed high-probability topics into `study-quiz` for timed mock exam drills.
- Use `study-feynman` on the top 3 high-confidence topics to verify zero conceptual blindspots.
