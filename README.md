### Hướng dẫn kết nối Google Cloud API và cấu hình OAuth

#### 1. Truy cập Google Cloud Console
- Truy cập Google Cloud Console thông qua link: [Google Cloud Console](https://console.cloud.google.com/welcome?project=original-fort-392115).
- Tại giao diện Google Cloud, chọn dự án như trong hình dưới đây:
  ![Chọn dự án](https://github.com/user-attachments/assets/68df7ef1-5382-4945-a454-6b02694a06a4)

#### 2. Cấu hình API
- Ở giao diện Google Cloud Console, chọn **API & Services** ở menu bên trái.
- Cuộn chuột xuống và chọn **Google Cloud API** để kích hoạt API cần thiết.

#### 3. Tạo Credentials
- Bên góc trái màn hình, chọn **Credentials**.
  ![Chọn Credentials](https://github.com/user-attachments/assets/0902b262-e021-499f-84dd-c63e712fa51f)
- Tại trang **Credentials**, tích chọn **Create Credentials** và sau đó chọn **OAuth Client ID**.

#### 4. Cấu hình OAuth Client ID
- Chọn **Create** để bắt đầu quá trình tạo OAuth Client ID.
- Ở bước thêm **URIs**, nhập URL: `http://localhost:8080/`.
  ![Thêm URIs](https://github.com/user-attachments/assets/1eb9af87-89d5-4c14-b6a5-f99e49f9a31c)

#### 5. Tải tệp JSON chứa OAuth Credentials
- Sau khi cấu hình thành công, chọn tải tệp JSON về chứa thông tin OAuth Client ID.
  ![Tải tệp JSON](https://github.com/user-attachments/assets/d5b94dd9-3d29-4a04-bdde-832fb688af1b)

#### 6. Chạy code và xác thực OAuth
- Tiếp theo, bạn sẽ cần chạy tệp code `confirmAuthorize_2`.
- Tải tệp JSON mới về và chỉ định đường dẫn của nó vào biến `CLIENT_SECRET_FILE` trong mã nguồn:
  ```python
  CLIENT_SECRET_FILE = 'path/to/your/client_secret.json'
  ```
  ![Chỉ định đường dẫn](https://github.com/user-attachments/assets/be65ad5d-53d9-4797-92d7-bcaaed4dcdfc)

#### 7. Nhận token và lưu lại
- Sau khi chạy code, bạn sẽ được yêu cầu xác nhận tài khoản Google. Sau khi xác nhận thành công, hệ thống sẽ gửi về một mã token.
- Token sẽ được lưu vào tệp có tên **token.json** như hình dưới đây:
  ![Lưu token.json](https://github.com/user-attachments/assets/7e2a3c88-7436-4343-80ab-412a99c60be6)

#### 8. Cập nhật đường dẫn token trong code
- Trong hàm `authenticate_with_google()`, hãy nhập đường dẫn đến tệp **token.json** mà bạn đã lưu.
- Hoàn tất cấu hình để chạy hệ thống.

### Đóng góp và cải tiến
- Sau khi cài đặt thành công, bạn có thể tự khám phá và tìm hiểu logic của code. Nếu có ý kiến đóng góp để cải thiện mã nguồn, vui lòng phản hồi.
- Chú thích: Đây là bản hướng dẫn nhanh được viết trong buổi chiều, rất mong sự đóng góp ý kiến từ các bạn. Xin cảm ơn!
