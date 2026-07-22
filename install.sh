#!/bin/bash
echo "🚀 Installing MicroCode..."
pip install tabulate
chmod +x micro
mkdir -p /data/data/com.termux/files/usr/bin
cp micro /data/data/com.termux/files/usr/bin/
echo 'alias micro="python ~/MicroCode/cli.py"' >> ~/.bashrc
echo "✅ Done! Run: source ~/.bashrc && micro data.mc"
