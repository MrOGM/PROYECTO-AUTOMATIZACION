import serial
import time
from icecream import ic

# Initialize serial communication
arduino = serial.Serial(
    "COM7", 9600, timeout=1
)  # Adjust 'COM3' for Windows or '/dev/ttyUSB0' for Linux/Mac


def send_command(command):
    """
    Sends a command to the Arduino via serial.
    """
    try:

        if command in ["R", "G", "B"]:
            arduino.write(command.encode())  # Encode the string to bytes
            time.sleep(0.5)

        while arduino.in_waiting > 0:  # Check if there's data to read
            response = arduino.readline().decode("utf-8").strip()
            print("Arduino says:", response)
    except Exception as e:
        print(f"Error sending command: {e}")
