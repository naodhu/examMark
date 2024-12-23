import csv
import sqlite3
from colorama import Fore, Style


def create_database():
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()

    # Create units table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS units (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unit_name TEXT UNIQUE NOT NULL
        )
        """
    )

    # Create assessments table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unit_id INTEGER NOT NULL,
            assessment_name TEXT NOT NULL,
            raw_score TEXT NOT NULL,
            percentage_weight REAL NOT NULL,
            adjusted_mark REAL NOT NULL,
            FOREIGN KEY (unit_id) REFERENCES units (id)
        )
        """
    )

    conn.commit()
    conn.close()


def insert_mark(
    unit_name, assessment_name, raw_score, percentage_weight, adjusted_mark
):
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()

    # Insert unit if it doesn't exist
    cursor.execute(
        """
        INSERT OR IGNORE INTO units (unit_name) VALUES (?)
        """,
        (unit_name,),
    )

    # Get unit ID
    cursor.execute(
        """
        SELECT id FROM units WHERE unit_name = ?
        """,
        (unit_name,),
    )
    unit_id = cursor.fetchone()[0]

    # Insert assessment
    cursor.execute(
        """
        INSERT INTO assessments (unit_id, assessment_name, raw_score, percentage_weight, adjusted_mark)
        VALUES (?, ?, ?, ?, ?)
        """,
        (unit_id, assessment_name, raw_score, percentage_weight, adjusted_mark),
    )

    conn.commit()
    conn.close()


def fetch_all_marks():
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT 
                units.unit_name, 
                assessments.assessment_name, 
                assessments.raw_score, 
                assessments.percentage_weight, 
                assessments.adjusted_mark
            FROM assessments
            JOIN units ON assessments.unit_id = units.id
            ORDER BY units.unit_name
            """
        )
        rows = cursor.fetchall()

        if not rows:
            print(Fore.YELLOW + "No marks found in the database." + Style.RESET_ALL)
            return []

        return rows

    except sqlite3.Error as e:
        print(Fore.RED + f"Database error: {e}" + Style.RESET_ALL)
        return []

    finally:
        conn.close()


def delete_mark_by_name(assessment_name):
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM assessments WHERE assessment_name = ?", (assessment_name,)
    )
    conn.commit()
    conn.close()


def delete_marks_by_unit(unit_name):
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()

    # Get unit ID
    cursor.execute(
        """
        SELECT id FROM units WHERE unit_name = ?
        """,
        (unit_name,),
    )
    unit_id = cursor.fetchone()

    if unit_id:
        cursor.execute("DELETE FROM assessments WHERE unit_id = ?", (unit_id[0],))
        conn.commit()

    conn.close()


def update_mark(
    conn, assessment_name, new_raw_score, new_percentage_weight, new_adjusted_mark
):
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE assessments 
        SET raw_score = ?, percentage_weight = ?, adjusted_mark = ? 
        WHERE assessment_name = ?
        """,
        (new_raw_score, new_percentage_weight, new_adjusted_mark, assessment_name),
    )
    conn.commit()

    # Debugging: Verify the update
    cursor.execute(
        """
        SELECT raw_score, percentage_weight, adjusted_mark 
        FROM assessments WHERE assessment_name = ?
        """,
        (assessment_name,),
    )
    updated_row = cursor.fetchone()
    print(f"Updated row: {updated_row}")


def calculate_grades():
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 
            units.unit_name, 
            SUM(assessments.adjusted_mark) as total_percentage, 
            SUM(assessments.percentage_weight) as total_weight
        FROM assessments
        JOIN units ON assessments.unit_id = units.id
        GROUP BY units.unit_name
        """
    )
    rows = cursor.fetchall()

    grades = []
    for row in rows:
        unit_name, total_percentage, total_weight = row
        if total_weight < 100:
            grade = "Incomplete (More assessments pending)"
        elif total_percentage >= 85:
            grade = "HD (High Distinction)"
        elif total_percentage >= 75:
            grade = "D (Distinction)"
        elif total_percentage >= 65:
            grade = "C (Credit)"
        elif total_percentage >= 50:
            grade = "P (Pass)"
        else:
            grade = "F (Fail)"
        grades.append((unit_name, total_percentage, total_weight, grade))

    conn.close()
    return grades


def export_to_csv(filename="marks_export.csv"):
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT 
                units.unit_name, 
                assessments.assessment_name, 
                assessments.raw_score, 
                assessments.percentage_weight, 
                assessments.adjusted_mark
            FROM assessments
            JOIN units ON assessments.unit_id = units.id
            """
        )
        rows = cursor.fetchall()

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Unit Name",
                    "Assessment Name",
                    "Raw Score",
                    "Percentage Weight",
                    "Adjusted Mark",
                ]
            )
            writer.writerows(rows)

        print(
            Fore.GREEN + f"Data successfully exported to {filename}." + Style.RESET_ALL
        )
    except Exception as e:
        print(Fore.RED + f"An error occurred during export: {e}" + Style.RESET_ALL)
    finally:
        conn.close()


def import_from_csv(filename="marks_import.csv"):
    conn = sqlite3.connect("exam_marks.db")
    cursor = conn.cursor()

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Insert unit if it doesn't exist
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO units (unit_name) VALUES (?)
                    """,
                    (row["Unit Name"],),
                )

                # Get unit ID
                cursor.execute(
                    """
                    SELECT id FROM units WHERE unit_name = ?
                    """,
                    (row["Unit Name"],),
                )
                unit_id = cursor.fetchone()[0]

                # Insert assessment
                cursor.execute(
                    """
                    INSERT INTO assessments (unit_id, assessment_name, raw_score, percentage_weight, adjusted_mark)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        unit_id,
                        row["Assessment Name"],
                        row["Raw Score"],
                        float(row["Percentage Weight"]),
                        float(row["Adjusted Mark"]),
                    ),
                )

        conn.commit()
        print(
            Fore.GREEN
            + f"Data imported from {filename} successfully."
            + Style.RESET_ALL
        )

    except Exception as e:
        print(Fore.RED + f"An error occurred during import: {e}" + Style.RESET_ALL)

    finally:
        conn.close()
