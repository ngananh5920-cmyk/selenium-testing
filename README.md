# Selenium Web Testing Assignment

## 1. Giới thiệu

Bài tập thực hành Selenium WebDriver bằng Python để tự động hóa kiểm thử website.

Website kiểm thử:

https://the-internet.herokuapp.com/login


## 2. Công nghệ sử dụng

* Python 3.13
* Selenium 4
* Google Chrome
* Visual Studio Code


## 3. Các Test Case

### TC01 - Login Success

**Mục tiêu:**
Kiểm tra đăng nhập thành công với tài khoản hợp lệ.

**Dữ liệu kiểm thử:**

* Username: tomsmith
* Password: SuperSecretPassword!

**Kết quả mong đợi:**

Người dùng đăng nhập thành công và chuyển đến trang Secure Area.

**Kết quả thực tế:**

PASS


### TC02 - Login Failed

**Mục tiêu:**
Kiểm tra đăng nhập thất bại với tài khoản không hợp lệ.

**Dữ liệu kiểm thử:**

* Username: admin
* Password: 123456

**Kết quả mong đợi:**

Hệ thống hiển thị thông báo lỗi.

**Kết quả thực tế:**

PASS


### TC03 - Logout Success

**Mục tiêu:**
Kiểm tra chức năng đăng xuất.

**Các bước thực hiện:**

1. Đăng nhập thành công.
2. Chọn Logout.

**Kết quả mong đợi:**

Người dùng quay về trang đăng nhập.

**Kết quả thực tế:**

PASS


## 4. Cấu trúc thư mục

* test_login_success.py
* test_login_fail.py
* test_logout.py
* README.md

---

## 5. Kết luận

Đã xây dựng thành công 03 test case kiểm thử tự động bằng Selenium:

* Login Success
* Login Failed
* Logout Success
