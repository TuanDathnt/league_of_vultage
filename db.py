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
   
    (12,"Flow - Dòng Chảy","Tâm lý - Kĩ năng sống", "Kĩ năng sống","","Mihaly Csikszentmihalyi","NXB Dân Trí","2021-12-09",4,7.8,159600,"https://cdn0.fahasa.com/media/catalog/product/8/9/8935086854792.png",""),
    (13,"Tâm Lý Học Mối Quan Hệ","Tâm lý - Kĩ năng sống","Tâm lý","","Choi Kwanghyun","NXB Thanh Niên","2020-05-04",5,8.1,83300,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/tam_ly_hoc_moi_quan_he/2023_02_07_09_03_07_1-390x510.jpg",""),
    (14," Minh Triết Nội Tại","Tâm lý - Kĩ năng sống","Tâm lý","","David R Hawkins MD, PhD","NXB Thanh Niên","2021-10-21",5,7.8,143650,"https://cdn0.fahasa.com/media/catalog/product/8/9/8936066695152_1.jpg",""),
    (15,"Tư Duy Chiến Lược - Lý Thuyết Trò Chơi Thực Hành","Kinh tế","Bài học Kinh doanh","","Avinash K. Dixit, Barry J. Nalebuff","NXB Dân Trí","2022-03-17",0,7.5,115320,"https://cdn0.fahasa.com/media/catalog/product/b/_/b_a_tr_c_t_duy_chi_n_l_c.png",""),
    (16,"Nghĩ Giàu & Làm Giàu","Kinh tế","Quản trị - Lãnh đạo","","Napoleon Hill","NXB Tổng Hợp TPHCM","2020-09-11",0,8.4,86400,"https://cdn0.fahasa.com/media/catalog/product/n/g/nghigiaulamgiau_110k-01_bia_1.jpg",""),
    (17,"Một Đời Quản Trị","Kinh tế","Quản trị - Lãnh đạo","","Phan Văn Trường","NXB Trê","2022-09-30",0,9.1,160000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/mot_doi_quan_tri_tai_ban_2019/2023_03_21_16_14_02_1-390x510.jpg",""),
    (18,"Kênh Tương Tác Chủ Đạo - The Master Channel","Kinh tế","Marketing - Bán hàng","NXB Công Thương","2021-03-13",0,9,134100,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/kenh_tuong_tac_chu_dao___the_master_channel/2023_11_11_10_27_24_1-390x510.jpg",""),
   
    (20," Chinh Phục Luyện Thi Vào 10 Môn Tiếng Anh Theo Chủ Đề","Giáo khoa - Tham khảo","Sách tham khảo","","Dương Hương","NXB Đại Học Quốc Gia Hà Nội","2022-09-04",3,7.9,127200,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/chinh_phuc_luyen_thi_vao_10_mon_tieng_anh_theo_chu_de/2023_03_23_16_21_38_1-390x510.jpg",""),
    (21,"Luyện Tập Mĩ Thuật 5 - Tập 2","Giáo khoa - Tham khảo","Sách tham khảo","","Nhiều Tác Giả","NXB Giáo Dục Việt Nam","2020-10-10",2,8.1,21000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/luyen_tap_mi_thuat_5_2_n3/2023_04_24_16_58_18_1-390x510.jpg",""),
    (22,"Bồi Dưỡng Năng Lực Tự Học Toán 8","Giáo khoa - Tham khảo","Sách tham khảo","","Đặng Đức Trọng, Nguyễn Đức Tấn","NXB Đại Học Quốc Gia Hà Nội","2021-11-09",2,8,85500,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/boi_duong_nang_luc_tu_hoc_toan_8/2023_09_28_17_00_58_1-390x510.jpg",""),
    (23,"Tiếng Anh 12","Giáo khoa - Tham khảo","Sách giáo khoa","","Bộ Giáo Dục Và Đào Tạo","NXB Giáo Dục Việt Nam","2021-03-14",4,8.4,19000,"https://cdn0.fahasa.com/media/catalog/product/9/7/9786040286581_1_2.jpg",""),
    (24,"i-Learn Smart World 8 Student Book","Giáo khoa - Tham khảo","Sách giáo khoa","","Nhiều Tác Giả","NXB ĐHSP TPHCM","2022-06-17",3,7.4,80000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/i_learn_smart_world_8_student_book_2023/2023_06_21_09_03_29_1-390x510.jpg",""),
    (25,"Chuyên Đề Học Tập Hoá Học 11 (Cánh Diều)","Giáo khoa - Tham khảo","Sách giáo khoa","","Trần Thành Huế, Vũ Quốc Trung","NXB Đại Học Sư Phạm","2021-09-19",4,8,15000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/chuyen_de_hoc_tap_hoa_hoc_11_canh_dieu_2023/2023_07_26_09_42_39_1-390x510.jpg",""),
    (26,"Tài Liệu Dạy Và Học Toán 9 - Tập 2","Giáo khoa - Tham khảo","Sách giáo viên","","Nhiều Tác Giả","NXB Giáo Dục Việt Nam","2020-12-12",5,9,56000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/tai_lieu_day_va_hoc_toan_9___tap_2_2022/2022_06_20_13_58_14_1-390x510.jpg",""),
    (27,"Tài Liệu Dạy - Học Tin Học 9","Giáo khoa - Tham khảo","Sách giáo viên","","Nhiều Tác Giả","NXB Giáo Dục Việt Nam","2020-12-12",5,9,40000,"https://cdn0.fahasa.com/media/catalog/product/t/a/tai-lieu-day-hoc-tin-hoc-9_1543369439_2.jpg",""),
    (28,"Tài Liệu Dạy - Học Hóa Học 9 - Tập 1","Giáo khoa - Tham khảo","Sách giáo viên","","Nhiều Tác Giả","NXB Giáo Dục Việt Nam","2020-12-12",5,9,58000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/tai_lieu_day_va_hoc_hoa_hoc_9___tap_1_2021/2022_07_02_10_17_21_1-390x510.jpg",""),
    (29,"Tài Liệu Dạy Và Học Vật Lý 9 - Tập 2","Giáo khoa - Tham khảo","Sách giáo viên","","Phạm Ngọc Tiến","NXB Giáo Dục Việt Nam","2020-12-12",5,9,59000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/tai_lieu_day_va_hoc_vat_ly_9___tap_2_2021/2021_06_10_11_27_57_1-390x510.jpg",""),
    (30,"Đế Chế Atlantis Và Những Vương Quốc Biến Mất ","Lịch sử - Địa lí - Tôn giáo","Lịch sử","","Frank Joseph","NXB Dân trí","2022-05-14",0,9.2,140250,"https://cdn0.fahasa.com/media/catalog/product/b/i/bia_1__de_che_atlantis-01_-_copy.jpg",""),
    (31,"Làm Mới Vườn Tâm","Lịch sử - Địa lí - Tôn giáo","Tôn giáo","","Suối Thông","NXB Hội Nhà Văn","2018-09-23",0,8.3,99000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/lam_moi_vuon_tam/2023_06_19_16_56_22_1-390x510.jpg",""),
    (32,"Hoa Trôi Trên Sóng Nước","Lịch sử - Địa lí - Tôn giáo","Tôn giáo","","Satomi Myodo","NXB Tổng Hợp TPHCM","2019-09-03",0,8.1,83000,"https://cdn0.fahasa.com/media/catalog/product/8/9/8935086827154_1.jpg",""),
    (33,"Các Triều Đại Việt Nam","Lịch sử - Địa lí - Tôn giáo","Lịch sử","","Quỳnh Cư, Đỗ Đức Hùng","NXB Thanh Niên","2022-09-19",0,7.8,81500,"https://cdn0.fahasa.com/media/catalog/product/8/9/8935095632008_1.jpg",""),
    (34,"Những Ngày Cuối Của Dòng Mekong Hùng Vĩ","Lịch sử - Địa lí - Tôn giáo","Địa lí","","Brian Eyler","NXB Phụ Nữ Việt Nam","2021-08-03",0,8,253000,"https://cdn0.fahasa.com/media/catalog/product/8/9/8936144200834.jpg",""),
    (35,"S54 Câu Hỏi Đáp Về Các Huyện Đảo Việt Nam","Lịch sử - Địa lí - Tôn giáo","Địa lí","","Phan Thị Ánh Tuyết","NXB Dân Trí","2020-07-14",0,8.6,61200,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/54_cau_hoi_dap_ve_cac_huyen_dao_viet_nam/2021_06_19_10_44_55_1-390x510.JPG",""),
    (36,"Cha Voi: Dạy Con Nên Người Ở Thời Đại Số","Nuôi dạy con","Cẩm nang làm cha mẹ","","Trương Nguyện Thành","NXB Tổng Hợp TPHCM","2020-07-14",0,8.6,120000,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/cha_voi_day_con_nen_nguoi_o_thoi_dai_so/2022_12_29_17_05_36_1-390x510.jpg",""),
    (37,"Thực Đơn Ăn Dặm Kiểu Nhật","Nuôi dạy con","Dinh dưỡng - Sức khỏe cho con","","Reiko Ueda, Junko Ueda","NXB Lao Động","2022-01-31",0,7.7,134000,"https://cdn0.fahasa.com/media/catalog/product/t/h/th_c-_n-_n-d_m-ki_u-nh_t---b_a-1_1.jpg",""),
    (38,"Dạy Con Dùng Tiền","Nuôi dạy con","Phát triển kỹ năng - Trí tuệ cho trẻ","","Adam Khoo, Keon Chee","NXB Trẻ","2022-07-25",0,9,63750,"https://cdn0.fahasa.com/media/flashmagazine/images/page_images/day_con_dung_tien_tai_ban_2019/2021_06_08_16_20_22_1-390x510.jpg",""),
    # Thêm thêm 18 dòng dữ liệu khác...
]

# Câu lệnh SQL để chèn dữ liệu
insert_sql = "INSERT INTO Book (Book_ID,Book_Name,Book_Category,Book_Subcategory,Book_Genre,Author,Publisher,Date_Published,Age_Range,Rating,Price,Picture,Description) VALUES (?, ?, ?, ?,?,?,?,?,?,?,?,?,?)"

# Chèn dữ liệu vào bảng
for book in books_data:
    cursor.execute(insert_sql, book)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()