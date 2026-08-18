import streamlit as st
import datetime
import time
import threading
import winsound


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Alarm Clock",
    page_icon="⏰",
    layout="centered"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

.clock {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    margin: 20px;
}

.alarm-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #f5f5f5;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "alarm_set" not in st.session_state:
    st.session_state.alarm_set = False

if "alarm_datetime" not in st.session_state:
    st.session_state.alarm_datetime = None

if "alarm_triggered" not in st.session_state:
    st.session_state.alarm_triggered = False

if "tone" not in st.session_state:
    st.session_state.tone = "Classic Beep"

if "snooze" not in st.session_state:
    st.session_state.snooze = 5

if "alarm_thread" not in st.session_state:
    st.session_state.alarm_thread = None


# =========================================================
# ALARM SOUND
# =========================================================

def play_alarm_sound(tone):

    try:

        if tone == "Classic Beep":

            for i in range(5):
                winsound.Beep(2000, 500)
                time.sleep(0.2)

        elif tone == "Soft Chime":

            for i in range(3):
                winsound.Beep(800, 600)
                time.sleep(0.3)

        elif tone == "Rapid Alert":

            for i in range(15):
                winsound.Beep(1500, 200)
                time.sleep(0.1)

    except Exception as e:
        print("Sound error:", e)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">⏰ Smart Alarm Clock</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Set your alarm, choose a tone, and snooze when needed.</div>',
    unsafe_allow_html=True
)


# =========================================================
# CURRENT TIME
# =========================================================

now = datetime.datetime.now()

current_time = now.strftime("%I:%M:%S %p")

st.markdown(
    f'<div class="clock">{current_time}</div>',
    unsafe_allow_html=True
)


# =========================================================
# ALARM SETTINGS
# =========================================================

st.markdown("### 🔔 Alarm Settings")

col1, col2, col3 = st.columns(3)


# ---------------------------------------------------------
# HOUR
# ---------------------------------------------------------

with col1:

    hour = st.selectbox(
        "⏰ Hour",
        list(range(1, 13)),
        index=(now.hour - 1) % 12
    )


# ---------------------------------------------------------
# MINUTE
# ---------------------------------------------------------

with col2:

    minute = st.selectbox(
        "🕐 Minute",
        list(range(0, 60)),
        index=now.minute
    )


# ---------------------------------------------------------
# AM / PM
# ---------------------------------------------------------

with col3:

    current_period = "AM" if now.hour < 12 else "PM"

    period = st.selectbox(
        "🌞 AM / PM",
        ["AM", "PM"],
        index=0 if current_period == "AM" else 1
    )


# =========================================================
# TONE
# =========================================================

tone = st.selectbox(
    "🎵 Select Alarm Tone",
    [
        "Classic Beep",
        "Soft Chime",
        "Rapid Alert"
    ]
)


# =========================================================
# SNOOZE
# =========================================================

snooze_duration = st.number_input(
    "😴 Snooze Duration (minutes)",
    min_value=1,
    max_value=60,
    value=5,
    step=1
)


# =========================================================
# DISPLAY SELECTED TIME
# =========================================================

selected_time_display = f"{hour:02d}:{minute:02d} {period}"

st.info(
    f"⏰ Selected Alarm Time: **{selected_time_display}**"
)


# =========================================================
# SET / CANCEL BUTTONS
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# SET ALARM
# =========================================================

with col1:

    if st.button(
        "🔔 Set Alarm",
        use_container_width=True
    ):

        # Convert 12-hour format to 24-hour format
        alarm_hour = hour

        if period == "AM":

            if hour == 12:
                alarm_hour = 0

        else:

            if hour != 12:
                alarm_hour = hour + 12

        # Create alarm datetime
        alarm_datetime = datetime.datetime.now().replace(
            hour=alarm_hour,
            minute=minute,
            second=0,
            microsecond=0
        )

        # If selected time already passed,
        # schedule for tomorrow
        if alarm_datetime <= datetime.datetime.now():

            alarm_datetime += datetime.timedelta(days=1)

        st.session_state.alarm_datetime = alarm_datetime
        st.session_state.alarm_set = True
        st.session_state.alarm_triggered = False
        st.session_state.tone = tone
        st.session_state.snooze = snooze_duration

        st.success(
            f"✅ Alarm set for "
            f"{alarm_datetime.strftime('%I:%M %p')}"
        )


# =========================================================
# CANCEL ALARM
# =========================================================

with col2:

    if st.button(
        "❌ Cancel Alarm",
        use_container_width=True
    ):

        st.session_state.alarm_set = False
        st.session_state.alarm_triggered = False
        st.session_state.alarm_datetime = None

        st.warning("Alarm cancelled.")


# =========================================================
# ALARM STATUS
# =========================================================

if st.session_state.alarm_set:

    st.markdown("---")

    st.markdown("### 📢 Alarm Status")

    alarm_time = st.session_state.alarm_datetime

    st.info(
        f"""
**⏰ Alarm:** {alarm_time.strftime('%I:%M %p')}

**🎵 Tone:** {st.session_state.tone}

**😴 Snooze:** {st.session_state.snooze} minutes
"""
    )


# =========================================================
# CHECK ALARM
# =========================================================

if (
    st.session_state.alarm_set
    and st.session_state.alarm_datetime is not None
):

    now = datetime.datetime.now()

    alarm_time = st.session_state.alarm_datetime

    # Check whether alarm time has arrived
    if now >= alarm_time:

        if not st.session_state.alarm_triggered:

            st.session_state.alarm_triggered = True

            # Play alarm in background
            alarm_thread = threading.Thread(
                target=play_alarm_sound,
                args=(st.session_state.tone,),
                daemon=True
            )

            alarm_thread.start()

            st.session_state.alarm_thread = alarm_thread


# =========================================================
# ALARM RINGING
# =========================================================

if st.session_state.alarm_triggered:

    st.markdown("---")

    st.error(
        "🚨🚨 WAKE UP! ALARM IS RINGING! 🚨🚨"
    )

    st.markdown(
        "### 🔊 Alarm Sound Playing..."
    )

    col1, col2 = st.columns(2)


    # =====================================================
    # SNOOZE
    # =====================================================

    with col1:

        if st.button(
            "😴 Snooze",
            use_container_width=True
        ):

            new_alarm = (
                datetime.datetime.now()
                + datetime.timedelta(
                    minutes=st.session_state.snooze
                )
            )

            st.session_state.alarm_datetime = new_alarm

            st.session_state.alarm_triggered = False

            st.success(
                f"😴 Snoozed until "
                f"{new_alarm.strftime('%I:%M:%S %p')}"
            )

            st.rerun()


    # =====================================================
    # STOP
    # =====================================================

    with col2:

        if st.button(
            "🛑 Stop Alarm",
            use_container_width=True
        ):

            st.session_state.alarm_set = False
            st.session_state.alarm_triggered = False
            st.session_state.alarm_datetime = None

            st.success(
                "✅ Alarm stopped. Have a great day! 😊"
            )

            st.rerun()


# =========================================================
# AUTOMATIC REFRESH
# =========================================================

if st.session_state.alarm_set:

    time.sleep(1)

    st.rerun()
