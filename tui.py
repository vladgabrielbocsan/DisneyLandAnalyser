def main_menu():
    print("\n[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    return input("Select an option: ").strip().upper()


def view_data_menu():
    print("\nView Data Menu")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Location")
    print("[C] Average Reviews by Park and Year")
    print("[X] Return to Main Menu")
    return input("Select an option: ").strip().upper()


def ask_park(parks):
    print("\nAvailable parks:")
    for p in parks:
        print(f"- {p}")
    return input("Type a park name exactly as shown: ").strip()


def ask_location():
    return input("Type a reviewer location (e.g., United Kingdom): ").strip()

def ask_year():
    return input("Type a year (e.g.,2019): ").strip()

def visual_menu():
    print("\nVisualise Data Menu")
    print("[A] Pie Chart: Reviews per Park")
    print("[x] Return to Main Menu")
    return input("Select an option: ").strip().upper()