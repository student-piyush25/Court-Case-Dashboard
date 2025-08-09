from flask import Blueprint, render_template, request
from .models import CaseInfo
from . import db

# Simulated court scraper function
def fetch_case_data(case_type, case_number, filing_year):
    return {
        "petitioner": "John Doe",
        "respondent": "State of XYZ",
        "next_hearing": "20-Aug-2025",
        "order_pdf": "https://example.com/fake-order.pdf"
    }

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form.get('case_type')
        case_number = request.form.get('case_number')
        filing_year = request.form.get('filing_year')

        # Save to DB
        new_case = CaseInfo(
            case_type=case_type,
            case_number=case_number,
            filing_year=filing_year
        )
        db.session.add(new_case)
        db.session.commit()

        # Fetch simulated data
        case_details = fetch_case_data(case_type, case_number, filing_year)

        # Pass all data to result.html
        return render_template(
            'result.html',
            case_type=case_type,
            case_number=case_number,
            filing_year=filing_year,
            petitioner=case_details['petitioner'],
            respondent=case_details['respondent'],
            next_hearing=case_details['next_hearing'],
            order_pdf=case_details['order_pdf']
        )

    return render_template('index.html')


@main.route('/cases')
def all_cases():
    # Fetch all saved cases from DB
    cases = CaseInfo.query.all()
    return render_template('cases.html', cases=cases)


