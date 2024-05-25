# Projektron POM Selenium Example

This repository contains a fully functional example of using the Page Object Model (POM) design pattern with Selenium for automating tests on Projektron. The aim is to demonstrate how to structure and implement a robust test automation framework in Python.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Introduction
The Page Object Model (POM) is a design pattern in Selenium that creates an object repository for web elements. It enhances test maintenance and reduces code duplication. This example illustrates how to set up and use POM in a Selenium project for Projektron.

## Features
- Demonstrates the Page Object Model design pattern.
- Uses Selenium WebDriver for browser automation.
- Includes sample test cases for Projektron.
- Easy to extend and maintain.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- `pip` (Python package installer)
- A web browser (Chrome, Firefox, etc.)
- ChromeDriver or GeckoDriver (for Firefox)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/jonathanAnguise/projektron-automator
    cd projektron-pom-selenium-example
    touch .env
    echo "PASSWORD=Your_password" >> .env
    echo "USERNAME=Your_username" >> .env
    echo "URL=www.example.com" >> .env
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Input a day (arguments are optional):
    ```sh
    python main.py hours=4 minutes=36 title=great_title reference=my_ref task_description="RACK maintenance"
    ```
    If you don't provide arguments, the following default values will be used:
    ```python
    "hours": 9
    "minutes": 0
    "title": "TA"
    "reference": "TA"
    "task_description": "RACK maintenance"
    ```

## Project Structure
```plaintext
projektron-pom-selenium-example
├── input.bat
├── main.py
├── pages
│   ├── base_page.py
│   ├── login_page.py
│   └── main_page.py
├── README.md
├── requirements.txt
├── test_secret_manager.py
├── test_time_parser.py
└── utils
    ├── locators.py
    ├── secret_manager.py
    └── time_parser.py
```
