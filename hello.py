import bluetooth

# Địa chỉ MAC của thiết bị Bluetooth
bd_addr = "3C:5A:B4:01:02:03"

port = 1

# Tạo kết nối
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

while True:
    # Gửi dữ liệu
    data = input("Enter data to send: ")
    sock.send(data)

    # Nhận dữ liệu
    received_data = sock.recv(1024)
    print("Received:", received_data)

# Đóng kết nối
sock.close()
