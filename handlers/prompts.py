TXT_TO_IMAGE_PROMPT = """
{
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "cfg": 7,
            "denoise": 1,
            "latent_image": [
                "5",
                0
            ],
            "model": [
                "4",
                0
            ],
            "negative": [
                "7",
                0
            ],
            "positive": [
                "6",
                0
            ],
            "sampler_name": "euler",
            "scheduler": "normal",
            "seed": 123456789,
            "steps": 25
        }
    },
    "4": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "sdxl\\\Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"
        }
    },
    "5": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "batch_size": 1,
            "height": 768,
            "width": 768
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": ""
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": ""
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [
                "3",
                0
            ],
            "vae": [
                "4",
                2
            ]
        }
    },
    "save_image_websocket_node": {
        "class_type": "SaveImageWebsocket",
        "inputs": {
            "images": [
                "8",
                0
            ]
        }
    },
    "save_image": {
    "inputs": {
      "filename_prefix": "comfy-bot-txt-2-img-",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  }
}
"""

IMG_TO_IMG_PROMPT = """
{
  "3": {
    "inputs": {
      "seed": 333592799566352,
      "steps": 20,
      "cfg": 8,
      "sampler_name": "dpmpp_2m",
      "scheduler": "normal",
      "denoise": 0.87,
      "model": [
        "4",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "11",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "sdxl\\\Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "6": {
    "inputs": {
      "text": "",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "10": {
    "inputs": {
      "url": "https://raw.githubusercontent.com/comfyanonymous/ComfyUI/master/input/example.png"
    },
    "class_type": "LoadImageFromUrl",
    "_meta": {
      "title": "Load Image From URL"
    }
  },
  "11": {
    "inputs": {
      "pixels": [
        "10",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEEncode",
    "_meta": {
      "title": "VAE Encode"
    }
  },
  "save_image_websocket_node": {
    "inputs": {
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImageWebsocket",
    "_meta": {
      "title": "SaveImageWebsocket"
    }
  },
   "save_image": {
    "inputs": {
      "filename_prefix": "comfy-bot-img-2-img-",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  }
}
"""

INSTANT_ID_BASIC = """
{
  "3": {
    "inputs": {
      "seed": 1631591050,
      "steps": 30,
      "cfg": 4.5,
      "sampler_name": "ddpm",
      "scheduler": "karras",
      "denoise": 1,
      "model": [
        "60",
        0
      ],
      "positive": [
        "60",
        1
      ],
      "negative": [
        "60",
        2
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "sdxl\\\Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "5": {
    "inputs": {
      "width": 1024,
      "height": 1024,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "11": {
    "inputs": {
      "instantid_file": "ip-adapter.bin"
    },
    "class_type": "InstantIDModelLoader",
    "_meta": {
      "title": "Load InstantID Model"
    }
  },
  "16": {
    "inputs": {
      "control_net_name": "diffusion_pytorch_model.safetensors"
    },
    "class_type": "ControlNetLoader",
    "_meta": {
      "title": "Load ControlNet Model"
    }
  },
  "38": {
    "inputs": {
      "provider": "CPU"
    },
    "class_type": "InstantIDFaceAnalysis",
    "_meta": {
      "title": "InstantID Face Analysis"
    }
  },
  "39": {
    "inputs": {
      "text": "comic character. graphic illustration, comic art, graphic novel art, vibrant, highly detailed",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "40": {
    "inputs": {
      "text": "photograph, deformed, glitch, noisy, realistic, stock photo",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "60": {
    "inputs": {
      "weight": 0.8,
      "start_at": 0,
      "end_at": 1,
      "instantid": [
        "11",
        0
      ],
      "insightface": [
        "38",
        0
      ],
      "control_net": [
        "16",
        0
      ],
      "image": [
        "67",
        0
      ],
      "model": [
        "4",
        0
      ],
      "positive": [
        "39",
        0
      ],
      "negative": [
        "40",
        0
      ]
    },
    "class_type": "ApplyInstantID",
    "_meta": {
      "title": "Apply InstantID"
    }
  },
  "67": {
    "inputs": {
      "url": "https://raw.githubusercontent.com/stavsap/ComfyUI-Discord-Bot/19b050360d36e076c33460dd327587561d23adcc/.meta/man.png"
    },
    "class_type": "LoadImageFromUrl",
    "_meta": {
      "title": "Load Image From URL"
    }
  },
  "save_image_websocket_node": {
    "inputs": {
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImageWebsocket",
    "_meta": {
      "title": "SaveImageWebsocket"
    }
  },
   "save_image": {
    "inputs": {
      "filename_prefix": "comfy-bot-instant-id-basic-",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  }
}
"""

