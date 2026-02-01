import csv


def load_reviews(filename):
    data = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def resolve_columns(sample_row):
    keys = set(sample_row.keys())

    def pick(options):
        for opt in options:
            if opt in keys:
                return opt
        return None

    return {
        "id": pick(["Review_ID", "ID"]),
        "park": pick(["Branch", "Park", "Disneyland_Park"]),
        "location": pick(["Reviewer_Location", "Location", "Country"]),
        "rating": pick(["Rating", "Score"]),
        "date": pick(["Year_Month", "Date"]),
    }


def list_parks(data, cols):
    park_col = cols["park"]
    parks = set()
    for row in data:
        parks.add(row[park_col].strip())
    return sorted(parks)


def filter_by_park(data, cols, park_name):
    park_col = cols["park"]
    wanted = park_name.strip().lower()
    return [
        row for row in data
        if row[park_col].strip().lower() == wanted
    ]


def count_by_park_and_location(data, cols, park_name, location_name):
    park_col = cols["park"]
    loc_col = cols["location"]

    want_park = park_name.strip().lower()
    want_loc = location_name.strip().lower()

    count = 0
    for row in data:
        if (
            row[park_col].strip().lower() == want_park
            and row[loc_col].strip().lower() == want_loc
        ):
            count += 1

    return count

def average_rating_by_park_and_year(data, cols, park_name, year):
    park_col = cols["park"]
    rating_col = cols["rating"]
    date_col = cols["date"]

    want_park = park_name.strip().lower()
    want_year = year.strip()

    total = 0.0
    count = 0

    for row in data:
        if row[park_col].strip().lower() != want_park:
            continue

        ym = row[date_col].strip()          # e.g. "2018-07"
        row_year = ym[:4]                   # "2018"

        if row_year == want_year:
            total += float(row[rating_col])
            count += 1

    if count == 0:
        return None

    return total / count


