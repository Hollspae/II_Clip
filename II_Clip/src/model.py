# src/model.py
import clip
import torch
from config import MODEL_NAME, DEVICE

model, preprocess = clip.load(MODEL_NAME, device=DEVICE)
model.eval()

def encode_text_prompts(prompts_dict):
    class_names = list(prompts_dict.keys())
    class_features = []
    for name in class_names:
        tokens = clip.tokenize(prompts_dict[name]).to(DEVICE)
        with torch.no_grad():
            feats = model.encode_text(tokens)
            feats = feats / feats.norm(dim=-1, keepdim=True)
        mean_feat = feats.mean(dim=0)
        mean_feat = mean_feat / mean_feat.norm()
        class_features.append(mean_feat)
    return class_names, torch.stack(class_features)

def encode_image(image):
    image_input = preprocess(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        feat = model.encode_image(image_input)
        feat = feat / feat.norm(dim=-1, keepdim=True)
    return feat