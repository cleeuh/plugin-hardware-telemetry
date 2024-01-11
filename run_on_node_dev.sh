#!/bin/bash

# --develop allows access to wan network
git fetch && git pull
sudo pluginctl run --name plugin-network-test --privileged --develop $(sudo pluginctl build .)