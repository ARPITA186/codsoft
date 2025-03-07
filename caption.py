from google.colab import files
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_taking = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

def make_caption(img_path):
    img=Image.open(img_path).convert("RGB")
    pixel_values= feature_taking(images=img, return_tensors="pt").pixel_values
    output_id=model.generate(pixel_values,max_length=100,num_beams=5)
    caption = tokenizer.decode(output_id[0],skip_special_tokens=True)
    return caption

while True:
    customar_input=input("\n upload an image so press enter or type exit ").strip().lower()

    if "exit"in customar_input  or "quit" in customar_input:
          print("bye")
          break
    tracked = files.upload()

    image_all =list(tracked.keys())[0]

    caption = make_caption(image_all)

    img=Image.open(image_all)
    plt.imshow(img)
    plt.axis("off")
    plt.title(caption)
    plt.show()
    print(f" Generated Caption: {caption}")