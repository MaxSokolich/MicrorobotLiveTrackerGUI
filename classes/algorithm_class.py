
import numpy as np


class algorithm:
    def __init__(self):
        pass

    def run(self, robot_list, frame):
        """
        input: data about robot. eg, velocity or position
        output: magnetic field action commands
        """
        
        
        #input:  robot_list which stores all the attributes for each robot you select
        for bot_num in range(len(robot_list)):
            robot = robot_list[bot_num]
            pos = robot.position_list[-1]
            print("robot {} pos = {}".format(bot_num, pos))
            
        
        trajectory = robot_list[-1].trajectory  #can set as a different trajectory or use the drawn trajectory
        
       
        #output: actions which is the magetnic field commands applied to the arduino

        #most important action commands
        alpha = np.radians(30) #0 -> 360 deg. must be in radians
        gamma = np.radians(90) #0 -> 180 deg. must be in radians
        freq = 0 #0 -> 180 Hz

        # other variables not really used
        Bx = 0 # -1 -> 1
        By = 0 # -1 -> 1
        Bz = 0 # -1 -> 1
        psi = np.radians(90) #0 -> 90 deg. must be in radians
        gradient = 0 # gradient has to be 1 for the gradient to work
        equal_field = 0 # not used
        acoustic_freq = 0  # not used
        
        
        return frame, Bx, By, Bz, alpha, gamma, freq, psi, gradient, equal_field, acoustic_freq