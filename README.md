# ROCKPro64 Fan Controller
This system is a Python-based service for controlling the fan of
the 10mm heatsink with fan. The fan speed is configurable as a text
file to optimize for thermals or noise.

# Installing
Installing can be done with the following:
```
wget https://github.com/TheNexusAvenger/ROCKPro64-Fan-Controller/archive/master.zip
unzip master.zip
rm master.zip
cd ROCKPro64-Fan-Controller-master
sudo chmod +x ./Installer.sh
sudo ./Installer.sh
```

# Uninstalling
Uninstalling can be done with the following:
```
wget https://github.com/TheNexusAvenger/ROCKPro64-Fan-Controller/archive/master.zip
unzip master.zip
rm master.zip
cd ROCKPro64-Fan-Controller-master
sudo chmod +x ./Uninstaller.sh
sudo ./Uninstaller.sh
```

# Customizing The Fan Curve
By default, the fan curve file is in `/etc/FanControl/FanCurve.txt`. Each line
contains a fan curve point, with the first number being the temperature in celsius
and the second number is the relative fan speed as a decimal. Note that the fan will
be off if set below `0.25`.
The following is a fan curve with 25% at 60oC, 60% at 90oC, and 100% at 100oC:
```
60,0.25
90,0.6
100,1
```
