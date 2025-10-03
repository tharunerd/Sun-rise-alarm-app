import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

import requests
from datetime import datetime, timedelta, timezone
import time
import threading

class AlarmApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.info_label = Label(text="Press the button to set alarm before sunrise")
        self.layout.add_widget(self.info_label)
        self.button = Button(text="Set Sunrise Alarm")
        self.button.bind(on_press=self.set_alarm)
        self.layout.add_widget(self.button)
        return self.layout

    def get_sunrise_time(self, lat, lng):
        url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0"
        res = requests.get(url, verify=False).json()
        sunrise_utc = res['results']['sunrise']
        return datetime.fromisoformat(sunrise_utc)

    def wait_and_ring(self, alarm_time):
        while datetime.now(timezone.utc) < alarm_time:
            time.sleep(10)
        self.info_label.text = "⏰ It's time to RISE BEFORE THE SUN!"
        sound = SoundLoader.load("alarm.mp3")
        if sound:
            sound.play()
        else:
            self.info_label.text += "\n(Alarm sound not found or failed to play)"

    def set_alarm(self, instance):
        latitude = 28.4595  # Gurgaon
        longitude = 77.0266
        sunrise = self.get_sunrise_time(latitude, longitude)
        alarm_time = sunrise - timedelta(minutes=30)
        self.info_label.text = f"Sunrise at {sunrise.strftime('%H:%M:%S')}\nAlarm set for {alarm_time.strftime('%H:%M:%S')}"
        threading.Thread(target=self.wait_and_ring, args=(alarm_time,), daemon=True).start()

if __name__ == '__main__':
    print("Starting Alarm App...")
    AlarmApp().run()


