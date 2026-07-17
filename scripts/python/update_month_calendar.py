import calendar
from pathlib import Path
import sys


def generate_month_navigation(month):
    # Calculate previous and next month indexes (handling 1 and 12 loop wraps)
    prev_month = 12 if month == 1 else month - 1
    next_month = 1 if month == 12 else month + 1

    # Convert to lowercase 3-letter abbreviations
    prev_abbr = calendar.month_abbr[prev_month].lower()
    next_abbr = calendar.month_abbr[next_month].lower()

    # Create top-level navigation layout line
    return f"[[{prev_abbr}]] | [[{next_abbr}]]\n\n"


def generate_month_markdown(year, month):
    month_name = calendar.month_name[month]
    # Table columns starting on Monday
    md_output = f"## {month_name} {year}\n\n"
    md_output += "| Mo | Tu | We | Th | Fr | Sa | Su |\n"
    md_output += "| :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"

    # Set MONDAY as the first day of the week
    cal = calendar.TextCalendar(calendar.MONDAY)
    weeks = cal.monthdays2calendar(year, month)

    for week in weeks:
        row_cells = []
        for day, _ in week:
            if day == 0:
                row_cells.append("--")
            else:
                padded_month = f"{month:02}"
                padded_day = f"{day:02}"
                row_cells.append(f"[{padded_day}]({padded_month}-{padded_day})")

        md_output += f"| {' | '.join(row_cells)} |\n"

    md_output += "\n"
    return md_output


def process_month(year, month):
    month_name = calendar.month_name[month]
    month_abbr = calendar.month_abbr[month].lower()

    # Define path relative to script location: ../../monthly/mmm.md
    output_dir = Path(__file__).parent / ".." / ".." / "monthly"
    output_file = output_dir / f"{month_abbr}.md"

    # Ensure directories exist safely
    output_dir.mkdir(parents=True, exist_ok=True)

    target_header = f"## {month_name} {year}"

    # Check if the year block already exists in the file
    if output_file.exists():
        with open(output_file, "r", encoding="utf-8") as file:
            content = file.read()
            if target_header in content:
                print(f"[{month_abbr}.md] -> Skipped. '{month_name} {year}' already exists.")
                return

    # Check file state prior to file writing operations
    file_exists = output_file.exists()
    
    # Generate the calendar table content string
    month_content = generate_month_markdown(year, month)

    if not file_exists:
        # File is brand new: Generate navigation prefix and combine it
        nav_header = generate_month_navigation(month)
        final_output = nav_header + month_content
        write_mode = "w"
    else:
        # File exists: Append calendar directly underneath existing contents
        final_output = month_content
        write_mode = "a"

    with open(output_file, write_mode, encoding="utf-8") as file:
        file.write(final_output)

    action = "Created with navigation" if not file_exists else "Appended to"
    print(f"[{month_abbr}.md] -> {action} successfully.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide at least a year.")
        print("Usage (All Months):  python script.py YEAR")
        print("Usage (Single Month): python script.py YEAR MONTH")
        sys.exit(1)

    try:
        target_year = int(sys.argv[1])

        # Scenario 1: Only Year is given -> Run for all 12 months
        if len(sys.argv) == 2:
            print(f"Processing all months for the year {target_year}...")
            for m in range(1, 13):
                process_month(target_year, m)

        # Scenario 2: Both Year and Month are given -> Run for single month
        else:
            target_month = int(sys.argv[2])
            if not (1 <= target_month <= 12):
                print("Error: Month must be between 1 and 12.")
                sys.exit(1)

            process_month(target_year, target_month)

    except ValueError:
        print("Error: Year and Month arguments must be valid integer numbers.")
        sys.exit(1)
