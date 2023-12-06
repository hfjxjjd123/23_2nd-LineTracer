import serial

def cmd_arduino(left, right):
    # /dev/tty/serial{NUM} 먼저 확인하기
    ser = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_5573631303835101F150-if00',9600)

    cmd = "L{:03d}R{:03d}\n".format(left, right).encode('ascii')
    print("Debug cmd -- %s" %cmd)
    ser.write(cmd)
    
    # For debugging = ACK
    read_serial=ser.readline()
    print(read_serial)
