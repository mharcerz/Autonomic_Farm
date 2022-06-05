import torch
import torch.nn.functional as F
from torch import nn

import utils


class ImageClassificationBase(nn.Module):
    def training_step(self, batch):
        images, labels = batch
        general_prediction = self(images)
        loss = F.cross_entropy(general_prediction, labels)
        return loss

    def validation_step(self, batch):
        images, labels = batch
        general_prediction = self(images)
        loss = F.cross_entropy(general_prediction, labels)
        accuracy = utils.accuracy(general_prediction, labels)
        return {'val_loss': loss.detach(), 'val_acc': accuracy}

    def validation_epoch_end(self, outputs):
        batch_losses = [x['val_loss'] for x in outputs]
        epoch_loss = torch.stack(batch_losses).mean()
        batch_accuracy = [x['val_acc'] for x in outputs]
        epoch_accuracy = torch.stack(batch_accuracy).mean()
        return {'val_loss': epoch_loss.item(), 'val_acc': epoch_accuracy.item()}

    def epoch_end(self, epoch, result):
        print("Epoch [{}], Training loss: {:.4f}, Validation loss: {:.4f}, Validation accuracy: {:.4f}".format(
            epoch, result['train_loss'], result['val_loss'], result['val_acc']))
