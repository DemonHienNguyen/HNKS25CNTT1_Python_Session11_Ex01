""" 
    Phân tích lỗi:
        + tuple: product_info ban đầu có 4 phần tử
        + Phần tử SP001 nằm ở vị trí index 0
        + dòng này lỗi vì lấy sai mã sản phẩm: 
            product_code = product_info[1]
            => Vì đã lấy nhầm vị trí của tên sản phẩm thay vì là mã sản phẩm
        + "Áo polo nam" đang nằm ở index 1
        + Dòng này lỗi:
            product_name = product_info[2]
            => Vì đã lấy nhầm vị trí của kích cỡ của áo đó thay vì là tên của sản phẩm
        + 
        Vì dòng lấy lỗi:
            + product_length = product_info.length()
            => Vì dòng này chỉ lấy theo phương thức len()
            + chứ không phải là length() trong Js
        + Muốn đến số phân tử trong tuple ta cần dùng hàm len()
        + Dòng này lỗi 
            product_info[3] = 279000
            => Vì tuple có tính bất biến nên không được sửa trực tiếp phần tử
            => Cần được cập nhập giá bán ta sẽ tạo biến mới và cập nhập lại
        SỬA LỖI
"""

# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
product_code = product_info[0]

# Lấy tên sản phẩm
product_name = product_info[1]

product_size = product_info[2]
# Đếm số lượng thông tin sản phẩm
product_length = len(product_info)

# Cập nhật giá bán
product_new_money = 279000

new_product_info = (product_code, product_name, product_size, product_new_money)

print("Mã sản phẩm:", new_product_info[0])
print("Tên sản phẩm:", new_product_info[1])
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", new_product_info)
