# FP Central (MBID) UAT Automation

This project contains UAT (User Acceptance Testing) automation scripts for FP Central.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Setup

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
cd 04_Automation
pip install -r requirements.txt
```

This will install:
- `playwright` - For browser automation
- `pytest` - For test execution

### 4. Install Playwright Browsers

After installing dependencies, run:
```bash
playwright install
```

## Running the UAT Tests

### Run the main test script

```bash
cd .\04_Automation\
python run_uat.py
```

This will execute the UAT test cases defined in the automation suite.

### Run specific tests with pytest

```bash
pytest tests/
```

### Run tests with verbose output

```bash
pytest tests/ -v
```

## Project Structure

```
UAT Automation/
├── 00_README/               # Documentation
├── 01_Test_Plan/            # Test planning documents
├── 04_Automation/           # Automation scripts
│   ├── run_uat.py           # Main test runner
│   ├── tests/               # Test case files
│   └── requirements.txt      # Python dependencies
├── 05_Execution/            # Execution reports
├── 06_Defects/              # Defect logs
└── Policy Test Data.csv/xlsx # Test data
```

## Troubleshooting

- **Module not found errors**: Ensure you've installed all dependencies with `pip install -r requirements.txt`
- **Playwright browser issues**: Run `playwright install` to install browser binaries
- **Permission denied**: On macOS/Linux, ensure the script has execute permissions: `chmod +x run_uat.py`

## Support

For issues or questions, refer to the documentation in the `00_README` directory.
