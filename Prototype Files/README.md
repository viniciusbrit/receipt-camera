# Prototype Information

## Hardware & Software Details
### Build
The first prototype was built around a W&J Graham's Port Wine tin that originally housed 3 mini bottles of aged port wine. The printer was disassembled to it's bare assemblies, having some connectors removed in favor or wires being directly soldered due to the limited space. The printer's battery was re-purposed to power the entire system, lasting around 3 hours in idle. A compact DC to DC converter was used to convert the battery's 7.4v to 5v in order to power the Raspberry Pi Zero. For camera operations, there is a physical on/off switch, along with 2 GPIO buttons, one for shutting down the Raspberry Pi safely, and another to take the picture and subsequently print it. 3D Models used in the build have been lost.

### Camera Module Details 
The OV5647 camera module was equipped with a 72 degree FOV lens, which had a similar calculated FOV to the viewfinder used in the build. The viewfinder was salvaged off of a disposable kodak 35mm film camera, which had a 28mm full frame lens. The camera module connected to the Pi's camera connector using a ribbon cable.

### Software
In software, a python script named pic.py handled the initialization of the camera, autofocus and picture taking through a GPIO button, then signaling the printer to print the generated image. This script would run once the shell fully initialized, which took about 30 to 45 seconds after power on, using bash. On the .bashrc file, the printer configuration is initialized along with the python script.

## Improvements to be made:
Since no protection circuit was used, the Raspberry Pi had it's usb controller die due to overvoltage from powering it through USB while unknowingly having the battery power turned on. This resulted in communication with the printer having to be done over bluetooth serial.

The 3d printed assembly for the Thermal Paper spool and Printer Hot Element/Motor was not adequate and resulted in the motor burning out due to mechanical stress.

