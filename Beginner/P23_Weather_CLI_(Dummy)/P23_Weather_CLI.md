# ☁️ Dummy Weather Report

This Python program generates a **dummy weather report** for any city you enter.  
It is a fun simulation and **does not fetch real-world weather data**.

---

## 📌 Features
- Enter a city name to get a random weather report.
- Displays:
  - Weather condition (Sunny, Rainy, Cloudy, Stormy, Snowy)
  - Temperature (°C)
  - Humidity (%)
  - Emoji representing the condition
- Exit the program anytime by typing `exit`.
- Includes a warning message that this is **not real data**.

---

## ⚙️ How It Works
1. The user enters a city name.
2. The program randomly selects:
   - A weather condition
   - A temperature between -5°C and 49°C
   - Humidity between 20% and 95%
3. Prints the weather report with an emoji.
4. Displays a **warning message** clarifying that this is for learning purposes.
5. Repeats until the user types `exit`.

---

## ▶️ Example Usage

```yml
---------------------
Weather Information
---------------------
Enter 'exit' to quit the program or City Name to check weather: kanpur
Weather Report For:  kanpur
Condition: Stormy🍃
Temprature: 13°C
Humidity: 69%
-------------------------------------------------------------------------
this program is just for understanding doesn't fetch real world reports
-------------------------------------------------------------------------
```
If exit:
```yml
Enter 'exit' to quit the program or City Name to check weather: exit
--------------------------
Thanks for using program
--------------------------
```

## 🚀 How to Run
1. Save the script as `dummy_weather.py`.
2. Run using Python:
   ```bash
   python dummy_weather.py
3. nter a city name to get a random weather report or type `exit` to quit.

## ⚠️ Note

- This program does not connect to any real weather API.

- All data (condition, temperature, humidity) is randomly generated.

- The warning message reminds users that this is for learning and understanding only.

## 💡 Future Improvements

- Integrate real-world weather API (e.g., OpenWeatherMap) for live reports.

- Add forecast for multiple days.

- Allow user to choose temperature units (Celsius/Fahrenheit).


## Author
Made with ❤️ by Pratyaksh Yadav