#import the module for the serial port
import serial

#make the port; "COM3" is the address in the computer
port = serial.Serial("COM3", baudrate=115200)

# This is how to send the trigger code. It will send as soon as the .write() line runs.
# The format for selecting your trigger code should be b'\x00' where 00 can be replaced by 
    # the proper code in hexadecimal. See the website for a conversion table (Hex column for input, Unsigned column for produced trigger code)
    # http://web.cecs.pdx.edu/~harry/compilers/ASCIIChart.pdf
port.write(b'\x00')
port.flush() # Clear inputs to the serial port


# At the end, terminate the serial port connection
port.close()
