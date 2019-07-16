# TheNexusAvenger
#
# Uninstalls the Fan Controller service.

# The install location of the scripts.
INSTALL_LOCATION="/etc/FanControl"

# The location of the services.
SERVICE_LOCATION="/lib/systemd/system/FanControl.service"

# Stop and disable the services.
systemctl stop FanControl.service
systemctl disable FanControl.service

# Remove the files.
rm -rf $INSTALL_LOCATION
rm -f $SERVICE_LOCATION
