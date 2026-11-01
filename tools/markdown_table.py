AUTHOR = "Daniel Belville Jr."
APP_NAME = "Markdown Table Helper"


def run():
    """Generate a Markdown table from user-entered headers and rows."""

    headers_input = input("Enter column headers separated by commas: ").strip()

    if not headers_input:
        print("At least one header is required.")
        return

    headers = [header.strip() for header in headers_input.split(",")]

    rows = []

    print("Enter table rows separated by commas.")
    print("Press Enter on an empty line when finished.")

    while True:
        row_input = input("Row: ").strip()

        if not row_input:
            break

        row = [value.strip() for value in row_input.split(",")]

        if len(row) != len(headers):
            print(
                f"Invalid row. Expected {len(headers)} values "
                f"but received {len(row)}."
            )
            continue

        rows.append(row)

    if not rows:
        print("At least one valid row is required.")
        return

    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    print("\nGenerated Markdown table:")
    print(header_row)
    print(separator_row)

    for row in rows:
        print("| " + " | ".join(row) + " |")