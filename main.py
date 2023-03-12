import subprocess

yes = ["Y", "y"]
no = ["N", "n"]

print("Please run in Python3 (e.g. Python3 filename.py \n")

subprocess.call("iwconfig", shell=True)

iface = input("Which Interface do you wish to change? ")

print("sudo ifconfig " + iface + " down")
subprocess.call("sudo ifconfig " + iface + " down", shell=True)
print("sudo airmon-ng check kill")
subprocess.call("sudo airmon-ng check kill", shell=True)
print("sudo iwconfig " + iface + " mode monitor")
subprocess.call("sudo iwconfig " + iface + " mode monitor", shell=True)

new_mac = input("Do you wish to spoof a MAC address? Y/N ")
if new_mac in yes:
    print("sudo macchanger " + iface + " -m 00:11:22:33:44:55")
    subprocess.call("sudo macchanger " + iface + " -m 00:11:22:33:44:55", shell=True)

print("sudo ifconfig " +  iface + " up")
subprocess.call("sudo ifconfig " + iface + " up", shell=True)

run_snif = input("Do you wish to run an initial network scan? Y/N ")

if run_snif in yes:
    print("sudo airodump-ng " + iface)
    subprocess.call("sudo airodump-ng " + iface, shell=True)
elif run_snif in no:
    exit()
else:
    iface = input("Please select either Y or N... ")
  