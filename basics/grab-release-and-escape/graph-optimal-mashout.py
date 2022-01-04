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

def get_mashout_groundedcargo(p): 
    """
    Input opponent's percent, output minimum amount of frames to mashout of cargo. 
    """
    return math.floor(get_gripstrength_cargo(p)/2)

def get_mashout_aerialcargo(p): 
    """
    Input opponent's percent, output minimum amount of frames to mashout of cargo. 
    """
    return math.floor(get_gripstrength_cargo(p)/3)

def get_mashout_grab(p): 
    """
    Input opponent's percent, output minimum amount of frames to mashout of grab. 
    """
    return math.floor(get_gripstrength_grab(p)/13)

# Initialize variables
gripstrength_cargo, gripstrength_grab = [], []
mashout_groundedcargo, mashout_aerialcargo, mashout_grab = [], [], []
size = 101
xaxis = np.arange(size)

# Build data
for i in range (0, size): 
    gripstrength_cargo.append(get_gripstrength_cargo(i))
    gripstrength_grab.append(get_gripstrength_grab(i))
    mashout_groundedcargo.append(get_mashout_groundedcargo(i))
    mashout_aerialcargo.append(get_mashout_aerialcargo(i))

    mashout_grab.append(get_mashout_grab(i))

# Build graph
font = {'family' : 'JetBrains Mono',
        'weight' : 'normal',
        'size'   : 18,}

plt.rc('font', **font)
plt.step(xaxis, mashout_groundedcargo, label='Grounded Cargo')
plt.step(xaxis, mashout_aerialcargo, label='Aerial Cargo')
plt.step(xaxis, mashout_grab, label='Grab')
plt.title('Opponent\'s Percent VS Minimum Frames To Mash Out')
plt.ylabel('Frames')
plt.xlabel('Percent')
plt.legend()
plt.show()

