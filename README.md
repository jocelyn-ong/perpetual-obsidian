# Perpetual Daily Notes for Obsidian

# Python Scripts

- `create_year_calendar.py` creates a note with the `year` as the title with a monthly calendar with links to each day
- `update_month_calendar.py` reads the notes in the `monthly` folder and appends the current year's month layout to the respective `month` note
- `create_daily_note.py` creates 1 note per day - this should only be required in the initial set up

# Initial Set Up

- Clone repo
- cd to python folder and run
    - `python create_daily_note.py`
    - `python update_month_calendar.py {YYYY}`, replace `{YYYY}` with the desired year
    - `python create_year_calendar.py {YYYY}`, replace `{YYYY}` with the desired year
- Copy `daily`, `monthly`, `yearly` folders into your Obsidian Vault as desired, rename if you want to
- Update Obsidian settings

# No Script Set Up

- Download `daily` folder into your Obsidian Vault, no further updates required from this repo

# Obsidian Settings

Core plugins > Daily notes 
Date format: Custom
Custom format: MM-DD
New file location: daily (or whatever you want to name the folder)

# Updates

- Copy `monthly` or `yearly` folder from Obsidian back into this repo then run the respective python scripts as required

