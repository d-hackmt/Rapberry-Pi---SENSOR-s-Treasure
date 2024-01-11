import serial
uart_channel = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=2)
data1=" "
data=" "
while 1:
 data = uart_channel.read(1)
 data1+=str(data)
 print (data1)
 data = uart_channel.write(1)
 
 uart_channel.flush()
 data=" "
 data1=" "
