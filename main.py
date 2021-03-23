#! python3
import obd


ports = obd.scan_serial()  # return list of valid USB or RF ports
print(ports)
connection = obd.OBD(ports[1])  # connect to the second port in the list
# connection = obd.OBD() # auto connect

def main():
    print('Press Ctrl-C to quit.')
    while True:
        try:

            r = connection.query(obd.commands.RPM)  # returns the response from the car
            r2 = connection.query(obd.commands.SPEED)  # returns the response from the car
            print(r)
            print(r2)
        except KeyboardInterrupt:
            print('\nDone')
            break


if __name__ == '__main__':
    main()
