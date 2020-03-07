from model import *
from data import *
import sys

rnn = torch.load('D:\DjProject\mysite\char-rnn-classification.pt')


# Just return an output given a line
def evaluate(line_tensor):
    hidden = rnn.initHidden()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    return output


def predict(line, n_predictions=1):
    output = evaluate(Variable(lineToTensor(line)))



    # Get top N categories
    topv, topi = output.data.topk(n_predictions, 1, True)

    category_index = topi[0][0]
    categories = ["Arabic", "Chinese", "Czech", "Dutch", "English", "French", "German", "Greek", "Irish", "Italian",
                      "Japanese", "Korean", "Polish", "Portuguese", "Russian", "Scottish", "Spanish", "Vietnamese"]
    ca = categories[category_index]
    return ca

