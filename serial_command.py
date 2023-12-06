import sys
sys.path.append('/usr/lib/python3/dist-packages')
import serial

def main():
    cmd_arduino(20,20)
    print('d')

def cmd_arduino(left, right):
    ser = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_5573631303835101F150-if00',9600)

    cmd = "L{:03d}R{:03d}\n".format(left, right).encode('ascii')
    print("Debug cmd -- %s" %cmd)
    ser.write(cmd)
    
    read_serial=ser.readline()
    print(read_serial)

main()
