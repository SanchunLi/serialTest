# coding=UTF-8

import sys
import time
import math
import string
import serial
# import queue
import threading
from PyQt4 import QtCore, QtGui, uic

# import wx
# from wx.lib.pubsub import Publisher

qtCreatorFile = "mainwindow.ui" # Enter file here. #导入第三方界面文件
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# 以下6个信号量用于发送线程和接受线程通信
ev1 = threading.Event()
ev2 = threading.Event()
ev3 = threading.Event()
ev4 = threading.Event()
ev5 = threading.Event()
ev6 = threading.Event()
class Send(threading.Thread):
	def __init__(self, signal, port, data1,data2,data3, interval, sendLabel1,sendLabel2,sendLabel3):
	    threading.Thread.__init__(self)  #You must call
	    self.signal = signal
	    self.port = port
	    self.data1 = data1
	    self.data2 = data2
	    self.data3 = data3
	    self.interval = interval
	    self.sendLabel1 = sendLabel1
	    self.sendLabel2 = sendLabel2
	    self.sendLabel3 = sendLabel3
	    self.sendCnt1 = 0
	    self.sendCnt2 = 0
	    self.sendCnt3 = 0

	    self.daemon = True # When the main thread exits the sub-thread to quit
	    self.start()       #start the thread
	def run(self):
		print(self.port)

		#以下是要发送的三个命令和时间间隔
		data1 = str(self.data1) #Qstring is changed to string
		#Qstring是啥？？？？

		data2 = str(self.data2)
		data3 = str(self.data3)
		interval = self.interval
		# self.sendLabel1.setText('0')

		# if interval1 != '':
		# 	interval1num = float (interval1txt)
		# 	interval1 = round (interval1num)
		# else:
		# 	interval1 =
		# if interval2txt != '':
		# 	interval2num = float (interval2txt)
		# 	interval2 = round (interval2num)
		# if interval3txt != '':
		# 	interval3num = float (interval3txt)
		# 	interval3 = round (interval3num)

		while 1:
			# print('send thread: ' + str(self.signal.isSet()))
			if self.signal.isSet():
				break
			# print("send ...")

			while 1:
				# 发送命令1
				ev4.set()
				ev1.set()
				if (data1 != ''):
					# ev4.set()

					# print((round(float(interval1))))
					self.port.write(data1.encode(encoding = "utf-8"))
					self.port.write(b'\x0D\x0A')
					self.sendCnt1 += 1
					# ev4.clear()
					self.sendLabel1.setText(str(self.sendCnt1))
				time.sleep(int(interval))
				ev1.clear()
				ev5.set()


				#发送命令2
				ev2.set()
				if (data2 != ''):
					# ev5.set()

					self.port.write(data2.encode(encoding = "utf-8"))
					self.port.write(b'\x0D\x0A')
					self.sendCnt2 += 1
					# ev4.clear()
					self.sendLabel2.setText(str(self.sendCnt2))
				time.sleep(int(interval))
				ev2.clear()
				ev6.set()

				#发送命令3
				ev3.set()
				if (data3 != ''):
					# ev6.set()

					self.port.write(data3.encode(encoding = "utf-8"))
					self.port.write(b'\x0D\x0A')
					self.sendCnt3 += 1
					# ev4.clear()
					self.sendLabel3.setText(str(self.sendCnt3))
				time.sleep(int(interval))
				ev3.clear()
				# ev4.set()



				if self.signal.isSet():
					break



		print("send thread exit.")
		# self.exiting = True
		# self.wait()

