# nest-wifi-nagios-plugins
Nagios plugins to monitor Google Nest WIFI

No SNMP available to monitor Google Nest WIFI routers, only a very basic API, so here is a way to get basic monitoring working.

check_nestonline.py:
- Looks at the online status and reports output string and exit(0) if online, exit(2) if offline (CRITICAL)

check_nestuptime.py:
- Takes the uptime in seconds and converts to human readable for output.


Config:

- Install the python3 packages globally using PIP. I reference these ones: requests, json, time, pprint, datetime
- Copy the check files to your libexec directory (mine is /usr/local/nagios/libexec
- Change owner to your nagios user (mine was chown nagios:nagios)
- Give execute permissions (chmod +x)
- Add the command definitions to you commands.cfg (mine is provided as a sample)
- Define the checks in your host configuration file. I used switch.cfg and provided as a sample.
Note you will need to change the Nest router IP in the python scripts if you are not using the default address of 192.168.86.1
