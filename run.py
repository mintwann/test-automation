import pytest

if __name__ == "__main__":
    pytest.main([
        "tests/",             # path to testcase files
        "-v",                 # display verbose output
        "--tb=short",         # short traceback
        "--html=reports/report.html",     # report file path
        "--self-contained-html"           # include CSS and JS in the report
    ])
    