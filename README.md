
# Selenium Web Testing Assignment

## Thông tin sinh viên

* Họ và tên: Phương Ngân
* Mã sinh viên: 23010450

---

# 1. Giới thiệu

Trong quá trình phát triển phần mềm, kiểm thử tự động giúp giảm thời gian kiểm thử thủ công, tăng độ chính xác và đảm bảo chất lượng sản phẩm. Selenium WebDriver là một công cụ phổ biến được sử dụng để tự động hóa các thao tác trên trình duyệt web.

Bài thực hành này sử dụng Selenium WebDriver kết hợp với ngôn ngữ Python để xây dựng các kịch bản kiểm thử tự động cho chức năng đăng nhập của website mẫu:

[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

Thông qua bài thực hành, sinh viên có thể làm quen với việc:

* Cài đặt và cấu hình Selenium WebDriver.
* Tương tác với các phần tử trên giao diện web.
* Tự động nhập dữ liệu vào biểu mẫu.
* Kiểm tra kết quả trả về của hệ thống.
* Viết các kịch bản kiểm thử tự động cơ bản.

---

# 2. Mục tiêu bài thực hành

Mục tiêu của bài thực hành là:

* Tìm hiểu cách hoạt động của Selenium WebDriver.
* Thực hiện tự động hóa các thao tác đăng nhập trên website.
* Xây dựng các test case kiểm thử chức năng Login và Logout.
* Kiểm tra tính đúng đắn của hệ thống thông qua kết quả thực thi.
* Nâng cao kỹ năng lập trình Python trong lĩnh vực kiểm thử phần mềm.

---

# 3. Môi trường kiểm thử

| Thành phần    | Phiên bản              |
| ------------- | ---------------------- |
| Python        | 3.13                   |
| Selenium      | 4.x                    |
| Google Chrome | Phiên bản mới nhất     |
| ChromeDriver  | Tương thích với Chrome |
| IDE           | Visual Studio Code     |
| Hệ điều hành  | Windows 10/11          |

---

# 4. Website kiểm thử

Website được sử dụng trong bài thực hành:

[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

Thông tin tài khoản hợp lệ được cung cấp bởi website:

* Username: tomsmith
* Password: SuperSecretPassword!

Chức năng được kiểm thử:

* Đăng nhập thành công.
* Đăng nhập thất bại.
* Đăng xuất khỏi hệ thống.

---

# 5. Các Test Case

## TC01 - Login Success

### Mục tiêu

Kiểm tra khả năng đăng nhập thành công khi người dùng nhập đúng tài khoản và mật khẩu.

### Dữ liệu kiểm thử

* Username: tomsmith
* Password: SuperSecretPassword!

### Các bước thực hiện

1. Mở trình duyệt Chrome.
2. Truy cập trang Login.
3. Nhập Username hợp lệ.
4. Nhập Password hợp lệ.
5. Nhấn nút Login.

### Kết quả mong đợi

* Hệ thống đăng nhập thành công.
* Chuyển hướng tới trang Secure Area.
* Hiển thị thông báo đăng nhập thành công.

### Kết quả thực tế

PASS

---

## TC02 - Login Failed

### Mục tiêu

Kiểm tra khả năng xử lý khi người dùng nhập sai thông tin đăng nhập.

### Dữ liệu kiểm thử

* Username: admin
* Password: 123456

### Các bước thực hiện

1. Mở trình duyệt Chrome.
2. Truy cập trang Login.
3. Nhập Username không hợp lệ.
4. Nhập Password không hợp lệ.
5. Nhấn Login.

### Kết quả mong đợi

* Hệ thống từ chối đăng nhập.
* Hiển thị thông báo lỗi.
* Người dùng vẫn ở trang Login.

### Kết quả thực tế

PASS

---

## TC03 - Logout Success

### Mục tiêu

Kiểm tra chức năng đăng xuất sau khi đăng nhập thành công.

### Các bước thực hiện

1. Đăng nhập bằng tài khoản hợp lệ.
2. Truy cập Secure Area.
3. Nhấn nút Logout.

### Kết quả mong đợi

* Phiên đăng nhập kết thúc.
* Người dùng được chuyển về trang Login.
* Hiển thị thông báo đăng xuất thành công.

### Kết quả thực tế

PASS

---

# 6. Cấu trúc thư mục

```text
selenium-testing/
│
├── test_login_success.py
├── test_login_fail.py
├── test_logout.py
└── README.md
```

Mỗi file kiểm thử được xây dựng độc lập nhằm dễ dàng quản lý, thực thi và bảo trì.

---

# 7. Kết quả thực thi

Sau khi thực hiện các kịch bản kiểm thử, toàn bộ test case đều đạt kết quả mong đợi.

| Test Case             | Trạng thái |
| --------------------- | ---------- |
| TC01 - Login Success  | PASS       |
| TC02 - Login Failed   | PASS       |
| TC03 - Logout Success | PASS       |

Tỷ lệ thành công: 100%

---

# 8. Kết luận

Bài thực hành đã xây dựng thành công hệ thống kiểm thử tự động bằng Selenium WebDriver với Python cho chức năng đăng nhập của website mẫu.

Thông qua bài thực hành, đã thực hiện được:

* Tự động hóa thao tác nhập liệu trên website.
* Kiểm tra kết quả đăng nhập thành công và thất bại.
* Kiểm thử chức năng đăng xuất.
* Xác nhận hệ thống hoạt động đúng theo yêu cầu.

