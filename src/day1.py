def parse_historians_lists(raw_input: str) -> tuple[list[int], list[int]]:
    first_ids: list[int] = []
    second_ids: list[int] = []

    for line in raw_input.strip().split("\n"):
        first_id, second_id = map(int, line.split())
        first_ids.append(first_id)
        second_ids.append(second_id)

    return first_ids, second_ids


def pair_locations_by_size(first_ids: list[int], second_ids: list[int]) -> tuple[list[int], list[int]]:
    return sorted(first_ids), sorted(second_ids)


def calculate_total_distance(first_sorted: list[int], second_sorted: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(first_sorted, second_sorted))


def main() -> None:
    print("Input two lists collected by groups of historians:")

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
        first_ids, second_ids = parse_historians_lists(raw_input)
        first_sorted, second_sorted = pair_locations_by_size(first_ids, second_ids)
        total_distance = calculate_total_distance(first_sorted, second_sorted)
        print(f"\nTotal distance: {total_distance}")
    except ValueError as error:
        print(f"Error processing input: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
