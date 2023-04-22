import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):
        self.contents = []
        for color in colors.items():
            ball, number = color
            [self.contents.append(ball) for _ in range(number)]
        
    def draw(self, take):
        random.shuffle(self.contents)
        taken = []
        for _ in range(take):
            k = self.contents.pop()
            taken.append(k)
            if len(self.contents) == 0: return taken
        return taken


def check(balls, expballs):
    
    for expball in expballs.items():
        xball, xnumber = expball
        if balls.count(xball) < xnumber:
            return False

    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    inst = copy.deepcopy(hat.contents)
    for _ in range(num_experiments):
        balls = hat.draw(num_balls_drawn)
        success += 1 if check(balls, expected_balls) else 0
        hat.contents = copy.deepcopy(inst)

    print(success / num_experiments)
    return success / num_experiments