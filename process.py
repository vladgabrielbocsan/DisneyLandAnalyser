import csv
from collections import defaultdict


def load_reviews(filename):
    data = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        cols = {h: i for i, h in enumerate(headers)}

        for row in reader:
            data.append(row)

    return data, cols


def get_parks(data, cols):
    parks = set()
    for row in data:
        parks.add(row[cols["Branch"]].strip())
    return sorted(parks)


def view_reviews_by_park(data, cols, park):
    found = False
    for row in data:
        if row[cols["Branch"]].strip() == park:
            # Print the whole row (you can format this nicer if you want)
            print(row)
            found = True
    if not found:
        print("No reviews found for that park.")


def count_reviews_by_park_location(data, cols, park, location):
    count = 0
    for row in data:
        if row[cols["Branch"]].strip() == park and row[cols["Reviewer_Location"]].strip() == location:
            count += 1
    return count


def average_rating_by_park_year(data, cols, park, year):
    ratings = []
    for row in data:
        if row[cols["Branch"]].strip() != park:
            continue

        ym = row[cols["Year_Month"]].strip()
        if not ym.startswith(year):
            continue

        try:
            ratings.append(int(row[cols["Rating"]]))
        except ValueError:
            continue

    if not ratings:
        return None
    return sum(ratings) / len(ratings)


def average_score_per_park_by_location(data, cols):
    store = defaultdict(lambda: defaultdict(list))

    for row in data:
        park = row[cols["Branch"]].strip()
        loc = row[cols["Reviewer_Location"]].strip()

        try:
            rating = int(row[cols["Rating"]])
        except ValueError:
            continue

        store[park][loc].append(rating)

    for park in sorted(store):
        print(f"\nPark: {park}")
        locs = store[park]

        for loc in sorted(locs):
            ratings = locs[loc]
            avg = sum(ratings) / len(ratings)
            print(f"  {loc}: {avg:.2f} (n={len(ratings)})")
