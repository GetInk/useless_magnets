from me import *
from npc import *
from rooms import *
from sortingAlg import *
from pygame_functions import *
from colors import *
from random import *

class Current():
    def __init__(self, current):
        self.current = current
        self.x = self.current["X"]
        self.y = self.current["Y"]
        self.speed = self.current["speed"]
        self.origSpeed = self.speed
        self.sprite = self.current["sprite"]
        self.looking = self.current["directionLooking"]
        self.lastLooking = ""
        self.spriteArray = self.current["spriteArray"]
        self.randomStandAnimation = self.current["randomStandChance"]
        self.weightL = self.current["weightLimit"]
        self.holding = 0
        self.standAnimationStart = False
        self.spriteChange = 1
        self.image = 0
        self.itemsM = self.current["items"]
        self.itemsE = self.itemsM["equiped"]
        self.itemsB = self.itemsM["backpack"]
        self.size = self.current["size"]
        self.HP = self.current["HP"]
        self.maxHP = self.current["maxHP"]
class Where():
    def __init__(self, where):
        self.where = where
        self.itemsR = self.where["items"]
        self.npc = self.where["npc"]
        self.roomName = self.where["name"]
        self.message = self.where["message"]
        for roomName in room:
            if room[roomName] == self.where:
                self.roomKey = roomName
class Door():
    def __init__(self, conection1, conection2, conector, where):
        self.conector = conector
        self.where = where
        self.door = [{conection1:conection2}, {conection2:conection1}]
    def use(self, where):
        for conection in self.door:
            for key in conection:
                if key == where.roomKey:
                    newRoom = Where(room[conection[key]])
                    return newRoom
class Timer():
    num = 0
    def count(self, countTime):
        self.num += 1
        if self.num >= countTime:
            return True
        else:
            return False
    def reset(self):
        self.num = 0

# DISPLAY VARS
screenSizeX = 800
screenSizeY = 800
fps = 100
gameName = "Useless Magnets"

screenSize(screenSizeX, screenSizeY, gameName)
nextFrame = clock()

# DEFS
def anounce(anouncement, color=white):
    renderAnounce(anouncement, color, 25, screenSizeX, screenSizeY)
def collideNoDirect(draw):
    wallSize = [draw[2], draw[3]]
    if current.x <= draw[0]+wallSize[0]/2+current.size[0] and current.x >= draw[0]-wallSize[0]/2-current.size[0] and current.y >= draw[1]-wallSize[1]/2-current.size[1] and current.y <= draw[1]+wallSize[1]/2+current.size[1]:
        return True
    else:
        return False
def collideDirect(draw, direction):
    wallSize = [draw[2], draw[3]]
    if direction == "right":
        if current.x < draw[0] and current.x >= draw[0]-wallSize[0]/2-current.size[0] and current.y < draw[1]+wallSize[1]/2+current.size[1]-current.speed*1.5 and current.y > draw[1]-wallSize[1]/2-current.size[1]+current.speed*1.5:
            return [True, draw[0]-wallSize[0]/2-current.size[0]]
        else:
            return [False]
    elif direction == "left":
        if current.x <= draw[0]+wallSize[0]/2+current.size[0] and current.x > draw[0] and current.y < draw[1]+wallSize[1]/2+current.size[1]-current.speed*1.5 and current.y > draw[1]-wallSize[1]/2-current.size[1]+current.speed*1.5:
            return [True, draw[0]+wallSize[0]/2+current.size[0]]
        else:
            return [False]
    elif direction == "up":
        if current.x < draw[0]+wallSize[0]/2+current.size[0]-current.speed*1.5 and current.x > draw[0]-wallSize[0]/2-current.size[0]+current.speed*1.5 and current.y < draw[1] and current.y >= draw[1]-wallSize[1]/2-current.size[1]:
            return [True, draw[1]-wallSize[1]/2-current.size[1]]
        else:
            return [False]
    elif direction == "down":
        if current.x < draw[0]+wallSize[0]/2+current.size[0]-current.speed*1.5 and current.x > draw[0]-wallSize[0]/2-current.size[0]+current.speed*1.5 and current.y <= draw[1]+wallSize[1]/2+current.size[1] and current.y > draw[1]:
            return [True, draw[1]+wallSize[1]/2+current.size[1]]
        else:
            return [False]
