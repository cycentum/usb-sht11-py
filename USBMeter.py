from ctypes import WinDLL, c_int, byref, string_at, c_double
from sys import stderr

class USBMeter:
	def __init__(self, pathToDLL):
		self.dll=WinDLL(pathToDLL)
	
	
	def FindUSB(self, idx:int):
		'''
		Return: device name (str)
		'''
		c_idx=c_int(idx)
		self.deviceNamePointer=self.dll.FindUSB(byref(c_idx))
		return string_at(self.deviceNamePointer).decode()
	
	
	def GetVers(self):
		'''
		Return: version (str)
		'''
		verPointer=self.dll.GetVers(self.deviceNamePointer)
		return string_at(verPointer).decode()
	
	
	def GetTempHumidTrue(self):
		'''
		Return: tuple of (temperature, humidity).
		When error, returns None.
		'''
		temp=c_double()
		humid=c_double()
		
		re = self.dll.GetTempHumidTrue(self.deviceNamePointer, byref(temp), byref(humid))
		if re==0:
			return temp.value, humid.value
		
		print("Error: GetTempHumidTrue", file=stderr)
		return None

	
	def ControlIO(self, port:int, val:bool):
		'''
		port (int): index of LED. 0 or 1 is supported.
		val (bool): True=on, False=off.
		'''
		
		self.dll.ControlIO(self.deviceNamePointer, c_int(port), c_int(int(val)))
	
	
	def SetHeater(self, val:bool):
		'''
		val (bool): True=on, False=off.
		'''
		
		self.dll.SetHeater(self.deviceNamePointer, c_int(int(val)))