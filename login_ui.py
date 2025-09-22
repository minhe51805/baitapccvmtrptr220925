import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class LoginUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("User name")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        
        # Căn giữa cửa sổ
        self.center_window()
        
        # Tạo giao diện
        self.create_widgets()
        
        # Dữ liệu đăng nhập mẫu (trong thực tế nên lưu trong database)
        self.users = {
            "admin": "123456",
            "user": "password",
            "test": "test123"
        }
    
    def center_window(self):
        """Căn giữa cửa sổ trên màn hình"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        
        # Frame chính
        main_frame = tk.Frame(self.window, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Tiêu đề
        title_label = tk.Label(
            main_frame, 
            text="User name", 
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=(0, 30))
        
        # Frame cho form đăng nhập
        login_frame = tk.Frame(main_frame, bg='#f0f0f0')
        login_frame.pack(expand=True)
        
        # Tên đăng nhập
        username_label = tk.Label(
            login_frame, 
            text="Tên đăng :", 
            font=('Arial', 10),
            bg='#f0f0f0'
        )
        username_label.grid(row=0, column=0, sticky='w', pady=(0, 5))
        
        self.username_entry = tk.Entry(
            login_frame, 
            font=('Arial', 10),
            width=25,
            relief='solid',
            borderwidth=1
        )
        self.username_entry.grid(row=1, column=0, pady=(0, 15))
        self.username_entry.focus()  # Focus vào ô username khi khởi động
        
             # Mật khẩu
        password_label = tk.Label(
            login_frame, 
            text="Mật khẩu:", 
            font=('Arial', 10),
            bg='#f0f0f0'
        )
        password_label.grid(row=2, column=0, sticky='w', pady=(0, 5))
        
        self.password_entry = tk.Entry(
            login_frame, 
            font=('Arial', 10),
            width=25,
            show='*',  # Ẩn mật khẩu
            relief='solid',
            borderwidth=1
        )
        self.password_entry.grid(row=3, column=0, pady=(0, 20))
        
        
        # Frame cho buttons
        button_frame = tk.Frame(login_frame, bg='#f0f0f0')
        button_frame.grid(row=5, column=0)
        
        # Nút đăng nhập
        login_button = tk.Button(
            button_frame,
            text="Đăng Nhập",
            font=('Arial', 10, 'bold'),
            bg='#4CAF50',
            fg='white',
            width=12,
            height=1,
            relief='flat',
            cursor='hand2',
        )
        login_button.pack(side='left', padx=(0, 10))
      
       

        # Bind Enter key để đăng nhập
        self.window.bind('<Return>', lambda event: self.login())
    
 
    
    def run(self):
        """Chạy ứng dụng"""
        self.window.mainloop()

# Chạy ứng dụng
if __name__ == "__main__":
    app = LoginUI()
    app.run()