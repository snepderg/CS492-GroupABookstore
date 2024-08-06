# CS492 - Group A Capstone Project
## Bookstore Management Application: PageTurners


## Installation Instructions

NOTE: This project utilizes a local MySQL server. If you do not have MySQL installed on your machine, you will need to install it before running the application. You can download MySQL from the official website: https://dev.mysql.com/downloads/installer/

## Installing Python and pipenv
1. Download and install **Python 3.12** from the official website: https://www.python.org/downloads/
2. Open a terminal and run one of the following commands to install pipenv:
    - `pip install pipenv` (for Windows)
    - `pip3 install pipenv`(for MacOS)
    (Note: Linux users can use either command)
3. Navigate to the project directory in your terminal, and run the following command to install the project dependencies:
    - `pipenv install`


## Setting up the MySQL Database
1. Download and install MySQL from the official website.
- For Windows, download version 8.0.39: https://dev.mysql.com/downloads/installer/
- For MacOS (Sonoma), download the archive for 8.0.33: https://downloads.mysql.com/archives/community/


- Make sure to install both MySQL Server and MySQL Workbench.
- Write down the root password you set during installation. This will be needed to connect to the MySQL server.
- Do *not* use port 5001 for the MySQL server. This port is used by the Flask application.
2. Open MySQL Workbench and create a new connection to your local MySQL server.
3. Click File > Open SQL Script, and select the `page_turners.sql` file from the project directory.
4. Run the script (Click on the lightning bolt next to the save icon) to create the database and tables.


## Setting up the Application
1. Open a terminal and navigate to the project directory.
2. Run the following command to activate the virtual environment:
    - `pipenv shell`
3. Run the following command to start the development server:
    - `python server.py`
4. Open a web browser and navigate to `http://localhost:5001/` to access the application.


## Testing the Application's Functionality
1. On the homepage, enter the following details to register an account:
    - First Name
    - Last Name
    - Email
    - Password
    - Confirm Password
2. Click the "Register" button to create the account.
- Note that the dashboard will show the account's name at the top of the page.
- At this time, you can check the MySQL database to see the account created.
3. Click the "Logout" button to log out of the account.
4. Enter your Email and Password to log back in.


## Terminating the Application
1. Press `Ctrl + C` in the terminal to stop the Python development server.
2. Run the following command to deactivate the virtual environment:
    - `exit`
3. Close out of the terminal, and close MySQL Workbench.
- Note: The MySQL server will continue running in the background.


# Notes
- Since the application uses a local MySQL server, the schema and tables will save to your local machine independent from the project files.
