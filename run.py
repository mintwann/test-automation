import pytest

if __name__ == "__main__":
    pytest.main([
        "tests/",             # đường dẫn tới thư mục chứa test
        "-v",                 # hiển thị chi tiết
        "--tb=short",         # traceback ngắn gọn
        "--html=reports/report.html",     # file báo cáo
        "--self-contained-html"           # nhúng CSS/JS vào file HTML (không phụ thuộc file ngoài)
    ])
    