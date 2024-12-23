# Exam Marks Calculator

## Overview

The Exam Marks Calculator is a Python-based CLI tool designed to help students and educators manage and calculate exam marks efficiently. It allows users to input marks, calculate adjusted percentages, view grades, export/import data, and filter marks by various criteria. This tool simplifies academic tracking and ensures accurate grade calculations.

## Features

- **Add Marks**: Add your exam marks and their weights to calculate adjusted percentages.
- **View Marks**: Display all stored marks grouped by unit.
- **Calculate Grades**: Automatically calculate grades based on total percentages (HD, D, C, P, F).
- **Delete Marks**: Remove specific marks or all marks for a unit.
- **Export to CSV**: Save your marks to a CSV file for backup or sharing.
- **Import from CSV**: Load marks from a CSV file for bulk updates.
- **Filter Marks**: Filter marks by unit name or assessment name.
- **Help**: Access program documentation directly in the CLI.

## How to Run the Program

### Prerequisites

- Python 3.10 or later installed on your machine.
- A terminal or IDE capable of running Python scripts.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/exam-marks-calculator.git
   cd exam-marks-calculator
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the program from the terminal:

```bash
python main.py
```

Examples
Adding a Mark
When adding a new mark, the program will ask you to input the unit name, assessment name, raw score, and percentage weight. Here's an example interaction:

plaintext
Copy code
Enter the unit name: Object Oriented Programming
Enter the name of the assessment: Iteration 1
Enter your raw score (e.g., 43/60): 45/50
Enter the percentage weight of the assessment (e.g., 5 for 5%): 20

--- Exam Mark Adjustment Results ---
Unit: Object Oriented Programming
Assessment: Iteration 1
Raw Score: 45/50
Raw Percentage: 90.00%
Weighted Contribution (at 20%): 18.00%
Viewing Marks
To view all the marks you’ve entered, select the appropriate option from the menu. Here's an example output:

plaintext
Copy code
--- All Stored Marks ---
Unit: Object Oriented Programming
Assessment: Iteration 1, Raw Score: 45/50, Weight: 20.0%, Adjusted Mark: 18.00%
Total Adjusted Percentage: 18.00% (Out of 100%)
Exporting Marks
You can export your stored marks to a CSV file. The program will confirm a successful export:

plaintext
Copy code
Data successfully exported to marks_export.csv.
Help Menu
The help menu provides a quick overview of the program's features and how to use them:

plaintext
Copy code
--- Help ---
This program allows you to manage and calculate exam marks effectively.

Features:

1. Add a new mark: Add your exam marks and their weight to calculate percentages.
2. View all marks: Display all stored marks grouped by unit.
3. Display grades: View your grades based on total percentages.
4. Delete marks: Remove specific marks or all marks for a unit.
5. Export marks (CSV): Save your marks to a CSV file for backup.
6. Import marks (CSV): Load marks from a CSV file.
7. Filter marks: View marks for a specific unit or assessment.
8. Help: Display this help documentation.
9. Exit: Exit the program.

For more detailed documentation, check the README.md file in the project folder.
Exiting the Program
When you exit the program, you’ll see the following message:

plaintext
Copy code
Goodbye! Exiting...
Project Structure
plaintext
Copy code
exam-marks-calculator/
├── main.py # Entry point for the program
├── cli.py # CLI functions and menu displays
├── database.py # Database operations
├── tests/ # Unit tests for the program
│ ├── test_database.py
│ ├── test_calculate_grades.py
│ ├── test_edit_mark.py
├── requirements.txt # Python dependencies
├── README.md # Project documentation
Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

License
This project is licensed under the MIT License.