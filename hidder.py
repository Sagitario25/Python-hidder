import ctypes
import os
import win32process
import platform

def _hide ():
	"""Hide window where the program is running.
	Only works on windows and if the program is called through the command line or is compiled to a .exe"""
	hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
	if hwnd != 0:      
		ctypes.windll.user32.ShowWindow(hwnd, 0)      
		ctypes.windll.kernel32.CloseHandle(hwnd)
		_, pid = win32process.GetWindowThreadProcessId(hwnd)
		os.system('taskkill /PID ' + str(pid) + ' /f')

def _checkOS (ignore = False):
	if not ignore:
		if platform.system () != "Windows":
			raise OSError ("OS must be Windows")

def hide (ignore = False):
	_checkOS (ignore)
	_hide ()

def main ():
        hide ()
        import main
        main.main ()

if __name__ == "__main__":
        main ()
