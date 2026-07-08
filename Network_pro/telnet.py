# import getpass
# import telnetlib3

# HOST = "192.168.168.139"
# user = input("Enter your remote account: ")
# password = getpass.getpass()

# tn = telnetlib3.open_connection(HOST)

# tn.read(b"login: ")
# tn.write(user.encode('ascii') + b"\n")
# if password:
#     tn.read(b"Password: ")
#     tn.write(password.encode('ascii') + b"\n")

# tn.write(b"ls\n")
# tn.write(b"exit\n")

# print(tn.read_all().decode('ascii'))
import asyncio
import telnetlib3

async def telnet_client():
    HOST = "192.168.168.139"  # IP ของ Ubuntu ใน VMware ของคุณ
    
    print(f"Connecting to {HOST}...")
    
    # เชื่อมต่อไปยังเซิร์ฟเวอร์ (เปิดด่านอ่านและเขียนข้อมูล)
    try:
        reader, writer = await telnetlib3.open_connection(HOST, 23)
        
        # อ่านข้อความแรกที่เซิร์ฟเวอร์ส่งมา (เช่น หน้า Login)
        output = await reader.read(1024)
        print(output)
        
        # --- ถ้าต้องการส่งคำสั่งพิมพ์ตามนี้ ---
        # writer.write("username\n")
        # await writer.drain() # บังคับให้ส่งข้อมูลออกไปทันที
        
        # ปิดการเชื่อมต่อเมื่อเสร็จสิ้น
        writer.close()
        print("Connection closed.")
        
    except Exception as err:
        print(f"Connect failed: {err}")

# สั่งให้โปรแกรม Asyncio เริ่มทำงาน
asyncio.run(telnet_client())