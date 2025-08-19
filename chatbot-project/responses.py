import random
import re
from rapidfuzz import process, fuzz

RESPONSES = {
    # Chào hỏi
  
    "chào,hello,hey": [
        "Chào bạn 👋! ",
        "Xin chào! Bạn có cần hỗ trợ thông tin về trường không?",
        "Hello! Rất vui được gặp bạn tại chatbot đại học 🤖."
    ],
    "cảm ơn,thank": [
        "Không có gì đâu 😊.",
        "Rất vui được giúp bạn!",
        "Luôn sẵn sàng hỗ trợ bạn 👍."
    ],
    "tạm biệt,bye": [
        "Chào tạm biệt 👋, chúc bạn học tập tốt.",
        "Hẹn gặp lại bạn ở thư viện 📚.",
        "Bye bye, nhớ giữ sức khỏe nhé."
    ],

    # Thông tin trường
    "trường": [
        "Trường mình có nhiều khoa: CNTT, Kinh tế, Ngôn ngữ, Cơ khí…",
        "Bạn muốn hỏi về cơ sở chính hay cơ sở 2?",
        "Trường có khuôn viên rộng với thư viện, căng tin và khu thể thao."
    ],
    "khoa": [
        "Các khoa tiêu biểu: Công nghệ Thông tin, Quản trị Kinh doanh, Điện tử Viễn thông.",
        "Khoa CNTT đào tạo lập trình, AI, dữ liệu, an ninh mạng."
    ],
    "lịch học": [
        "Lịch học được đăng trên website đào tạo hoặc LMS của trường.",
        "Bạn có thể kiểm tra lịch học trên cổng thông tin sinh viên."
    ],
    "thi": [
        "Lịch thi thường được công bố trước 2 tuần.",
        "Bạn nên theo dõi thông báo trên phòng đào tạo."
    ],
    "điểm": [
        "Điểm sẽ được cập nhật trên hệ thống sau khi thi 1-2 tuần.",
        "Nếu chưa thấy điểm, bạn có thể hỏi giảng viên bộ môn."
    ],
    "học phí": [
        "Học phí tùy theo số tín chỉ bạn đăng ký.",
        "Bạn có thể đóng học phí qua ngân hàng hoặc ví điện tử liên kết."
    ],
    "thư viện": [
        "Thư viện mở cửa từ 7h30 đến 20h.",
        "Bạn cần thẻ sinh viên để mượn sách."
    ],
    "mượn sách": [
        "Bạn có thể mượn tối đa 5 quyển/lần.",
        "Thời hạn mượn sách là 14 ngày, có thể gia hạn."
    ],
    "câu lạc bộ": [
        "Trường có nhiều CLB: âm nhạc, bóng đá, khởi nghiệp, tiếng Anh.",
        "Bạn muốn tham gia CLB nào? CNTT cũng có CLB lập trình."
    ],
    "ký túc xá": [
        "Ký túc xá có phòng 4 người và 8 người.",
        "Bạn cần đăng ký trước mỗi năm học để giữ chỗ."
    ],
    "ăn uống": [
        "Căng tin trường có nhiều món ăn sinh viên giá rẻ.",
        "Xung quanh trường cũng có nhiều quán cơm, trà sữa."
    ],
    "giảng viên": [
        "Giảng viên trường rất thân thiện và hỗ trợ sinh viên.",
        "Bạn có thể liên hệ giảng viên qua email hoặc giờ hành chính."
    ],
    "bài tập": [
        "Bài tập sẽ được giao trên lớp hoặc trên hệ thống LMS.",
        "Đừng quên nộp bài đúng hạn để tránh bị trừ điểm."
    ],
    "đồ án": [
        "Đồ án thường làm theo nhóm 3–5 người.",
        "Giảng viên sẽ hướng dẫn chi tiết yêu cầu đồ án."
    ],
    "học bổng": [
        "Học bổng dựa trên điểm GPA và rèn luyện.",
        "Ngoài ra còn có học bổng doanh nghiệp tài trợ."
    ],
    "hỗ trợ": [
        "Bạn có thể liên hệ phòng công tác sinh viên để được hỗ trợ.",
        "Hỗ trợ có thể về tài chính, tư vấn tâm lý hoặc tìm việc."
    ],
    "tốt nghiệp": [
        "Điều kiện tốt nghiệp: hoàn thành tín chỉ và đạt chuẩn đầu ra ngoại ngữ.",
        "Sinh viên cần nộp đơn đăng ký xét tốt nghiệp tại phòng đào tạo."
    ]
}

def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

def get_response(user_input: str) -> str:
    text = normalize_text(user_input)
    if not text:
        return "Bạn hãy nhập câu hỏi trước nhé."

    best_match, score, _ = process.extractOne(
        query=text,
        choices=RESPONSES.keys(),
        scorer=fuzz.WRatio
    )

    threshold = 40 if len(text) <= 3 else 50

    if best_match and score >= threshold:
        return random.choice(RESPONSES[best_match])

    return "Xin lỗi, mình chưa hiểu ý bạn 😅. Bạn thử hỏi theo cách khác nhé."
