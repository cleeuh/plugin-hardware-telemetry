#!/bin/bash

# --develop allows access to wan network
# privileged gives access to more devices
git fetch && git pull
sudo pluginctl run --name plugin-network-test --privileged --develop $(sudo pluginctl build .)