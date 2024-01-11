import UART

uart = UART(0,9600)

while True:
    print('checking BT')
    if uart.any():
        command = uart.readline()
        print(command)
