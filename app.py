from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle
from datetime import datetime

app = Flask(__name__)

# Oracle Database Configuration
dsn = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1')  # Adjust host, port, and service_name
connection = cx_Oracle.connect(user='system', password='mehakfaheem47', dsn=dsn)
cursor = connection.cursor()

@app.route('/home')
def home():
    return render_template('home.html')

# Redirect the root URL ('/') to /home
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer_form():
    if request.method == 'POST':
            # Collect form data with defaults for optional fields
            data = {
                # Personal Information
                'last_name': request.form['last_name'],
                'first_name': request.form['first_name'],
                'dob': datetime.strptime(request.form['dob'], '%Y-%m-%d'),
                'street_address': request.form['street_address'],
                'city': request.form['city'],
                'state': request.form['state'],
                'zip': request.form['zip'],
                'home_phone': request.form['home_phone'],
                'work_phone': request.form.get('work_phone', None),
                'email': request.form['email'],
                'convicted_felony': request.form['convicted_felony'],
                'felony_explanation': request.form.get('felony_explanation', None),

                # Emergency Contact
                'emergency_last_name': request.form['emergency_last_name'],
                'emergency_first_name': request.form['emergency_first_name'],
                'emergency_relationship': request.form['emergency_relationship'],
                'emergency_phone': request.form['emergency_phone'],

                # Reference 1
                'reference1_last_name': request.form['reference1_last_name'],
                'reference1_first_name': request.form['reference1_first_name'],
                'reference1_relationship': request.form['reference1_relationship'],
                'reference1_phone': request.form['reference1_phone'],
                'reference1_address': request.form['reference1_address'],
                'reference1_city': request.form['reference1_city'],
                'reference1_state': request.form['reference1_state'],
                'reference1_zip': request.form['reference1_zip'],

                # Reference 2
                'reference2_last_name': request.form['reference2_last_name'],
                'reference2_first_name': request.form['reference2_first_name'],
                'reference2_relationship': request.form['reference2_relationship'],
                'reference2_phone': request.form['reference2_phone'],
                'reference2_address': request.form['reference2_address'],
                'reference2_city': request.form['reference2_city'],
                'reference2_state': request.form['reference2_state'],
                'reference2_zip': request.form['reference2_zip'],

                # Employment
                'employer_name': request.form.get('employer_name', None),
                'employer_address': request.form.get('employer_address', None),
                'position': request.form.get('position', None),
                'employment_dates': request.form.get('employment_dates', None),

                # Prior Volunteer Service
                'prior_mvch_volunteer': request.form['prior_mvch_volunteer'],
                'mvch_volunteer_details': request.form.get('mvch_volunteer_details', None),
                'prior_experience': request.form['prior_experience'],
                'experience_details': request.form.get('experience_details', None),

                # Interests & Preferences
                'reason_to_volunteer': request.form['reason_to_volunteer'],
                'hobbies': request.form['hobbies'],
                'languages': request.form['languages'],
                'envision_volunteer_role': request.form['envision_volunteer_role'],

                # Availability
                'monday_morning': request.form.get('monday_morning', '0'),
                'monday_afternoon': request.form.get('monday_afternoon', '0'),
                'monday_evening': request.form.get('monday_evening', '0'),
                'tuesday_morning': request.form.get('tuesday_morning', '0'),
                'tuesday_afternoon': request.form.get('tuesday_afternoon', '0'),
                'tuesday_evening': request.form.get('tuesday_evening', '0'),
                'wednesday_morning': request.form.get('wednesday_morning', '0'),
                'wednesday_afternoon': request.form.get('wednesday_afternoon', '0'),
                'wednesday_evening': request.form.get('wednesday_evening', '0'),
                'thursday_morning': request.form.get('thursday_morning', '0'),
                'thursday_afternoon': request.form.get('thursday_afternoon', '0'),
                'thursday_evening': request.form.get('thursday_evening', '0'),
                'friday_morning': request.form.get('friday_morning', '0'),
                'friday_afternoon': request.form.get('friday_afternoon', '0'),
                'friday_evening': request.form.get('friday_evening', '0'),
                'saturday_morning': request.form.get('saturday_morning', '0'),
                'saturday_afternoon': request.form.get('saturday_afternoon', '0'),
                'saturday_evening': request.form.get('saturday_evening', '0'),
                'sunday_morning': request.form.get('sunday_morning', '0'),
                'sunday_afternoon': request.form.get('sunday_afternoon', '0'),
                'sunday_evening': request.form.get('sunday_evening', '0'),

                # Signature
                'signature': request.form['signature'],
                'signature_date': datetime.strptime(request.form['signature_date'], '%Y-%m-%d')
            }

            # SQL Insert Query
            query = """
            INSERT INTO volunteers (
                last_name, first_name, date_of_birth, street_address, city, state, zip,
                home_phone, work_phone, email, convicted_felony, felony_explanation,
                emergency_last_name, emergency_first_name, emergency_relationship, emergency_phone,
                reference1_last_name, reference1_first_name, reference1_relationship, reference1_phone,
                reference1_address, reference1_city, reference1_state, reference1_zip,
                reference2_last_name, reference2_first_name, reference2_relationship, reference2_phone,
                reference2_address, reference2_city, reference2_state, reference2_zip,
                employer_name, employer_address, position, employment_dates,
                prior_mvch_volunteer, mvch_volunteer_details, prior_experience, experience_details,
                reason_to_volunteer, hobbies, languages, envision_volunteer_role,
                monday_morning, monday_afternoon, monday_evening,
                tuesday_morning, tuesday_afternoon, tuesday_evening,
                wednesday_morning, wednesday_afternoon, wednesday_evening,
                thursday_morning, thursday_afternoon, thursday_evening,
                friday_morning, friday_afternoon, friday_evening,
                saturday_morning, saturday_afternoon, saturday_evening,
                sunday_morning, sunday_afternoon, sunday_evening,
                signature, signature_date
            ) VALUES (
                :last_name, :first_name, :dob, :street_address, :city, :state, :zip,
                :home_phone, :work_phone, :email, :convicted_felony, :felony_explanation,
                :emergency_last_name, :emergency_first_name, :emergency_relationship, :emergency_phone,
                :reference1_last_name, :reference1_first_name, :reference1_relationship, :reference1_phone,
                :reference1_address, :reference1_city, :reference1_state, :reference1_zip,
                :reference2_last_name, :reference2_first_name, :reference2_relationship, :reference2_phone,
                :reference2_address, :reference2_city, :reference2_state, :reference2_zip,
                :employer_name, :employer_address, :position, :employment_dates,
                :prior_mvch_volunteer, :mvch_volunteer_details, :prior_experience, :experience_details,
                :reason_to_volunteer, :hobbies, :languages, :envision_volunteer_role,
                :monday_morning, :monday_afternoon, :monday_evening,
                :tuesday_morning, :tuesday_afternoon, :tuesday_evening,
                :wednesday_morning, :wednesday_afternoon, :wednesday_evening,
                :thursday_morning, :thursday_afternoon, :thursday_evening,
                :friday_morning, :friday_afternoon, :friday_evening,
                :saturday_morning, :saturday_afternoon, :saturday_evening,
                :sunday_morning, :sunday_afternoon, :sunday_evening,
                :signature, :signature_date
            )
            """
            # Execute the query and commit the transaction
            cursor.execute(query, data)
            connection.commit()
            return redirect(url_for('thankyou'))
            
    return render_template('index.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)