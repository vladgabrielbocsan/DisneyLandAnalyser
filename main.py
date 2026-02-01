import tui
import process


def main():
    title = "Disneyland Review Analyser"
    print(title)
    print("-" * len(title))

    data = process.load_reviews("Disneyland_reviews.csv")
    print(f"{len(data)} reviews loaded.")

    cols = process.resolve_columns(data[0])

    if (
        cols["park"] is None
        or cols["rating"] is None
        or cols["date"] is None
        or cols["location"] is None
        or cols["id"] is None
    ):
        print("Error: CSV is missing required columns.")
        print("Found columns:", list(data[0].keys()))
        print("Resolved columns:", cols)
        return

    while True:
        choice = tui.main_menu()

        if choice == "A":
            handle_view_data(data, cols)

        elif choice == "X":
            print("Goodbye!")
            break

        else:
            print("Option not implemented yet")


def handle_view_data(data, cols):
    while True:
        sub = tui.view_data_menu()

        if sub == "A":
            # B.7 View Reviews by Park
            parks = process.list_parks(data, cols)
            park = tui.ask_park(parks)

            matches = process.filter_by_park(data, cols, park)

            print(f"\nFound {len(matches)} reviews for park: {park}")

            id_col = cols["id"]
            rating_col = cols["rating"]
            date_col = cols["date"]
            loc_col = cols["location"]

            for row in matches[:10]:
                print("-" * 40)
                print(f"Review ID: {row[id_col]}")
                print(f"Rating: {row[rating_col]}")
                print(f"Year_Month: {row[date_col]}")
                print(f"Reviewer Location: {row[loc_col]}")

        elif sub == "B":
            # B.8 Number of Reviews by Park and Location
            parks = process.list_parks(data, cols)
            park = tui.ask_park(parks)
            location = tui.ask_location()

            count = process.count_by_park_and_location(data, cols, park, location)
            print(f"\nNumber of reviews for {park} from {location}: {count}")

        elif sub == "C":
            parks = process.list_parks(data, cols)
            park = tui.ask_park(parks)
            year = tui.ask_year()

            avg = process.average_rating_by_park_and_year(data, cols, park, year)

            if avg is None:
                print(f"\nNo reviews for {park} from {year}.")
            else:
                print(f"\nAverage rating for {park} in {year}: {avg:.2f}")

        elif sub == "X":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
