# MindScape
http://mayank29.pythonanywhere.com/

![Screenshot 2024-01-21 at 11 29 26 PM](https://github.com/mayank-bharwal/MentalHealthWebsite/assets/119955673/f3f6ab7c-53ff-4767-b439-bc7ffb1e8d39)
![Screenshot 2024-01-21 at 11 28 15 PM](https://github.com/mayank-bharwal/MentalHealthWebsite/assets/119955673/11701e23-a905-47cf-8cb0-9ed320f87de1)
![Screenshot 2024-01-21 at 11 28 31 PM](https://github.com/mayank-bharwal/MentalHealthWebsite/assets/119955673/bea499c2-82e3-475e-987b-55e5a6dcfadb)

This is a simple web application developed using Flask, SQLAlchemy, and Werkzeug for managing journal entries and conducting tests. Users can register, log in, create journal entries, take tests, and view their dashboard.

## Features

- User registration and login
- Create and view journal entries
- Take tests(Kessler Psychological Test (k10) and view test results
- Secure password storage using Werkzeug
- SQLite database integration using SQLAlchemy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mayank-bharwal/mindscape.git
   cd mindscape
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Run the application:

   ```bash
   python app.py
   ```

The app should now be running locally at http://localhost:5000.

## Usage

1. Register a new user account.
2. Log in with your credentials.
3. Create journal entries on the 'Journal' page.
4. Take tests on the 'Test' page.
5. View your dashboard to see your journal entries and test results.

## Contribute

If you would like to contribute to this project, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE - see the LICENSE file for details.
```
