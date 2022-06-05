import os
from pathlib import Path

import torch
from PIL import Image
from torchvision import transforms
from torchvision.datasets import ImageFolder

from crops360CnnModel import Crops360CnnModel
from utils import get_default_device, to_device


def predict_image(img, model):
    # Convert to a batch of 1
    xb = to_device(img.unsqueeze(0), device)
    # Get predictions from model
    yb = model(xb)
    # Pick index with highest probability
    _, preds = torch.max(yb, dim=1)
    # Retrieve the class label
    return dataset.classes[preds[0].item()]


device = get_default_device()

transform = transforms.Compose([
    transforms.CenterCrop(260),
    transforms.Resize((100, 100)),
    transforms.ToTensor(),
    transforms.Normalize([0.3], [0.3])
])

dataset = ImageFolder('resources/warzywa', transform=transform)


def categorise_crop(source):
    dir_path = os.getcwd()
    path = Path(dir_path + '/' + source)

    img = Image.open(path)

    # img.show()

    x = transform(img)

    model = to_device(Crops360CnnModel(), device)
    model.load_state_dict(torch.load('crops360-cnn.pth'))

    print('Predicted:', predict_image(x, model))
