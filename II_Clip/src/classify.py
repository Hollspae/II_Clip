# src/classify.py
import torch
from model import encode_image
from config import TOPK

def classify_image(image, class_names, text_features, topk=TOPK):
    img_feat = encode_image(image)
    with torch.no_grad():
        logits = 100.0 * img_feat @ text_features.T
        probs = logits.softmax(dim=-1)[0].cpu().numpy()
    order = probs.argsort()[::-1][:topk]
    return [(class_names[i], float(probs[i])) for i in order]