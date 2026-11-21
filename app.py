from flask import Flask, render_template, request
import os
from datetime import datetime
import re
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_document():

    if "document" not in request.files:
        return "No document selected"

    file = request.files["document"]

    if file.filename == "":
        return "Please select a document"

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

        image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(image_path)

        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)

        # Required field checking
        required_fields = [
            "Name:",
            "Date of Birth:",
            "Document ID:",
            "Country:"
        ]

        missing_fields = []

        for field in required_fields:
            if field.lower() not in extracted_text.lower():
                missing_fields.append(field)

        # Name validation
        name_match = re.search(
            r"Name:\s*(.*)",
            extracted_text,
            re.IGNORECASE
        )

        name_issue = None

        if not name_match or not name_match.group(1).strip():
            name_issue = "Name is missing or empty"

        # Date of birth validation
        date_match = re.search(
            r"Date of Birth:\s*(\d{2}-\d{2}-\d{4})",
            extracted_text,
            re.IGNORECASE
        )

        date_issue = None

        if date_match:
            try:
                datetime.strptime(date_match.group(1), "%d-%m-%Y")
            except ValueError:
                date_issue = "Invalid date of birth"
        else:
            date_issue = "Date of birth is missing or has an invalid format"

        # Demo Document ID format validation
        id_match = re.search(
            r"Document ID:\s*DEMO\d{5}",
            extracted_text,
            re.IGNORECASE
        )

        id_issue = None

        if not id_match:
            id_issue = "Invalid or missing Document ID format"

        # Country validation
        country_match = re.search(
            r"Country:\s*(.*)",
            extracted_text,
            re.IGNORECASE
        )

        country_issue = None

        if not country_match or not country_match.group(1).strip():
            country_issue = "Country is missing or empty"

        # Final screening result
        if (
            missing_fields
            or name_issue
            or date_issue
            or id_issue
            or country_issue
        ):
            screening_result = "Review Recommended"
        else:
            screening_result = "No Obvious Issues Found"

        return render_template(
            "result.html",
            filename=filename,
            extracted_text=extracted_text,
            screening_result=screening_result,
            missing_fields=missing_fields,
            name_issue=name_issue,
            date_issue=date_issue,
            id_issue=id_issue,
            country_issue=country_issue
        )

    return "Invalid file type. Upload JPG, JPEG or PNG."


if __name__ == "__main__":
    app.run(debug=True)