from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# Thay thế đường dẫn đến file JSON của bạn
CLIENT_SECRET_FILE = './client_secret_1067445661075-qvmk4s6iqb9as91enokc2tqlqr43d574.apps.googleusercontent.com.json'
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