# PC SIZE FINDER VARS
doSquare = False
squareWidth = 135
squareHight = 270
# LOADED VARS
me = loadMe()
room = loadRooms()
# OTHER VARS
pickUpDistance = 175
scaleSize = 15
doTake = True
spaceRest = 0
spaceAdd = 0
doDrop = True
shiftRest = 0
shiftAdd = 0
holdingPB = False
standAnimationStart = False
canMove = True
canMoveRight = True
canMoveLeft = True
canMoveUp = True
canMoveDown = True
wallRight = True
wallLeft = True
wallUp = True
wallDown = True
movingRight = False
movingLeft = False
movingUp = False
movingDown = False
movementMod = [0, 0, 0, 0]
nearestItem = []
doors = []
pickableItems = ["item", "pedistalBlock", "door", "heal"]
anounceUnlocking = Timer()
anounceDeath = Timer()
damageTimer = Timer()
unlockedDoor = ""
unlockedWith = ""
roomAnounce = ""
hitByProjectile = [False, "", 0]
died = False
diedBC = ""

startRoom = room["start"]
startSprite = me["butcher"]

lastRoom = startRoom
DOORS = room["doorConections"]
setAutoUpdate(False)
current = Current(startSprite)
where = Where(startRoom)
doors = []
for DOOR in DOORS:
    doors.append(Door(DOOR[0], DOOR[1], DOOR[2], where))
moveSprite(current.sprite, current.x, current.y, True)
showSprite(current.sprite)
changeSpriteImageNoSmoothing(current.sprite, current.image)
transformSpriteNoSmoothing(current.sprite, 0, scaleSize)

