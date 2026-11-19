"""
Test nhanh: xem trang dauthau.info / dauthau.asia có render bằng JS
(cần Selenium) hay là HTML tĩnh (chỉ cần requests là đủ).

Cài đặt trước khi chạy:
    pip install requests beautifulsoup4 --break-system-packages
"""

import requests
from bs4 import BeautifulSoup

# Đổi URL này thành 1 trang danh sách gói thầu thật, ví dụ trang TBMT
URL = "https://dauthau.asia/tinh-thanh/year-2026/"  # <-- sửa URL thật ở đây

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def test_static_fetch(url: str):
    print(f"--- Đang thử fetch tĩnh: {url} ---\n")
    resp = requests.get(url, headers=headers, timeout=15)
    print(f"Status code: {resp.status_code}")
    print(f"Content-Length: {len(resp.text)} ký tự\n")

    soup = BeautifulSoup(resp.text, "html.parser")

    # In ra 1500 ký tự đầu để mắt thường xem có nội dung thật không
    print("--- 1500 ký tự đầu của trang ---")
    print(resp.text[:1500])
    print("\n--- Hết đoạn xem trước ---\n")

    # Heuristic đơn giản: đếm số bảng / danh sách item
    rows = soup.find_all("tr")
    items = soup.find_all(class_=lambda c: c and ("item" in c.lower() or "row" in c.lower()))

    print(f"Số thẻ <tr> tìm thấy: {len(rows)}")
    print(f"Số thẻ có class chứa 'item'/'row': {len(items)}")

    if len(rows) == 0 and len(items) == 0:
        print(
            "\n⚠️  KHẢ NĂNG CAO: trang này render bằng JavaScript.\n"
            "    requests chỉ lấy được HTML gốc (chưa chạy JS), nên nếu\n"
            "    dữ liệu bảng không xuất hiện ở đây, bạn cần Selenium\n"
            "    hoặc Playwright để lấy nội dung sau khi JS chạy xong."
        )
    else:
        print(
            "\n✅ Có vẻ trang trả về HTML tĩnh có chứa dữ liệu — "
            "requests + BeautifulSoup có thể đủ dùng, không cần Selenium."
        )


if __name__ == "__main__":
    test_static_fetch(URL)