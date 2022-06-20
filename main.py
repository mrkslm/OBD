#! python3
import obd
import time

ports = obd.scan_serial()  # return list of valid USB or RF ports
if ports:
    print(ports)
    connection = obd.Async(ports[1])  # connect to the second port in the list
    # connection = obd.OBD()  # auto connect
else:
    connection = obd.Async("/dev/pts/9")    # used for ELM simulator


# connection = obd.OBD("/dev/pts/9")

def new_rpm(r):
    print(f"RPM {r.value}")


def new_speed(s):
    print(f"SPEED: {s.value}")


if __name__ == '__main__':
    connection.watch(obd.commands.RPM, callback=new_rpm)
    connection.watch(obd.commands.SPEED, callback=new_speed)
    connection.start()
    time.sleep(60)
    connection.stop()
