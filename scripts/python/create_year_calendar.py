path = '../../yearly'

import calendar
import sys


def generate_md_calendar(year):
    # Initialize markdown content with a header
    md_output = f"# Calendar {year}\n\n"

    # Set MONDAY as the first day of the week
    cal = calendar.TextCalendar(calendar.MONDAY)

    for month in range(1, 13):
        month_name = calendar.month_name[month]
        # Add a clean month header
        md_output += f"## {month_name}\n\n"
        # Table columns starting on Monday
        md_output += "| Mo | Tu | We | Th | Fr | Sa | Su |\n"
        md_output += "| :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"

        # Returns a list of weeks starting on Monday containing tuples: (day_number, weekday_number)
        weeks = cal.monthdays2calendar(year, month)

        for week in weeks:
            row_cells = []
            for day, _ in week:
                if day == 0:
                    # Fill blank days with '--'
                    row_cells.append("--")
                else:
                    # Pad month and day to two digits
                    padded_month = f"{month:02}"
                    padded_day = f"{day:02}"
                    # Format as standard markdown link: [DD](MM-DD)
                    row_cells.append(f"[{padded_day}]({padded_month}-{padded_day})")

            # Join individual week cells into a markdown row string
            md_output += f"| {' | '.join(row_cells)} |\n"

        # Insert spacing between monthly tables
        md_output += "\n"

    return md_output


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a year.")
        print("Usage: python script.py YEAR")
        sys.exit(1)

    try:
        target_year = int(sys.argv[1])
        filename = f"{path}/{target_year}.md"

        # Generate content string
        calendar_content = generate_md_calendar(target_year)

        # Write to file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(calendar_content)

        print(f"Success! Generated Monday-start markdown calendar: {filename}")

    except ValueError:
        print("Error: The year must be a valid integer.")
        sys.exit(1)
