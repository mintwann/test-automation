import pytest
import sys
import os
from utils.file_utils import parse_arguments, get_report_path, ensure_dir_exists

def main():
    """Run tests with customizable report name and directory structure"""
    # Parse command line arguments
    args = parse_arguments()
    
    # Ensure reports directory exists
    ensure_dir_exists("reports")
    
    # Get report path with automatic timestamping if no custom name provided
    report_path = get_report_path(args.report_name)
    
    # Build pytest arguments
    pytest_args = [
        "tests/",             # path to testcase files
        "-v",                 # display verbose output
        "--tb=short",         # short traceback
        f"--html={report_path}",  # dynamic report file path
        "--self-contained-html"   # include CSS and JS in the report
    ]
    
    print(f"Running tests with report output to: {report_path}")
    
    # Run pytest with the arguments
    return pytest.main(pytest_args)

if __name__ == "__main__":
    # Exit with the pytest exit code
    sys.exit(main())
