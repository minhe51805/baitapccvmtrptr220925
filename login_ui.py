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
            text="txt.Username:", 
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
            text="Password:", 
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
            text="btnlogin",
            font=('Arial', 10, 'bold'),
            bg='#4CAF50',
            fg='white',
            width=12,
            height=1,
            relief='flat',
            cursor='hand2',
            command=self.login
        )
        login_button.pack(side='left', padx=(0, 10))
        

        # Bind Enter key để đăng nhập
        self.window.bind('<Return>', lambda event: self.login())
    
    def toggle_password(self):
        """Hiển thị/ẩn mật khẩu"""
        if self.show_password_var.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
    
    def login(self):
        """Xử lý đăng nhập"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        # Kiểm tra thông tin đăng nhập
        if not username:
            messagebox.showerror("Lỗi", "Vui lòng nhập tên đăng nhập!")
            self.username_entry.focus()
            return
        
        if not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập mật khẩu!")
            self.password_entry.focus()
            return
        
        # Kiểm tra tài khoản
        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Thành công", f"Đăng nhập thành công!\nXin chào {username}!")
            self.show_main_app(username)
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()
    
    def show_main_app(self, username):
        """Hiển thị ứng dụng chính sau khi đăng nhập thành công"""
        # Ẩn cửa sổ đăng nhập
        self.window.withdraw()
        
        # Tạo cửa sổ ứng dụng chính
        main_window = tk.Toplevel()
        main_window.title("Ứng Dụng Chính")
        main_window.geometry("600x400")
        main_window.resizable(True, True)
        
        # Căn giữa cửa sổ
        main_window.update_idletasks()
        width = main_window.winfo_width()
        height = main_window.winfo_height()
        x = (main_window.winfo_screenwidth() // 2) - (width // 2)
        y = (main_window.winfo_screenheight() // 2) - (height // 2)
        main_window.geometry(f'{width}x{height}+{x}+{y}')
        
        # Nội dung ứng dụng chính
        welcome_label = tk.Label(
            main_window,
            text=f"Chào mừng {username}!",
            font=('Arial', 20, 'bold'),
            fg='#2E8B57'
        )
        welcome_label.pack(pady=50)
        
        content_label = tk.Label(
            main_window,
            text="Đây là ứng dụng chính sau khi đăng nhập thành công.",
            font=('Arial', 12),
            fg='#333333'
        )
        content_label.pack(pady=20)
        
        # Nút đăng xuất
        logout_button = tk.Button(
            main_window,
            text="Đăng Xuất",
            font=('Arial', 12, 'bold'),
            bg='#FF6B6B',
            fg='white',
            width=15,
            height=2,
            relief='flat',
            cursor='hand2',
            command=lambda: self.logout(main_window)
        )
        logout_button.pack(pady=30)
        
        # Xử lý khi đóng cửa sổ chính
        main_window.protocol("WM_DELETE_WINDOW", lambda: self.logout(main_window))
    
    def logout(self, main_window):
        """Đăng xuất và quay lại màn hình đăng nhập"""
        main_window.destroy()
        self.window.deiconify()  # Hiển thị lại cửa sổ đăng nhập
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username_entry.focus()
    
    def exit_app(self):
        """Thoát ứng dụng"""
        if messagebox.askokcancel("Thoát", "Bạn có chắc chắn muốn thoát?"):
            self.window.quit()
    
    def run(self):
        """Chạy ứng dụng"""
        self.window.mainloop()

# Chạy ứng dụng
if __name__ == "__main__":
    app = LoginUI()
    app.run()