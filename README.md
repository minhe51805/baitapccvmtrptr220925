# UI Đăng Nhập bằng Python Tkinter

Ứng dụng giao diện đăng nhập đơn giản được xây dựng bằng Python và thư viện Tkinter.

## 🚀 Tính năng

- ✅ Giao diện đăng nhập đẹp mắt
- ✅ Validation thông tin đăng nhập
- ✅ Hiển thị/ẩn mật khẩu
- ✅ Phím tắt (Enter để đăng nhập)
- ✅ Màn hình ứng dụng chính sau khi đăng nhập
- ✅ Chức năng đăng xuất
- ✅ Tài khoản mẫu để test

## 📋 Yêu cầu hệ thống

- Python 3.6 trở lên
- Tkinter (có sẵn trong Python)

## 🔧 Cài đặt

### Cách 1: Cài đặt tự động (Khuyến nghị)
```bash
python setup_env.py
```

### Cách 2: Cài đặt thủ công
```bash
# Cài đặt thư viện cơ bản
pip install -r requirements.txt

# Hoặc cài đặt đầy đủ (bao gồm thư viện nâng cao)
pip install -r requirements-full.txt
```

## 🎮 Cách sử dụng

### Chạy ứng dụng
```bash
python login_ui.py
```

### Tài khoản mẫu
| Username | Password |
|----------|----------|
| admin    | 123456   |
| user     | password |
| test     | test123  |

## 📁 Cấu trúc dự án

```
baitapccvmtrptr220925/
├── login_ui.py           # File chính chứa giao diện đăng nhập
├── requirements.txt      # Thư viện cơ bản
├── requirements-full.txt # Thư viện đầy đủ (nâng cao)
├── setup_env.py         # Script cài đặt tự động
└── README.md            # Hướng dẫn sử dụng
```

## 🎯 Hướng dẫn sử dụng

1. **Khởi động**: Chạy `python login_ui.py`
2. **Đăng nhập**: Nhập username/password từ bảng tài khoản mẫu
3. **Khám phá**: Sau khi đăng nhập thành công, khám phá ứng dụng chính
4. **Đăng xuất**: Click "Đăng Xuất" để quay lại màn hình đăng nhập
5. **Thoát**: Click "Thoát" để đóng ứng dụng

## 🔍 Chi tiết kỹ thuật

### Class LoginUI
- `__init__()`: Khởi tạo giao diện và dữ liệu
- `create_widgets()`: Tạo các thành phần giao diện
- `login()`: Xử lý logic đăng nhập
- `show_main_app()`: Hiển thị ứng dụng chính
- `logout()`: Xử lý đăng xuất
- `toggle_password()`: Hiển thị/ẩn mật khẩu

### Tính năng bảo mật
- ✅ Ẩn mật khẩu khi nhập
- ✅ Validation input
- ✅ Thông báo lỗi rõ ràng
- ⚠️ Mật khẩu chưa được mã hóa (để demo)

## 🚀 Mở rộng

### Thêm mã hóa mật khẩu
```python
import bcrypt

# Hash password
password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Verify password  
bcrypt.checkpw(password.encode('utf-8'), password_hash)
```

### Kết nối Database
```python
import sqlite3

# Tạo database users
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password_hash TEXT
    )
''')
```

### GUI đẹp hơn với CustomTkinter
```python
import customtkinter as ctk

# Thay thế tkinter widgets bằng customtkinter
```

## 🤝 Đóng góp

1. Fork dự án
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📝 License

Dự án này được phát hành dưới MIT License. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 📞 Liên hệ

Nếu có thắc mắc hoặc đề xuất, vui lòng tạo issue trên GitHub.

---
**Chúc bạn code vui vẻ! 🎉**