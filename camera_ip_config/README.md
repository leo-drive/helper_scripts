## Force IP to Arena Camera 
The following steps are required to run the force_ip.sh file.
- You must make sure that the MAC address parameter is the MAC address of the cameras used

```bash
MAC1=1C0FAF2E667F # MAC address of camera1 
MAC2=1C0FAF2E8016 # MAC address of camera2
MAC3=1C0FAF2A7C10 # MAC address of camera3 
```
- IP address parameters should be the address that is desired to be assigned for the cameras.
```bash
IP1=169.207.128.102 # IP address of camera1 
IP2=169.209.0.10    # IP address of camera2
IP3=169.219.0.68    # IP address of camera3
```
- The directory where the IpConfigUtility file is located must be entered in the PATH parameter.
```bash
PATH=/path/to/IpConfigUtility
```
- After adding parameters to the script, the command should be run in the directory where the force_ip.sh file is located.
```bash
./force_ip.sh
```