#!/bin/bash

# This script creates a self-extracting archive using makeself.

makeself --notemp apps/ installer.run "Your App Installer" ./install.sh
