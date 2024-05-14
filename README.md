# Automated Testing Project for Flip.ro Website
Welcome to the documentation for the automated testing project designed for the Flip.ro website. This project leverages Selenium and the unittest framework to implement a robust suite of tests, ensuring the functionality and reliability of Flip.ro's webshop.

## Table of Contents
1. Introduction 
2. Getting-Started
3. Usage
4. Reports
5. Conclusion

## Introduction
   This project aims to implement automated tests for the Flip.ro website using Selenium and unittest. The primary objectives include simulating user interactions and navigating through the webshop's various functionalities.

Library Versions:

 >selenium 4.17.2

 >webdriver-manager 4.0.1

 >html-testRunner 1.2.1

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/CSMN132/Proiect-Final.git
    ```

2. **Navigate to the project directory:**
    
    ```bash
    cd Proiect-Final
    ```

3. **Create venv:**
    
    ```bash
    python -m venv venv
    ```
    
4. **Install Dependencies:**

    ```bash
    pip install -r requirmments.txt
    ```

5. **Activate the Virtual Environment:**
    
    ```Terminal
     venv/Scripts/Activate  
    ```
    
6. **Run the Test Suite with html reports:**

    ```bash
    python -m unittest Test_Suite.py
    ```

# Usage

Execute the automated tests to verify the Flip.ro website's login and search functionalities.

# Reports

The project includes HTML reports generated after each test suite run, offering detailed insights into test results. The reports provide a clear overview of the tested functionalities, making it easy to identify any issues that may arise during testing.

- Below, you can see the report generated on April 24, 2024, for the sogin and search functionality:

![image](https://github.com/CSMN132/Proiect-Final/assets/139993897/2563bf50-631d-4ad7-8098-d30b9ef44c07)

2 of 4 test are passed.

# Conclusions

In conclusion, the automated testing project for the Flip.ro website has been successfully implemented using Selenium and the unittest framework. The Page Object Model (POM) design pattern was employed to enhance modularity and maintainability, allowing for efficient management of locators, pages, and test scripts.

The project covers critical functionalities such as login and search, with a focus on various test scenarios to ensure robustness. The tests are organized into a structured project layout, including locators, pages, tests, reports, screenshots, and a virtual environment. The project also provides clear documentation on how to clone the repository, install dependencies, activate the virtual environment, and run the test suite

Automated tests have been designed to cover a range of scenarios, including positive and negative cases for the login functionality, as well as comprehensive testing of the search functionality. Screenshots are captured for failed test cases, providing visual aids for debugging and issue identification.

In the future, the project can be expanded to cover additional functionalities and scenarios, ensuring continuous testing and validation of the Flip.ro webshop. Regular maintenance and updates to locators and test scripts will be crucial as the website evolves.
