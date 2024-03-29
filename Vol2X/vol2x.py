#Vol2X-Reloaded v.2.2.0 Copyright (c) 2017 JJ Posti <techtimejourney.net>  Vol2X-Reloaded  comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991"
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
import os, sys, subprocess
from subprocess import Popen
from volChange import Volume #Volume levels from 0-100% are moved to another module. 
#Volume levels are coming in as a static method - since they have nothing to do with instancing.         
class Press(QWidget):
    def __init__(self, parent):
        super(Press, self).__init__()        
#Layouts            
        self.horizontal = QHBoxLayout(self)
#For microphone.  #Microphone volume comes in as a static method - together with volume levels.      
        self.horizontal2 = QHBoxLayout()
#No QHBoxLayout(self) on the above. Self belongs to the Main layout of this window -> to the self.horizontal. 
#Also, we do not add (self) after our widgets - because we have layouts, which show up correctly.      
#Slider 2 for microphone.        
        self.slider2 = QSlider() #For Microphone.
        self.slider2.setOrientation(QtCore.Qt.Vertical)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        self.slider2.setTickInterval(5)
        self.slider2.setRange(0, 100)
        self.slider2.setFixedSize(25, 120)
        self.slider2.setToolTip('Microphone level')       
#Slider for sound.
        self.slider = QSlider() #For Sound.          
    #Slider geometry & size.
        self.slider.setGeometry(QtCore.QRect(50, 20, 521, 41))
        self.slider.setMinimumSize(QtCore.QSize(321, 41))
        self.slider.setMaximumSize(QtCore.QSize(521, 41))                
    #Orientation and ticks+intervals+slider range+tooltip.
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setRange(0, 100)
        self.slider.setToolTip('Volume level')        
    #Connect to functions when int values change.
        self.slider.valueChanged[int].connect(Volume.levels)        
        self.slider2.valueChanged[int].connect(Volume.mic)
        
    #Add sliders to layouts. Notice that these are child window's layouts, here.
    #Later, we add the child layouts to the main layout.
        self.horizontal.addWidget(self.slider)
        self.horizontal2.addWidget(self.slider2)        
#Define the lcd numbers and properties.
        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.lcd.setFixedSize(65, 40)
        self.lcd.setToolTip('Volume level')
        self.slider.valueChanged.connect(self.lcd.display)                       
#LCD
        self.horizontal.addWidget(self.lcd)                        
                 
#Layout box for buttons. Notice that we have no self here. Self belongs to the first layout of this window.
        self.vertical = QVBoxLayout() 
#Volume 0%        
        self.zero_button = QPushButton()
        self.zero_button.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")                
        self.zero_button.setObjectName("Volume 0%")
        self.zero_button.setText("Volume 0%")
        self.zero_button.clicked.connect(self.zero)  
        self.vertical.addWidget(self.zero_button) #Add to vertical layout.
#Volume 50%        
        self.medium_button = QPushButton()
        self.medium_button.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")                
        self.medium_button.setObjectName("Volume 50%")
        self.medium_button.setText("Volume 50%")
        self.medium_button.clicked.connect(self.mediums)  
        self.vertical.addWidget(self.medium_button) #Add to vertical layout.
#Volume 100%        
        self.high_button = QPushButton()
        self.high_button.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")        
        self.high_button.setObjectName("Volume 100%")
        self.high_button.setText("Volume 100%")
        self.high_button.clicked.connect(self.highs)  
        self.vertical.addWidget(self.high_button) #Add to vertical layout.
#Open Pavucontrol button
        self.pavu_button = QPushButton()
        self.pavu_button.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")                
        self.pavu_button.setObjectName("Pavucontrol")
        self.pavu_button.setText("Pavucontrol")
        self.pavu_button.clicked.connect(self.pavu)  
        self.vertical.addWidget(self.pavu_button) 
                
        self.horizontal.addLayout(self.vertical) #Add vertical layout to horizontal layout (which has other elements there as well(slider etc.)).
        self.horizontal.addLayout(self.horizontal2) #Add horizontral2(the microphone slider) layout to horizontal layout.

        self.adjustSize() #This makes sure that the size is large enough for slider and others to fit in.        

#Layout to self.horizontal. We declare this as our main layout - since our widgets and sliders are here.
        self.setLayout(self.horizontal)        
#Run update function
        self.update()        
#Update sound & mic levels every n seconds
    def update(self):
        #Get the initial Volume/microphone levels.
        self.initial1=subprocess.Popen(['bash', 'mixer.sh'], stdout=subprocess.PIPE) #Using Popen and piping subprocess to standard output.
        self.initial2=self.initial1.stdout.read() #Reading the standard output.
        self.initial3=int(self.initial2) #Changing to integrer.         
        self.slider.setValue(self.initial3) #Set slider value.
        self.lcd.display(self.initial3)     #Set lcd value         
#Microphone values
        self.initial4=subprocess.Popen(['bash', 'capture.sh'], stdout=subprocess.PIPE) #Using Popen and piping subprocess to standard output.
        self.initial5=self.initial4.stdout.read() #Reading the standard output.
        self.initial6=int(self.initial5) #Changing to integrer.         
        self.slider2.setValue(self.initial6) #Set slider value.		
#Keypress events        
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_VolumeUp:
            self.slider.setValue(self.slider.value() + 5)
            print ("Volume +5%")
        elif event.key()==Qt.Key_VolumeDown:
            self.slider.setValue(self.slider.value() - 5)
            print ("Volume -5%")
        elif event.key()==Qt.Key_Escape:
            app.quit()
            print ("Program ends.")    
        else:
            pass  
#Click button functions. Code is cleaned here as well - since the first version of Vol2X-Reloaded.
    def zero(self,widget):
        subprocess.Popen(['pactl', 'set-sink-mute', '0', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '1', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '2', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '3', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '4', '1'])
        self.slider.setValue(0)
            
    def highs(self,widget):
        subprocess.Popen(['pactl', 'set-sink-volume', '0', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '1', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '2', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '3', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '4', '100%'])
        self.slider.setValue(100)
            
    def mediums(self,widget):
        subprocess.Popen(['pactl', 'set-sink-volume', '0', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '1', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '2', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '3', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '4', '50%'])        
        self.slider.setValue(50)
#Pavucontrol function
    def pavu(self,widget):
        subprocess.Popen(['pavucontrol'])

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
#Notice that QMainWindow is parent of QWidget. This is a bit implicit but that 

#Set MainWindow Size attributes.		
        self.setMinimumSize(QtCore.QSize(530, 134))
        self.setMaximumSize(QtCore.QSize(530, 134))
        		
#Set window title and move the window to the center of screen. Set window style.		
        self.setWindowTitle("Vol2X-Reloaded")
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setStyleSheet("color:#ffffff; background-color:#6b6b6b; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
                        
#Main layout & Child Window declarations.
        self.mainLayout = QHBoxLayout()
                
        self.childWindow = Press(self)
        self.setCentralWidget(self.childWindow) #Set slider's window(childWindow) as a central widget.

#Add childWindow to mainLayout  
        self.mainLayout.addWidget(self.childWindow)
    
#Set focus to childWindow.
        self.childWindow.setFocus(True)
        self.adjustSize() #This makes sure that the size is large enough for slider and others to fit in.
        #Technically, we do not need another self.adjustSize here. However, it is sometimes good to make
        #sure that everything works as it should.        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec_())
