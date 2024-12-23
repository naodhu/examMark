import questionary
from cli import (
    display_all_marks,
    delete_mark,
    display_filtered_marks,
    display_grades,
    display_help,
    show_progress,
)
from database import create_database, insert_mark, export_to_csv, import_from_csv
from colorama import Fore, Style


def calculate_adjusted_mark():
    print(Fore.YELLOW + "Exam Mark Adjustment Calculator" + Style.RESET_ALL)

    unit_name = input("Enter the unit name: ")
    assessment_name = input("Enter the name of the assessment: ")
    raw_score = input("Enter your raw score (e.g., 43/60): ")
    percentage_weight = float(
        input("Enter the percentage weight of the assessment (e.g., 5 for 5%): ")
    )

    try:
        score, total = map(float, raw_score.split("/"))
    except ValueError:
        print(
            Fore.RED
            + "Invalid score format. Please enter in 'x/y' format, e.g., 43/60."
            + Style.RESET_ALL
        )
        return

    if total == 0:
        print(Fore.RED + "Total marks cannot be zero." + Style.RESET_ALL)
        return

    raw_percentage = (score / total) * 100
    adjusted_mark = (raw_percentage * percentage_weight) / 100

    insert_mark(unit_name, assessment_name, raw_score, percentage_weight, adjusted_mark)

    print(Fore.GREEN + "\n--- Exam Mark Adjustment Results ---" + Style.RESET_ALL)
    print(f"Unit: {unit_name}")
    print(f"Assessment: {assessment_name}")
    print(f"Raw Score: {raw_score}")
    print(f"Raw Percentage: {raw_percentage:.2f}%")
    print(f"Weighted Contribution (at {percentage_weight}%): {adjusted_mark:.2f}%")


def main_menu():
    while True:
        try:
            choice = questionary.select(
                "What would you like to do?",
                choices=[
                    "1. Add a new mark",
                    "2. View all marks",
                    "3. Display grades",
                    "4. Delete marks",
                    "5. Export marks (CSV)",
                    "6. Import marks (CSV)",
                    "7. Filter marks",
                    "8. Help",
                    "9. Exit",
                ],
            ).ask()

            if choice == "1. Add a new mark":
                calculate_adjusted_mark()
            elif choice == "2. View all marks":
                display_all_marks()
            elif choice == "3. Display grades":
                display_grades()
            elif choice == "4. Delete marks":
                delete_mark()
            elif choice == "5. Export marks (CSV)":
                # Add progress animation for exporting
                show_progress("Exporting marks to CSV...", delay=2)
                export_to_csv()
                print(Fore.GREEN + "Marks successfully exported!" + Style.RESET_ALL)
            elif choice == "6. Import marks (CSV)":
                # Add progress animation for importing
                show_progress("Importing marks from CSV...", delay=2)
                import_from_csv()
                print(Fore.GREEN + "Marks successfully imported!" + Style.RESET_ALL)
            elif choice == "7. Filter marks":
                display_filtered_marks()
            elif choice == "8. Help":
                display_help()
            elif choice == "9. Exit":
                print(Fore.RED + "Goodbye! Exiting program..." + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        except KeyboardInterrupt:
            print(
                Fore.RED + "\nProgram interrupted by user. Exiting..." + Style.RESET_ALL
            )
            break
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)

    while True:
        try:
            choice = questionary.select(
                "What would you like to do?",
                choices=[
                    "1. Add a new mark",
                    "2. View all marks",
                    "3. Display grades",
                    "4. Delete marks",
                    "5. Export marks (CSV)",
                    "6. Import marks (CSV)",
                    "7. Filter marks",
                    "8. Help",
                    "9. Exit",
                ],
            ).ask()

            if choice == "1. Add a new mark":
                calculate_adjusted_mark()
            elif choice == "2. View all marks":
                display_all_marks()
            elif choice == "3. Display grades":
                display_grades()
            elif choice == "4. Delete marks":
                delete_mark()
            elif choice == "5. Export marks (CSV)":
                export_to_csv()
            elif choice == "6. Import marks (CSV)":
                import_from_csv()
            elif choice == "7. Filter marks":
                display_filtered_marks()
            elif choice == "8. Help":
                display_help()
            elif choice == "9. Exit":
                print(Fore.GREEN + "Goodbye! Exiting..." + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        except KeyboardInterrupt:
            print(
                Fore.RED + "\nProgram interrupted by user. Exiting..." + Style.RESET_ALL
            )
            break
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        print("Initializing database...")
        create_database()
        print("Starting the main menu...")
        main_menu()
        print("Exited the main menu.")
    except Exception as e:
        print(Fore.RED + f"Critical error: {e}" + Style.RESET_ALL)
