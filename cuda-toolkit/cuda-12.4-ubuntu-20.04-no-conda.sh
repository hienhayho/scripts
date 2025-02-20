#!/bin/bash

apt update && apt install wget -y
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda-repo-ubuntu2004-12-4-local_12.4.0-550.54.14-1_amd64.deb
dpkg -i cuda-repo-ubuntu2004-12-4-local_12.4.0-550.54.14-1_amd64.deb
cp /var/cuda-repo-ubuntu2004-12-4-local/cuda-*-keyring.gpg /usr/share/keyrings/
apt-get update
apt-get -y install cuda-toolkit-12-4
