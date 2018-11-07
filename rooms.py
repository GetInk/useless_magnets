from colors import *


def loadRooms():
    rooms = {
        "doorConections":[["start", "room1", "door1"], ["start", "room2", "door2"], ["room1", "puzzleRoom", "door3"], ["room2", "puzzleRoom", "door4"], ["puzzleRoom", "chestRoom", "door5"]],
        "start":{
            "name":"PUZZLE ROOM",
            "items":[
                {
                    "block5":{
                        "name":"block5",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 30, gray, "squ"],
                        "whenDraw": 5
                    }
                },
                {
                    "block4":{
                        "name":"block4",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 60, cian, "squ"],
                        "whenDraw": 4
                    }
                },
                {
                    "block3":{
                        "name":"block3",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 90, blue, "squ"],
                        "whenDraw": 3
                    }
                },
                {
                    "block2":{
                        "name":"block2",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 120, purple, "squ"],
                        "whenDraw": 2
                    }
                },
                {
                    "block1":{
                        "name":"block1",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 150, darkBlue, "squ"],    
                        "whenDraw": 1
                    }
                },
                {
                    "pedistal1":{
                        "name":"pedistal1",
                        "type":"pedistal",
                        "draw":[130, 400, 190, yellow, "squ"],
                        "whenDraw": 0,
                        "items":[],
                        "pressure":True,
                        "pressed":False
                    }
                },
                {
                    "pedistal2":{
                        "name":"pedistal2",
                        "type":"pedistal",
                        "draw":[400, 400, 190, white, "squ"],
                        "whenDraw": 0,
                        "items":["block1", "block2", "block3", "block4", "block5"],
                        "pressure":True,
                        "pressed":False
                    }
                },
                {
                    "pedistal3":{
                        "name":"pedistal3",
                        "type":"pedistal",
                        "draw":[670, 400, 190, yellow, "squ"],
                        "whenDraw": 0,
                        "items":[],
                        "pressure":True,
                        "pressed":False
                    }
                },
                {
                    "door1":{
                        "name":"door1",
                        "type":"door",
                        "draw":[15, 200, 30, 105, red, "rect"],
                        "whenDraw": 0,
                        "open": False,
                        "used": False
                }
                },
                    {
                    "door2":{
                        "name":"door2",
                        "type":"door",
                        "draw":[785, 200, 30, 105, red, "rect"],
                        "whenDraw": 0,
                        "open": False,
                        "used": False
                    }
                }
            ],
            "message":[["SPACE TO PICK UP", cian, 0, 200, 50, False], ["LSHIFT TO DROP", cian, 0, 250, 50, False]],
            "npc":[],
            "background":[],
            "light":True
        },
        "room1":{
            "name":"ROOM 1",
            "items":[
                {
                    "door1":{
                        "name":"door1",
                        "type":"door",
                        "draw":[785, 200, 30, 105, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False,
                    }
                },
                {
                    "magnet1":{
                        "name":"magnet1",
                        "type":"item",
                        "ability":"magnet",
                        "conected":"magnet2",
                        "direction":"",
                        "draw":[400, 400, 45, red, "squ"],
                        "whenDraw":6,
                        "weight":0
                    }
                },
                {
                    "door3":{
                        "name":"door3",
                        "type":"door",
                        "draw":[700, 785, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                }
            ],
            "message":[["INTERESTING ITEM", red, 0, -100, 50, False]],
            "npc":[],
            "background":[],
            "light":True
        },
        "room2":{
            "name":"ROOM 2",
            "items":[
                {
                    "door2":{
                        "name":"door2",
                        "type":"door",
                        "draw":[15, 200, 30, 105, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False,
                    }
                },
                {
                    "magnet2":{
                        "name":"magnet2",
                        "type":"item",
                        "ability":"magnet",
                        "conected":"magnet1",
                        "direction":"",
                        "draw":[400, 400, 45, blue, "squ"],
                        "whenDraw":6,
                        "weight":0
                    }
                },
                {
                    "door4":{
                        "name":"door4",
                        "type":"door",
                        "draw":[100, 785, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                }
            ],
            "message":[["INTERESTING ITEM", red, 0, -100, 50, False]],
            "npc":[],
            "background":[],
            "light":True
        },
        "puzzleRoom":{
            "name":"PUZZLE ROOM",
            "items":[
                {
                    "door3":{
                        "name":"door3",
                        "type":"door",
                        "draw":[94, 15, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                },
                {
                    "door4":{
                        "name":"door4",
                        "type":"door",
                        "draw":[707, 15, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                },
                {
                    "wall1":{
                        "name":"wall1",
                        "type":"wall",
                        "draw":[200, 400, 25, 800, white, "rect"],
                        "whenDraw":0
                    }
                },
                {
                    "wall2":{
                        "name":"wall2",
                        "type":"wall",
                        "draw":[600, 400, 25, 800, white, "rect"],
                        "whenDraw":0
                    }
                },
                {
                    "pp":{
                        "name":"Pressure Plate",
                        "type":"itemPP",
                        "draw":[400, 400, 200, yellow, "squ"],
                        "pressed":False,
                        "whenDraw":0
                    }
                },
                {
                    "door5":{
                        "name":"door5",
                        "type":"door",
                        "draw":[400, 785, 105, 30, green, "rect"],
                        "open":True,
                        "used":False,
                        "whenDraw":0
                    }
                }
            ],
            "message":[],
            "npc":[],
            "background":[],
            "light":True
        },
        "chestRoom":{
            "name":"CHEST ROOM",
            "items":[
                {
                    "door5":{
                        "name":"door5",
                        "type":"door",
                        "draw":[400, 15, 105, 30, green, "rect"],
                        "open":True,
                        "used":False,
                        "whenDraw":0
                    }
                },
                {
                    "key":{
                        "name":"key",
                        "type":"item",
                        "ability":"key",
                        "unlocks":"DOOR",
                        "draw":[400, 700, 50, orange, "squ"],
                        "weight":0,
                        "whenDraw":8
                    }
                }
            ],
            "message":[["CONGRADJULATIONS!", yellow, 0, -50, 70, False], ["YOU DID IT!", yellow, 0, 50, 85, False]],
            "npc":[],
            "background":[],
            "light":True
        }
    }

    return rooms