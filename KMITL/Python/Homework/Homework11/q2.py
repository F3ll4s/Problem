from turtle import *

def RobotBattle():
    robotList = []

    while True:
        clear()
        for robot in robotList:
            robot.draw()
            
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, "", end="")
            robot.displayStatus()
            i += 1
        print("====")

        
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")

        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")

            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()

            robotList.append(newRobot)
        else:
            n = int(choice)
            robotList[n].command(robotList)

        i = 0
        while i < len(robotList):
            if robotList[i].health <= 0:
                del robotList[i]
            else:
                i += 1

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy < 0:
            print("Not enough energy to move")
        else:
            self.x = x
            self.y = y
            self.energy -= 10
    def draw(self):
        penup()
        goto(self.x, self.y-20)
        pendown()
        circle(20)

    def displayStatus(self):
        print("x =", self.x, "y =", self.y, "health =", self.health, "energy =", self.energy)

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def heal(self,r):
        if self.energy >= 20 and abs(self.x - r.x) <= 10 and abs(self.y - r.y) <= 10:
            self.energy -= 20
            r.health += 10
            print(f"MedicBot healed {r}. New health of robot: {r.health}")
        else:
            print("Not enough energy to heal or target is out of range.")
    def command(self, robotList):   
        action = input("Enter 'm' to move or 'h' to heal another robot: ")
        if action == 'm':
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        elif action == 'h':
            print("Choose which robot to heal:")
            for i, robot in enumerate(robotList):
                if robot != self:
                    print(f"{i}: Robot at ({robot.x}, {robot.y}) with health {robot.health}")
            target = int(input("Enter the index of the robot to heal: "))
            self.heal(robotList[target])
    def draw(self):
        penup()
        goto(self.x, self.y-20)
        pendown()
        circle(20)
        penup()
        goto(self.x+5,self.y+5)
        pendown()
        goto(self.x+10,self.y+5)
        goto(self.x+10,self.y-5)
        goto(self.x+5,self.y-5)
        goto(self.x+5,self.y-10)
        goto(self.x-5,self.y-10)
        goto(self.x-5,self.y-5)
        goto(self.x-10,self.y-5)
        goto(self.x-10,self.y+5)
        goto(self.x-5,self.y+5)
        goto(self.x-5,self.y+10)
        goto(self.x+5,self.y+10)
        goto(self.x+5,self.y+5)
        penup()
        
class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        if self.energy >= 20 and self.missile > 0 and abs(self.x - r.x) <= 10 and abs(self.y - r.y) <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50
            print(f"StrikerBot struck {r}. New health of robot: {r.health}")
        else:
            print("Not enough energy or missiles to strike or target is out of range.")

    def displayStatus(self):
        super().displayStatus()
        print("missiles =", self.missile)

    def command(self, robotList):
        action = input("Enter 'm' to move or 's' to strike another robot: ")
        if action == 'm':
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        elif action == 's':
            print("Choose which robot to strike:")
            for i, robot in enumerate(robotList):
                if robot != self:
                    print(f"{i}: Robot at ({robot.x}, {robot.y}) with health {robot.health}")
            target = int(input("Enter the index of the robot to strike: "))
            self.strike(robotList[target])
    def draw(self):
        penup()
        goto(self.x, self.y-20)
        pendown()
        circle(20)
        penup()
        goto(self.x, self.y+12)
        pendown()
        goto(self.x+12, self.y)
        goto(self.x, self.y-12)
        goto(self.x-12, self.y)
        goto(self.x, self.y+12)
        
        
        
        
RobotBattle()