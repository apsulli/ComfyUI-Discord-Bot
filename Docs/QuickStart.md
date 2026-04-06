# 🎨 ComfyUI Discord Bot Quick Start

### 🚀 Basic Generation
Use the `/q` command followed by your prompt to start generating.
**Example:** `/q a majestic cat in space`

---

### ⚙️ Adding Arguments (Flags)
You can customize your generation by adding flags directly to your message.
*   `--res 1024x1024` or `--res 1024:1024` : Change resolution (height:width or heightxwidth)
*   `--steps 30` : Set sampling steps
*   `--cfg 7.5` : Set CFG scale
*   `--seed 123` : Set a specific seed
*   `--ckpt <name>` : Use a specific model/checkpoint
*   `--guidance N` : Set Flux guidance (Flux2Dev handler only)
*   `!neg!` : Use this to separate positive and negative prompts.
    *Example:* `/q a majestic cat !neg! blurry, low quality`

---

### 🔄 Switching Workflows (Handlers)
Workflows (like Txt2Img, Flux, or Img2Img) are called **Handlers**.
1. Use `/handlers` to see the list.
2. Click the button for the workflow you want to use.
3. Use `/handler-info` to see specific flags supported by your current selection.

**Available handlers include:**
*   **Txt2Img** - Standard SDXL text-to-image
*   **Flux2Dev** - FLUX.1-dev with guidance scale support
*   **CrystalClearXL** - SDXL with Crystal Clear XL model
*   **Img2Img** - Image-to-image generation
*   **FluxSchnell** - Fast FLUX.1-schnell workflow

---

### 💾 Saving Your Defaults (Context)
If you always use the same resolution or style, save it so you don't have to type it every time.
*   Use `/handler-context` to set a permanent **Prefix**, **Postfix**, or **Flags**.
*   These settings stay saved specifically for the handler you are currently using.

---

### 🏷️ Custom Shortcuts (References)
Save long prompt strings as short tags to use anywhere.
1.  **Save it:** `/ref-set cinematic "highly detailed, 8k, anamorphic lens"`
2.  **Use it:** `/q a lone robot #cinematic`
    *(The bot will automatically swap #cinematic for your saved text)*
3.  **Manage:** Use `/ref-view` to see your list or `/ref-del` to remove one.

---

### 🖼️ Working with Images
Upload an image to any channel where the bot is present. The bot will reply with a URL that you can copy and use with the `--url` flag in supported workflows.
