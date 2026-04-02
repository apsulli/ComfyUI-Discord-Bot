# ComfyUI Discord Bot - Project Architecture

This project is a Discord bot designed to interface with a local ComfyUI instance for Stable Diffusion image generation.

## Core Components

- **Discord Bot (`comfy_bot.py`):** Built with `pycord`, handles slash commands, message events, and user interactions.
- **ComfyUI Client (`comfy_client.py`):** A singleton managing communication with the ComfyUI API via HTTP (REST) and WebSocket (for real-time status and image retrieval).
- **Handler Manager (`comfy_handlers_manager.py`):** Orchestrates the dynamic loading of workflow "handlers" from `handlers/` and `custom_handlers/`.
- **Workflow Handlers (`handlers/`):** Classes that translate user input (prompts + flags like `--res`, `--seed`, etc.) into specific ComfyUI workflow JSON structures.
- **Database (`bot_db.py`):** Uses SQLite to persist global settings, current handler selection, and handler-specific configurations (prefixes, postfixes, and reference macros).

## System Flow

1.  **Input:** User submits a prompt via `/q <message>` or wakes the host via `/wake`.
2.  **Processing (Prompt):** The `ComfyHandlersManager` retrieves the active handler, which uses `FlagsHandler` to parse command-line style flags and inject them into a base workflow JSON.
3.  **Wake-on-LAN:** The `/wake` command sends a magic packet to `COMFY_UI_MAC` and polls `COMFY_UI_HOST` for up to 60 seconds until a response is received.
4.  **Queueing:** `ComfyClient` sends the modified JSON to ComfyUI via `/prompt`.
4.  **Monitoring:** The client monitors execution progress via a persistent WebSocket connection.
5.  **Output:** A background task (`publish_images`) identifies completed prompts and sends the resulting images and a generation summary back to the Discord channel.

## Extension and Customization

- **New Workflows:** Add new handler classes in `handlers/` or `custom_handlers/` and export them via `__init__.py`.
- **Reference Macros:** Users can define shortcuts via `/ref-set <name> <value>` which are expanded during prompt processing.
- **Context Modifiers:** Handlers support persistent prefixes, postfixes, and flags to standardize generation styles.

## Standards and Conventions

- **Singletons:** Core managers (`ComfyClient`, `ComfyHandlersManager`, `BotDB`) are implemented as singletons using the `__new__` pattern.
- **Logging:** Centralized logging is provided by `common.py`.
- **AsyncIO:** The bot relies heavily on `asyncio` for non-blocking I/O operations with Discord and the background result poller.
