'''
RaspberryPi Alphabot: battery check

@Andrea-Tomatis
@Nicolo-Cora
'''

import subprocess

# this function runs the "vcgencmd get_throttled" command on the command line 
# to check the battery status. It returns a byte string containing a code.
# If the code is 0x0 it means the barrery is working properly.
# If the code is 0x5000 it means the battery as to be charged.
def check_battery():
	s = subprocess.check_output(["vcgencmd", "get_throttled"])
	return s.decode()