INSTANT_ID_IP_ADAPTER = """
{
  "3": {
    "inputs": {
      "seed": 19538649205350,
      "steps": 30,
      "cfg": 4.5,
      "sampler_name": "ddpm",
      "scheduler": "karras",
      "denoise": 1,
      "model": [
        "74",
        0
      ],
      "positive": [
        "60",
        1
      ],
      "negative": [
        "60",
        2
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "sdxl\\\Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "5": {
    "inputs": {
      "width": 1024,
      "height": 1536,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "11": {
    "inputs": {
      "instantid_file": "ip-adapter.bin"
    },
    "class_type": "InstantIDModelLoader",
    "_meta": {
      "title": "Load InstantID Model"
    }
  },
  "16": {
    "inputs": {
      "control_net_name": "diffusion_pytorch_model.safetensors"
    },
    "class_type": "ControlNetLoader",
    "_meta": {
      "title": "Load ControlNet Model"
    }
  },
  "38": {
    "inputs": {
      "provider": "CPU"
    },
    "class_type": "InstantIDFaceAnalysis",
    "_meta": {
      "title": "InstantID Face Analysis"
    }
  },
  "39": {
    "inputs": {
      "text": "a tiki god island",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "40": {
    "inputs": {
      "text": "photograph, deformed, glitch, noisy, realistic, stock photo",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "60": {
    "inputs": {
      "weight": 0.8,
      "start_at": 0,
      "end_at": 1,
      "instantid": [
        "11",
        0
      ],
      "insightface": [
        "38",
        0
      ],
      "control_net": [
        "16",
        0
      ],
      "image": [
        "75",
        0
      ],
      "model": [
        "4",
        0
      ],
      "positive": [
        "39",
        0
      ],
      "negative": [
        "40",
        0
      ]
    },
    "class_type": "ApplyInstantID",
    "_meta": {
      "title": "Apply InstantID"
    }
  },
  "72": {
    "inputs": {
      "weight": 1,
      "ipadapter": [
        "73",
        1
      ],
      "image": [
        "76",
        0
      ]
    },
    "class_type": "IPAdapterEncoder",
    "_meta": {
      "title": "IPAdapter Encoder"
    }
  },
  "73": {
    "inputs": {
      "preset": "PLUS (high strength)",
      "model": [
        "60",
        0
      ]
    },
    "class_type": "IPAdapterUnifiedLoader",
    "_meta": {
      "title": "IPAdapter Unified Loader"
    }
  },
  "74": {
    "inputs": {
      "weight": 0.8,
      "weight_type": "linear",
      "start_at": 0,
      "end_at": 1,
      "embeds_scaling": "V only",
      "model": [
        "73",
        0
      ],
      "ipadapter": [
        "73",
        1
      ],
      "pos_embed": [
        "72",
        0
      ]
    },
    "class_type": "IPAdapterEmbeds",
    "_meta": {
      "title": "IPAdapter Embeds"
    }
  },
  "75": {
    "inputs": {
      "url": "https://raw.githubusercontent.com/stavsap/ComfyUI-Discord-Bot/19b050360d36e076c33460dd327587561d23adcc/.meta/man.png"
    },
    "class_type": "LoadImageFromUrl",
    "_meta": {
      "title": "Face Image From URL"
    }
  },
  "76": {
    "inputs": {
      "url": "https://raw.githubusercontent.com/stavsap/ComfyUI-Discord-Bot/main/.meta/king.jpg"
    },
    "class_type": "LoadImageFromUrl",
    "_meta": {
      "title": "Style Image From URL"
    }
  },
  "save_image_websocket_node": {
    "inputs": {
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImageWebsocket",
    "_meta": {
      "title": "SaveImageWebsocket"
    }
  },
   "save_image": {
    "inputs": {
      "filename_prefix": "comfy-bot-instant-id-ip-adapter-face-",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  }
}
"""

