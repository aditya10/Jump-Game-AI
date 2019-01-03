import random

obs = []
rate = 15
next_obs = 0
frame_count = 0
gravity = 1.2
time = 0
player = None

class Obstacle(object):
  def __init__(self, loc, ht):
    self.loc = loc
    self.ht = 120 if ht == 0 else 60

class Player(object):
  def __init__(self):
    self.y = 0
    self.y_vel = 1
    self.is_jumping = False

def setup():
    size(1000,600)
    frameRate(30)
    global frame_count
    frame_count = 0
    global player
    player = Player()

def draw():
    obstacleCreator()
    background(225, 225, 225)
    rect(0,540,1000,60)
    for ob in obs:
        rect(ob.loc, 540-ob.ht, 30, ob.ht)
        ob.loc-=rate
    global player
    global time
    if player.is_jumping:
        player.y+=player.y_vel*time*0.2
        player.y_vel-=gravity*time*0.2
        if player.y <= 0:
            player.is_jumping = False
            player.y = 0
            player.y_vel = 1
    rect(40, 510-player.y, 30, 30, 10)
    time+=1

def obstacleCreator():
    # After a random amount of frames, add a new obstacle
    global frame_count
    global next_obs
    if frame_count == next_obs:
        frame_count = 0
        next_obs = random.randint(20,60)
        addObstacle()
    frame_count+=1    

def addObstacle():
    rand_ht = random.randint(0,2)
    global obs
    obs.append(Obstacle(1000, rand_ht))
    
def hasCollided():
    print "collided"

def keyTyped():
    if key == ' ':
        bigJump()
    elif key == 'w':
        smallJump()
        
def bigJump():
    global player
    global time
    if player.y == 0:
        player.is_jumping = True
        player.y_vel = 25
        time = 1
        
        
def smallJump():
    global player
    global time
    if player.y == 0:
        player.is_jumping = True
        player.y_vel = 15
        time = 1

        
    

    
