obs = [30, 230, 630]
RATE = 5


def setup():
    size(1000,600)
    frameRate(24)

def draw():
    background(225, 225, 225)
    rect(0,540,1000,60)
    global obs 
    obs = [x-5 for x in obs]
    rect(obs[0],480,30,60)
    rect(obs[1],480,30,60)
    rect(obs[2],480,30,60)
    
    