class Recv(threading.Thread):
	def __init__(self,signal, port, recv1Label, recv2Label, recv3Label):
	    threading.Thread.__init__(self) # You must call
	    self.signal = signal
	    self.port = port
	    self.recv1Label = recv1Label
	    self.recv1Cnt = 0
	    self.recv2Label = recv2Label
	    self.recv2Cnt = 0
	    self.recv3Label = recv3Label
	    self.recv3Cnt = 0
	    # self.sendcount1 = sendcount1
	    # self.sendcount2 = sendcount2
	    # self.sendcount3 = sendcount3
	    # self.sendCnt1 = sendCnt1
	    # self.recvData = queue.Queue()

	    self.laststate = 0x00   # 用于记录上一次状态（u8Mode）,,,,,

	    self.daemon = True # When the main thread exits the sub-thread to quit
	    self.start()    # start the thread
	def run(self):
		print(self.port)
		while 1:
			# print('recv thread: ' + str(self.signal.isSet()))
			# if self.signal.isSet():
			# 	self.recv1Cnt = 0
			# 	self.recv1Label.setText(str(self.recv1Cnt))
			# 	self.recv2Cnt = 0
			# 	self.recv2Label.setText(str(self.recv2Cnt))
			# 	self.recv3Cnt = 0
			# 	self.recv3Label.setText(str(self.recv3Cnt))
			# 	break
			# print("listen ...")
			if self.signal.isSet():
				break
			# if ev4.isSet():
			# 	self.laststate = ''

			# 这段因为遥测信息（小卫星发来的）格式变了，可以看我给你转发的邮件
			# 找到u8Mode
			datatemp = self.port.readline()
			# print 'Read:'+datatemp
			if "YaoCe" in datatemp:
				data = datatemp.strip().split(',')
				# print data
				# data = []
				u8Modetemp = data[len(data) - 3]  # 倒数第三个数据
				# print 'U8Modetmp:'+u8Modetemp
				u8Mode = int(u8Modetemp,16)  #这个具体是啥意思？？？？
				# print 'u8Mode:'+str(u8Mode)
			# data = self.port.read(1)
			# if data == b'\x05':
				# data = self.port.read(1)
				# if data == b'\x0A':
				# 	u8Type = self.port.read(1)
				# 	u8Len = self.port.read(1)
				# 	u8Mode = self.port.read(1)
				# 	u8ExpTime1 = self.port.read(1)
				# 	u8ExpTime2 = self.port.read(1)
				# 	u8ExpTime3 = self.port.read(1)
				# 	u8checkSum = ord(self.port.read(1))
				# 	# check
				# 	realSumtmp = ord(u8Type) + ord(u8Len) + ord(u8Mode) +ord(u8ExpTime1) + ord(u8ExpTime2) + ord(u8ExpTime3)

				#这个ord啥意思？？？

				# 	realSum = realSumtmp % 256
				# 	print 'Sum: ' + str(realSum)
				# 	print 'Check: ' + str(u8checkSum)
				# 	if realSum == u8checkSum:

				# 		# print( 'check succeed: ' + str(u8Mode))

				if (u8Mode & 0x30) == 0x10:  # 检查是否是对命令1的反馈
				# if (ord(u8Mode) & 0x30) == 0x10:
				# if (u8Mode & b'\x30') == b'\x10':
				# if u8Mode== b'\x10':
					# if self.sendCnt1.currentText() >= self.recv1Cnt:  #Another type of method calls in a class variable, not ready yet how to achieve, also need to debug conditions here,
					# if  self.recv1Cnt < 1:
					# send = Send()
					# send.run(self)
					# if  MyApp.sendCnt1.Label() >= self.recv1Cnt:
					# if 10 >= self.recv1Cnt:
					# if sendcount1 >= self.recv1Cnt:
					if ev4.isSet():
						self.laststate = 0x00    #laststate的作用：发送命令间隔较大，而反馈信息以很小的间隔循环发送（见小卫星），而我们要求只加接计数器1次
						ev4.clear()
					# print 'pre:'+str(self.laststate)

					# 只有此时状态和上一个状态不同才会计数加1
					if (self.laststate != 0x10) and (self.laststate != 0x20) and (self.laststate != 0x30) and (ev1.isSet()):
					# if (self.laststate != b'\x10'):
						self.recv1Cnt += 1
						self.recv1Label.setText(str(self.recv1Cnt))
				if (u8Mode & 0x30) == 0x20:  # 检查是否是对命令2的反馈
				# elif u8Mode == b'\x20':
					# if Send.sendCnt1 >= self.recv2Cnt:
					# if  sendcount2 >= self.recv2Cnt:
					if ev5.isSet():
						self.laststate = 0x00
						ev5.clear()
					if (self.laststate != 0x20) and (self.laststate != 0x10) and (self.laststate != 0x30)  and (ev2.isSet()):
					# if (self.laststate != b'\x20'):
						self.recv2Cnt += 1
						self.recv2Label.setText(str(self.recv2Cnt))
				if (u8Mode & 0x30) == 0x30:  # 检查是否是对命令3的反馈
				# elif u8Mode == b'\x30':
					# if  sendcount3 >= self.recv3Cnt:
					# if Send.sendCnt2 >= self.recv3Cnt:
					if ev6.isSet():
						self.laststate = 0x00
						ev6.clear()
					if (self.laststate != 0x30) and (self.laststate != 0x10) and (self.laststate != 0x20)  and (ev3.isSet()):
					# if (self.laststate != b'\x30'):
						self.recv3Cnt += 1
						self.recv3Label.setText(str(self.recv3Cnt))
				self.laststate = u8Mode  #很重要！！！
				# self.laststate = u8Modetemp
				# print str(u8Mode)
				# print 'final:'+str(self.laststate)
				# ev4.clear()
		# self.recv1Cnt.clear()
		# self.recv1Label.setText.clear()

		print("recv thread exit.")
		self.exiting = True

