from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# Thay thế đường dẫn đến file JSON của bạn
CLIENT_SECRET_FILE = 'path/to/your/client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Tạo flow OAuth2
flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET_FILE, SCOPES)

# Chạy flow xác thực và nhận token truy cập
credentials = flow.run_local_server(port=8080)

# Lưu lại credentials (token) để sử dụng sau này
with open('token.json', 'w') as token:
    token.write(credentials.to_json())

print("Access token đã được lưu.")
