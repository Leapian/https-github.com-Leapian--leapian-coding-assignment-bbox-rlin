# import dataset data
from dataset import data
# your code here
# let x_coordinate be x, y_coordinate be y, text be text, word height be height
class Word:
    def __init__(self, x, y, text, height, width):
        self.x = x
        self.y = y 
        self.text = text
        self.height = height
        self.width = width
word_dict = []

del data[0]

for i in range(len(data)):
    word = Word(data[i][3], data[i][4], data[i][7], data[i][6], data[i][5])
    word_dict.append(word)

print(word_dict)


    
    

        