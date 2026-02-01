import tui
import process
import visual


def main():
    title = "Disneyland Review Analyser"
    print(title)
    print("-" * len(title))

    try:
        data, cols = process.load_reviews("Disneyland_reviews.csv")
        print(f"{len(data)} reviews loaded.")
    except FileNotFoundError:
        print("CSV file not found. Make sure Disneyland_reviews.csv is in the same folder.")
        return

    while True:
        choice = tui.main_menu()

        if choice == "A":
            handle_view_data(data, cols)

        elif choice == "B":
            handle_visualise_data(data, cols)

        elif choice == "X":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


def handle_view_data(data, cols):
    while True:
        sub = tui.view_data_menu()

        if sub == "A":
            park = tui.ask_park(process.get_parks(data, cols))
            process.view_reviews_by_park(data, cols, park)
            input("\nPress Enter to return to the View Data menu...")

        elif sub == "B":
            park = tui.ask_park(process.get_parks(data, cols))
            location = input("Enter reviewer location (e.g. United Kingdom): ").strip()
            count = process.count_reviews_by_park_location(data, cols, park, location)
            print(f"\nNumber of reviews for {park} from {location}: {count}")
            input("\nPress Enter to return to the View Data menu...")

        elif sub == "C":
            park = tui.ask_park(process.get_parks(data, cols))
            year = input("Enter year (e.g. 2019): ").strip()
            avg = process.average_rating_by_park_year(data, cols, park, year)
            if avg is None:
                print("\nNo data found for that park/year.")
            else:
                print(f"\nAverage rating for {park} in {year}: {avg:.2f}")
            input("\nPress Enter to return to the View Data menu...")

        elif sub == "D":
            process.average_score_per_park_by_location(data, cols)
            input("\nPress Enter to return to the View Data menu...")

        elif sub == "X":
            break

        else:
            print("Invalid option")


def handle_visualise_data(data, cols):
    while True:
        sub = tui.visual_menu()

        if sub == "A":
            visual.pie_reviews_per_park(data, cols)

        elif sub == "B":
            park = tui.ask_park(process.get_parks(data, cols))
            visual.bar_top10_locations_avg(data, cols, park)

        elif sub == "C":
            park = tui.ask_park(process.get_parks(data, cols))
            visual.bar_avg_rating_by_month(data, cols, park)

        elif sub == "X":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
