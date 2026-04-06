# User Guide

To interact with the Bot, there is a need to use '/' commands.

Just type '/' and you should be able to see the list of all commands under you Bot name.

## Commands List

### /q {message}

Queue a workflow of the current handler with a given message. The message should contain all the required information and syntax for the current handler.

**Note:** The bot will immediately respond with "⏳ Queuing generation..." and then deliver the completed images directly to the channel (not as an interaction followup). This ensures images are always delivered to the originating channel, even if generation takes longer than 15 minutes.

To make efficient prompting without the need to deal with long repeating prompts check the [handler-context](#handler-context) command to set prefix or postfix and [refs](#ref-set-ref-value) features.

The message will be processed by appending a prefix if set to the beginning of the message then appending the postfix if set to the end of the message, then the message`s refs will be replaced with their corresponding value.

### /q-status

View the current queue information, the running and the pending prompt ids.

### /ref-set {ref} {value}

Will set a reference to a given string value under the given ref-name. This will be set as #<ref-name> and if present in the **/q** {message}, will be replaced with the corresponding value.

<details>
  <summary>Example</summary>

/ref-set 'config' '--res 1024:768 --cfg 5 --steps 40'

Will result in

```shell
#config=--res 1024:768 --cfg 5 --steps 40
```

and the /q message is

```shell
a robot #config
```

will result in message

```shell
a robot --res 1024:768 --cfg 5 --steps 40
```

</details>

The refs are stored per handler.

**restrictions**: the given ref-name can`t include '#' char or white spaces!.

### /ref-del {ref}

Remove a certain ref by name. 

**restrictions**: the given ref-name cant include '#' char or white spaces!.

### /ref-view 

View all current ref tuples.

### /handlers

View all supported handler, the list is buttons, pressing a button will set the current handler as selected.

### /handler-info

View information regarding the current selected workflow handler.

### /handler-context

Set and View the handler constant context. Upon submit all data will be persisted per handler.

the final message that will be constructed to be passed to the handler as follows:

{**Flags**}{**Prefix**}`{/q meesage}`{**Postfix**}

#### Prefix

This will set a constant prefix that will be appended to the beginning of the submitted message when using the /q {message} command.

#### Postfix

This will set a constant Postfix that will be appended to the end of  submitted message when using the /q {message} command.

#### Flags

This will set the flags for the handler (can be any other text), the flags section will be appended to the begging of the message after the prefix is appended, resulting that the flags are the first to parse, so other section can override their values if present.

<details>
  <summary>Example</summary>

![pic](../.meta/handler-context.png)

</details>

### /checkpoints

View all the checkpoints currently set in comfy server.

## Uploading Images

Uploading any images to the bot will result in corresponding ordered url links for the image. this urls can be used for workloads that can load image via url.

---

## Handlers Reference

The following handlers are available for different generation workflows:

### Flux2Dev

A FLUX.1-dev based workflow using UNETLoader with fp8 precision.

**Supported flags:**
- `--res height:width` - Resolution (default: 1024:1024)
- `--steps N` - Sampling steps (default: 20)
- `--seed N` - Random seed (default: random)
- `--guidance N` - Flux guidance scale (default: 3.5)
- `--batch N` - Batch size (default: 1)
- `--unet <filename>` - Diffusion model filename (from models/unet/)
- `--negative-prompt <text>` - Negative conditioning text

**Example:**
```
/q a beautiful landscape --res 1920x1080 --steps 25 --guidance 4
```

### CrystalClearXL

An SDXL-based workflow using the Crystal Clear XL checkpoint.

**Supported flags:**
- `--res height:width` - Resolution (default: 1024:1024, supports both `:` and `x` separators)
- `--cfg N` - CFG scale (default: 7)
- `--steps N` - Sampling steps (default: 30)
- `--seed N` - Random seed (default: random)
- `--batch N` - Batch size (default: 1)
- `--ckpt <name>` - Checkpoint to use (default: crystalClearXL_ccxl.safetensors)
- `--schd <name>` - Scheduler (default: karras)
- `--sampler <name>` - Sampler (default: dpmpp_2m)

**Special tokens:**
- `!neg!` - Splits message into positive/negative prompts

**Example:**
```
/q portrait of a wizard !neg! blurry, low quality --res 1024x1024 --cfg 7
```

### Other Handlers

Use `/handler-info` to see specific flags for other handlers like:
- **Txt2Img** - Standard SDXL text-to-image
- **Img2Img** - Image-to-image generation
- **FluxSchnell** - Fast FLUX.1-schnell workflow
- **InstantIDFace** - Face swapping with InstantID
- **IPAdapterStyle** - Style transfer with IP-Adapter

---

## Technical Notes

### Image Delivery Architecture

The bot uses an asynchronous architecture to handle long-running image generations:

1. **Immediate Acknowledgment**: When you submit a `/q` command, the bot immediately responds with "⏳ Queuing generation..." to resolve the Discord interaction
2. **Background Processing**: The prompt is queued to ComfyUI and processed in a background WebSocket thread
3. **Channel-Based Delivery**: When images are ready, they are sent directly to the originating channel using the bot's API (not interaction webhooks)

This approach ensures images are always delivered to the correct channel, even if generation takes longer than Discord's 15-minute interaction timeout window.

### Thread Safety

The bot maintains thread-safe communication between:
- The main async event loop (handling Discord interactions)
- The WebSocket thread (communicating with ComfyUI)
- The background task (processing completed generations)

All cross-thread operations use proper synchronization primitives to prevent race conditions and ensure reliable message delivery.