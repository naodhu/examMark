import pytest
from database import calculate_grades, insert_mark  # Add calculate_grades import


def test_calculate_grades(setup_database):
    """Test calculating grades."""
    conn = setup_database
    cursor = conn.cursor()

    # Insert sample data specific to this test
    cursor.execute("INSERT INTO units (unit_name) VALUES ('Statistics')")
    unit_id = cursor.lastrowid
    cursor.executemany(
        """
        INSERT INTO assessments (unit_id, assessment_name, raw_score, percentage_weight, adjusted_mark)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (unit_id, "Assignment 1", "40/50", 10, 8.00),
            (unit_id, "Final Exam", "80/100", 40, 32.00),
        ],
    )
    conn.commit()

    # Call the function
    grades = calculate_grades()

    # Filter results for the "Statistics" unit only
    grades = [grade for grade in grades if grade[0] == "Statistics"]

    # Assertions
    assert len(grades) == 1
    assert grades[0][0] == "Statistics"
    assert grades[0][1] == 40.00
    assert grades[0][3] == "Incomplete (More assessments pending)"
