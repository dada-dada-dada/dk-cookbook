import math
import numpy as np
import matplotlib.pyplot as plt

def get_gripstrength_cargo(p): 
    """
    Input opponent's percent, output DK's cargo grip strength. 
    """
    return math.floor(2 * (p/25) + 14)

def get_gripstrength_grab(p): 
    
    """
    Input opponent's percent, output DK's grip strength.
    """
    return math.floor(40 * (p/25) + 75)

def get_mashout_cargo(p): 
    """
    Input opponent's percent, output minimum amount of frames to mashout of cargo. 
    """
    return math.floor(get_gripstrength_cargo(p)/2)

def get_mashout_grab(p): 
    """
    Input opponent's percent, output minimum amount of frames to mashout of grab. 
    """
    return math.floor(get_gripstrength_grab(p)/13)

# Initialize variables
gripstrength_cargo, gripstrength_grab = [], []
mashout_cargo, mashout_grab = [], []
size = 101
xaxis = np.arange(size)

# Build data
for i in range (0, size): 
    gripstrength_cargo.append(get_gripstrength_cargo(i))
    gripstrength_grab.append(get_gripstrength_grab(i))
    mashout_cargo.append(get_mashout_cargo(i))
    mashout_grab.append(get_mashout_grab(i))

# Build graph
font = {'family' : 'JetBrains Mono',
        'weight' : 'normal',
        'size'   : 18,}

plt.rc('font', **font)
plt.step(xaxis, gripstrength_cargo, label='Cargo')
plt.step(xaxis, gripstrength_grab, label='Grab')
plt.title('Opponent\'s Percent VS Grip Strength')
plt.ylabel('Grip Strength')
plt.xlabel('Percent')
plt.legend()
plt.show()
