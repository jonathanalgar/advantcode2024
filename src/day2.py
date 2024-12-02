def parse_level_reports(raw_input: str) -> list[list[int]]:
    reports: list[list[int]] = []
    for line in raw_input.strip().split("\n"):
        levels = [int(x) for x in line.split()]
        reports.append(levels)
    return reports


def is_safe_report(levels: list[int]) -> bool:
    """Check if reactor levels are all gradually increasing or decreasing within bounds."""
    diffs = [b - a for a, b in zip(levels, levels[1:])]

    # All differences must be in the same direction
    if not (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        return False

    # All differences must be between 1 and 3 inclusive
    return all(1 <= abs(d) <= 3 for d in diffs)


def count_safe_reports(reports: list[list[int]]) -> int:
    return sum(1 for report in reports if is_safe_report(report))


def main() -> None:
    print("Input reactor level reports:")

    input_lines: list[str] = []
    try:
        while True:
            line = input()
            input_lines.append(line)
    except EOFError:
        pass

    raw_input = "\n".join(input_lines)
    if not raw_input.strip():
        print("No input provided!")
        return

    try:
        reports = parse_level_reports(raw_input)
        safe_count = count_safe_reports(reports)
        print(f"\nSafe reports: {safe_count}")
    except ValueError as error:
        print(f"Error processing input: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
