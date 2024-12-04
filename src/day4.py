def parse_grid(input_text: str) -> list[list[str]]:
    """Convert input text into a 2D grid of characters."""
    return [list(line.strip()) for line in input_text.splitlines() if line.strip()]


def find_xmas(grid: list[list[str]]) -> set[tuple[tuple[int, int], ...]]:
    """Find all instances of 'XMAS' in the grid in all directions."""
    height = len(grid)
    width = len(grid[0])
    target = "XMAS"
    found_patterns = set()

    # Direction vectors
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (-1, 1),  # diagonal up-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # diagonal up-left
        (1, -1),  # diagonal down-left
    ]

    def is_valid_position(x: int, y: int) -> bool:
        """Check if position is within grid bounds."""
        return 0 <= x < height and 0 <= y < width

    def check_pattern(start_x: int, start_y: int, dx: int, dy: int) -> tuple[tuple[int, int], ...] | None:
        """Check if 'XMAS' exists starting from (start_x, start_y) in direction (dx, dy)."""
        positions = []
        x, y = start_x, start_y

        for char in target:
            if not is_valid_position(x, y) or grid[x][y] != char:
                return None
            positions.append((x, y))
            x, y = x + dx, y + dy

        return tuple(positions)

    # Find all X positions first
    x_positions = [(i, j) for i in range(height) for j in range(width) if grid[i][j] == "X"]

    # Only check patterns starting from X positions
    for i, j in x_positions:
        for dx, dy in directions:
            pattern = check_pattern(i, j, dx, dy)
            if pattern:
                found_patterns.add(pattern)

    return found_patterns


def create_highlighted_grid(grid: list[list[str]], patterns: set[tuple[tuple[int, int], ...]]) -> str:
    """Create a string representation of the grid with non-pattern letters replaced by dots."""
    used_positions = set()
    for pattern in patterns:
        for pos in pattern:
            used_positions.add(pos)

    result = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            if (i, j) in used_positions:
                row.append(grid[i][j])
            else:
                row.append(".")
        result.append("".join(row))

    return "\n".join(result)


def main() -> None:
    print("Enter the word search grid:")

    input_lines = []
    try:
        while True:
            line = input()
            if not line:
                break
            input_lines.append(line)
    except EOFError:
        pass

    if not input_lines:
        print("No input provided!")
        return

    try:
        grid = parse_grid("\n".join(input_lines))
        patterns = find_xmas(grid)
        highlighted = create_highlighted_grid(grid, patterns)

        print(f"\nFound {len(patterns)} instances of 'XMAS'")
        print("\nHighlighted grid (non-pattern letters replaced with dots):")
        print(highlighted)
    except ValueError as error:
        print(f"Error processing input: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
