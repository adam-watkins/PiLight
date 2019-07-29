import serial

# 0 = LEDs OFF
# 1 = LEDs ON
# c = Change colour
# --- r = red
# --- g = green
# --- b = blue

PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

OFF = b'0'
ON = b'1'
FADE = b'9'

colours = {
    'Red': b'2',
    'Green': b'3',
    'Blue': b'4',
}

serialPort = serial.Serial(PORT, BAUD_RATE)


def on():
    serialPort.write(ON)


def off():
    serialPort.write(OFF)


def colour(c):
    serialPort.write(colours[c])


def fade():
    serialPort.write(FADE)
