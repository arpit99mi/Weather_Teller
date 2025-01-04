import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel('Enter City Name : ',self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton('Get Weather',self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App Created by Arpit')

        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_weather_button.setObjectName('get_weather_button')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')

        self.setStyleSheet('''
         Qlabel,QPushButton{
                               font-size:Calibri;
                               font-weight:bold;
                               
                           }
          QLabel#city_label{
                               color:black;
                               font-size:40px;
                               font_style:italic;
                           }
         QLineEdit#city_input{
                               font-size:40px;
                           }
          QPushButton#get_weather_button{
                               font-size:30px;
                           background-color:blue;
                           font-weight:bold;
                           }
          QLabel#temperature_label{
                               color:black;
                               font-size:75px;
                           }
                           QLabel#emoji_label{
                               color:black;
                               font-size:40px;
                           }
                           Qlabel#emoji_label{
                               font-size:100px;
                               font_family:Segoe UI Emoji;
                           }
                           QLabel#description_label{
                                  font-size:40px;
                           }

                    
                    
        ''') 

        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
            
            api_key="729431ada70d64ad249c19992814ca3f"
            city=self.city_input.text()
            url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            try:
                response=requests.get(url)
                response.raise_for_status()
                data=response.json()
                if data['cod']==200:
                    self.display_weather(data)
            except Exception as e:
                print(e)
                self.display_error('City not found')
            except requests.exceptions.HTTPError as e:
                self.display_error(f"HTTP Error: {e}")
                       

            response=requests.get(url)
            data=response.json()
                 
            if data['cod']==200:
                self.display_weather(data)
            

    def display_error(self,meassage):
            pass

    def display_weather(self,data):
        self.temperature_label.setStyleSheet('color:red')
        temperature=data['main']['temp']-273.15
        self.temperature_label.setText(f"{temperature:.2f}°C")
        emoji=data['weather'][0]['main']
        self.emoji_label.setText(emoji)
        self.description_label.setText(data['weather'][0]['description'])

       

       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
                        
                             