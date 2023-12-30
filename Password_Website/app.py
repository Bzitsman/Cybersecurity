from flask import Flask, render_template, request
import string
import random
import math

app = Flask(__name__)

# Code for generating a strong password
def generate_strong_password(length=12):
    """
    Generate a strong password with a given length.

    Parameters:
    - length (int): Length of the password (default is 12)

    Returns:
    - str: Strong password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for _ in range(length))
    return strong_password

# Code for providing feedback about a password's strength
def password_strength_feedback(password):
    """
    Provide feedback about a password's strength.

    Parameters:
    - password (str): Password to evaluate

    Returns:
    - str: Feedback message
    """
    # Insert your code here for providing feedback

    if len(password) < 8:
        return "Weak: Password is too short."
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "Strong: Password is a good mix of letters and numbers."
    else:
        return "Moderate: Consider adding a mix of letters, numbers, and special characters."

# Code for calculating time to crack a password
def time_to_crack_password(password, attempts_per_second=1000000000):
    """
    Calculate the time it would take to crack a password using brute force.

    Parameters:
    - password (str): Password to evaluate
    - attempts_per_second (int): Number of password attempts per second (default is 1 billion)

    Returns:
    - str: Time to crack in years, days, hours, minutes, and seconds
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    possible_combinations = len(characters) ** len(password)
    seconds_to_crack = possible_combinations / attempts_per_second
    time_in_years = seconds_to_crack / (60 * 60 * 24 * 365)
    
    years = int(time_in_years)
    days = int((time_in_years - years) * 365)
    hours = int(((time_in_years - years) * 365 - days) * 24)
    minutes = int((((time_in_years - years) * 365 - days) * 24 - hours) * 60)
    seconds = int((((time_in_years - years) * 365 - days) * 24 - hours) * 60 - minutes) * 60
    
    return f"{years} years, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"


    # Insert your code here for providing feedback
    pass



# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form.get('length', 12))
    print(f"Generating password of length {length}")
    strong_password = generate_strong_password(length)
    print(f"Generated password: {strong_password}")
    return render_template('index.html', strong_password=strong_password)

@app.route('/check_strength', methods=['POST'])
def check_strength():
    user_password = request.form.get('user_password')
    feedback = password_strength_feedback(user_password)
    return render_template('index.html', feedback=feedback)

@app.route('/estimate_crack_time', methods=['POST'])
def estimate_crack_time():
    user_password = request.form.get('user_password')
    crack_time = time_to_crack_password(user_password)
    print(f"Estimated time to crack: {crack_time}")
    return render_template('index.html', crack_time=crack_time)

if __name__ == '__main__':
    app.run(debug=True)