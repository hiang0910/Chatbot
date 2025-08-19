# Chatbot

# Flask Chatbot (Demo cho CV)

Chatbot Q&A cơ bản bằng **Python Flask**, có giao diện web tối giản.

## ✨ Tính năng
- Giao diện chat đơn giản (HTML/CSS/JS).
- API `/chat` nhận message và trả lời theo kịch bản.
- Dễ mở rộng: thêm rule/intent trong `responses.py`.

## 🧱 Cấu trúc
```
chatbot-project/
├─ app.py
├─ responses.py
├─ templates/
│  └─ index.html
└─ static/
   └─ style.css
```

## 🚀 Chạy dự án (Windows / macOS / Linux)
```bash
# 1) Tạo & kích hoạt môi trường ảo
python -m venv .venv         # (hoặc: python3 -m venv .venv)
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 2) Cài thư viện
pip install -r requirements.txt

# 3) Chạy server
python app.py                 # (hoặc: python3 app.py)
```

Mở trình duyệt: http://127.0.0.1:5000

## 🧩 Tùy biến nhanh
- Sửa logic trả lời trong `responses.py`.
- Sửa giao diện trong `templates/index.html` và `static/style.css`.

## 📦 Tech stack
- Python + Flask
- HTML/CSS/JS (frontend tối giản)

## 🗺 Hướng phát triển
- Thêm NLP (regex, từ khóa, thư viện NLP).
- Lưu lịch sử chat vào file/SQLite.
- Viết test (pytest) cho `get_response`.
```
