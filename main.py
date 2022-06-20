#! python3
import obd
import PySimpleGUI as sg

layout = [[sg.Text('Current speed: '), sg.Text('', key='-speed-', size=(20, 1))],
          [sg.Text('Current RPM: '), sg.Text('', key='-rpm-', size=(20, 1))],
          [sg.Quit()]]

window = sg.Window('CAR DASHBOARD').Layout(layout)

ports = obd.scan_serial()  # return list of valid USB or RF ports
if ports:
    print(ports)
    connection = obd.Async(ports[1])  # connect to the second port in the list
    # connection = obd.OBD()  # auto connect
else:
    connection = obd.Async("/dev/pts/9")  # used for ELM simulator


# connection = obd.OBD("/dev/pts/9")

def get_dtc(d):
    print(d)


def speed():
    connection.watch(obd.commands.SPEED)  # keep track of the Speed
    connection.start()  # start the async update loop
    connection.stop()
    return connection.query(obd.commands.SPEED).value.magnitude  # non-blocking, returns immediately


def rpm():
    connection.watch(obd.commands.RPM)  # keep track of the RPM
    connection.start()  # start the async update loop
    connection.stop()
    return connection.query(obd.commands.RPM).value.magnitude  # non-blocking, returns immediately


def main(gui_obj):
    # Event loop
    while True:
        event, values = gui_obj.Read(timeout=10)
        if event in (None, 'Quit'):
            break

        # Update '_time_' key value with return value of getTime()

        gui_obj['-speed-'].Update(speed())
        gui_obj['-rpm-'].Update(rpm())


if __name__ == '__main__':
    main(window)
