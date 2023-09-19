# 1. In ra chuỗi "Hello, world!"
print("Hello, world!")

# 2. Khai báo biến và gán giá trị
x = 5
y = 10

# 3. Thực hiện phép tính và in ra kết quả
sum_result = x + y
print("Tổng của x và y là:", sum_result)

# 4. Sử dụng vòng lặp for
for i in range(5):
    print("Giá trị của i là:", i)

# 5. Sử dụng điều kiện if-else
if x < y:
    print("x nhỏ hơn y")
else:
    print("x lớn hơn hoặc bằng y")

# 6. Định nghĩa một hàm
def multiply(a, b):
    return a * b

# 7. Gọi hàm và in ra kết quả
result = multiply(3, 4)
print("Kết quả của phép nhân là:", result)

# 8. Sử dụng danh sách (list) và vòng lặp
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Quả:", fruit)

# 9. Đọc và viết vào tệp
with open("example.txt", "w") as file:
    file.write("Đây là nội dung mẫu.")

with open("example.txt", "r") as file:
    content = file.read()
    print("Nội dung trong tệp là:", content)

# 10. Sử dụng thư viện bên ngoài (ví dụ: requests)
import requests
response = requests.get("https://www.example.com")
print("Mã trạng thái HTTP:", response.status_code)
