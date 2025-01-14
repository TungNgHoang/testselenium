
# Web Application for Book Management

This project provides a simple web application for managing books. It includes functionalities for login, viewing book lists, searching for books, and adding new books. The application is designed with HTML, CSS (via Bootstrap), and JavaScript for client-side interactivity. It also includes automated tests for login, search, and add book functionalities using Selenium.

## Features

- **Login Page:** Allows users to log in with a predefined username and password.
- **Book List Page:** Displays a list of books with the ability to search books by name.
- **Add Book Page:** Allows users to add new books with information like book name, author, and quantity.
- **Validation:** Form validation for required fields, valid email format, and minimum password length.
- **Alerts:** Alerts displayed for successful or failed operations (login, book addition, etc.).
- **Dynamic Content:** Books are stored in `localStorage` and can be dynamically added, searched, or displayed.

## Project Structure

- **index.html:** The main page for login.
- **2.html:** Displays the list of books.
- **3.html:** The page for adding new books.
- **styles.css:** Contains custom styles.
- **script.js:** Contains JavaScript logic for form validation, searching, and adding books.
- **testselenium:** Folder containing Selenium tests for login, book searching, and book addition.

## Setup

1. Clone this repository to your local machine.
2. Open `index.html` in a browser to start the application.
3. Use the built-in features for logging in, viewing books, and adding books.

## Technologies Used

- **HTML** for structure
- **CSS (Bootstrap)** for styling
- **JavaScript** for interactivity and form validation
- **Selenium** for automated testing

## Automated Tests

This project includes several automated tests written in Python using Selenium. These tests verify the login, search, and add book functionalities.

### Test Scenarios

#### Login Tests

- **Test Login:** Attempts to log in with both invalid and valid credentials and checks for corresponding alerts.
- **Test Login Attempts:** Simulates multiple failed login attempts.
- **Test Invalid Account:** Tests login with a non-existing account.

#### Search Tests

- **Test Search:** Verifies searching for a book by name.
- **Test Empty Search:** Checks that an appropriate message is displayed when no books match the search.
- **Test Special Character Search:** Verifies searching with special characters.

#### Add Book Tests

- **Test Add Book:** Verifies adding a new book to the list.
- **Test Duplicate Book:** Tests for adding a book with the same name and checks for the appropriate alert.
- **Test Invalid Quantity:** Tests adding a book with an invalid quantity and checks for validation.

### Running the Tests

1. Install Selenium and required dependencies:
   ```bash
   pip install selenium
   ```
2. Run the tests:
   ```bash
   pytest testselenium/test_login.py
   pytest testselenium/test_search.py
   pytest testselenium/test_add.py
   ```

## Usage

- **Login:** Enter `admin@example.com` as the email and `password123` as the password to log in successfully.
- **Add Book:** After logging in, navigate to the "Add Book" page and enter valid book details to add a book to the list.
- **Search Book:** On the Book List page, use the search bar to search for books by name.

