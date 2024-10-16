import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Tải token từ tệp token.json
def authenticate_with_google():
    credentials = Credentials.from_authorized_user_file('token.json')
    return credentials  # Trả về credentials thay vì service

# Kiểm tra sự thay đổi trong file Google Sheets
def check_file_in_google_drive(service, file_name):
    results = service.files().list(q=f"name='{file_name}'", spaces='drive', fields="files(id, name)").execute()
    files = results.get('files', [])
    
    if not files:
        print(f"No file named {file_name} found.")
        return None
    else:
        for file in files:
            print(f"Found file: {file['name']} (ID: {file['id']})")
            return file['id']
    return None

# Lấy dữ liệu từ Google Sheets
def get_sheet_data(spreadsheet_id, credentials):
    service = build('sheets', 'v4', credentials=credentials).spreadsheets()  # Tạo service với credentials
    
    result = service.values().get(spreadsheetId=spreadsheet_id, range="A1:F").execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found in the sheet.')
    else:
        print('Data from the sheet:')
        for row in values:
            print(row)
    
    return values

# Gửi thông báo (có thể thay bằng email hoặc bất kỳ thông báo nào bạn muốn)
def send_notification(message):
    # Đoạn này bạn có thể thay thế bằng logic gửi email hoặc sử dụng một thư viện như smtplib
    print(f"Notification: {message}")

# Chạy kiểm tra liên tục
def monitor_google_sheet():
    file_name = "theodoisinhvien"
    
    credentials = authenticate_with_google()  # Lấy credentials từ hàm authenticate_with_google
    service = build('drive', 'v3', credentials=credentials)  # Dùng credentials để tạo service cho Google Drive
    
    spreadsheet_id = check_file_in_google_drive(service, file_name)

    if spreadsheet_id:
        previous_data = None
        while True:
            current_data = get_sheet_data(spreadsheet_id, credentials)  # Truyền credentials vào hàm get_sheet_data
            if current_data != previous_data:
                send_notification("The file 'theodoisinhvien' has been updated!")
                previous_data = current_data
            time.sleep(0.5)  # Kiểm tra mỗi phút (có thể thay đổi tùy vào yêu cầu)
    else:
        print("File not found. Please check the file name.")

# Thực thi hàm monitor
if __name__ == '__main__':
    monitor_google_sheet()
