# Welcome to PyShine
# This is part 12 of the PyQt5 learning series
# Start and Stop Qthreads
# Source code available: www.pyshine.com
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5 import uic
import sys, time
import signal
import socket
import numpy as np
from numpy import pi,cos,sin,tan
import pyqtgraph as pg
import csv
import time
#from PySide2 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QApplication, qApp
from PyQt5.QtCore import Qt
from qroundprogressbar import QRoundProgressBar
#IMPORTING THE MODULE
from PySide2extn.RoundProgressBar import roundProgressBar
global array_data


class PyShine_THREADS_APP(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('adadxyz2.ui',self)
        #gauge = 
        #self.resize(950, 800)
        icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("PyShine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.setWindowIcon(icon)

        self.thread={}
        self.array = []
        global data

        #self.win = pg.plot(title="Real-time plot")
        self.curve = self.graphicsView.plot(pen='y')
        

        

        self.start_ethenet()


    def start_ethenet(self):
        self.thread[1] = ThreadClass(parent=None,index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)
        self.pushButton1.setEnabled(False)

        # self.thread[2] = LoggingThread()
        # self.thread[2].start()
        # self.thread[2].log_signal.connect(self.log_csv)
        # #self.thread[2].join()
        

        # self.thread[3] = ChronometerThread()
        # self.thread[3].start()
        # self.thread[3].time_signal.connect(self.timer_csv)
        #self.thread[2].join()
        

    def timer_csv(self,timer):
         
        self.lcdNumber_timer_2.setProperty("value", float(timer))
    def log_csv(self,x):
         with open(namafile, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #if (array_data[0][0]!=0):
            for i in range(0,np.shape(array_data)[0]):
                #print(array_data)
                info = {
                    header1: array_data[i][0],
                    header2: array_data[i][1],
                }
                csv_writer.writerow(info)

            

    def my_function(self,phi : str,psi,d,x,y,z,timer):
         print(1)
         
        
        
        
class ChronometerThread(QtCore.QThread):
    time_signal = QtCore.pyqtSignal(int)

    def run(self):
        start_time = time.perf_counter()
        while True:
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000
            self.time_signal.emit(round(elapsed_time))
            #time.sleep(0.001)

class LoggingThread(QtCore.QThread):
    log_signal = QtCore.pyqtSignal(str)

    def run(self):
        while True:
            self.log_signal.emit("Logging every 2")
            time.sleep(2)                

           

class ThreadClass(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(str,str,str,str,str,str,str)
    
    #array_data = np.zeros((5000, 2))

    #array_data=np.empty(shape=[500, 2])

    #print(array_data)
    #array_data=[]
    #array_data=array_data.reshape(1000,2)
    #array_data = np.array(array_data)
    
    def __init__(self, parent=None,index=0):
        super(ThreadClass, self).__init__(parent)
        self.index=index
        self.is_running = True

    def run(self):
        print('Starting thread...',self.index)
        cnt=0
        UDP_IP = "127.0.0.1"  # Listen on all available network interfaces
        UDP_PORT = 5005

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.bind((UDP_IP, UDP_PORT))
        #print('ok')
        data_asly_star=['0','0','0','0']
        data_not_proceed=''

        data=0
        data2=0
        data3=0
        l__0=0.006;
        l__1=0.1820;
        # l__1=0.1760;
        l__3=0.05;
        l__5=0.1150;
        l__2=0.07;
        l__7=0.0342;
        theta=42*(pi/180);
        alpha=50*(pi/180);
        data_baghi=''
        num=0
        global array_data
        array_data = np.empty((0, 2), float)
        while (True):
            data = sock.recv(20).decode()
            #print(data)
            data_ma=str(data_baghi)+str(data)
            #print(data_ma)
            # Decode the data
            n_hashtak = data_ma.find('#')
            data_baghi=str(data_ma[n_hashtak+1:])
            data_asly_star = data_ma[0:n_hashtak].split('*')
            #print(str(data_asly_star))
            if data_asly_star[0]=='':
                del data_asly_star[0]
            #print(data_asly_star)
            if len(data_asly_star) == 4:
                data_q1=int(data_asly_star[0])
                data2_q2=int(data_asly_star[1])
                data3_q3=int(data_asly_star[2])
                data3_timer=int(data_asly_star[3])
                #data_q1, data2_q2, data3_q3,data3_timer = map(float, str(data_asly_star))
                #print(f"x={x}, y={y}, z={z}")
                
            
            
            
             
                 #print(packet)     

            #tedad_moraba=data_asly.count('#')
            #data_asly_star=[data_asly_star[0], data_asly_star[1],data_asly_star[2],data_asly_star[3]]
            #data_asly_star=[]    
            #print(data_not_proceed,type(data_not_proceed))
            
            
            #data_asly_star=data_asly_q
            # while("" in data_asly_star):
            #     data_asly_star.remove("")
                       
            #data_q1=int(data_asly_star[0])
            #data2_q2=int(data_asly_star[1])
            #data3_q3=int(data_asly_star[2])
            #data3_timer=int(data_asly_star[3])
            #print(data_q1,data2_q2,data3_q3,data3_timer)
            phi=(data_q1)*(pi/180)
            psi=(data2_q2)*(pi/180)
            d=((-data3_q3))/1000
            x=(sin(theta) * cos(psi + alpha) * d + cos(theta) * cos(phi) * sin(psi + alpha) * d + sin(theta) * (l__1 + l__3 + l__5))
            y=(sin(phi) * sin(psi + alpha) * d)
            z=(cos(theta) * cos(psi + alpha) * d - cos(phi) * sin(theta) * sin(psi + alpha) * d + cos(theta) * (l__1 + l__3 + l__5))
            # array_values = [phi, psi]
            # array_values = np.array(array_values)
            #self.array.append(array_values)
            array_values = np.array([phi, psi]).reshape(1, 2)  # create a new row to append
            array_data = np.append(array_data, array_values, axis=0) 
            if(num<500):
                #array_data=np.append(array_values)
                array_data = np.append(array_data, array_values, axis=0)
                num=num+1
                #print(array_data) 
            else:
                      
                array_data[:-1] = array_data[1:]
                array_data[-1] = array_values
                #print(array_data)
            
            self.any_signal.emit(str(phi),str(psi),str(d),str(x),str(y),str(z),str(data3_timer)) 

    def stop(self):
        self.is_running = False
        print('Stopping thread...',self.index)
        self.terminate()

app = QtWidgets.QApplication(sys.argv)
#start_time = time.time()
namafile = 'data1D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"
header4 = "phi_value"
header5 = "psi_value"
header6 = "d_value"
header7 = "counter"
header8 = "Time"


fieldnames = [header1, header2, header3, header4, header5, header6,header7,header8]
with open(namafile, 'w') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
mainWindow = PyShine_THREADS_APP()
#array=[1000]
mainWindow.show()
sys.exit(app.exec_())

