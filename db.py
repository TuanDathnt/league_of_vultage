import sqlite3


# Kết nối với cơ sở dữ liệu SQLite
conn = sqlite3.connect('db/lovdb.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS books (
#     Book_ID INTEGER PRIMARY KEY,
#     Book_Name NVARCHAR,
#     Book_Category NVARCHAR,
#     Book_Subcategory NVARCHAR,
#     Book_Genre NVARCHAR,
#     Author NVARCHAR,
#     Publisher NVARCHAR,
#     Date_Published INTEGER,
#     Age_Range INTEGER,
#     Rating REAL,
#     Price INTEGER,
#     Picture VARCHAR,
#     Description VARCHAR,
#     Content VARCHAR
# )
# ''')
# Tạo một số dữ liệu mẫu
books_data = [
    (9,"1TuanDat","123543","qstuandat@gmail.com"),
    (7,"2HinaTuanDat","12312312","qstuandat@gmail.com"),
    # Thêm thêm 18 dòng dữ liệu khác...
]

# Câu lệnh SQL để chèn dữ liệu
insert_sql = '''
INSERT INTO Account
(Account_ID,Username,Password,Gmail) 
VALUES 
(?, ?, ?, ?)
'''

# Chèn dữ liệu vào bảng
for book in books_data:
    cursor.execute(insert_sql, book)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()