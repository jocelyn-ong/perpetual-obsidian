import calendar
import os

def create_daily_note(day, month):
    # Create a daily note for the given day and month
    fname = f"{month:02d}-{day:02d}"
    month_name = calendar.month_abbr[month]

    # IF LAST DAY OR FIRST DAY OF MONTH, LINK TO PREVIOUS OR NEXT MONTH NOTE
    # IF MONTH IS JANUARY, LINK TO DECEMBER OF PREVIOUS YEAR; IF MONTH IS DECEMBER, LINK TO JANUARY OF NEXT YEAR
    if month == 1 and day == 1:
        ytd = f"12-31"
    else:
        ytd = f"{month:02d}-{day-1:02d}" if day > 1 else f"{month-1:02d}-{calendar.monthrange(year, month-1)[1]:02d}"
    
    if month == 12 and day == 31:
        tmr = f"01-01"
    else:
        tmr = f"{month:02d}-{day+1:02d}" if day < calendar.monthrange(year, month)[1] else f"{month+1:02d}-01"

    existing_files = os.listdir('../../daily')
    # print(existing_files)
    if f"{fname}.md" in existing_files:
        # print(f"Daily note for {fname} already exists. Skipping creation.")
        return 0
    else:
        with open(f"../../daily/{fname}.md", "w") as f:
            # f.write(f"# {fname}\n\n") # TITLE
            f.write(f"\n\n[[{month_name}]]\n\n") # LINK TO MONTH NOTE
            f.write(f"[[{ytd}]] | [[{tmr}]]\n\n") # LINK TO BEFORE AND AFTER
    return 0

year = 2024 # USE A LEAP YEAR FOR FULL DAYS

for i in range(1, 13):
    month = i
    month_name = calendar.month_abbr[i]
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        create_daily_note(day, month)

print('All daily notes created successfully.')