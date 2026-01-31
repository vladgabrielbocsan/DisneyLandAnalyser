def main_menu():
    print("\n[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    return input("Select an option: ").strip().upper()


def view_data_menu():
    print("\nView Data Menu")
    print("[A] View Reviews by Park")
    print("[X] Return to Main Menu")
    return input("Select an option: ").strip().upper()


def ask_park(parks):
    print("\nAvailable parks:")
    for p in parks:
        print(f"- {p}")
    return input("Type a park name exactly as shown: ").strip()
