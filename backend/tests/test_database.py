import pytest
from database import insert_mark, fetch_all_marks


def test_insert_mark(setup_database):
    """Test inserting a mark into the database."""
    conn = setup_database
    cursor = conn.cursor()

    # Insert a unit and an assessment
    cursor.execute(
        "INSERT INTO units (unit_name) VALUES ('Object Oriented Programming')"
    )
    unit_id = cursor.lastrowid
    cursor.execute(
        """
        INSERT INTO assessments (unit_id, assessment_name, raw_score, percentage_weight, adjusted_mark)
        VALUES (?, ?, ?, ?, ?)
        """,
        (unit_id, "Iteration 1", "45/50", 20, 18.00),
    )
    conn.commit()

    # Fetch the data
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

    # Assertions
    assert len(rows) == 1
    assert rows[0][0] == "Object Oriented Programming"
    assert rows[0][1] == "Iteration 1"
    assert rows[0][2] == "45/50"
    assert rows[0][3] == 20
    assert rows[0][4] == 18.00
