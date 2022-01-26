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
    word = Word(float(data[i][3]), float(data[i][4]), data[i][7], round(float(data[i][6])), float(data[i][5]))
    word_dict.append(word)


height_dict = {}

for item in word_dict:
    
    if item.height not in height_dict:
        height_dict[item.height] = [item]

    else:
        height_dict[item.height].append(item)

temp = [(len(value), key) for key, value in height_dict.items()]
print(max(temp)[1])


    

    


    
    

        