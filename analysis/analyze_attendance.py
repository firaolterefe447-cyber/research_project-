import csv
import sys
from collections import Counter
from pathlib import Path

LIKERT_COLUMNS = [
    "manual_time_problem", "manual_record_accuracy", "learning_interruption",
    "proxy_risk", "correction_difficulty", "digital_time_saving",
    "digital_acceptance", "internet_barrier", "privacy_concern"
]


def read_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def frequency(rows, column):
    values = [row[column].strip() for row in rows if row.get(column, "").strip()]
    counts = Counter(values)
    total = sum(counts.values())
    return [(value, counts[value], counts[value] / total * 100 if total else 0)
            for value in sorted(counts)]


def likert_summary(rows, column):
    values = []
    for row in rows:
        raw = row.get(column, "").strip()
        if raw:
            try:
                value = int(raw)
                if 1 <= value <= 5:
                    values.append(value)
            except ValueError:
                pass
    mean = sum(values) / len(values) if values else None
    return len(values), mean, Counter(values)


def main():
    if len(sys.argv) != 2:
        print("Usage: python analysis/analyze_attendance.py data/anonymized_responses.csv")
        return

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Dataset not found: {input_path}")
        return

    rows = read_csv(input_path)
    output_dir = Path("analysis/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = ["Attendance Management Descriptive Analysis", "", f"Valid participant records: {len(rows)}"]

    for column in ["participant_role", "attendance_method", "class_size_category"]:
        if column in (rows[0] if rows else {}):
            lines.extend(["", f"{column}:"])
            for value, count, percent in frequency(rows, column):
                lines.append(f"  {value}: {count} ({percent:.1f}%)")

    lines.append("\nLikert summaries:")
    for column in LIKERT_COLUMNS:
        count, mean, distribution = likert_summary(rows, column)
        mean_text = f"{mean:.2f}" if mean is not None else "Not available"
        distribution_text = ", ".join(f"{key}: {distribution[key]}" for key in range(1, 6))
        lines.append(f"  {column}: n={count}, mean={mean_text}; {distribution_text}")

    output_path = output_dir / "descriptive-analysis.txt"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\nOutput: {output_path}")


if __name__ == "__main__":
    main()

