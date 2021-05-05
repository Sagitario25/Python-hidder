import ctypes
import os
import win32process

def hide ():
	"""Hide window where the program is running.
	Only works on windows and if the program is called through the command line or is compiled to a .exe"""
	hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
	if hwnd != 0:      
		ctypes.windll.user32.ShowWindow(hwnd, 0)      
		ctypes.windll.kernel32.CloseHandle(hwnd)
		_, pid = win32process.GetWindowThreadProcessId(hwnd)
		os.system('taskkill /PID ' + str(pid) + ' /f')

hide ()