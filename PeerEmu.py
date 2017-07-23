# coding=UTF-8

# 在地面对小卫星进行遥控

# 这是一个模拟的小卫星，接收到遥控命令后，发送遥测信息（也即反馈信息）

import serial  # 需安装python的串口模块（串口库）
import string
import time

sp = serial.Serial('COM2')   # 使用串行端口2通信
print('listen ...')          # 方便调试的打印信息（正式版本不需要）

# data = 'aa'
# data = input("Please enter the command")

while 1:
	# 由下面可知，每0.5秒重读一次data
	data = sp.read(2)  # 读取遥控命令 2是什么？读2个ascii码？
	print(data)
	cnt = 1

	while cnt <= 10:
	# while 1:

		if data == b'aa':
			# cnt1 = 1
			# while cnt1 <= 10:
			print("recv cmd1 ok")
			# sp.write(b'\x05\x0A\x00\x00\x20\x00\x00\x00\x20')
			sp.write(b'>dykb 3')
			sp.write(b'\x0D\x0A')
			sp.write(b'dykb send 8 bytes.')
			sp.write(b'\x0D\x0A')
			sp.write(b'  (05 0A 24 03)')
			sp.write(b'\x0D\x0A')
			sp.write(b'  (14 03 03 41)')
			sp.write(b'\x0D\x0A')
			sp.write(b'>1126 YaoCe B: 0x50,0x0A,0xAA,0x04,0x20,6380,0xD2')
			sp.write(b'\x0D\x0A')
			sp.write(b'>1127 YaoCe B: 0x50,0x0A,0xAA,0x04,0x10,5931,0x00')
			#工作状态调整0x20->0x10
			sp.write(b'\x0D\x0A')
			# sp.write(b'\x05\x0A\x00\x00\x10\x00\x00\x00\x10')
			# time.sleep(0.01)
			# cnt1 += 1
		elif data == b'bb':
			# cnt2 = 1
			# while cnt2 <= 10:
			print("recv cmd2 ok")
			# sp.write(b'\x05\x0A\xAA\x04\x20\x00\x00\x00\x00')
			sp.write(b'>dykb 3')
			sp.write(b'\x0D\x0A')
			sp.write(b'dykb send 8 bytes.')
			sp.write(b'\x0D\x0A')
			sp.write(b'  (05 0A 24 03)')
			sp.write(b'\x0D\x0A')
			sp.write(b'  (14 03 03 41)')
			sp.write(b'\x0D\x0A')
			sp.write(b'>1126 YaoCe B: 0x50,0x0A,0xAA,0x04,0x10,6337,0x97')
			sp.write(b'\x0D\x0A')
			sp.write(b'>1127 YaoCe B: 0x50,0x0A,0xAA,0x04,0x20,5973,0x3A')
			sp.write(b'\x0D\x0A')
			# sp.write(b'\x05\x0A\x00\x00\x20\x00\x00\x00\x20')
			# sp.write(b'\x0D\x0A')
				# time .sleep(0.01)
				# cnt2 += 1
		elif data == b'cc':
			# cnt3 = 1
			# while cnt3 <= 10:
			print("recv cmd3 ok")
			# sp.write(b'\x05\x0A\xAA\x04\x30\x00\x00\x00\x00')
			sp.write(b'>dykb 3')
			sp.write(b'\x0D\x0A')
			sp.write(b'dykb send 8 bytes.')
			sp.write(b'\x0D\x0A')
			sp.write(b'  (05 0A 24 03)')
			sp.write(b'\x0D\x0A')
			sp.write(b'  (14 03 03 41)')
			sp.write(b'\x0D\x0A')
			sp.write(b'>1126 YaoCe B: 0x50,0x0A,0xAA,0x04,0x20,6348,0xB2')
			sp.write(b'\x0D\x0A')
			sp.write(b'>1127 YaoCe B: 0x50,0x0A,0xAA,0x04,0x30,5943,0x2C')
			sp.write(b'\x0D\x0A')
			# sp.write(b'\x05\x0A\x00\x00\x30\x00\x00\x00\x30')
			# sp.write(b'\x0D\x0A')
				# time.sleep(1)
				# cnt3 += 1
		else:
			print('error cmd')

		time.sleep(0.01)  #遥测信息周期性的循环发送，假设间隔0.05秒
		cnt += 1


sp.close()
