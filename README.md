```markdown
# Selenium POM Example

This project demonstrates a Selenium-based test automation framework using the Page Object Model (POM) design pattern. It includes tests for a sample website, such as verifying page titles and navigation.

## Project Structure

```
.
├── conftest.py          # Pytest configuration and fixtures
├── custom.css           # Custom CSS for HTML reports
├── drivers/             # WebDriver setup and utilities
├── pages/               # Page Object Model classes
├── reports/             # Test reports and screenshots
├── tests/               # Test cases
├── requirements.txt     # Python dependencies
├── pytest.ini           # Pytest configuration file
└── .gitignore           # Ignored files and directories
```

## Prerequisites

1. **Python**: Ensure Python 3.10 or higher is installed.
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: This project uses `webdriver-manager` to automatically manage ChromeDriver.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/selenium-pom-example.git
   cd selenium-pom-example
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

1. Run all tests:
   ```bash
   pytest
   ```

2. Generate an HTML report:
   ```bash
   pytest --html=reports/report.html --self-contained-html --css=custom.css
   ```

3. Run a specific test:
   ```bash
   pytest tests/test_home_page.py
   ```

## Features

- **Page Object Model (POM)**: Encapsulates page-specific logic in classes under the `pages/` directory.
- **HTML Reports**: Generates detailed test reports with screenshots for failed tests.
- **WebDriver Management**: Automatically downloads and configures ChromeDriver using `webdriver-manager`.

## Project Configuration

- **`conftest.py`**: Contains the `driver` fixture for managing the WebDriver lifecycle and hooks for generating reports.
- **`pytest.ini`**: Configures pytest options.
- **`custom.css`**: Customizes the appearance of HTML reports.

## Troubleshooting

1. **ChromeDriver Issues**: Ensure that the version of Google Chrome matches the version of ChromeDriver managed by `webdriver-manager`.
2. **Environment Variables**: If required, create a `.env` file to store sensitive data like credentials.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.