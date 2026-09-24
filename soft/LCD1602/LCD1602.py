# -*- coding: utf-8 -*-
import time
from smbus import SMBus

I2C = SMBus(1)

# LCD1602 LCD commands and addresses
LCD_ADDRESS = (0x7c >> 1)  # LCD I2C address
#LCD_ADDRESS = 0x27  # LCD I2C address

# LCD control command constants
LCD_CLEARDISPLAY = 0x01  # Clear display command
LCD_RETURNHOME = 0x02  # Return to home position command
LCD_ENTRYMODESET = 0x04  # Entry mode set command
LCD_DISPLAYCONTROL = 0x08  # Display control command
LCD_CURSORSHIFT = 0x10  # Cursor shift command
LCD_FUNCTIONSET = 0x20  # Function set command
LCD_SETCGRAMADDR = 0x40  # Set CGRAM address command
LCD_SETDDRAMADDR = 0x80  # Set DDRAM address command

# Flags for entry mode (text direction)
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# Flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# Flags for display and cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# Flags for function set (data length, number of lines, etc.)
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x8DOTS = 0x00


class LCD1602:
  def __init__(self, col, row):
    self._row = row
    self._col = col

    # Set the display function (4-bit mode, 1-line, 5x8 font)
    self._showfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
    self.begin(self._row,self._col)

        
  # Send command to the LCD
  def command(self, cmd):
      I2C.write_byte_data(LCD_ADDRESS,0x80,cmd)

  # Send data to the LCD
  def data(self, data):
      I2C.write_byte_data(LCD_ADDRESS,0x40,data)

  # Set the cursor position
  def setCursor(self, col, row):
      if row == 0:
          col |= 0x80  # Set address for the first row
      else:
          col |= 0xc0  # Set address for the second row
      self.command(col)

  # Clear the LCD display
  def clear(self):
      self.command(LCD_CLEARDISPLAY)  # Send clear command
      time.sleep(0.005)  # Wait for the command to execute

  # Print a string or number to the display
  def printout(self, arg):
      if isinstance(arg, int):
          arg = str(arg)  # Convert integer to string
#      for x in bytearray(arg, 'utf-8'):  # Send each character to LCD
      for x in bytearray(arg, 'iso-8859-1'):  # Send each character to LCD
          if x in ( 0xe4, 0xc4 ): # ä,Ä
              x = 0xE1
          elif x in ( 0xd6, 0xf6 ): #ö,Ö
              x= 0xef
          elif x in ( 0xdc, 0xfc ): #ü,Ü
              x = 0xf5
          elif x == 0xfd: #ß
              x = 0xe2
          self.data(x)

  # Create a custom character at a specified location
  def createChar(self, location, charmap):
      location = location & 0x7  # Ensure location is within bounds (0-7)
      self.command(LCD_SETCGRAMADDR | (location << 3))  # Set CGRAM address
      for i in range(0, 8):
          self.data(charmap[i])  # Write the character map data to CGRAM

  # Scroll the display left
  def scrollDisplayLeft(self):
      self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT)

  # Scroll the display right
  def scrollDisplayRight(self):
      self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT)

  # Turn on the underline cursor
  def cursor(self):
#      self._showcontrol |= LCD_CURSORON 
      self._showcontrol |= ( LCD_CURSORON | LCD_BLINKON )
      self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  # Turn off the underline cursor
  def nocursor(self):
      self._showcontrol &= ( ~LCD_CURSORON & ~LCD_BLINKON )
      self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  # Set text direction from left to right
  def leftToRight(self):
      self._showmode |= LCD_ENTRYLEFT
      self.command(LCD_ENTRYMODESET | self._showmode)

  # Set text direction from right to left
  def rightToLeft(self):
      self._showmode &= ~LCD_ENTRYLEFT
      self.command(LCD_ENTRYMODESET | self._showmode)

  # Enable auto-scroll
  def autoscroll(self):
      self._showmode |= LCD_ENTRYSHIFTINCREMENT
      self.command(LCD_ENTRYMODESET | self._showmode)

  # Disable auto-scroll
  def noautoscroll(self):
      self._showmode &= ~LCD_ENTRYSHIFTINCREMENT
      self.command(LCD_ENTRYMODESET | self._showmode)

  # Turn on the display
  def display(self):
      self._showcontrol |= LCD_DISPLAYON
      self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  # Initialize the LCD (send necessary commands for configuration)
  def begin(self, cols, lines):
      if lines > 1:
          self._showfunction |= LCD_2LINE  # Enable 2-line display
      self._numlines = lines
      self._currline = 0
      time.sleep(0.05)

      # Send function set command sequence
      self.command(LCD_FUNCTIONSET | self._showfunction)
      time.sleep(0.005)
      self.command(LCD_FUNCTIONSET | self._showfunction)
      time.sleep(0.005)
      self.command(LCD_FUNCTIONSET | self._showfunction)
      self.command(LCD_FUNCTIONSET | self._showfunction)

      # Turn on display with no cursor or blinking
      self._showcontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF
      self.display()

      # Clear the screen
      self.clear()

      # Set entry mode for text direction (left to right)
      self._showmode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT
      self.command(LCD_ENTRYMODESET | self._showmode)


