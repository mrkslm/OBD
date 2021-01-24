#! python3
import obd

connection = obd.OBD()
cmd = obd.commands.SPEED

response = connection.query(cmd)
print("the speed is" + response.value)
print("the speed in kph is" + response.value.to("kph"))


rpm = connection.query(obd.commands.RMP)
print("RPM is " + rpm)