IP_ADAPTER_STYLE = """
{
  "3": {
    "inputs": {
      "seed": 522221112627545,
      "steps": 20,
      "cfg": 8,
      "sampler_name": "euler",
      "scheduler": "normal",
      "denoise": 1,
      "model": [
        "10",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "sdxl\\\Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "5": {
    "inputs": {
      "width": 768,
      "height": 768,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "6": {
    "inputs": {
      "text": "beautiful scenery nature glass bottle landscape, , purple galaxy bottle,",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "text, watermark",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "save_image": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  },
  "10": {
    "inputs": {
      "weight": 1,
      "weight_type": "style transfer",
      "combine_embeds": "concat",
      "start_at": 0,
      "end_at": 1,
      "embeds_scaling": "V only",
      "model": [
        "11",
        0
      ],
      "ipadapter": [
        "11",
        1
      ],
      "image": [
        "14",
        0
      ]
    },
    "class_type": "IPAdapterAdvanced",
    "_meta": {
      "title": "IPAdapter Advanced"
    }
  },
  "11": {
    "inputs": {
      "preset": "PLUS (high strength)",
      "model": [
        "4",
        0
      ]
    },
    "class_type": "IPAdapterUnifiedLoader",
    "_meta": {
      "title": "IPAdapter Unified Loader"
    }
  },
  "save_image_websocket_node": {
    "inputs": {
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImageWebsocket",
    "_meta": {
      "title": "SaveImageWebsocket"
    }
  },
  "14": {
    "inputs": {
      "url": "https://raw.githubusercontent.com/stavsap/ComfyUI-Discord-Bot/main/.meta/king.jpg"
    },
    "class_type": "LoadImageFromUrl",
    "_meta": {
      "title": "Load Image From URL"
    }
  }
}
"""

LORA_CONTROLNET_PROMPT = """
{
  "3": {
    "class_type": "KSampler",
    "_meta": { "title": "KSampler" },
    "inputs": {
      "seed": 500659386568470,
      "steps": 35,
      "cfg": 7,
      "sampler_name": "dpmpp_2m",
      "scheduler": "karras",
      "denoise": 1,
      "model": ["20", 0],
      "positive": ["23", 0],
      "negative": ["23", 1],
      "latent_image": ["5", 0]
    }
  },
  "4": {
    "class_type": "CheckpointLoaderSimple",
    "_meta": { "title": "Load Checkpoint" },
    "inputs": {
      "ckpt_name": "dreamshaper_8.safetensors"
    }
  },
  "5": {
    "class_type": "EmptyLatentImage",
    "_meta": { "title": "Empty Latent Image" },
    "inputs": {
      "width": 1216,
      "height": 320,
      "batch_size": 1
    }
  },
  "6": {
    "class_type": "CLIPTextEncode",
    "_meta": { "title": "CLIP Text Encode (Positive)" },
    "inputs": {
      "text": "",
      "clip": ["4", 1]
    }
  },
  "7": {
    "class_type": "CLIPTextEncode",
    "_meta": { "title": "CLIP Text Encode (Negative)" },
    "inputs": {
      "text": "black background, dark background, night, nighttime, sky, landscape, ground, terrain, horizon, outdoor scene, monochrome, grayscale, desaturated, brown, sepia, flat color, flat shading, cel shading, vector art, clip art, coloring book, uniform line weight, SVG, simple shapes, digital art, CG, smooth plastic, uniform color, single shade of green, watercolor, wash, smoke, mist, fog, translucent, transparent, ghostly, glow, bloom, splatter, dripping ink, muddy texture, soft edges, blurry, photorealistic, 3d render, smooth gradients, character, floor, wall, text, pumpkin, fruit, flower cluster, dead tree, single tree",
      "clip": ["4", 1]
    }
  },
  "8": {
    "class_type": "VAEDecode",
    "_meta": { "title": "VAE Decode" },
    "inputs": {
      "samples": ["3", 0],
      "vae": ["26", 0]
    }
  },
  "9": {
    "class_type": "SaveImage",
    "_meta": { "title": "Save Image (RMBG)" },
    "inputs": {
      "filename_prefix": "rmbg",
      "images": ["24", 0]
    }
  },
  "20": {
    "class_type": "LoraLoaderModelOnly",
    "_meta": { "title": "LoRA Loader (Model Only)" },
    "inputs": {
      "lora_name": "don_bluth_backgrounds.safetensors",
      "strength_model": 0.3,
      "model": ["4", 0]
    }
  },
  "21": {
    "class_type": "LoadImage",
    "_meta": { "title": "Load Image (ControlNet)" },
    "inputs": {
      "image": "controlnet_block_v7 (1).png",
      "upload": "image"
    }
  },
  "22": {
    "class_type": "ControlNetLoader",
    "_meta": { "title": "Load ControlNet Model" },
    "inputs": {
      "control_net_name": "control_v11p_sd15_lineart.pth"
    }
  },
  "23": {
    "class_type": "ControlNetApplyAdvanced",
    "_meta": { "title": "Apply ControlNet (Advanced)" },
    "inputs": {
      "strength": 0.9,
      "start_percent": 0,
      "end_percent": 0.8,
      "positive": ["6", 0],
      "negative": ["7", 0],
      "control_net": ["22", 0],
      "image": ["21", 0]
    }
  },
  "24": {
    "class_type": "RMBG",
    "_meta": { "title": "Remove Background (RMBG)" },
    "inputs": {
      "model": "RMBG-2.0",
      "sensitivity": 0.4,
      "resolution": 1024,
      "offset_x": 3,
      "offset_y": -3,
      "invert": false,
      "bg_white": true,
      "output_format": "Alpha",
      "bg_color": "#ffffff",
      "image": ["8", 0]
    }
  },
  "25": {
    "class_type": "SaveImage",
    "_meta": { "title": "Save Image (Original)" },
    "inputs": {
      "filename_prefix": "original",
      "images": ["8", 0]
    }
  },
  "26": {
    "class_type": "VAELoader",
    "_meta": { "title": "Load VAE" },
    "inputs": {
      "vae_name": "vae-ft-mse-840000-ema-pruned.safetensors"
    }
  },
  "29": {
    "class_type": "PostImageToProject",
    "_meta": { "title": "Post Image To Project" },
    "inputs": {
      "url": "http://alexs-macbook-pro.tailf7db2.ts.net:9090/upload",
      "category": "environment",
      "slot": "act1_parallax_near",
      "original_image": ["8", 0],
      "positive": ["6", 0],
      "negative": ["7", 0],
      "rmbg_image": ["24", 0],
      "alpha_image": ["31", 0]
    }
  },
  "30": {
    "class_type": "AILab_ColorToMask",
    "_meta": { "title": "Color To Mask" },
    "inputs": {
      "invert": false,
      "threshold": 200,
      "color": "#ffffff",
      "images": ["8", 0]
    }
  },
  "31": {
    "class_type": "JoinImageWithAlpha",
    "_meta": { "title": "Join Image With Alpha" },
    "inputs": {
      "image": ["8", 0],
      "alpha": ["30", 0]
    }
  },
  "32": {
    "class_type": "SaveImage",
    "_meta": { "title": "Save Image (ColorToMask)" },
    "inputs": {
      "filename_prefix": "colortomask",
      "images": ["31", 0]
    }
  },
  "save_image_websocket_node": {
    "class_type": "SaveImageWebsocket",
    "_meta": { "title": "SaveImageWebsocket" },
    "inputs": {
      "images": ["8", 0]
    }
  },
  "save_image": {
    "class_type": "SaveImage",
    "_meta": { "title": "Save Image" },
    "inputs": {
      "filename_prefix": "comfy-bot-lora-controlnet-",
      "images": ["8", 0]
    }
  }
}
"""

