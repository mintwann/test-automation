# Test Automation Framework

A Selenium-based test automation framework for web application testing, using Python and Page Object Model design pattern.

## Project Structure

```
test/
├── config/
│   └── settings.py         # Configuration settings
├── pages/
│   └── login_page.py       # Page object for login functionality
├── screenshots/            # Test failure screenshots
│   └── YYYY-MM-DD/         # Organized by date
├── tests/
│   └── test_login_success.py  # Test cases
├── utils/
│   ├── browser_setup.py    # Browser configuration
│   ├── file_utils.py       # File handling utilities
│   └── helpers.py          # Helper functions
├── .env                    # Environment variables (not committed to Git)
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Chrome browser
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/test-automation.git
cd test-automation
```

2. **Create and activate virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the project root with the following variables:

```
EMAIL=your-test-email@example.com
PASSWORD=your-test-password
URL=https://your-application-url.com
WAIT_TIME=10
```

## Git Repository Setup

1. **Initialize Git repository** (if not already done)

```bash
git init
```

2. **Create .gitignore file**

Create a `.gitignore` file with the following content:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
env/

# Environment variables
.env

# Screenshots
screenshots/

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# Logs
*.log
```

3. **Add files and commit**

```bash
git add .
git commit -m "Initial commit"
```

4. **Add remote repository** (if needed)

```bash
git remote add origin https://github.com/your-username/test-automation.git
git branch -M main
git push -u origin main
```

## Running Tests

To run all tests:

```bash
pytest
```

To run a specific test:

```bash
pytest tests/test_login_success.py -v
```

For detailed output with logging:

```bash
pytest tests/test_login_success.py -vvs
```

## Adding New Tests

1. Create a new test file in the `tests` directory
2. Create page objects in the `pages` directory
3. Follow the Page Object Model pattern
4. Use utility functions from the `utils` directory

## Best Practices

- Use explicit waits instead of `time.sleep()`
- Organize tests by functionality
- Create dedicated page objects for different pages
- Use helper functions for common operations
- Take screenshots on test failures
- Use meaningful log messages

## Troubleshooting

- Check the screenshots directory for test failure evidence
- Use verbose output to see detailed test execution
- Verify environment variables in the `.env` file
- Ensure Chrome browser and WebDriver are compatible versions