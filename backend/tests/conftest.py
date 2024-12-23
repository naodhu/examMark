import sqlite3
import pytest


@pytest.fixture
def setup_database():
    """Fixture to create a fresh in-memory database for each test."""
    conn = sqlite3.connect(":memory:")  # Use an in-memory database
    cursor = conn.cursor()

    # Create the schema for `units` and `assessments` tables
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS units (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unit_name TEXT UNIQUE NOT NULL
        )
        """
    )
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

    yield conn  # Provide the connection to the tests

    conn.close()  # Cleanup after the test
