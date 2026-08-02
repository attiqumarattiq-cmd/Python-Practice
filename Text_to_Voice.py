import pyttsx3

# Re-initialize the engine
engine = pyttsx3.init()

# Stop any previous hanging processes
engine.stop()

# Force speed rate adjustment to trigger SAPI5 reload
engine.setProperty('rate', 175)

# Speak
engine.say("Sound check Sound check !! Hello Hello ")
engine.runAndWait()