FLUX2_DEV = """
{
  "1": {
    "inputs": {
      "unet_name": "FLUX1\\\\flux1-dev-fp8.safetensors",
      "weight_dtype": "fp8_e4m3fn"
    },
    "class_type": "UNETLoader",
    "_meta": { "title": "Load Diffusion Model" }
  },
  "2": {
    "inputs": {
      "clip_name1": "t5xxl_fp8_e4m3fn.safetensors",
      "clip_name2": "clip_l.safetensors",
      "type": "flux",
      "device": "default"
    },
    "class_type": "DualCLIPLoader",
    "_meta": { "title": "DualCLIPLoader" }
  },
  "3": {
    "inputs": {
      "vae_name": "flux_vae.safetensors"
    },
    "class_type": "VAELoader",
    "_meta": { "title": "Load VAE" }
  },
  "5": {
    "inputs": {
      "text": "beautiful scenery",
      "clip": ["2", 0]
    },
    "class_type": "CLIPTextEncode",
    "_meta": { "title": "CLIP Text Encode (Positive)" }
  },
  "6": {
    "inputs": {
      "guidance": 3.5,
      "conditioning": ["5", 0]
    },
    "class_type": "FluxGuidance",
    "_meta": { "title": "FluxGuidance" }
  },
  "11": {
    "inputs": {
      "width": 1024,
      "height": 1024,
      "batch_size": 1
    },
    "class_type": "EmptySD3LatentImage",
    "_meta": { "title": "EmptySD3LatentImage" }
  },
  "12": {
    "inputs": {
      "seed": 0,
      "steps": 20,
      "cfg": 1,
      "sampler_name": "euler",
      "scheduler": "simple",
      "denoise": 1,
      "model": ["1", 0],
      "positive": ["6", 0],
      "negative": ["43", 0],
      "latent_image": ["11", 0]
    },
    "class_type": "KSampler",
    "_meta": { "title": "KSampler" }
  },
  "13": {
    "inputs": {
      "samples": ["12", 0],
      "vae": ["3", 0]
    },
    "class_type": "VAEDecode",
    "_meta": { "title": "VAE Decode" }
  },
  "25": {
    "inputs": {
      "filename_prefix": "flux2-dev/discord_",
      "images": ["13", 0]
    },
    "class_type": "SaveImage",
    "_meta": { "title": "Save Image" }
  },
  "43": {
    "inputs": {
      "text": "",
      "clip": ["2", 0]
    },
    "class_type": "CLIPTextEncode",
    "_meta": { "title": "CLIP Text Encode (Negative)" }
  },
  "save_image_websocket_node": {
    "inputs": {
      "images": ["13", 0]
    },
    "class_type": "SaveImageWebsocket",
    "_meta": { "title": "SaveImageWebsocket" }
  }
}
"""

