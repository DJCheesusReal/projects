import serial

# Define serial port (replace with your actual port)
ser = serial.Serial('COM3', 9600)

while True:
  # Read data from the serial port
  data = ser.readline().decode('utf-8').strip()
  
  # Check for button press messages
  if data == "Button A pressed" or data == "Button B pressed":
    print(data)  # Print the button press message

  # You can add additional logic here to handle button presses

# Close the serial connection (optional)
ser.close()
