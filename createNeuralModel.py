import os

import torch
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor

from crops360CnnModel import Crops360CnnModel
from deviceDataLoader import DeviceDataLoader
from utils import get_default_device, to_device, fit

if __name__ == '__main__':
    data_dir = 'fruits-360_dataset/fruits-360'

    print(os.listdir(data_dir))
    vegetablesClasses = os.listdir(data_dir + "/Training")

    print(vegetablesClasses[:5])

    dataset = ImageFolder(data_dir + '/Training', transform=ToTensor())

    image, label = dataset[0]
    print(image.shape, label)
    image, dataset.classes[label]

    # show image based on img index
    # show_example(*dataset[1230])

    random_seed = 50
    torch.manual_seed(random_seed)
    print("dataset len:", len(dataset))

    validation_percent = 0.05  # 5% data for validation
    validation_size = int(validation_percent * len(dataset))
    train_size = len(dataset) - validation_size

    training_dataset, validation_dataset = random_split(dataset, [train_size, validation_size])
    print("Trainset len:", len(training_dataset), "\nValidationset len:", len(validation_dataset))

    # amount of data for one iteration
    batch_size = 64

    training_dataloader = DataLoader(training_dataset, batch_size, shuffle=True, num_workers=4, pin_memory=True)
    validation_dataloader = DataLoader(validation_dataset, batch_size * 2, num_workers=4, pin_memory=True)

    # show_batch(train_dl)

    model = Crops360CnnModel()
    print(model)

    device = get_default_device()
    print(device)

    training_dataloader = DeviceDataLoader(training_dataloader, device)
    validation_dataloader = DeviceDataLoader(validation_dataloader, device)
    to_device(model, device)

    model = to_device(Crops360CnnModel(), device)
    # testing accuracy of algorithm at start
    # result = evaluate(model,val_dl)
    # print(result)

    # define parameters for testing
    number_of_epochs = 3
    optimizer_function = torch.optim.Adam
    learning_rate = 0.001  # lerning rate The learning rate controls how quickly the model is adapted to the problem
    history = fit(number_of_epochs, learning_rate, model, training_dataloader, validation_dataloader,
                  optimizer_function)

    torch.save(model.state_dict(), 'crops360-cnn.pth')