FLUX_SCHNELL = """
{
  "5": {
    "inputs": {
      "width": 1024,
      "height": 1024,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "6": {
    "inputs": {
      "text": "Under the eerie glow of a full moon, a dark and ominous landscape unfolds. A vibrant, colorful boat floats on the serene lake, its vivid hues contrasting starkly with the foreboding atmosphere. In the background, a waterfall cascades down jagged rocks, the water glistening in the moonlight. Thick, swirling clouds loom overhead, adding to the sense of an evil presence. The moonlight filters through the clouds, casting an otherworldly glow over the scene. A falling star streaks across the sky, adding a touch of mysticism to the night. The air is thick with a sense of ancient secrets and dark magic, as if the very night is alive with hidden power. As daylight breaks, light glows on the landscape, illuminating the boat and the surrounding scenery with a surreal brightness. [romantic impressionism,dream scenery art,beautiful oil matte painting,romantic,style of thomas kinkade,beautiful digital painting,anime landscape,romantic painting,dreamlike digital painting,colorful painting,beautiful gorgeous digital art,style of greg rutkowski,janek sedlar,jenny saville:0] <lora:vivid_everclear:0.6> <lora:Sinozick:0.65>",
      "clip": [
        "11",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "13",
        0
      ],
      "vae": [
        "10",
        0
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "9": {
    "inputs": {
      "filename_prefix": "07-09-2024/discord_flux_",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  },
  "10": {
    "inputs": {
      "vae_name": "ae.safetensors"
    },
    "class_type": "VAELoader",
    "_meta": {
      "title": "Load VAE"
    }
  },
  "11": {
    "inputs": {
      "clip_name1": "t5xxl_fp16.safetensors",
      "clip_name2": "clip_l.safetensors",
      "type": "flux"
    },
    "class_type": "DualCLIPLoader",
    "_meta": {
      "title": "DualCLIPLoader"
    }
  },
  "12": {
    "inputs": {
      "unet_name": "flux1-schnell.safetensors",
      "weight_dtype": "fp8_e5m2"
    },
    "class_type": "UNETLoader",
    "_meta": {
      "title": "Load Diffusion Model"
    }
  },
  "13": {
    "inputs": {
      "noise": [
        "25",
        0
      ],
      "guider": [
        "22",
        0
      ],
      "sampler": [
        "16",
        0
      ],
      "sigmas": [
        "17",
        0
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "SamplerCustomAdvanced",
    "_meta": {
      "title": "SamplerCustomAdvanced"
    }
  },
  "16": {
    "inputs": {
      "sampler_name": "euler"
    },
    "class_type": "KSamplerSelect",
    "_meta": {
      "title": "KSamplerSelect"
    }
  },
  "17": {
    "inputs": {
      "scheduler": "simple",
      "steps": 4,
      "denoise": 1,
      "model": [
        "12",
        0
      ]
    },
    "class_type": "BasicScheduler",
    "_meta": {
      "title": "BasicScheduler"
    }
  },
  "22": {
    "inputs": {
      "model": [
        "12",
        0
      ],
      "conditioning": [
        "6",
        0
      ]
    },
    "class_type": "BasicGuider",
    "_meta": {
      "title": "BasicGuider"
    }
  },
  "25": {
    "inputs": {
      "noise_seed": 555909834447821
    },
    "class_type": "RandomNoise",
    "_meta": {
      "title": "RandomNoise"
    }
  },
  "save_image_websocket_node": {
    "inputs": {
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImageWebsocket",
    "_meta": {
      "title": "SaveImageWebsocket"
    }
  }
}
"""
