from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import matplotlib.pyplot as plt
from googleapiclient.errors import HttpError
# Định nghĩa các phạm vi quyền truy cập (scopes)
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
def FindName(name,files):
    if not files:
        print('No files found.')
    else:
        found_files = []  # Danh sách tệp tìm được
        other_files = []  # Danh sách tệp không tìm thấy

        # Duyệt qua từng tệp và phân loại theo tên
        for file in files:
            if name.lower() in file["name"].lower():
                found_files.append(f'{file["name"]}, id : {file["id"]}')
            # else:
            #     other_files.append(f'{file["name"]}, id: {file["id"]}')
        
        # Hiển thị kết quả tìm được
        print(f'Files matching "{name}":')
        for file in found_files:
            print(f'  {file}')

        print('\nOther files:')
        # for file in other_files:
        #     print(f'  {file}')

        # Trực quan hóa số lượng file tìm được và không tìm được
        labels = ['Found', 'Other']
        sizes = [len(found_files), len(other_files)]
        
        fig, ax = plt.subplots()
        ax.bar(labels, sizes, color=['blue', 'red'])
        ax.set_title(f'File Search Results for "{name}"')
        ax.set_xlabel('File Category')
        ax.set_ylabel('Number of Files')

        plt.show()

def AddNewFolder(nameFolder):
    # Thêm tệp mới vào Google Drive
    file_metadata = {'name': nameFolder}
    media = MediaFileUpload(nameFolder, mimetype='text/plain')

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id').execute()

    print(f'File ID: {file["id"]}')
def UpdateFolder(id, newName):
    # ID của tệp bạn muốn sửa
    file_id = id

    # Cập nhật thông tin tệp (sửa tên)
    updated_metadata = {'name': 'new_name.txt'}
    updated_file = service.files().update(
        fileId=file_id,
        body=updated_metadata).execute()

    print(f'Updated File ID: {updated_file["id"]}')
def DeleteFolder(id):
    # ID của tệp bạn muốn xóa
    file_id = id
    # Xóa tệp
    service.files().delete(fileId=file_id).execute()
    print('File deleted successfully')

# Hàm xác thực với Google Drive API
def authenticate_with_google():
    credentials = Credentials.from_authorized_user_file('./token.json', SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    return service
    # Hàm hiển thị danh sách tệp trong thư mục
def list_files_in_folder(service, folder_id):
    try:
        query = f"'{folder_id}' in parents"
        results = service.files().list(
            q=query,
            fields="files(id, name, mimeType, createdTime, size)",
            pageSize=100
        ).execute()
        files = results.get('files', [])
        
        if not files:
            print('No files found.')
        else:
            print('Files in folder:')
            for file in files:
                print(f"Name: {file['name']}, ID: {file['id']}, MimeType: {file['mimeType']}, Created: {file['createdTime']}, Size: {file.get('size', 'N/A')}")
    
    except HttpError as error:
        print(f"An error occurred: {error}")
# Hàm tạo báo cáo (ví dụ: tổng hợp thông tin về các tệp)
def generate_report(files):
    print("\n--- Report ---")
    if not files:
        print("No files available to report.")
        return
    print(f"Total files: {len(files)}")
    for file in files:
        print(f"File Name: {file['name']}, ID: {file['id']}, MimeType: {file['mimeType']}, Created: {file['createdTime']}")

# Hàm phân tích với AI (ví dụ: phân tích tên tệp hoặc nội dung nếu có thể)
def ai_analysis(files):
    print("\n--- AI Analysis ---")
    for file in files:
        print(f"Analyzing {file['name']}...")
        # Có thể sử dụng AI mô hình hoặc phân tích khác ở đây (ví dụ: phân tích nội dung tệp nếu là văn bản hoặc hình ảnh)
        print(f"Finished analyzing {file['name']}")

# Hàm phân tích thư mục
def AnlysisFolder(folder_id="1rhVgoOiArbaBWluUV18SidUOTfE9VmG3"):
    # Xác thực với Google Drive API
    service = authenticate_with_google()
    
    # Hiển thị danh sách tệp trong thư mục
    list_files_in_folder(service, folder_id)

    # Giả sử bạn muốn tạo báo cáo và phân tích AI
    query = f"'{folder_id}' in parents"
    files = service.files().list(q=query, fields="files(id, name, mimeType, createdTime, size)", pageSize=100).execute().get('files', [])
    
    # Tạo báo cáo
    generate_report(files)
    
    # Phân tích AI
    ai_analysis(files)

if __name__ == "__main__":
    credentials = Credentials.from_authorized_user_file('./token.json')

    #Service
    service = build('drive','v3',credentials=credentials)
    results = service.files().list(
        pageSize=100, fields="files(id, name)").execute()
    files = results.get('files', [])
    FindName('EXPLORING',files)
    #add new folder
    # AddNewFolder("token.json")
    AnlysisFolder()