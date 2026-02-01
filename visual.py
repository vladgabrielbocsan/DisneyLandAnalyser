import matplotlib.pyplot as plt


def pie_reviews_per_park(data, cols):
    park_col = cols["park"]
    counts = {}

    for row in data:
        park = row[park_col].strip()
        counts[park] = counts.get(park, 0) + 1

    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.show()


def bar_top10_locations_by_avg_rating(data, cols, park_name):
    park_col = cols["park"]
    loc_col = cols["location"]
    rating_col = cols["rating"]

    want_park = park_name.strip().lower()

    totals = {}   # location -> sum ratings
    counts = {}   # location -> count

    for row in data:
        if row[park_col].strip().lower() != want_park:
            continue

        loc = row[loc_col].strip()
        rating = float(row[rating_col])

        totals[loc] = totals.get(loc, 0.0) + rating
        counts[loc] = counts.get(loc, 0) + 1

    avgs = []
    for loc in totals:
        avgs.append((loc, totals[loc] / counts[loc]))

    avgs.sort(key=lambda x: x[1], reverse=True)
    top10 = avgs[:10]

    if not top10:
        print("No data found for that park.")
        return

    labels = [x[0] for x in top10]
    values = [x[1] for x in top10]

    plt.figure()
    plt.bar(labels, values)
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top 10 Locations by Avg Rating — {park_name}")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()


def bar_avg_rating_by_month(data, cols, park_name):
    park_col = cols["park"]
    rating_col = cols["rating"]
    date_col = cols["date"]

    want_park = park_name.strip().lower()

    totals = {m: 0.0 for m in range(1, 13)}
    counts = {m: 0 for m in range(1, 13)}

    for row in data:
        if row[park_col].strip().lower() != want_park:
            continue

        ym = row[date_col].strip()  # "YYYY-MM"
        if len(ym) < 7 or ym[4] != "-":
            continue

        month = int(ym[5:7])
        rating = float(row[rating_col])

        if 1 <= month <= 12:
            totals[month] += rating
            counts[month] += 1

    months = list(range(1, 13))
    avg_by_month = []
    for m in months:
        if counts[m] == 0:
            avg_by_month.append(0.0)
        else:
            avg_by_month.append(totals[m] / counts[m])

    month_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    plt.figure()
    plt.bar(month_labels, avg_by_month)
    plt.title(f"Average Rating by Month — {park_name}")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()
