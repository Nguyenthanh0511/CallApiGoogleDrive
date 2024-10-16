from google_auth_oauthlib.flow import InstalledAppFlow

# Tải client secrets từ file JSON
flow = InstalledAppFlow.from_client_secrets_file(
    './client_secret_1067445661075-qvmk4s6iqb9as91enokc2tqlqr43d574.apps.googleusercontent.com.json', 
    scopes=['https://www.googleapis.com/auth/drive.readonly'])

# Cung cấp redirect_uri đã cấu hình trong Google Cloud Console
flow.redirect_uri = 'http://localhost:8080/'

# Tạo URL ủy quyền
auth_url, _ = flow.authorization_url(prompt='consent')

print(f'Visit this URL to authorize the application: {auth_url}')

# Nhập mã xác nhận từ người dùng
code = input('Enter the authorization code: ')

# Lấy token truy cập
credentials = flow.fetch_token(code=code)

# Bây giờ bạn đã có 'credentials' để truy cập Google Drive API
