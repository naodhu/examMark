import pytest
from database import update_mark, fetch_all_marks


def test_edit_mark(setup_database):
    """Test editing an existing mark."""
    conn = setup_database
    cursor = conn.cursor()

    # Insert a unit and an assessment
    cursor.execute("INSERT INTO units (unit_name) VALUES ('Math')")
    unit_id = cursor.lastrowid
    cursor.execute(
        """
        INSERT INTO assessments (unit_id, assessment_name, raw_score, percentage_weight, adjusted_mark)
        VALUES (?, ?, ?, ?, ?)
        """,
        (unit_id, "Midterm", "30/40", 25, 18.75),
    )
    conn.commit()

    # Update the mark using the same connection
    update_mark(conn, "Midterm", "35/40", 25, 21.88)

    # Fetch the updated data
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
        WHERE assessments.assessment_name = 'Midterm'
        """
    )
    rows = cursor.fetchall()

    # Assertions
    assert len(rows) == 1
    assert rows[0][0] == "Math"
    assert rows[0][1] == "Midterm"
    assert rows[0][2] == "35/40"  # Updated raw score
    assert rows[0][3] == 25  # Percentage weight remains the same
    assert rows[0][4] == 21.88  # Updated adjusted mark
