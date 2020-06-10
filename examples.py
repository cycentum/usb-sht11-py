from USBMeter import USBMeter
import time

if __name__=="__main__":
	meter=USBMeter(r"Path-to-USBMeter.dll")
	
	deviceName=meter.FindUSB(0)
	print("Device name:", deviceName)
	
	ver=meter.GetVers()
	print("Ver:", ver)
	
	temp_humid=meter.GetTempHumidTrue()
	if temp_humid is not None:
		temp, humid=temp_humid
		print("Temperature:", temp)
		print("Humidity:", humid)
	
	print("LED_0 on")
	meter.ControlIO(0, True)
	time.sleep(1)
	print("LED_0 off")
	meter.ControlIO(0, False)
	time.sleep(1)
	
	print("LED_1 on")
	meter.ControlIO(1, True)
	time.sleep(1)
	print("LED_1 off")
	meter.ControlIO(1, False)
	time.sleep(1)
	
	print()
	print("Heater on")
	print("Temperature should increase and humidity should decrease if working properly")
	print()
	meter.SetHeater(True)
	
	for i in range(10):
		temp_humid=meter.GetTempHumidTrue()
		if temp_humid is not None:
			temp, humid=temp_humid
			print("Temperature:", temp)
			print("Humidity:", humid)
			print()
		time.sleep(1)
	
	print("Heater off")
	print("Temperature should decrease and humidity should increase if working properly")
	print()
	meter.SetHeater(False)
	
	for i in range(10):
		temp_humid=meter.GetTempHumidTrue()
		if temp_humid is not None:
			temp, humid=temp_humid
			print("Temperature:", temp)
			print("Humidity:", humid)
			print()
		time.sleep(1)