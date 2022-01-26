# import dataset data
from dataset import data
import numpy as np
import statistics
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
main_word_dict = height_dict[max(temp)[1]]
ycoordinate_dict = {}
for item in word_dict:
    
    if item.y not in ycoordinate_dict:
        ycoordinate_dict[item.y] = [item]

    else:
        ycoordinate_dict[item.y].append(item)

print(ycoordinate_dict)

position_lst = [key for key, value in ycoordinate_dict.items()]
position_lst = sorted(position_lst)
vert_dist = []
for i in range(1, len(position_lst)):
    vert_dist.append((position_lst[i])- position_lst[i-1] - max(temp)[1])



print("The mean of the vertical distance is" + ' ' + str(np.mean(vert_dist)))
print("The mode of the vertical distance is" + ' ' + str(statistics.mode(vert_dist)))
print("The median of the vertical distance is" + ' ' + str(np.median(vert_dist)))

def give_x(elem):
    return elem.x
for key in ycoordinate_dict:
  ycoordinate_dict[key] = sorted(ycoordinate_dict[key], key = give_x)

print(ycoordinate_dict)

dist_lst = []
for key in ycoordinate_dict:
    tuple_list = []
    for word in ycoordinate_dict[key]:
        tuple_list.append((word.x, word.width))
    for i in range(1, len(tuple_list)):
        dist_lst.append(tuple_list[i][0]- tuple_list[i-1][0] - tuple_list[i-1][1])
    
print("The distance between words is" + ' ' + str(np.mean(dist_lst)))
print("The distance between words is" + ' ' + str(statistics.mode(dist_lst)))
print("The distance between words is" + ' ' + str(np.median(dist_lst)))

    


    
    

        