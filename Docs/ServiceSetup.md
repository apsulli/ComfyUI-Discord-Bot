# Running the Bot as a Systemd Service

This guide explains how to set up the ComfyUI Discord Bot as a persistent service on a Raspberry Pi or other Linux-based systems.

## 1. Prerequisites

- Ensure Python 3.10+ is installed.
- Ensure your `.env` file is complete with:
  - `DISCORD_BOT_API_TOKEN`
  - `COMFY_UI_HOST`
  - `COMFY_UI_MAC`
  - `COMFY_BOT_LOG_LEVEL` (optional)

## 2. Setup a Virtual Environment (Recommended)

From the project root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Create the Service File

Create a new service file (requires root):

```bash
sudo nano /etc/systemd/system/comfy-bot.service
```

Paste the following configuration (adjust `User` and `WorkingDirectory` to your setup):

```ini
[Unit]
Description=ComfyUI Discord Bot Service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Projects/ComfyUI-Discord-Bot
# Point to the python executable in your virtual environment
ExecStart=/home/pi/Projects/ComfyUI-Discord-Bot/venv/bin/python comfy_bot.py
Restart=always
RestartSec=5
# Optional: Load environment variables directly from a file
# EnvironmentFile=/home/pi/Projects/ComfyUI-Discord-Bot/.env

[Install]
WantedBy=multi-user.target
```

## 4. Manage the Service

Reload systemd, enable the service to start on boot, and start it now:

```bash
sudo systemctl daemon-reload
sudo systemctl enable comfy-bot.service
sudo systemctl start comfy-bot.service
```

## Troubleshooting

### Python 3.13: ModuleNotFoundError: No module named 'audioop'
Python 3.13 removed the `audioop` module. To fix this, ensure you have `audioop-lpm` installed:
```bash
pip install audioop-lpm
```

### ModuleNotFoundError: No module named 'dotenv'
Ensure `python-dotenv` is installed:
```bash
pip install python-dotenv
```

### Checking Status and Logs
```bash
# Check if running
sudo systemctl status comfy-bot.service

# View live logs
journalctl -u comfy-bot.service -f
```


## 5. Tailscale Considerations

If you are using Tailscale:

- Ensure the Raspberry Pi is a node on your Tailnet.
- The `COMFY_UI_HOST` should be the **local LAN IP** or the **Tailscale IP** of the host PC.
- Note: Wake-on-LAN packets (Layer 2) only work if the Pi is on the same **physical LAN** as the target PC. The magic packet will NOT travel over the Tailscale VPN layer itself.
