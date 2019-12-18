from PIL import Image
from keras.datasets import mnist
import random
(X_train,y_train), (X_test, y_test) = mnist.load_data()
trainingdates = X_train.tolist()
new_image = list(trainingdates[0])
counter = 0

def trainingloop():
    counter = 0
    loops = 0 + 6 
    for imageidx,image in enumerate(trainingdates):
        counter += 1
        if imageidx > loops:
            for rowidx,row in enumerate(image):
                new_image[rowidx].extend(row)
                if counter % 6 == 0:
                    return new_image
                    
trainingloop()
print(new_image)            
    


