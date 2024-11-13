import pyvisa
from time import sleep

rm = pyvisa.ResourceManager()

myDevice = rm.open_resource("USB0::0x1AB1::0x0588::DS1EB134904883::INSTR")

myDevice.timeout = 1000

myDevice.write("OUTP1 ON")
myDevice.write("SOUR1:APPL:SIN 1000, 0.1")

sleep(5)

myDevice.write("OUTP2 OFF")