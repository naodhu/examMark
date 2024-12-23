import time
from tqdm import tqdm
from colorama import Fore, Style
from database import (
    fetch_all_marks,
    delete_mark_by_name,
    delete_marks_by_unit,
    calculate_grades,
    fetch_all_marks,
)


def display_all_marks():
    """Display all stored marks."""
    rows = fetch_all_marks()
    if not rows:
        print(Fore.RED + "No marks found in the database." + Style.RESET_ALL)
        return

    current_unit = None
    total_percentage = 0

    print(Fore.YELLOW + "\n--- All Stored Marks ---" + Style.RESET_ALL)
    for row in rows:
        unit_name, assessment_name, raw_score, percentage_weight, adjusted_mark = row[
            1:
        ]
        if unit_name != current_unit:
            if current_unit is not None:
                print("\n")
            print(Fore.CYAN + f"Unit: {unit_name}" + Style.RESET_ALL)
            current_unit = unit_name

        print(
            f"  {Fore.GREEN}Assessment: {assessment_name}, Raw Score: {raw_score}, Weight: {percentage_weight}%, Adjusted Mark: {adjusted_mark:.2f}%{Style.RESET_ALL}"
        )
        total_percentage += adjusted_mark

    print(
        Fore.YELLOW
        + f"\nTotal Adjusted Percentage: {total_percentage:.2f}% (Out of 100%)"
        + Style.RESET_ALL
    )


def delete_mark():
    """Delete specific marks or all marks for a unit."""
    print(Fore.YELLOW + "\nDelete Options:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Delete specific assessment" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Delete all assessments in a unit" + Style.RESET_ALL)
    choice = input("Enter your choice: ")

    if choice == "1":
        assessment_name = input("Enter the name of the assessment to delete: ")
        delete_mark_by_name(assessment_name)
        print(Fore.GREEN + f"Assessment '{assessment_name}' deleted." + Style.RESET_ALL)
    elif choice == "2":
        unit_name = input("Enter the unit name to delete all assessments: ")
        delete_marks_by_unit(unit_name)
        print(
            Fore.GREEN
            + f"All assessments for unit '{unit_name}' deleted."
            + Style.RESET_ALL
        )
    else:
        print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)


def display_grades():
    """Display grades for all units."""
    grades = calculate_grades()
    if not grades:
        print(
            Fore.RED
            + "No grades available. Add marks to calculate grades."
            + Style.RESET_ALL
        )
        return

    print(Fore.YELLOW + "\n--- Grades by Unit ---" + Style.RESET_ALL)
    for unit_name, total_percentage, total_weight, grade in grades:
        print(
            f"Unit: {Fore.CYAN}{unit_name}{Style.RESET_ALL}, "
            f"Total Percentage: {Fore.GREEN}{total_percentage:.2f}%{Style.RESET_ALL}, "
            f"Total Weight: {Fore.GREEN}{total_weight:.2f}%{Style.RESET_ALL}, "
            f"Grade: {Fore.MAGENTA}{grade}{Style.RESET_ALL}"
        )


def filter_marks_by_unit(unit_name):
    rows = fetch_all_marks()
    filtered_rows = [row for row in rows if row[1] == unit_name]
    return filtered_rows


def filter_marks_by_assessment(assessment_name):
    rows = fetch_all_marks()
    filtered_rows = [row for row in rows if row[2] == assessment_name]
    return filtered_rows


def display_filtered_marks():
    print(Fore.YELLOW + "\nFilter Options:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Filter by unit name" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Filter by assessment name" + Style.RESET_ALL)
    choice = input("Enter your choice: ")

    if choice == "1":
        unit_name = input("Enter the unit name: ")
        rows = filter_marks_by_unit(unit_name)
    elif choice == "2":
        assessment_name = input("Enter the assessment name: ")
        rows = filter_marks_by_assessment(assessment_name)
    else:
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        return

    for row in rows:
        print(
            f"Unit: {row[1]}, Assessment: {row[2]}, Raw Score: {row[3]}, Weight: {row[4]}%, Adjusted Mark: {row[5]:.2f}%"
        )


def display_help():
    """Display help documentation."""
    print(Fore.CYAN + "\n--- Help ---" + Style.RESET_ALL)
    print("This program allows you to manage and calculate exam marks effectively.")
    print("\nFeatures:")
    print(
        "1. Add a new mark: Add your exam marks and their weight to calculate percentages."
    )
    print("2. View all marks: Display all stored marks grouped by unit.")
    print("3. Display grades: View your grades based on total percentages.")
    print("4. Delete marks: Remove specific marks or all marks for a unit.")
    print("5. Export marks (CSV): Save your marks to a CSV file for backup.")
    print("6. Import marks (CSV): Load marks from a CSV file.")
    print("7. Filter marks: View marks for a specific unit or assessment.")
    print("8. Help: Display this help documentation.")
    print("9. Exit: Exit the program.")
    print(
        Fore.CYAN
        + "\nFor more detailed documentation, check the README.md file in the project folder."
        + Style.RESET_ALL
    )


def show_progress(message, delay=2):
    """Show a loading animation."""
    print(Fore.YELLOW + message + Style.RESET_ALL)
    for _ in tqdm(range(100), desc="Processing", ascii=" █", colour="green"):
        time.sleep(delay / 100)