while True:
    clearShapes()

    # PC SIZE MESSURER
    if doSquare == True:
        rect(current.x, current.y, squareWidth, squareHight, green)

    if keyPressed("space") and doTake:
        if where.itemsR != {}:
            weight = 0
            for item in where.itemsR:
                for inItem in item:
                    Item = item[inItem]
                    draw = Item["draw"]
                    if nearestItem == []:
                        nearestItem = abs(current.x-draw[0]) + abs(current.y-draw[1])
                        takeItem = item
                        isItem = Item["type"]
                        takeDistance = draw[2]/2
                        PI = False
                        for inPickable in pickableItems:
                            if Item["type"] == inPickable:
                                PI = True
                        if PI:
                            pedistalPrevent = False
                        else:
                            pedistalPrevent = True
                        if isItem == "item":
                            weight = Item["weight"]
                    else:
                        PI = False
                        for inPickable in pickableItems:
                            if Item["type"] == inPickable:
                                PI = True
                        if (nearestItem > abs(current.x-draw[0]) + abs(current.y-draw[1]) or pedistalPrevent) and PI:
                            pedistalPrevent = False
                            nearestItem = abs(current.x-draw[0]) + abs(current.y-draw[1])
                            takeItem = item
                            isItem = Item["type"]
                            takeDistance = draw[2]/2
                            if isItem == "item":
                                weight = Item["weight"]
        PI = False
        for inPickable in pickableItems:
            if isItem == inPickable:
                PI = True
        if PI:
            if nearestItem <= takeDistance+pickUpDistance and weight + current.holding <= current.weightL and holdingPB == False:
                if isItem == "pedistalBlock":
                    holdingPB = True
                    for item in where.itemsR:
                        for inItem in item:
                            Item = item[inItem]
                            Type = Item["type"]
                            if Type == "pedistal":
                                pedistalItem = Item["items"]
                                for inPedistalItem in pedistalItem:
                                    for inTaken in takeItem:
                                        if inPedistalItem == inTaken:
                                            if inPedistalItem != pedistalItem[len(pedistalItem)-1]:
                                                for ITEM in where.itemsR:
                                                    for INITEM in ITEM:
                                                        if INITEM == pedistalItem[len(pedistalItem)-1]:
                                                            takeItem = ITEM
                                                            pedistalItem.remove(INITEM)
                                            else:
                                                pedistalItem.remove(inTaken)
                if isItem == "door":
                    for item in takeItem:
                        if takeItem[item]["open"] == True:
                            if collideNoDirect(takeItem[item]["draw"]):
                                doTake = False
                                takeItem[item]["used"] = True
                                for inItem in takeItem:
                                    for door in doors:
                                        if inItem == door.conector:
                                            lastRoom = where
                                            where = door.use(where)
                                for item in takeItem:
                                    for items in where.itemsR:
                                        for inItem in items:
                                            if inItem == item:
                                                current.x = items[inItem]["draw"][0]
                                                current.y = items[inItem]["draw"][1]
                elif isItem == "heal":
                    for item in takeItem:
                        Item = takeItem[item]
                        if Item["heals"] == "max":
                            current.HP = current.maxHP
                        else:
                            if current.HP+Item["heals"] > current.maxHP:
                                current.HP = current.maxHP
                            else:
                                current.HP += Item["heals"]
                    for inItemsR in range(0, len(where.itemsR)):
                        if takeItem == where.itemsR[inItemsR]:
                            del where.itemsR[inItemsR]
                            break
                else:
                    doTake = False
                    current.holding += weight
                    current.itemsB.append(takeItem)
                    for inItemsR in range(0, len(where.itemsR)):
                        if takeItem == where.itemsR[inItemsR]:
                            del where.itemsR[inItemsR]
                            break
        nearestItem = []
        takeItem = []
    if keyPressed("lshift") and doDrop:
        if current.itemsB != []:
            dropp = []
            canDropp = True
            havePB = False
            for item in current.itemsB:
                for inItem in item:
                    if item[inItem]["type"] == "pedistalBlock":
                        thePB = item
                        PB = item[inItem]
                        havePB = True
            for dropped in current.itemsB:
                for inDropped in dropped:
                    Item = dropped[inDropped]
                    draw = Item["draw"]
                    isItem = Item["type"]
                    if isItem == "item" and havePB == False:
                        weight = Item["weight"]
                        current.holding -= weight
                        if current.looking == "right":
                            draw[0] = current.x + scaleSize*6
                            draw[1] = current.y + scaleSize*7
                        elif current.looking == "left":
                            draw[0] = current.x - scaleSize*6
                            draw[1] = current.y + scaleSize*7
                        elif current.looking == "down":
                            draw[0] = current.x
                            draw[1] = current.y + scaleSize*11.3
                        else:
                            draw[0] = current.x
                            draw[1] = current.y - scaleSize*11.3
                    elif isItem == "pedistalBlock" or havePB == True:
                        for droppedPB in current.itemsB:
                            for inPB in droppedPB:
                                if droppedPB[inPB] == PB:
                                    Item = droppedPB[inPB]
                                    draw = Item["draw"]
                                    draw[0] = current.x
                                    draw[1] = current.y
                                    nearestP = []
                                    sizes = []
                                    for pedistal in where.itemsR:
                                        for inPedistal in pedistal:
                                            item = pedistal[inPedistal]
                                            Type = item["type"]
                                            if Type == "pedistal":
                                                draw = item["draw"]
                                                if nearestP == []:
                                                    canDropp = True
                                                    nearestP = abs(current.x-draw[0]) + abs(current.y-draw[1])
                                                    isP = pedistal
                                                else:
                                                    if nearestP > abs(current.x-draw[0]) + abs(current.y-draw[1]):
                                                        nearestP = abs(current.x-draw[0]) + abs(current.y-draw[1])
                                                        isP = pedistal
                                    if nearestP > 175:
                                        canDropp = False
                                    if canDropp == True:
                                        for inPedistal in isP:
                                            for pItems in isP[inPedistal]["items"]:
                                                for ITEM in where.itemsR:
                                                    for INITEM in ITEM:
                                                        if INITEM == pItems:
                                                            size = ITEM[INITEM]["whenDraw"]
                                                            sizes.append(size)
                                        if sizes == []:
                                            canDropp = True
                                        else:
                                            for inSize in sizes:
                                                if inSize > Item["whenDraw"]:
                                                    canDropp = False
                                    if nearestP > 175:
                                        canDropp = False
                                    if canDropp == True:
                                        for inP in isP:
                                            for inDropp in droppedPB:
                                                newDraw = isP[inP]["draw"]
                                                oldDraw = droppedPB[inDropp]["draw"]
                                                oldDraw[0] = newDraw[0]
                                                oldDraw[1] = newDraw[1]
                                                pedistalArray = isP[inP]["items"]
                                                pedistalArray.append(inPB)
                if canDropp == True:
                    if Item["type"] == "pedistalBlock":
                        holdingPB = False
                        doDrop = False          
                        where.itemsR.append(droppedPB)
                        for delItem in range(0, len(current.itemsB)):
                            if current.itemsB[delItem] == thePB:
                                del current.itemsB[delItem]
                                break
                    else:
                        doDrop = False
                        where.itemsR.append(dropped)
                        del current.itemsB[0]
                        break
                else:
                    break
    
    if keyPressed("right") and canMoveRight and wallRight:
        current.looking = "right"
        if current.lastLooking != current.looking:
            current.lastLooking = current.looking
            butcherImage = current.spriteArray["walkR"][0]
            nextFrame = clock()  
        if clock() >= nextFrame:   
            current.image += 1
            if current.image < current.spriteArray["walkR"][0]:
                current.image = current.spriteArray["walkR"][0]
            if current.image > current.spriteArray["walkR"][1]:
                current.image = current.spriteArray["walkR"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        movingRight = True
        moveSprite(current.sprite, current.x, current.y, True)
        standAnimationStart = False
    elif keyPressed("left") and canMoveLeft and wallLeft:
        current.looking = "left"
        if current.lastLooking != current.looking:
            current.lastLooking = current.looking
            butcherImage = current.spriteArray["walkL"][0]
            nextFrame = clock()  
        if clock() >= nextFrame:   
            current.image += 1
            if current.image < current.spriteArray["walkL"][0]:
                current.image = current.spriteArray["walkL"][0]
            if current.image > current.spriteArray["walkL"][1]:
                current.image = current.spriteArray["walkL"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        movingLeft = True
        moveSprite(current.sprite, current.x, current.y, True)
        standAnimationStart = False
    elif keyPressed("up") and canMoveUp and wallUp:
        current.looking = "up"
        if current.lastLooking != current.looking:
            current.lastLooking = current.looking
            butcherImage = current.spriteArray["walkU"][0]
            nextFrame = clock()  
        if clock() >= nextFrame:   
            current.image += 1
            if current.image < current.spriteArray["walkU"][0]:
                current.image = current.spriteArray["walkU"][0]
            if current.image > current.spriteArray["walkU"][1]:
                current.image = current.spriteArray["walkU"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        movingUp = True
        moveSprite(current.sprite, current.x, current.y, True)
        standAnimationStart = False
    elif keyPressed("down") and canMoveDown and wallDown:
        current.looking = "down"
        if current.lastLooking != current.looking:
            current.lastLooking = current.looking
            butcherImage = current.spriteArray["walkD"][0]
            nextFrame = clock()  
        if clock() >= nextFrame:   
            current.image += 1
            if current.image < current.spriteArray["walkD"][0]:
                current.image = current.spriteArray["walkD"][0]
            if current.image > current.spriteArray["walkD"][1]:
                current.image = current.spriteArray["walkD"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        movingDown = True
        moveSprite(current.sprite, current.x, current.y, True)
        standAnimationStart = False
    elif current.looking == "right":
        if clock() > nextFrame:
            randnum = rand(current.randomStandAnimation[0], current.randomStandAnimation[1])
            if randnum == 1 or standAnimationStart == True:
                current.image += current.spriteChange
                standAnimationStart = True
                if current.image < current.spriteArray["standR"][0]:
                    current.image = current.spriteArray["standR"][0]
                if current.image > current.spriteArray["standR"][1]:
                    current.image = current.spriteArray["standR"][0]
                if current.image <= current.spriteArray["standR"][0] and standAnimationStart == True:
                    current.spriteChange = 1
                    standAnimationStart = False
                if current.image >= current.spriteArray["standR"][1] and standAnimationStart == True:
                    current.spriteChange = -1
            else:
                current.image = current.spriteArray["standR"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        moveSprite(current.sprite, current.x, current.y, True)
    elif current.looking == "left":
        if clock() > nextFrame:
            randnum = rand(current.randomStandAnimation[0], current.randomStandAnimation[1])
            if randnum == 1 or standAnimationStart == True:
                current.image += current.spriteChange
                standAnimationStart = True
                if current.image < current.spriteArray["standL"][0]:
                    current.image = current.spriteArray["standL"][0]
                if current.image > current.spriteArray["standL"][1]:
                    current.image = current.spriteArray["standL"][0]
                if current.image <= current.spriteArray["standL"][0] and standAnimationStart == True:
                    current.spriteChange = 1
                    standAnimationStart = False
                if current.image >= current.spriteArray["standL"][1] and standAnimationStart == True:
                    current.spriteChange = -1
            else:
                current.image = current.spriteArray["standL"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        moveSprite(current.sprite, current.x, current.y, True)
    elif current.looking == "up":
        if clock() > nextFrame:
            randnum = rand(current.randomStandAnimation[0], current.randomStandAnimation[1])
            if randnum == 1 or standAnimationStart == True:
                current.image += current.spriteChange
                standAnimationStart = True
                if current.image < current.spriteArray["standU"][0]:
                    current.image = current.spriteArray["standU"][0]
                if current.image > current.spriteArray["standU"][1]:
                    current.image = current.spriteArray["standU"][0]
                if current.image <= current.spriteArray["standU"][0] and standAnimationStart == True:
                    current.spriteChange = 1
                    standAnimationStart = False
                if current.image >= current.spriteArray["standU"][1] and standAnimationStart == True:
                    current.spriteChange = -1
            else:
                current.image = current.spriteArray["standU"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        moveSprite(current.sprite, current.x, current.y, True)
    elif current.looking == "down":
        if clock() > nextFrame:
            randnum = rand(current.randomStandAnimation[0], current.randomStandAnimation[1])
            if randnum == 1 or standAnimationStart == True:
                current.image += current.spriteChange
                standAnimationStart = True
                if current.image < current.spriteArray["standD"][0]:
                    current.image = current.spriteArray["standD"][0]
                if current.image > current.spriteArray["standD"][1]:
                    current.image = current.spriteArray["standD"][0]
                if current.image <= current.spriteArray["standD"][0] and standAnimationStart == True:
                    current.spriteChange = 1
                    standAnimationStart = False
                if current.image >= current.spriteArray["standD"][1] and standAnimationStart == True:
                    current.spriteChange = -1
            else:
                current.image = current.spriteArray["standD"][0]
            changeSpriteImageNoSmoothing(current.sprite, current.image)
            transformSpriteNoSmoothing(current.sprite, 0, scaleSize)
            nextFrame = clock() + current.current["animationSpeed"]
        moveSprite(current.sprite, current.x, current.y, True)

    # WALK OF SCREEN
    if current.x < 0 - scaleSize*10:
        current.x = screenSizeX + scaleSize*10
    elif current.x > screenSizeX + scaleSize*10:
        current.x = 0 - scaleSize*10
    elif current.y < 0 - scaleSize*10:
        current.y = screenSizeY + scaleSize*10
    elif current.y > screenSizeY + scaleSize*10:
        current.y = 0 - scaleSize*10

    # MAKE EDGE SCREEN A WALL
    if current.x <= current.size[0]:
        wallLeft = False
        current.x = current.size[0]
    else:
        wallLeft = True
    if current.x >= screenSizeX-current.size[0]:
        wallRight = False
        current.x = screenSizeX-current.size[0]
    else:
        wallRight = True
    if current.y <= current.size[1]:
        wallUp = False
        current.y = current.size[1]
    else:
        wallUp = True
    if current.y >= screenSizeY-current.size[1]:
        wallDown = False
        current.y = screenSizeY-current.size[1]
    else:
        wallDown = True

    #   TAKE AND DROP DELAY
    if doTake == False:
        spaceAdd = 1
    if spaceRest >= 10:
        doTake = True
        spaceAdd = 0
        spaceRest = 0
    if doDrop == False:
        shiftAdd = 1
    if shiftRest >= 10:
        doDrop = True
        shiftAdd = 0
        shiftRest = 0
    shiftRest +=  shiftAdd
    spaceRest += spaceAdd
    
    # NEW ITEMS:
    #   MAGNETS
    for item in where.itemsR:
        for inItem in item:
            if item[inItem]["type"] == "item":
                if item[inItem]["ability"] == "magnet":
                    for item2 in where.itemsR:
                        for inItem2 in item2:
                            if inItem2 == item[inItem]["conected"]:
                                magnetDirect = item[inItem]["direction"]
                                draw = item[inItem]["draw"]
                                draw2 = item2[inItem2]["draw"]
                                shape = draw[len(draw)-1]
                                shape2 = draw[len(draw2)-1]
                                xDiff = draw[0]-draw2[0]
                                yDiff = draw[1]-draw2[1]
                                xDiff2 = draw2[0]-draw[0]
                                yDiff2 = draw2[1]-draw[1]
                                blockSpeed = 5
                                if magnetDirect == "":
                                    if abs(xDiff) <= abs(yDiff):
                                        magnetDirect = "x"
                                    else:
                                        magnetDirect = "y"
                                if abs(xDiff) <= blockSpeed*2:
                                    newXPos = (draw[0]+draw2[0])/2
                                    draw[0] = newXPos
                                    draw2[0] = newXPos
                                    xDiff = 0
                                    xDiff2 = 0
                                if abs(yDiff) <= blockSpeed*2:
                                    newYPos = (draw[1]+draw2[1])/2
                                    draw[1] = newYPos
                                    draw2[1] = newYPos
                                    yDiff = 0                                                                   
                                    yDiff2 = 0
                                if magnetDirect == "x":
                                    if xDiff != 0:
                                        draw[0] -= blockSpeed*(xDiff/abs(xDiff))
                                        draw2[0] -= blockSpeed*(xDiff2/abs(xDiff2))
                                    else:
                                        if yDiff != 0:
                                            draw[1] -= blockSpeed*(yDiff/abs(yDiff))
                                            draw2[1] -= blockSpeed*(yDiff2/abs(yDiff2))
                                        else:
                                            magnetDirect = ""
                                            break
                                elif magnetDirect == "y":
                                    if yDiff != 0:                    
                                        draw[1] -= blockSpeed*(yDiff/abs(yDiff))
                                        draw2[1] -= blockSpeed*(yDiff2/abs(yDiff2))
                                    else:
                                        if xDiff != 0:
                                            draw[0] -= blockSpeed*(xDiff/abs(xDiff))
                                            draw2[0] -= blockSpeed*(xDiff2/abs(xDiff2))
                                        else:
                                            magnetDirect = ""
                                            break
    #   WALLS
    isWall = False
    hitWallRight = False
    hitWallLeft = False
    hitWallUp = False
    hitWallDown = False
    for item in where.itemsR:
        for inItem in item:
            if item[inItem]["type"] == "wall":
                isWall = True
                draw = item[inItem]["draw"]
                wallSize = [draw[2], draw[3]]
                if collideDirect(draw, "right")[0]:
                    canMoveRight = False
                    hitWallRight = True
                    current.x = collideDirect(draw, "right")[1]
                elif hitWallRight == False:
                    canMoveRight = True
                if collideDirect(draw, "left")[0]:
                    canMoveLeft = False
                    hitWallLeft = True
                    current.x = collideDirect(draw, "left")[1]
                elif hitWallLeft == False:
                    canMoveLeft = True
                if collideDirect(draw, "up")[0]:
                    canMoveUp = False
                    hitWallUp = True
                    current.y = collideDirect(draw, "up")[1]
                elif hitWallUp == False:
                    canMoveUp = True
                if collideDirect(draw, "down")[0]:
                    canMoveDown = False
                    hitWallDown = True
                    current.y = collideDirect(draw, "down")[1]
                elif hitWallDown == False:
                    canMoveDown = True
    if isWall == False:
        canMoveRight = True
        canMoveLeft = True
        canMoveUp = True
        canMoveDown = True
    #   KEYS
    for key in current.itemsB:
        for inKey in key:
            Key = key[inKey]
            if Key["type"] == "item":
                if Key["ability"] == "key":
                    unlocks = Key["unlocks"]
                    for door in where.itemsR:
                        for inDoor in door:
                            if inDoor == unlocks:
                                Door = door[inDoor]
                                draw = Door["draw"]
                                doorSize = [draw[2], draw[3]]
                                if collideNoDirect(draw):
                                    if keyPressed("space"):
                                        doTake = False
                                        Door["open"] = True
                                        unlockedDoor = Door["name"]
                                        unlockedWith = Key["name"]
                                        roomAnounce = where.roomKey
                                        for delItem in range(0, len(current.itemsB)):
                                            if current.itemsB[delItem] == key:
                                                del current.itemsB[delItem]
    #   PROJECTILES:
    #       MOVEMENT
    for item in where.itemsR:
        for inItem in item:
            Item = item[inItem]
            Type = Item["type"]
            if Item["type"] == "projectile":
                draw = Item["draw"]
                speed = Item["speed"]
                direction = Item["direction"]
                if direction == "left":
                    draw[0] -= speed
                elif direction == "right":
                    draw[0] += speed
                elif direction == "up":
                    draw[1] -= speed
                elif direction == "down":
                    draw[1] += speed
    #       CONTACT
    for item in where.itemsR:
        for inItem in item:
            Item = item[inItem]
            if Item["type"] == "projectile":
                draw = Item["draw"]
                if collideDirect(draw, "right")[0]:
                    current.x = collideDirect(draw, "right")[1]
                    movingLeft = False
                    wallRight = False
                    if Item["direction"] == "left":
                        hitByProjectile[0] = True
                        hitByProjectile[1] = Item["direction"]
                if collideDirect(draw, "left")[0]:
                    current.x = collideDirect(draw, "left")[1]
                    movingRight = False
                    wallLeft = False
                    if Item["direction"] == "right":
                        hitByProjectile[0] = True
                        hitByProjectile[1] = Item["direction"]
                if collideDirect(draw, "up")[0]:
                    current.y = collideDirect(draw, "up")[1]
                    movingUp = False
                    wallDown = False
                    if Item["direction"] == "down":
                        hitByProjectile[0] = True
                        hitByProjectile[1] = Item["direction"]
                if collideDirect(draw, "down")[0]:
                    current.y = collideDirect(draw, "down")[1]
                    movingDown = False
                    wallUp = False
                    if Item["direction"] == "up":
                        hitByProjectile[0] = True
                        hitByProjectile[1] = Item["direction"]
    # EVENTS:
    #   OPENING DOORS
    if where.where == room["start"]:
        for pedistal in where.itemsR:
            for inPedistal in pedistal:
                if inPedistal == "pedistal1":
                    if pedistal[inPedistal]["items"] == ["block1", "block2", "block3", "block4", "block5"]:
                        for door in where.itemsR:
                            for inDoor in door:
                                if inDoor == "door1":
                                    if door[inDoor]["open"] == False:
                                        door[inDoor]["open"] = True
                                        unlockedDoor = door[inDoor]["name"]
                                        roomAnounce = where.roomKey
                elif inPedistal == "pedistal3":
                    if pedistal[inPedistal]["items"] == ["block1", "block2", "block3", "block4", "block5"]:
                        for door in where.itemsR:
                            for inDoor in door:
                                if inDoor == "door2":
                                    if door[inDoor]["open"] == False:
                                        door[inDoor]["open"] = True
                                        unlockedDoor = door[inDoor]["name"]
                                        roomAnounce = where.roomKey
    #   FINAL ITEMPP
    if where.where == room["puzzleRoom"]:
        for item in where.itemsR:
            for inItem in item:
                if inItem == "pp":
                    if item[inItem]["pressed"] == True:
                        for item2 in where.itemsR:
                            for inItem2 in item2:
                                if inItem2 == "wall1" or inItem2 == "wall2":
                                    item2[inItem2]["type"] = "untuchable"
                    else:
                        for item2 in where.itemsR:
                            for inItem2 in item2:
                                if inItem2 == "wall1" or inItem2 == "wall2":
                                    item2[inItem2]["type"] = "wall"
    
    # ANOUNCE DOOR UNLOCKING
    if unlockedDoor != "":
        if roomAnounce == where.roomKey:
            if unlockedWith == "":
                if anounceUnlocking.count(75) == False:
                    anounce("Unlocked %s" % unlockedDoor)
                else:
                    anounceUnlocking.reset()
                    unlockedDoor = ""
                    roomAnounce = ""
            else:
                if anounceUnlocking.count(75) == False:
                    anounce("Unlocked %s with %s" % (unlockedDoor, unlockedWith))
                else:
                    anounceUnlocking.reset()
                    unlockedDoor = ""
                    unlockedWith = ""
                    roomAnunce = ""
    # CANMOVE
    if canMoveRight == False or canMoveLeft == False or canMoveUp == False or canMoveDown == False or wallRight == False or wallLeft == False or wallUp == False or wallDown == False:
        canMove = False
    else:
        canMove = True
    # DRAW ITEMS
    if where.itemsR != []:
        Sorted = []
        for item in where.itemsR:
            for inItem in item:
                when = item[inItem]["whenDraw"]
                Sorted.append(when)
        bubble(Sorted)
        for inSorted in Sorted:
            for item in where.itemsR:
                for inItem in item:
                    Item = item[inItem]
                    draw = Item["draw"]
                    when = Item["whenDraw"]
                    Type = Item["type"]
                    shape = draw[len(draw)-1]
                    if Type != "untuchable":
                        if Type != "pedistal" and Type != "PP" and Type != "itemPP":
                            if when == inSorted:
                                if shape == "rect":
                                    rect(draw[0], draw[1], draw[2], draw[3], draw[4])
                                elif shape == "heart":
                                    drawHeart(draw[0], draw[1], draw[2], draw[3])
                                elif shape == "ellipse":
                                    ellipse(draw[0], draw[1], draw[2], draw[3], draw[4])
                                if Item["type"] == "decor":
                                    if Item["type2"] == "lava":
                                        lavaBubbles = Item["lavaBubbles"]
                                        if lavaBubbles == []:
                                            for Bubble in range(0, 5):
                                                lavaBubbles.append([randint(draw[0]-draw[2]/2+20,draw[0]+draw[2]/2-20), randint(draw[1]-draw[3]/2+20,draw[1]+draw[3]/2-20), randint(5, 25)])
                                        for Bubble in lavaBubbles:
                                            ellipse(Bubble[0], Bubble[1], Bubble[2], Bubble[2], red)
                                            Bubble[2] += 0.5
                                            if Bubble[2] >= randint(25, 40):
                                                Bubble[0] = randint(draw[0]-draw[2]/2+20,draw[0]+draw[2]/2-20)
                                                Bubble[1] = randint(draw[1]-draw[3]/2+20,draw[1]+draw[3]/2-20)
                                                Bubble[2] = 0
                        elif Type == "pedistal":
                            if when == inSorted:
                                pressure = Item["pressure"]
                                if pressure == True:
                                    pressed = Item["pressed"]
                                    if pressed == False:
                                        rect(draw[0], draw[1], draw[2], draw[3], gray)
                                        rect(draw[0]-10, draw[1]-10, draw[2], draw[3], draw[4])
                                    else:
                                        rect(draw[0], draw[1], draw[2], draw[3], draw[4])
                                else:
                                    rect(draw[0], draw[1], draw[2], draw[3], draw[4])
                        elif Type == "PP" or Type == "itemPP":
                            if when == inSorted:
                                pressed = Item["pressed"]
                                if pressed == False:
                                    rect(draw[0], draw[1], draw[2], draw[3], gray)
                                    rect(draw[0]-10, draw[1]-10, draw[2], draw[3], draw[4])
                                else:
                                    rect(draw[0], draw[1], draw[2], draw[3], draw[4])
    # DRAW HEARTS
    for draw in range(0, current.maxHP):
        drawHeart(33+draw*55, 765, 30, red)
    for draw in range(0, current.maxHP-current.HP):
        drawHeart((33+(current.maxHP-1)*55)-draw*55, 765, 25, black)
    # CREATING PEDISTAL AND PRESSURE PLATE PRESSURE
    if where.itemsR != []:
        for item in where.itemsR:
            for inItem in item:
                Item = item[inItem]
                Type = Item["type"]
                if Type == "pedistal":
                    pressure = Item["pressure"]
                    items = Item["items"]
                    if pressure == True:
                        if items != []:
                            Item["pressed"] = True
                        else:
                            Item["pressed"] = False
                elif Type == "itemPP":
                    draw = Item["draw"]
                    for item2 in where.itemsR:
                        for inItem2 in item2:
                            Item2 = item2[inItem2]
                            draw2 = Item2["draw"]
                            if inItem != inItem2:
                                if draw2[0] < draw[0]+draw[2]/2+draw2[2]/2 and draw2[0] > draw[0]-draw[2]/2-draw2[2]/2 and draw2[1] < draw[1]+draw[len(draw)-3]/2+draw2[len(draw2)-3]/2 and draw2[1] > draw[1]-draw[len(draw)-3]/2-draw2[len(draw2)-3]/2:
                                    Item["pressed"] = True
                                else:
                                    Item["pressed"] = False
                                    break
    # DO ROOM NAME
    message(where.roomName, white, 0, -300, 50, screenSizeX, screenSizeY, True)
    # DO ROOM MESSAGES
    for Message in where.message:
        message(Message[0], Message[1], Message[2], Message[3], Message[4], screenSizeX, screenSizeY, Message[5])
    # MOVEMENT
    if movingRight:
        current.x += current.speed+movementMod[0]
    if movingLeft:
        current.x -= current.speed+movementMod[1]
    if movingUp:
        current.y -= current.speed+movementMod[2]
    if movingDown:
        current.y += current.speed+movementMod[3]
    # SQUASHED BY PROJECTILE
    if hitByProjectile[0]:
        if hitByProjectile[1] == "right" and (wallRight == False or canMoveRight == False):
            died = True
            where = lastRoom
            current.HP = current.maxHP
            current.x = 400
            current.y = 400
            diedBC = "BEING SQUASHED"
        elif hitByProjectile[1] == "left" and (wallLeft == False or canMoveLeft == False):
            died = True
            where = lastRoom
            current.HP = current.maxHP
            current.x = 400
            current.y = 400
            diedBC = "BEING SQUASHED"
        elif hitByProjectile[1] == "up" and (wallUp == False or canMoveUp == False):
            died = True
            where = lastRoom
            current.HP = current.maxHP
            current.x = 400
            current.y = 400
            diedBC = "BEING SQUASHED"
        elif hitByProjectile[1] == "down" and (wallDown == False or canMoveDown == False):
            died = True
            where = lastRoom
            current.HP = current.maxHP
            current.x = 400
            current.y = 400
            diedBC = "BEING SQUASHED"
    # ANOUNCE DEATH
    if died == True:
        if anounceDeath.count(50) == False:
            anounce("YOU DIED FROM %s" % diedBC)
        else:
            died = False
            diedBC = ""
            anounceDeath.reset()
        #   CHANGE DOOR COLOR
    # CHANGE DOOR COLOR
    for item in where.itemsR:
        for inItem in item:
            if item[inItem]["type"] == "door":
                if item[inItem]["open"] == True:
                    item[inItem]["draw"][len(item[inItem]["draw"])-2] = green
                else:
                    item[inItem]["draw"][len(item[inItem]["draw"])-2] = red
    # BURN IN LAVA
    for item in where.itemsR:
        for inItem in item:
            Item = item[inItem]
            if Item["type"] == "decor":
                if Item["type2"] == "lava":
                    draw = Item["draw"]
                    if collideNoDirect(draw):
                        if damageTimer.count(7):
                            current.HP -= 1
                            damageTimer.reset()
                            if current.HP >= 0:
                                diedBC = "BURNING ALIVE IN LAVA"
    # DIE FROM DAMAGE
    if current.HP <= 0:
        died = True
        current.HP = current.maxHP
        where = lastRoom
        current.x = 400
        current.y = 400
    # REAPEARING PROJECTILES
    for item in where.itemsR:
        for inItem in item:
            Item = item[inItem]
            draw = Item["draw"]
            if Item["type"] == "projectile":
                if draw[0] < 0-draw[2]-25:
                    draw[0] = 800+draw[2]+25
                elif draw[0] > 800+draw[2]+25:
                    draw[0] = 0-draw[2]-25
                elif draw[1] < 0-draw[3]-25:
                    draw[1] = 800+draw[3]+25
                elif draw[1] > 800+draw[3]+25:
                    draw[1] = 0-draw[3]-25

    # RESETING VARS
    if hitByProjectile[0] == True:
        if hitByProjectile[2] <= 2:
            hitByProjectile[2] += 1
        else:
            hitByProjectile = [False, "", 0]
    movementMod = [0, 0, 0, 0]
    movingRight = False
    movingLeft = False
    movingUp = False
    movingDown = False
    canMove = True

    tick(fps)
    updateDisplay()

endWait()
