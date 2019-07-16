# TheNexusAvenger
#
# Installs the Fan Controller service, enables it, and starts it.

# The install location of the scripts.
INSTALL_LOCATION="/etc/FanControl"

# The location of the services.
SERVICE_LOCATION="/lib/systemd/system/FanControl.service"

# Copy the scripts.
if test -d "$INSTALL_LOCATION"; then
    rm -rf $INSTALL_LOCATION
fi
cp -r src $INSTALL_LOCATION

# Create the service.
echo "[Unit]" > $SERVICE_LOCATION
echo "Description=Controls the PWM fan for the ROCKPro64" >> $SERVICE_LOCATION
echo "" >> $SERVICE_LOCATION
echo "[Service]" >> $SERVICE_LOCATION
echo "Type=simple" >> $SERVICE_LOCATION
echo "ExecStart=/usr/bin/python3 $INSTALL_LOCATION/Initializer.py" >> $SERVICE_LOCATION
echo "" >> $SERVICE_LOCATION
echo "[Install]" >> $SERVICE_LOCATION
echo "WantedBy=multi-user.target" >> $SERVICE_LOCATION

# Enable and start the service.
systemctl daemon-reload
systemctl enable FanControl.service
systemctl start FanControl.service
systemctl status FanControl.service