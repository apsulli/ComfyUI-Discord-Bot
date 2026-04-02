# Running the Bot as a Systemd Service

This guide explains how to set up the ComfyUI Discord Bot as a persistent service on a Raspberry Pi or other Linux-based systems.

## 1. Prerequisites
- Ensure Python 3.10+ is installed.
- Ensure your `.env` file is complete with:
  - `DISCORD_BOT_API_TOKEN`
  - `COMFY_UI_HOST`
  - `COMFY_UI_MAC`

## 2. Setup a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Create the Service File
Create a new service file:
```bash
sudo nano /etc/systemd/system/comfy-bot.service
```

Paste the following (adjust `User` and `WorkingDirectory` if your path is different):
```ini
[Unit]
Description=ComfyUI Discord Bot Service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Projects/ComfyUI-Discord-Bot
ExecStart=/home/pi/Projects/ComfyUI-Discord-Bot/venv/bin/python comfy_bot.py
Restart=always
RestartSec=5
TimeoutStopSec=5
KillSignal=SIGKILL
KillMode=mixed

[Install]
WantedBy=multi-user.target
```

## 4. Manage the Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable comfy-bot.service
sudo systemctl start comfy-bot.service
```

## Troubleshooting

### Nuclear Restart (If systemctl hangs)
If `systemctl restart` hangs, run this to force a clean slate:
```bash
sudo killall -9 python python3 && sudo systemctl daemon-reload && sudo systemctl start comfy-bot.service
```

### Python 3.13: ModuleNotFoundError: No module named 'audioop'
```bash
pip install audioop-lts
```

### Checking Logs
```bash
journalctl -u comfy-bot.service -f
```
