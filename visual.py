import matplotlib.pyplot as plt
from collections import defaultdict


def pie_reviews_per_park(data, cols):
    counts = defaultdict(int)

    for row in data:
        park = row[cols["Branch"]].strip()
        counts[park] += 1

    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.show()


def bar_top10_locations_avg(data, cols, park):
    location_ratings = defaultdict(list)

    for row in data:
        if row[cols["Branch"]].strip() != park:
            continue

        try:
            rating = int(row[cols["Rating"]])
        except ValueError:
            continue

        location = row[cols["Reviewer_Location"]].strip()
        location_ratings[location].append(rating)

    averages = []
    for loc, ratings in location_ratings.items():
        avg = sum(ratings) / len(ratings)
        averages.append((loc, avg))

    averages.sort(key=lambda x: x[1], reverse=True)
    top10 = averages[:10]

    locations = [x[0] for x in top10]
    avgs = [x[1] for x in top10]

    plt.bar(locations, avgs)
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top 10 Locations by Average Rating – {park}")
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()


def bar_avg_rating_by_month(data, cols, park):
    month_ratings = defaultdict(list)

    for row in data:
        if row[cols["Branch"]].strip() != park:
            continue

        ym = row[cols["Year_Month"]].strip()

        try:
            # expected format "YYYY-MM"
            month = int(ym.split("-")[1])
            rating = int(row[cols["Rating"]])
        except (IndexError, ValueError):
            continue

        month_ratings[month].append(rating)

    months = []
    avgs = []

    for m in range(1, 13):
        if m in month_ratings:
            avg = sum(month_ratings[m]) / len(month_ratings[m])
            months.append(m)
            avgs.append(avg)

    plt.bar(months, avgs)
    plt.xticks(
        range(1, 13),
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    )
    plt.title(f"Average Rating by Month – {park}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.show()
