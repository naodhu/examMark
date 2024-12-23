from flask import Flask, jsonify, request
from flask_cors import CORS
from database import create_database, fetch_all_marks, insert_mark, delete_mark_by_name

app = Flask(__name__)
CORS(app)  # Allow requests from the frontend

# Initialize database
create_database()
print("Creating database and tables...")


@app.route("/")
def home():
    return "Welcome to the Exam Marks API! This is the backend service."


@app.route("/api/marks", methods=["GET"])
def get_marks():
    marks = fetch_all_marks()
    if marks:
        return jsonify(marks), 200
    else:
        print("No marks found in the database.")  # Debugging message
        return jsonify([]), 200  # Return an empty array if no data


@app.route("/api/marks", methods=["POST"])
def add_mark():
    try:
        data = request.json

        # Validate input
        required_fields = [
            "unit_name",
            "assessment_name",
            "raw_score",
            "percentage_weight",
            "adjusted_mark",
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"'{field}' is required"}), 400

        # Add mark to the database
        insert_mark(
            data["unit_name"],
            data["assessment_name"],
            data["raw_score"],
            float(data["percentage_weight"]),
            float(data["adjusted_mark"]),
        )
        return jsonify({"message": "Mark added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/marks/<assessment_name>", methods=["DELETE"])
def delete_mark(assessment_name):
    try:
        delete_mark_by_name(assessment_name)
        return jsonify({"message": "Mark deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
