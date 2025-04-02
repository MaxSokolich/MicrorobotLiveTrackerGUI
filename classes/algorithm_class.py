

class algorithm:
    def __init__(self):
        pass

    def run(self, robot_list):
        """
        input: data about robot. eg, velocity or position
        output: magnetic field action commands
        """
        
        
        #input:  robot_list which stores all the attributes for each robot you select
        for bot_num in range(len(robot_list)):
            robot = robot_list[bot_num]
            pos = robot.position_list[-1]
            print("robot {} pos = {}".format(bot_num, pos))
            
        
        robot_list[-1].trajectory = [[400, 400], [1800,400], [400, 1800], [1800, 1800]]  #most recent robot trajectory
        
       

        
        #output: actions which is the magetnic field commands applied to the arduino

        Bx = 1 #-1 -> 1
        By = 0 #-1 -> 1
        Bz = 0 #-1 -> 1
        alpha = 30 #0 -> 360 deg
        gamma = 90 #0 -> 180 deg
        freq = 0 #0 -> 180 Hz
        psi = 0 #0 -> 90 deg
        gradient = 1 # gradient has to be 1 for the gradient thing to work
        acoustic_freq = 0
        
        
        return Bx, By, Bz, alpha, gamma, freq, psi, gradient, acoustic_freq