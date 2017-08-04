#Vol2X-Reloaded Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#Vol2X-Reloaded  comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991"

from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
import os, sys, subprocess
from subprocess import Popen 

class Press(QWidget):
    def __init__(self, parent):
        super(Press, self).__init__(parent)

#Notice that we declare parent above. QWidget will then know it has a parent somewhere.
        
#Layout            
        self.horizontal = QHBoxLayout(self)
        
#Slider#################################                
        self.slider = QSlider(self)        
    #Slider geometry & size.
        self.slider.setGeometry(QtCore.QRect(50, 20, 521, 41))
        self.slider.setMinimumSize(QtCore.QSize(321, 41))
        self.slider.setMaximumSize(QtCore.QSize(521, 41))
                
    #Orientation and ticks+intervals+slider range.
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setRange(0, 100)
        
    #Connect to function self.change when int value changes.
        self.slider.valueChanged[int].connect(self.change)
        
    #Add slider to layout. Notice that this is child window's layout.
    #Later, add the child layout to the main layout.
        self.horizontal.addWidget(self.slider)        
###########################################        
        
#Define the Lcd number indicator.

        self.lcd = QLCDNumber(self)
        self.lcd.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.lcd.setFixedSize(65, 40)
        self.lcd.setToolTip('Volume level')
        self.slider.valueChanged.connect(self.lcd.display)
        self.horizontal.addWidget(self.lcd)        

###########################################################        
#Buttons
#Layout box for buttons. Notice that we have no self here. Self belongs to first layout of this window and this is the second.
        self.vertical = QVBoxLayout() 
#Volume 0%        
        self.zero_button = QPushButton()
        self.zero_button.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.zero_button.setObjectName("Volume 0%")
        self.zero_button.setText("Volume 0%")
        self.zero_button.clicked.connect(self.zero)  
        self.vertical.addWidget(self.zero_button) #Add to vertical layout.
#Volume 50%        
        self.medium_button = QPushButton()
        self.medium_button.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.medium_button.setObjectName("Volume 50%")
        self.medium_button.setText("Volume 50%")
        self.medium_button.clicked.connect(self.mediums)  
        self.vertical.addWidget(self.medium_button) #Add to vertical layout.
#Volume 100%        
        self.high_button = QPushButton()
        self.high_button.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.high_button.setObjectName("Volume 100%")
        self.high_button.setText("Volume 100%")
        self.high_button.clicked.connect(self.highs)  
        self.vertical.addWidget(self.high_button) #Add to vertical layout.

#Open Pavucontrol button
        self.pavu_button = QPushButton()
        self.pavu_button.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.pavu_button.setObjectName("Pavucontrol")
        self.pavu_button.setText("Pavucontrol")
        self.pavu_button.clicked.connect(self.pavu)  
        self.vertical.addWidget(self.pavu_button) #Add to vertical layout.
                
        self.horizontal.addLayout(self.vertical) #Add vertical layout to horizontal layout (which has other elements there as well(slider etc.)).

######################################################                
        self.adjustSize() #This makes sure that the size is large enough for slider and others to fit in.        

#Layout to self.horizontal.
        self.setLayout(self.horizontal)

#Keypress events        
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_VolumeUp:
            self.slider.setValue(self.slider.value() + 5)
            print "Volume +5%"
        elif event.key()==Qt.Key_VolumeDown:
            self.slider.setValue(self.slider.value() - 5)
            print "Volume -5%"
        elif event.key()==Qt.Key_Escape:
            app.quit()
            print "Program ends."    
        else:
            pass  

#Click button functions.
    def zero(self,widget):
        subprocess.Popen(['pactl', 'set-sink-mute', '0', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '1', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '2', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '3', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '4', '1'])
        self.slider.setValue(self.slider.value() - 100)
        self.slider.setValue(self.slider.value() + 0)
    
    def highs(self,widget):
        subprocess.Popen(['pactl', 'set-sink-volume', '0', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '1', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '2', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '3', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '4', '100%'])
        subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
        self.slider.setValue(self.slider.value() - 100)
        self.slider.setValue(self.slider.value() + 100)
            
    def mediums(self,widget):
        subprocess.Popen(['pactl', 'set-sink-volume', '0', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '1', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '2', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '3', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '4', '50%'])
        subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
        self.slider.setValue(self.slider.value() - 100)
        self.slider.setValue(self.slider.value() + 50)
#########################################################

#Pavucontrol function
    def pavu(self,widget):
        subprocess.Popen(['pavucontrol'])
 
#Volume changing 
    def change(self,value):
        if value == 0:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '0%'])
            
        elif value == 1:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 2:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 3:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 4:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 5:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 6:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '6' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 7:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 8:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 9:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 10:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 11:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 12:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 13:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 14:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 15:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '15%'])	
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 16:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 17:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            	
        elif value == 18:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 19:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 20:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 21:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 22:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 23:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 24:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 25:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 26:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 27:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 28:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 29:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 30:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 31:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 32:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 33:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 34:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 35:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 36:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 37:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 38:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 39:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 40:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 41:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 42:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 43:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 44:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 45:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 46:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 47:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 48:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 49:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 50:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                   
        elif value == 51:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 52:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                    
        elif value == 53:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 54:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 55:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 56:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 57:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 58:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 59:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 60:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 61:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 62:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 63:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 64:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 65:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 66:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 67:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 68:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 69:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 70:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '70%'])	           
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 71:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 72:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '72%'])	
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 73:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 74:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 75:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 76:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 77:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 78:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 79:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 80:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 81:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 82:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 83:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 84:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 85:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 86:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '86%'])    
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 87:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                    
        elif value == 88:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 89:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                            
        elif value == 90:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 91:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 92:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 93:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '93%'])    
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 94:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                                                      
        elif value == 95:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 96:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 97:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 98:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 99:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 100:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])  

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
#Notice that QMainWindow is parent of QWidget. This is a bit implicit but that 
#is how it goes by default. MainWindow is the parent of QWidget - since MainWindow is the main thing here
#and it does not declare (parent) in __init__.

#Set MainWindow Size attributes.		
        self.setMinimumSize(QtCore.QSize(521, 110))
        self.setMaximumSize(QtCore.QSize(521, 110))
        		
#Set window title and move the window to the center of screen. Set window style.		
        self.setWindowTitle("Vol2X-Reloaded")
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setStyleSheet("color:#ffffff; background-color:#6b6b6b; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
                        
#Main layout & Child Window declarations.
        self.mainLayout = QHBoxLayout(self)
                
        self.childWindow = Press(self)
        self.setCentralWidget(self.childWindow) #Set slider's window(childWindow) as a central widget.

#Add childWindow to mainLayout  
        self.mainLayout.addWidget(self.childWindow)
    
#Set focus to childWindow.
        self.childWindow.setFocus(True)

        self.adjustSize() #This makes sure that the size is large enough for slider and others to fit in.
        #Technically, we do not need another self.adjustSize here. However, it is sometimes good to make
        #sure that everything works as it should.
        
#This window's layout is mainLayout.            
        self.setLayout(self.mainLayout)    

#Think layouts as boxes. We have boxes in in our childWindow. The boxes have all our objects
#packed into them. In our main window we have another box, which has our child window's boxes in it. 
               
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec_())
