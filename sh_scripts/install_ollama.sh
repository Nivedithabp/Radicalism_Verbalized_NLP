#!/bin/bash
# Install Ollama

nmcli network on

cd ~/Downloads || exit

curl -fsSL https://ollama.com/install.sh | sh

# >>> Downloading Linux amd64 bundle
# ######################################################################## 100.0%
# >>> Creating ollama user...
# >>> Adding ollama user to render group...
# >>> Adding ollama user to video group...
# >>> Adding current user to ollama group...
# >>> Creating ollama systemd service...
# >>> Enabling and starting ollama service...
# Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
# >>> NVIDIA GPU installed.

# Test Ollama
ollama run llama3.2
