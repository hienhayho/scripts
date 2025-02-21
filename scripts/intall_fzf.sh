#!/bin/bash

apt update && apt install git -y
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install --all

# shellcheck source=/dev/null
source ~/.bashrc
