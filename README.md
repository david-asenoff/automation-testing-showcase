
# 🚀 Automation Testing Showcase

This repository contains a series of automation scripts and unit tests for various domains, including Facebook automation, API interactions with JSONPlaceholder and SWAPI, math operations, and more. The project showcases the use of Selenium for browser automation and `unittest` for testing in Python.

## 📋 Table of Contents

- [🛠 Installation](#-installation)
- [📂 Folder Structure](#-folder-structure)
- [✅ How to Run the Tests](#-how-to-run-the-tests)
- [💻 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## 🛠 Installation

To get started with this project, you'll need to have Python 3.7+ installed. You will also need to install the required Python packages.

### Prerequisites

1. **Python 3.7+**: Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).
2. **pip**: Make sure you have `pip` installed to manage Python packages.

### Installing Required Packages

Install the necessary packages using pip:

```bash
pip install selenium
pip install requests
pip install pytest
pip install webdriver_manager
pip install beautifulsoup4
pip install pyodbc
```

## 📂 Folder Structure

The project is organized as follows:

```
/AutomationAndTestingShowcase/
│
├── /tests/
│   ├── /facebook/
│   │   └── test_facebook.py
│   ├── /jsonplaceholder/
│   │   ├── test_jsonplaceholder_add_and_get_cookies.py
│   │   ├── test_jsonplaceholder_get_request.py
│   │   └── test_jsonplaceholder_post_request_with_header.py
│   ├── /math_operations/
│   │   └── test_math_operations.py
│   ├── /other_tests/
│   │   ├── test_github_get_csrf_token.py
│   │   └── test_login.py
│   ├── /oxylabs/
│   │   ├── test_oxylabs_mini_scraper.py
│   │   ├── test_oxylabs_print_source.py
│   │   └── test_oxylabs_status_code_and_scroll_and_screenshot.py
│   ├── /swapi/
│   │   ├── test_swapi_click_scroll_check_title_screenshot.py
│   │   ├── test_swapi_find_planet_by_name.py
│   │   ├── test_swapi_get_request.py
│   │   ├── test_swapi_print_text_sibling_elements.py
│   │   ├── test_swapi_search_and_print_results.py
│   │   └── test_swapi_search_on_all_pages_and_find_title.py
│   ├── /sql/
│   │   ├── test_connection.py
│   │   ├── test_select_check_results.py
│   │   ├── test_sql_select.py
│   │   ├── test_update_price.py
│   │   ├── test_delete.py
│   │   └── test_create.py
│   └── /unittest/
│       └── test_swapi.py
│
└── requirements.txt
```

### Key Directories and Files

- **`/tests/`**: Contains various test files categorized into subfolders like `facebook`, `jsonplaceholder`, `swapi`, `sql`, etc.
- **`requirements.txt`**: Lists all the Python dependencies required to run the project.
- **`README.md`**: This document, which provides an overview of the project.

## ✅ How to Run the Tests

Navigate to the project root directory and use the following commands to run the tests:

### Running Individual Tests

Use the following commands to run specific tests:

```bash
python -m unittest tests.facebook.test_facebook
python -m unittest tests.math_operations.test_math_operations

python tests/jsonplaceholder/test_jsonplaceholder_add_and_get_cookies.py
python tests/jsonplaceholder/test_jsonplaceholder_get_request.py
python tests/jsonplaceholder/test_jsonplaceholder_post_request_with_header.py

python tests/other_tests/test_github_get_csrf_token.py
python tests/other_tests/test_login.py

python tests/oxylabs/test_oxylabs_mini_scraper.py
python tests/oxylabs/test_oxylabs_print_source.py
python tests/oxylabs/test_oxylabs_status_code_and_scroll_and_screenshot.py

pytest -v tests/pytest/test_swapi_single.py
pytest -v tests/pytest/tests_swapi_multiple.py

python tests/swapi/test_swapi_click_scroll_check_title_screenshot.py
python tests/swapi/test_swapi_find_planet_by_name.py
python tests/swapi/test_swapi_get_request.py
python tests/swapi/test_swapi_print_text_sibling_elements.py
python tests/swapi/test_swapi_search_and_print_results.py
python tests/swapi/test_swapi_search_on_all_pages_and_find_title.py

python -m unittest tests.unittest.test_swapi

python tests/sql/test_connection.py
python tests/sql/test_select_check_results.py
python tests/sql/test_sql_select.py
python tests/sql/test_update_price.py
python tests/sql/test_delete.py
python tests/sql/test_create.py
```

## 💻 Usage

Scripts in the `tests` directory can be run independently to test various functionalities like interacting with APIs, web scraping, performing database operations, and more.

## 🤝 Contributing

If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
