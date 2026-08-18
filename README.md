# ⏰ Smart Alarm Clock

A simple **Smart Alarm Clock** built with Python and Streamlit. The application allows users to set an alarm, select an alarm tone, snooze the alarm, cancel it, and stop the alarm when it rings.

## 📌 Project Overview

The Smart Alarm Clock provides a graphical web interface for setting and managing alarms. It uses Python's `datetime`, `threading`, and `winsound` modules along with Streamlit.

The application displays the current time in **12-hour format with AM/PM** and allows the user to select an alarm time.

## ✨ Features

- ⏰ Displays the current time
- 🔔 Set an alarm using hour, minute, and AM/PM
- 🎵 Choose from multiple alarm tones
- 😴 Snooze the alarm for 1–60 minutes
- ❌ Cancel a scheduled alarm
- 🛑 Stop a ringing alarm
- 🚨 Displays an alarm notification when the selected time is reached
- 🔊 Plays the alarm sound in a background thread
- 🔄 Automatically refreshes the application every second
- 📅 Automatically schedules a passed time for the next day

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit**
- **datetime**
- **time**
- **threading**
- **winsound**

## 📂 Project Structure

```text
Smart-Alarm-Clock/
│
├── alarm.py
└── README.md
```

> Rename the Python file containing the provided code to `alarm.py` if you want to use the commands below exactly.

## ⚙️ Requirements

This project is designed for **Windows**, because it uses Python's `winsound` module for generating alarm sounds.

Install Streamlit using:

```bash
pip install streamlit
```

Python's `datetime`, `time`, and `threading` modules are part of the Python standard library and do not need separate installation.

## ▶️ How to Run

1. Open **VS Code** or Command Prompt.
2. Navigate to the folder containing the Python file.

Example:

```bash
cd "C:\Users\YourName\Documents\Smart-Alarm-Clock"
```

3. Run the Streamlit application:

```bash
streamlit run alarm.py
```

4. Streamlit will display a local web address, normally similar to:

```text
http://localhost:8501
```

5. Open that address in your browser.

## 🕐 How to Use

### 1. Set the Alarm

Select:

- Hour
- Minute
- AM/PM
- Alarm tone
- Snooze duration

Then click **🔔 Set Alarm**.

### 2. Wait for the Alarm

The application continuously checks the current time. When the alarm time is reached, the application displays:

**🚨 WAKE UP! ALARM IS RINGING! 🚨**

and plays the selected sound.

### 3. Snooze

Click **😴 Snooze** to postpone the alarm by the selected number of minutes.

### 4. Stop

Click **🛑 Stop Alarm** to stop and clear the active alarm.

### 5. Cancel

Click **❌ Cancel Alarm** before the alarm rings to cancel the scheduled alarm.

## 🎵 Available Alarm Tones

| Tone | Description |
|---|---|
| Classic Beep | Five longer beeps |
| Soft Chime | Three softer beeps |
| Rapid Alert | A sequence of short alert beeps |

## 🧠 Main Python Components

### `datetime`

Used to obtain the current time and calculate the alarm time.

### `winsound`

Used to generate alarm sounds on Windows.

### `threading`

Used to play the alarm sound in the background so that the application can continue running.

### `st.session_state`

Streamlit session state stores information such as:

- Alarm status
- Alarm date/time
- Selected tone
- Snooze duration
- Alarm-triggered status

## 🔄 Alarm Logic

The application follows this basic flow:

```text
Start Application
       ↓
Display Current Time
       ↓
Select Alarm Settings
       ↓
Set Alarm
       ↓
Is Selected Time Passed?
   ↓              ↓
  Yes             No
   ↓              ↓
Schedule        Wait and
Tomorrow        Check Time
   ↓              ↓
   └──────→ Alarm Time Reached
                    ↓
             Play Alarm Sound
                    ↓
              ┌─────┴─────┐
              ↓           ↓
           Snooze        Stop
              ↓           ↓
        New Alarm Time   End
```

## ⚠️ Limitations

- The alarm sound uses `winsound`, so the project is intended for **Windows**.
- The Streamlit application needs to remain running for the alarm to be checked.
- Closing the browser does not necessarily stop the Streamlit process, but stopping the Python/Streamlit process will stop the alarm system.
- The current time and alarm time are handled using the computer's local system time.
- This is a local academic/project application and is not designed as a replacement for a dedicated alarm clock.

## 🚀 Possible Future Improvements

- Add custom MP3/WAV alarm sounds
- Add multiple alarms
- Add a recurring alarm option
- Add a date selector
- Add a dark/light theme switch
- Add alarm history
- Add volume control
- Add a desktop notification
- Add a mobile-friendly interface
- Add database support for saving alarms

## 👨‍💻 Project Type

**Mini Project / Python Application**

