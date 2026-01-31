import tui
import process

def main():
    title = "Disneyland Rewiew Analyser"
    print(title)
    print("-" * len(title))

    data = process.load_reviews("Disneyland_reviews.csv")
    print(f"{len(data)} reviews loaded.")
    print(data[0].keys())

    while True:
        choice = tui.main_menu()

        if choice == "X":
            print("Goodbye!")
            break

        else:
            print("Option not implemented yet")

if __name__ == "__main__":
    main()

