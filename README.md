pibakeoff
=========

Raspberry Pi Bake-off resources

A master copy of these resources is held on github here:

https://github.com/whaleygeek/pibakeoff



You can either download all files in one go as a ZIP by pointing your web
browser to the above address and then pressing the DOWNLOAD ZIP button.

Or, if the files have been pre-installed on your SDCard, you can use git
to update them like this:

open a lxterminal window

cd pibakeoff

git pull


If you have done the connectivity workshop, you would have reconfigured
your network interface for local networking with a static IP address.
To return this to it's original configuration and to allow connection
to the internet again, follow these steps:

sudo nano /etc/network/interfaces

Change 
iface eth0 inet static
to
iface eth0 inet dhcp

Delete lines:
address, netmask, network, broadcast, gateway

Then sudo reboot

You should now be able to connect to the internet and use the above git pull
instructions to update your resources from github




