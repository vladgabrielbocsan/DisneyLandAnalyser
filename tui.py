def main_menu():
    print("\n[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")
    return input("Select an option: ").strip().upper()


def view_data_menu():
    print("\nView Data Menu")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Location")
    print("[C] Average Rating by Park and Year")
    print("[D] Average Score per Park by Reviewer Location")
    print("[X] Return to Main Menu")
    return input("Select an option: ").strip().upper()


def visual_menu():
    print("\nVisualise Data Menu")
    print("[A] Pie Chart: Reviews per Park")
    print("[B] Bar Chart: Top 10 Locations by Average Rating (Park)")
    print("[C] Bar Chart: Average Rating by Month (Park)")
    print("[X] Return to Main Menu")
    return input("Select an option: ").strip().upper()


def ask_park(parks):
    print("\nAvailable parks:")
    for p in parks:
        print(f"- {p}")
    return input("Type a park name exactly as shown: ").strip()
