"""Check shared requirements in the standalone Compress workflows."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = (
    "AUDIT",
    "BUILD",
    "FIX",
    "INVESTIGATE",
    "REFACTOR",
    "REMOVE",
    "REVIEW",
)
REQUIRED = (
    "at least three full, relevant, peer-reviewed",
    "Elsevier",
    "Springer Nature",
    "Wiley",
    "Taylor & Francis",
    "IEEE",
    "Oxford University Press",
    "ACM",
    "peer-reviewed university research",
    "vendor blogs",
    "AI-written summaries",
    "search snippets",
    "method",
    "scope",
    "limitations",
    "wording dictionary",
    "../dictionary/wording.md",
    "incomplete",
)


def main() -> int:
    errors = []
    for name in WORKFLOWS:
        path = ROOT / "skill" / f"{name}.md"
        if not path.is_file():
            errors.append(f"Missing workflow: {path.relative_to(ROOT)}")
            continue

        content = path.read_text(encoding="utf-8")
        normalized = " ".join(content.split())
        for phrase in REQUIRED:
            if phrase.casefold() not in normalized.casefold():
                errors.append(f"{path.relative_to(ROOT)}: missing required text: {phrase}")

        numbers = [int(value) for value in re.findall(r"^(\d+)\. \*\*", content, re.M)]
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append(f"{path.relative_to(ROOT)}: workflow steps are not numbered in order")

    if errors:
        print("Workflow checks failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"Checked shared requirements in all {len(WORKFLOWS)} workflows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
