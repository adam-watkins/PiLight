import serial

# 0 = LEDs OFF
# 1 = LEDs ON
# c = Change colour
# --- r = red
# --- g = green
# --- b = blue

PORT = '/dev/ttyACM0'
BAUD_RATE = 9600
DEBUG = True

OFF = b'0'
ON = b'1'
FADE = b'9'

colours = {
    'Red': b'2',
    'Green': b'3',
    'Blue': b'4',
}

if not DEBUG:
    serialPort = serial.Serial(PORT, BAUD_RATE)


def on():
    if DEBUG:
        print("On")
    else:
        serialPort.write(ON)


def off():
    if DEBUG:
        print("Off")
    else:
        serialPort.write(OFF)


def colour(c):
    if DEBUG:
        print(c)
    else:
        serialPort.write(colours[c])


def fade():
    if DEBUG:
        print("Fade")
    else:
        serialPort.write(FADE)
