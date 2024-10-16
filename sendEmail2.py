import os
import time
import smtplib
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Cập nhật thông tin đăng nhập của bạn ở đây
def send_email_notification(subject, message, to_email):
    from_email = "nguyentrungthanhdev@gmail.com"  # Địa chỉ email của bạn
    password = "bqcd ijeq bvaq exkj"  # Mật khẩu ứng dụng của bạn (thay thế mật khẩu của bạn ở đây)

    # Tạo đối tượng message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Nội dung email
    msg.attach(MIMEText(message, 'plain'))

    # Thiết lập kết nối tới máy chủ SMTP (ở đây dùng Gmail)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Kết nối tới Gmail SMTP server
        server.starttls()  # Bật chế độ mã hóa TLS
        server.login(from_email, password)  # Đăng nhập vào email

        # Gửi email
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Lấy dữ liệu từ Google Sheets
def get_sheet_data(spreadsheet_id, range_name):
    creds = Credentials.from_authorized_user_file('token.json')
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    
    # Lấy dữ liệu trong range nhất định
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    
    return values

# Hàm kiểm tra thay đổi trong Google Sheets
def monitor_google_sheet(spreadsheet_id, range_name, last_known_data):
    current_data = get_sheet_data(spreadsheet_id, range_name)

    # Kiểm tra sự thay đổi trong Google Sheets (so sánh với dữ liệu đã lưu trước đó)
    if current_data != last_known_data:
        print("Google Sheet has been updated!")
        send_email_notification(
            subject="Google Sheet Updated",
            message="There is new data entered in the Google Sheet. Please check.",
            to_email="recipient@example.com"
        )
        return current_data  # Cập nhật dữ liệu đã kiểm tra
    return last_known_data  # Không có thay đổi

# Đoạn mã giám sát liên tục
def auto_notify():
    spreadsheet_id = '1pT1F7HR1ZK6HTci-thNlrH5lQ_TiKicJ_bL9m7wfeIY'  # ID của bảng tính Google Sheets
    range_name = 'Info!B2:G13'  # Phạm vi dữ liệu bạn muốn giám sát (ví dụ từ A1 đến F)
    
    # Lấy dữ liệu hiện tại từ Google Sheets lần đầu
    last_known_data = get_sheet_data(spreadsheet_id, range_name)
    
    while True:
        # Kiểm tra thay đổi sau mỗi 30 giây
        last_known_data = monitor_google_sheet(spreadsheet_id, range_name, last_known_data)
        time.sleep(0.5)  # Đợi 30 giây trước khi kiểm tra lại

if __name__ == "__main__":
    auto_notify()