# SN3193 Backlight control
SN3193_IIC_ADDRESS = 0x6B  # SN3193 I2C address

# SN3193 Register definitions
SHUTDOWN_REG = 0x00  # Set software shutdown mode
BREATHING_CONTROL_REG = 0x01  # Set breathing function
LED_MODE_REG = 0x02  # Set operation mode
LED_NORMAL_MODE = 0x00  # Normal mode
LED_BREATH_MODE = 0x20  # Breathing mode

CURRENT_SETTING_REG = 0x03  # Set output current
PWM_1_REG = 0x04  # 3 channels PWM duty cycle data
PWM_2_REG = 0x05  # 3 channels PWM duty cycle data
PWM_3_REG = 0x06  # 3 channels PWM duty cycle data
PWM_UPDATE_REG = 0x07  # Load PWM registers and LED control register data

T0_1_REG = 0x0A  # Set T0 time for OUT1
T0_2_REG = 0x0B  # Set T0 time for OUT2
T0_3_REG = 0x0C  # Set T0 time for OUT3

T1T2_1_REG = 0x10  # Set T1&T2 time for OUT1
T1T2_2_REG = 0x11  # Set T1&T2 time for OUT2
T1T2_3_REG = 0x12  # Set T1&T2 time for OUT3

T3T4_1_REG = 0x16  # Set T3&T4 time for OUT1
T3T4_2_REG = 0x17  # Set T3&T4 time for OUT2
T3T4_3_REG = 0x18  # Set T3&T4 time for OUT3

TIME_UPDATE_REG = 0x1C  # Load time register data
LED_CONTROL_REG = 0x1D  # Enable OUT1~OUT3
RESET_REG = 0x2F  # Reset all registers to default values

class SN3193:
    def __init__(self):
        # Initialize SN3193 with default settings
        self.write_bytes(SHUTDOWN_REG, 0x20)  # Set software shutdown mode
        self.write_bytes(LED_MODE_REG, LED_NORMAL_MODE)  # Set normal operation mode
        self.write_bytes(CURRENT_SETTING_REG, 0x00)  # Set output current to Imax=42mA
        time.sleep(0.01)
#        self.write_bytes(PWM_1_REG, 0xFF)  # Set PWM duty cycle (0x00 to 0xFF)
        self.write_bytes(PWM_1_REG, 0x50)  # Set PWM duty cycle (0x00 to 0xFF)
        time.sleep(0.1)
        self.write_bytes(PWM_UPDATE_REG, 0x00)  # Load PWM registers
        self.write_bytes(T0_1_REG, 0x40)  # Set T0 time for OUT1
        self.write_bytes(T0_2_REG, 0x40)  # Set T0 time for OUT2
        self.write_bytes(T0_3_REG, 0x40)  # Set T0 time for OUT3
        time.sleep(0.1)
        self.write_bytes(T1T2_1_REG, 0x26)  # Set T1&T2 time for OUT1   
        self.write_bytes(T1T2_2_REG, 0x26)  # Set T1&T2 time for OUT1
        self.write_bytes(T1T2_3_REG, 0x26)  # Set T1&T2 time for OUT1 
        time.sleep(0.1)
        self.write_bytes(T3T4_1_REG, 0x26)  # Set T3&T4 time for OUT2 
        self.write_bytes(T3T4_2_REG, 0x26)  # Set T3&T4 time for OUT2 
        self.write_bytes(T3T4_3_REG, 0x26)  # Set T3&T4 time for OUT3 
        time.sleep(0.1)

        self.write_bytes(LED_CONTROL_REG, 0x01)  # Enable OUT1, OUT2, and OUT3 (turn on LEDs)
        self.write_bytes(TIME_UPDATE_REG, 0x00)  # Load time register data
        time.sleep(0.1)

    # Function to write a byte to a specific register of SN3193
    def write_bytes(self, Cmd, Data):
        I2C.write_byte_data(SN3193_IIC_ADDRESS,Cmd,Data)

    # Set the brightness of the LEDs (value between 0 and 100)
    def set_brightness(self, Value):
        if Value < 0 or Value > 100:
            print("Please enter a value between 0 and 100.")
        else:
            # Convert percentage value to 8-bit scale (0x00 to 0xFF)
            self.write_bytes(PWM_1_REG, round(Value * (0xFF / 100)))
            time.sleep(0.1)
            self.write_bytes(PWM_UPDATE_REG, 0x00)  # Apply brightness update

    # Set the operation mode of the LEDs (e.g., breathing mode or steady mode)
    def set_mode(self, Mode):
        self.write_bytes(LED_MODE_REG, Mode)  # Set the operation mode
        # Mode options: 0x20 for breathing mode, 0x00 for steady mode


class PCF8574_backlight:
    def __init__(self):
        pass

    def set_brightness(self, Value):
        if Value < 0 or Value > 100:
            print("Please enter a value between 0 and 100.")
        else:
            print('set_brightness')


    def set_mode(self, Mode):
        print ('breath mode unsupported')
        return


