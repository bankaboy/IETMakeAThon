import matplotlib.pyplot as plt
import numpy as np
from time import time

def create_graph(std_values,input_values):
    for i in range(3):
        input_values[i] = float(input_values[i])

    values = []
    
    for i in range(3):
        values.append(input_values[i])
        values.append(std_values[i])

    objects = ('pH', 'Std pH', 'Temp' ,'Std Temperature', 'Moisture','Std Moisture')
    y_pos = np.arange(len(objects))
    performance = [] 
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    figsize = [10,6]
    plt.rcParams["figure.figsize"] = figsize
    plt.title('Sensor Values of sample')
 
    plt.show()
    #time.sleep(1)
 
    
    


