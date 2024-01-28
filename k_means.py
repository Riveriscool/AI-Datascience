import numpy as np
dataset = [[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)],[np.random.randint(1, 10), np.random.randint(1, 10)]]
def kmeans_3(dataset, center_red, center_blue, center_green):
    red,blue,green,red_distance,blue_distance,green_distance = ([],[],[],0,0,0)
    while True:
        for i in range(len(dataset)):
            red_distance = np.sqrt(np.power(dataset[i][0] - center_red[0], 2) +np.power(dataset[i][1] - center_red[1]))
            blue_distance = np.sqrt(np.power(dataset[i][0] - center_blue[0], 2) +np.power(dataset[i][1] - center_blue[1]))
            green_distance = np.sqrt(np.power(dataset[i][0] - center_green[0], 2) +np.power(dataset[i][1] - center_green[1]))
            if red_distance < blue_distance and red_distance < green_distance:
                red.append(i)
            if blue_distance < red_distance and blue_distance < green_distance:
                blue.append(i)
            else:
                green.append(i)
        sum = 0
        for i in range(len(red)):
            sum += red[i][0]
        center_red[0] = sum / len(red)
        sum = 0
        for i in range(len(red)):
            sum += red[i][1]
        center_red[1] = sum / len(red)
        sum = 0
        for i in range(len(blue)):
            sum += blue[i][0]
        center_blue[0] = sum / len(blue)
        sum = 0
        sum = 0
        for i in range(len(blue)):
            sum += blue[i][1]
        center_blue[1] = sum / len(blue)
        sum = 0
        sum = 0
        for i in range(len(green)):
            sum += green[i]
        center_green[0] = sum / len(blue)
        sum = 0
        for i in range(len(green)):
            sum += blue[i]
        center_green[0] = sum / len(green)
        sum = 0
        print(center_blue, center_red, center_green)
           
    
kmeans_3(dataset, [np.random.randint(1, 10), np.random.randint(1, 10)], [np.random.randint(1, 10), np.random.randint(1, 10)], [np.random.randint(1, 10), np.random.randint(1, 10)])