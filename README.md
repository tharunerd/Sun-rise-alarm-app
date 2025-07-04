# 🌅 Rise Before the Sun Alarm

> **"Don't wake up and watch the sunrise — let the sun watch you rise."**

A simple Python app that fetches the **daily sunrise time** for your location and rings an alarm **30 minutes before** sunrise. Start your day early, every day!

---
This Python project fetches the **daily sunrise time** for your location and rings an alarm **30 minutes before**, helping you start your day early with discipline and purpose.

## 🚀 Features

- Fetches real-time sunrise time using the Sunrise-Sunset API
- Automatically sets an alarm 30 minutes before sunrise
- Plays a customizable alarm sound
- Works on PC, Raspberry Pi, and can be packaged for Android (with Kivy)

---

## 🛠️ Setup

### 1. **Install Dependencies**
```bash
pip install kivy requests
```

### 2. **Add Alarm Sound**
Place your alarm sound file as `alarm.mp3` in the project folder.

### 3. **Run the App**
```bash
python main.py
```

---

## ⚙️ Automation (Optional)

- **Windows:** Use Task Scheduler to run the script daily at a set time.
- **Linux:** Add a cron job, for example:
  ```
  0 3 * * * /usr/bin/python3 /path/to/main.py
  ```

---

## 🌍 Location Settings

- **Default:** Gurgaon (Lat: 28.4595, Lon: 77.0266)
- **To change:** Edit the latitude and longitude in `main.py`.

---

## 📱 Android Support

You can package this app for Android using [Kivy](https://kivy.org/) and [Buildozer](https://github.com/kivy/buildozer).  
See the [Kivy documentation](https://kivy.org/doc/stable/guide/packaging-android.html) for details.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Feel free to open an issue for bugs or feature requests.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

Made with ❤️ by Tharun Kumar Akula
#   S u n - r i s e - a l a r m - a p p 
 
 
