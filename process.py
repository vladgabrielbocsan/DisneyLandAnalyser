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
