import re


def parse_multiplication_instructions(memory: str) -> list[tuple[int, int]]:
    """Extract valid multiplication instructions from corrupted memory."""
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, memory)

    instructions: list[tuple[int, int]] = []
    for match in matches:
        x, y = int(match.group(1)), int(match.group(2))
        instructions.append((x, y))

    return instructions


def calculate_total_result(instructions: list[tuple[int, int]]) -> int:
    return sum(x * y for x, y in instructions)


def main() -> None:
    print("Input corrupted memory content:")

    input_lines: list[str] = []
    try:
        while True:
            line = input()
            input_lines.append(line)
    except EOFError:
        pass

    memory = "\n".join(input_lines)
    if not memory.strip():
        print("No input provided!")
        return

    try:
        instructions = parse_multiplication_instructions(memory)
        total = calculate_total_result(instructions)
        print(f"\nSum of instructions: {total}")
    except ValueError as error:
        print(f"Error processing input: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
