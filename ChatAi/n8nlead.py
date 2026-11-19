"""
Gửi bộ lead test tới n8n webhook cho AI Lead Scoring Pipeline.

Cài đặt trước khi chạy:
    pip install requests --break-system-packages

Cách dùng:
    1. Sửa URL bên dưới thành đúng Production URL của Webhook trong n8n
    2. Chạy: python send_leads.py
"""

import json
import requests

# ĐỔI URL NÀY thành Production URL thật từ node Webhook trong n8n
# Ví dụ: http://localhost:5678/webhook/lead-scoring-in
URL = "http://localhost:5678/webhook-test/lead-scoring-in"

# Đọc file dữ liệu test
with open("leads.json", "r", encoding="utf-8") as f:
    data = json.load(f)

leads = data["leads"]

print(f"Chuẩn bị gửi {len(leads)} lead tới {URL}\n")

# Gửi cả mảng cùng lúc (giống cách bạn từng làm với Split Out ở workflow lead pipeline)
payload = {"leads": leads}

response = requests.post(URL, json=payload)

print(f"Status code: {response.status_code}")
print(f"Response: {response.text[:500]}")

if response.status_code == 200:
    print(f"\n✅ Đã gửi thành công {len(leads)} lead.")
else:
    print(f"\n⚠️  Có lỗi xảy ra — kiểm tra lại URL và trạng thái Published của workflow.")