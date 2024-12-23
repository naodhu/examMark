# Exam Marks Tracker

A comprehensive Exam Marks Tracker application that allows users to manage and track their exam marks by unit names. The application features a sleek Material-UI design, dynamic functionality, and smooth interactions between the backend and frontend.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Backend API Documentation](#backend-api-documentation)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Features

- Add, delete, and view marks by unit name.
- Group marks dynamically by unit name.
- Backend integration with SQLite database.
- Beautiful Material-UI frontend design.
- Notifications using MUI Snackbar.
- Lightweight REST API for seamless data communication.

---

## Technologies Used

### Frontend

- **React.js**
- **Material-UI (MUI)**
- **Axios** (for API calls)

### Backend

- **Python (Flask)**
- **SQLite** (Database)
- **Flask-CORS** (for cross-origin requests)

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- **Node.js** (v14 or above)
- **Python** (v3.10 or above)
- **Git** (optional but recommended)

### Installation

#### Clone the repository:

```bash
git clone https://github.com/your-repo/exam-marks-tracker.git
cd exam-marks-tracker
```

## Set up the backend:

```bash
Copy code
cd backend
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
python app.py
```

## Set up the frontend:

```bash
Copy code
cd ../frontend
npm install
npm start
```

##### Visit the app in your browser at http://localhost:3000.

## Project Structure

```
exam-marks-tracker/
├── backend/
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AddMarkForm.js
│   │   │   └── MarksTable.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   └── package.json
├── README.md
```

# Usage

### Frontend

#### Adding Marks:

- Fill out the form and click Add Mark.
- Snackbar notifications display success or failure messages.

#### Viewing Marks:

- Marks are grouped by Unit Name in a styled Material-UI table.
- Adjusted marks are displayed dynamically.

#### Deleting Marks:

- Click the Delete button next to an assessment to remove it.

# Backend API Documentation

### Base URL

##### **http://127.0.0.1:5000/api**

### Endpoints

1. **GET /marks**

- Description: Fetch all marks from the database.
- Response:

```
[
  ["Math", "Quiz 1", "40/50", 10, 8.00],
  ["Science", "Final Exam", "90/100", 30, 27.00]
]
```

2. **POST /marks**

- Description: Add a new mark.
- Request Body:

```
{
  "unit_name": "Math",
  "assessment_name": "Quiz 1",
  "raw_score": "40/50",
  "percentage_weight": 10,
  "adjusted_mark": 8.00
}
```

- Response:

```
{"message": "Mark added successfully"}
```

3. **DELETE /marks/<assessment_name>**

- Description: Delete a specific assessment by its name.
- Response:

```
{"message": "Mark deleted successfully"}
```

# Screenshots

## Landing Page

## Add Marks Form

## Marks Table

# Future Enhancements

- Add user authentication.
- Enable editing marks.
- Implement export/import of marks as CSV.
- Add graph visualization of performance trends.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

Copy code
