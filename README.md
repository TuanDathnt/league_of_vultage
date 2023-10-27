Project su dung vscode de lap trinh . Project backend

- Thư mục `venv`: Chứa môi trường ảo (virtual environment) cho project.
- File `README.md`: File mô tả project.

1. Clone repository này vào máy của bạn.

```commandline
git clone https://github.com/TuanDathnt/league_of_vultage.git
```
```commandline
cd league_of_vultage/
```

2.Khoi chay venv

# macOS/Linux

## You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs

```commandline
python3 -m venv .venv
```

# Windows

## You can also use `py -3 -m venv .venv`

```commandline
python -m venv .venv
```

# chay moi truong ao

```commandline
source .venv/bin/activate
```

3. Cài đặt các dependencies:

```commandline
pip install -r requirements.txt
```

4. Khởi chạy ứng dụng:

```commandline
python app.py
```

# League-Of-Vulgate

https://www.figma.com/file/oNKcqE5EyXvBSh4vddTSNn/LOV?type=design&node-id=0-1&mode=design&t=qdTKSmWZlPEdoxuT-0
Tên Trang |
------------- |
TRang đăng nhập |
Trang đăng ký |
Trang chủ |
Trang Cart |
Trang thanh toán |
Trang đọc ebook |
Trang nhắn tin(optional) |
Trang profile |
Trang lịch sử giao dịch |
Trang Achivemetnt |

# Luồng trang

1. trang chủ ->
   1. trang cart
   2. trang profile
   3. trang lịch sử
   4. trang achivement
   5. trang đăng nhập
   6. trang đăng ký
   7. trang đọc ebook
2. Trang Cart
   1. Trang thanh toan