# sendThread = Send()
# recvThread = Recv()
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	# global  sendcount1,sendcount2,sendcount3
	# sendcount1 = 0
	# sendcount2 = 0
	# sendcount3 = 0
	# global sendCnt1,sendCnt2,sendCnt3
	signal = threading.Event()  # 设置信号量，主线程和2个子线程通信

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.cmd1bt.clicked.connect(self.cmd1bt_func) # 按钮send连接到函数cmd1bt_func

	def cmd1bt_func(self):

		#按下发送按钮（在这之前，在界面设置好该填写的选项，如波特率，端口等）
		if self.cmd1bt.isChecked():
			print("cmd1 pressed")
			self.cmd1bt.setText('stop') #按钮“send”变成“stop”

			# 初始时，所有计数器都为0，（或者stop后再一次发送时需清零计数器）
			self.sendCnt1.setText('0')
			self.sendCnt2.setText('0')
			self.sendCnt3.setText('0')
			self.recvCnt1.setText('0')
			self.recvCnt2.setText('0')
			self.recvCnt3.setText('0')

			#从界面读取数据
			portID = self.comPortID.currentText()
			baudrate = self.baudrateLabel.currentText()

			# 这些都被设定好了不能下拉选择，也可以设成可下拉，如下注释部分
			bytesize = serial.EIGHTBITS   #8bit
			parity = serial.PARITY_NONE   #奇偶校验（无）
			stopbits= serial.STOPBITS_TWO #停止位2位(第2位也就是起始位，，，好像是这么说的)

			# bytesizetmp= self.bytesizeLabel.currentText()
			# print('gui: ' + bytesizetmp)
			# if bytesizetmp == '8':
			# 	bytesize = serial.EIGHTBITS
			# elif bytesizetmp == '7':
			# 	bytesize = serial.SEVENBITS
			# elif bytesizetmp == '6':
			# 	bytesize = serial.SIXBITS
			# elif bytesizetmp == '5':
			# 	bytesize = serial.FIVEBITS

			# paritytmp = self.parity.currentText()
			# if paritytmp == 'NONE':
			# 	parity = serial.PARITY_NONE
			# elif paritytmp == 'EVEN':
			# 	parity = serial.PARITY_EVEN
			# elif paritytmp == 'ODD':
			# 	parity = serial.PARITY_ODD
			# elif paritytmp == 'MARK':
			# 	parity = serial.PARITY_MARK
			# elif paritytmp == 'SPACE':
			# 	parity = serial.PARITY_SPACE
			# print(parity)

			# stopbitstmp = self.stopbitssize.currentText()
			# if stopbitstmp == '1':
			# 	stopbits= serial.STOPBITS_ONE
			# elif stopbitstmp == '1.5':
			# 	stopbits = serial.STOPBITS_ONE_POINT_FIVE
			# elif stopbitstmp == '2':
			# 	stopbits = serial.STOPBITS_TWO
			# print(stopbits)

			#self.comPort = serial.Serial(portID,baudrate = baudrate1,bytesize = bytesize1,parity = parity1,stopbits = stopbits1,timeout = 0.1,xonxoff) # open
			self.comPort = serial.Serial(str(portID),baudrate,bytesize,parity,stopbits,timeout = 0.1) # open 开启串口

			# 从界面读入数据
			data1 = self.cmd1label.toPlainText()
			interval = self.interval.toPlainText()
			data2 = self.cmd2label.toPlainText()
			data3 = self.cmd3label.toPlainText()

			# print('data2:' + str(data2))


			self.signal.clear()   # （使用前）对信号量清零
			# self.recvData. TODO



			# self.sendThread1= Send(self.signal, self.comPort, data1, interval1, self.sendCnt1)
			# self.sendThread1.daemon = True # When the main thread exits the sub-thread to quit
			# self.sendThread1.start()

			# self.sendThread2= Send(self.signal, self.comPort, data2, interval2, self.sendCnt2)
			# self.sendThread2.daemon = True # When the main thread exits the sub-thread to quit
			# self.sendThread2.start()

			# self.sendThread3= Send(self.signal, self.comPort, data3, interval3, self.sendCnt3)
			# self.sendThread3.daemon = True # When the main thread exits the sub-thread to quit
			# self.sendThread3.start()

			#self.sendThread= Send(self.signal, self.comPort, data1, data2, data3, interval1, interval2, interval3, self.sendCnt1, self.sendCnt2, self.sendCnt3)
			# self.thread.render(self.signal, self.comPort, data1, data2, data3, interval,self.sendCnt1, self.sendCnt2, self.sendCnt3)

			# 调用发送线程 （调用线程和创建线程？？？查一查）
			Send(self.signal, self.comPort, data1, data2, data3, interval,self.sendCnt1, self.sendCnt2, self.sendCnt3)
			# Send.sendThread = Send(self.signal, self.comPort, data1, data2, data3, interval,self.sendCnt1, self.sendCnt2, self.sendCnt3)

			# self.sendThread.daemon = True # When the main thread exits the sub-thread to quit
			# self.sendThread.start()
			# self.thread.render(self.signal, self.comPort, self.recvCnt1, self.recvCnt2, self.recvCnt3)

			# 调用接收线程
			Recv(self.signal, self.comPort, self.recvCnt1, self.recvCnt2, self.recvCnt3)
			# Send.recvThread = Recv(self.signal, self.comPort, self.recvCnt1, self.recvCnt2, self.recvCnt3)
			# self.recvThread.daemon = True # When the main thread exits the sub-thread to quit
			# self.recvThread.start()
		else:
			print("cmd1 released")         # 停止发送命令
			# self.recvCnt1.setText('0')
			# self.recvCnt1.setText('0')
			# self.recvCnt2.setText('0')
			# self.recvCnt3.setText('0')
			# self.recv1Label.setText('0')
			# self.recv2Label.setText('0')
			# self.recv3Label.setText('0')

			self.signal.set()     # 设置信号量，这会使得发送线程和接收线程结束
			self.cmd1bt.setText('send')

			print('main: ' + str(self.signal.isSet()))
			# self.sendThread1.join() # wait thread exit
			# self.sendThread2.join()
			# self.sendThread3.join()
			# Send.join()
			# Recv.join()
			# sendThread = Send()
			# recvThread = Recv()

			# self.sendThread.join()
			# self.recvThread.join()

			self.comPort.close() # close  关闭串口

	# 以下2个函数没有用
	def cmd2bt_func(self):
		print("cmd2 pushed")
	def cmd3bt_func(self):
		print("cmd3 pushed")


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
window.show()
sys.exit(app.exec_())
