from pygame_functions import *

def loadButcherAnimation():
    butcher = makeSprite("sprites/Butcher/stand forward 1.png")
    # 1-4   MOVE RIGHT
    addSpriteImage(butcher,"sprites/Butcher/walking right 1.png")
    addSpriteImage(butcher,"sprites/Butcher/walking right 2.png")
    addSpriteImage(butcher,"sprites/Butcher/walking right 3.png")
    addSpriteImage(butcher,"sprites/Butcher/walk right 4.png")
    # 5-8   MOVE LEFT
    addSpriteImage(butcher,"sprites/Butcher/walk left.png")
    addSpriteImage(butcher,"sprites/Butcher/walk left 2.png")
    addSpriteImage(butcher,"sprites/Butcher/walk left 3.png")
    addSpriteImage(butcher,"sprites/Butcher/walk left 4.png")
    # 9-12  MOVE UP
    addSpriteImage(butcher,"sprites/Butcher/walk back 1.png")
    addSpriteImage(butcher,"sprites/Butcher/walk back 2.png")
    addSpriteImage(butcher,"sprites/Butcher/walk back 3.png")
    addSpriteImage(butcher,"sprites/Butcher/walk back 4.png")
    # 13-16 MOVE DOWN
    addSpriteImage(butcher,"sprites/Butcher/walk forward.png")
    addSpriteImage(butcher,"sprites/Butcher/walk forward 2.png")
    addSpriteImage(butcher,"sprites/Butcher/walk forward 3.png")
    addSpriteImage(butcher,"sprites/Butcher/walk forward 4.png")


    # 17-20 LOOK RIGHT
    addSpriteImage(butcher,"sprites/Butcher/standing right.png")
    addSpriteImage(butcher,"sprites/Butcher/standing right 2.png")
    addSpriteImage(butcher,"sprites/Butcher/standing right 3.png")
    addSpriteImage(butcher,"sprites/Butcher/standing right 4.png")
    # 21-24 LOOK LEFT
    addSpriteImage(butcher,"sprites/Butcher/standing left.png")
    addSpriteImage(butcher,"sprites/Butcher/standing left 2.png")
    addSpriteImage(butcher,"sprites/Butcher/standing left 3.png")
    addSpriteImage(butcher,"sprites/Butcher/standing left 4.png")
    # 25 LOOK UP
    addSpriteImage(butcher,"sprites/Butcher/stand backward.png")
    # 26-28 LOOK DOWN
    addSpriteImage(butcher,"sprites/Butcher/stand forward 1.png")
    addSpriteImage(butcher,"sprites/Butcher/stand forward 2.png")
    addSpriteImage(butcher,"sprites/Butcher/stand forward 3.png")

    return butcher