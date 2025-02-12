import requests
import csv
import argparse

def read_school_data(input_file):
    """Reads school IDs and names from a CSV file."""
    school_data = []
    with open(input_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) >= 2:
                school_data.append((row[0], row[1]))  # (schoolId, schoolName)
    return school_data

def fetch_schedule(url, school_id, school_name):
    """Fetches the schedule data from the API."""
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data for {school_name} ({school_id}): {response.status_code}")
        return []

    data = response.json()

    schedules = data.get("schedules", [])
    if not schedules:
        print(f"No schedules found for {school_name} ({school_id}).")
        return []

    games = schedules[0].get("games", [])
    if not games:
        print(f"No games found for {school_name} ({school_id}).")
        return []

    schedule_data = []

    for game in games:
        date = game.get("eventDate", "Unknown")
        time = game.get("startTime", "Unknown")
        is_home = "Home" if game.get("isHome") else "Away"
        opponent = game.get("opponent", {}).get("name", "Unknown")
        result = game.get("result", "TBD")

        schedule_data.append([school_id, school_name, date, time, is_home, opponent, result])

    return schedule_data

def save_schedules(school_data, base_url, output_file):
    """Fetches and saves all schedules into a CSV file."""
    headers = ["School ID", "School Name", "Date", "Time", "Home/Away", "Opponent", "Result"]

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for school_id, school_name in school_data:
            url = base_url.replace("{schoolId}", school_id)
            schedule_data = fetch_schedule(url, school_id, school_name)
            writer.writerows(schedule_data)

    print(f"All schedules saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch volleyball schedules for multiple schools.")
    parser.add_argument("input_file", type=str, help="CSV file containing School IDs and Names")

    args = parser.parse_args()

    base_url = "https://www.countysports.zone/api/csz/schedules?countyId=7jMAWdKZ2X-G-Zy3aI5Xj&schoolId={schoolId}&season=2024-2025&sportId=11CpRFQNYGDj_9JpvaAk-&stateId=qC5FViFvLELikus3onZVb"
    output_file = "volleyball_schedules.csv"

    school_data = read_school_data(args.input_file)
    save_schedules(school_data, base_url, output_file)
