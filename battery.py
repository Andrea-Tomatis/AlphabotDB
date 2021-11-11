
import subprocess

def check_battery():
	s = subprocess.check_output(["vcgencmd", "get_throttled"])
	return s.decode()
