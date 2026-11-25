# Assessing Manual and Digital Attendance Systems at Addis Ababa University

**Course:** Research and Technical Writing — Group Assignment  
**Department:** Department of Information Science, College of Natural and Computational Science  
**Instructor:** Dr. Ermias Abebe  
**Repository status:** Research implementation workspace  
**Report due:** December 13, 2026

## Research question

What challenges occur with manual attendance management at selected Addis Ababa University departments, and what benefits and barriers are associated with adopting digital attendance systems?

## Objectives

1. Identify major challenges associated with manual attendance recording.
2. Examine perceived effects on instructional time and academic efficiency.
3. Assess acceptance of digital attendance systems among students and instructors.
4. Identify implementation barriers and recommend practical solutions.

## Repository structure

| Folder | Purpose |
|---|---|
| `proposal/` | Approved proposal and implementation design records |
| `instruments/` | Questionnaire, interview guide, observation checklist, and codebook |
| `pilot-study/` | Pilot procedure, participant feedback, revisions, and results |
| `data/` | Anonymized data, data dictionary, collection log, and analysis inputs |
| `analysis/` | Reproducible scripts and generated analysis outputs |
| `report/` | Final report draft and final PDF/Word submission |
| `presentation/` | Presentation slides and presentation notes |
| `meeting-notes/` | Group meeting decisions and action records |
| `references/` | Source list and reference-management files |

## Group members and suggested roles

| Member | ID | Suggested role |
|---|---|---|
| Tedros Meresa | UGR/2084/17 | Project coordination and report integration |
| Yoseph Legesse | UGR/3354/17 | Quantitative instrument and data analysis |
| Fanuel Negasi | UGR/5201/17 | Interviews and qualitative coding |
| Israel Tsegaye | UGR/2424/17 | Classroom observations and pilot testing |
| Fraol Terefe | UGR/5582/17 | Data management, references, and repository documentation |

Final role and contribution details must be confirmed collectively and recorded in `report/group-contribution-statement.md`.

## Method summary

- **Design:** Descriptive cross-sectional mixed-method study.
- **Participants:** Approximately 60–100 students and 5–10 instructors in selected AAU departments.
- **Sampling:** Convenience sampling for students and purposive sampling for instructors.
- **Quantitative instrument:** Student/instructor Likert-scale and closed-ended questionnaire.
- **Qualitative instruments:** Semi-structured interviews and classroom observations.
- **Analysis:** Frequencies, percentages, mean scores, and thematic analysis.
- **Ethics:** Participation will be voluntary and data will be anonymized. No real participant data should be stored in a public repository.

## Data status

The repository contains collection templates and a reproducible analysis workflow. It does not claim measured findings before the group completes ethical approval, pilot testing, and actual data collection. Replace the template dataset with an anonymized dataset only after coding and checking it for identifying information.

## Software and reproducibility

- Microsoft Word or LibreOffice for report and presentation deliverables.
- Microsoft Excel or CSV for the cleaned dataset.
- Python 3 for descriptive analysis.
- Optional SPSS for replication.

To reproduce the descriptive analysis:

```bash
python analysis/analyze_attendance.py data/anonymized_responses.csv
```

Generated tables and charts will be written to `analysis/outputs/`.

## Handling rules

- Do not upload names, student IDs, phone numbers, emails, or identifiable quotations.
- Keep raw research files outside the public repository if they contain personal information.
- Record methodology changes and seek instructor approval for major changes.
- Commit meaningful work regularly and clearly describe changes in commit messages.
