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
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Reviews by Park")
    plt.show()
