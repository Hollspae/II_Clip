# src/prompts.py

# === 1. Время года на аэрофото ===
SEASON_PROMPTS = {
    "winter": [
        "an aerial photo of a snowy winter landscape",
        "a satellite view of a snow-covered area in winter",
        "a drone shot of bare trees and snow in winter",
    ],
    "spring": [
        "an aerial photo of a landscape in spring",
        "a satellite view of green fields and blossoms in spring",
        "a drone shot of fresh green vegetation in spring",
    ],
    "summer": [
        "an aerial photo of a landscape in summer",
        "a satellite view of lush green fields in summer",
        "a drone shot of dense green vegetation in summer",
    ],
    "autumn": [
        "an aerial photo of a landscape in autumn",
        "a satellite view of yellow and brown fields in autumn",
        "a drone shot of trees with autumn colors",
    ],
}

# === 2. Что на изображении (ландшафт с неба) ===
AERIAL_PROMPTS = {
    "forest":    ["an aerial photo of a forest", "a drone shot over a forest"],
    "city":      ["an aerial photo of a city", "a drone shot over an urban area"],
    "farmland":  ["an aerial photo of farmland", "a drone shot over agricultural fields"],
    "desert":    ["an aerial photo of a desert", "a drone shot over sand dunes"],
    "coast":     ["an aerial photo of a coastline", "a drone shot over the sea shore"],
}