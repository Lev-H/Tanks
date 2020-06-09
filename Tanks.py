from tkinter import *
from tkinter import messagebox as mb
from threading import Timer
from enum import Enum

shellr = 5
shellSpeed = 20
tankshells = []

def keypress(event):
    global tank1
    global tank2
    if(event.keycode == 38):
        TankMove(tank1, "up")
    elif(event.keycode == 87):
        TankMove(tank2, "up")
    elif(event.keycode == 40):
        TankMove(tank1, "down")
    elif(event.keycode == 83):
        TankMove(tank2, "down")
    elif(event.keycode == 39):
        TankMove(tank1, "right")
    elif(event.keycode == 68):
        TankMove(tank2, "right")
    elif(event.keycode == 37):
        TankMove(tank1, "left")
    elif(event.keycode == 65):
        TankMove(tank2, "left")
    if(event.keycode == 13):
        Shoot(tank1)
    elif(event.keycode == 32):
        Shoot(tank2)

def Shoot(tank):
    global tankshells
    if(tank[4] == direction.Up):
        shell = [tank[2], tank[3] - 19, direction.Up]
    elif(tank[4] == direction.Right):
        shell = [tank[2] + 19, tank[3], direction.Right]
    elif(tank[4] == direction.Down):
        shell = [tank[2], tank[3] + 19, direction.Down]
    elif(tank[4] == direction.Left):
        shell = [tank[2] - 19, tank[3], direction.Left]
    tankshells.append(shell)
    DrawShells(tankshells)

def OnTimer():
    global tankshells
    if(len(tankshells) > 0):
        if MoveShells() == False:
            return False
    t = Timer(0.1, OnTimer)
    t.start()

def MoveShells():
    global tankshells
    DeleteShells(tankshells)
    if(WinOrLose() == False):
        for shell in tankshells:
            if(shell[2] == direction.Up):
                shell[1] -= shellSpeed
            elif(shell[2] == direction.Down):
                shell[1] += shellSpeed
            elif (shell[2] == direction.Right):
                shell[0] += shellSpeed
            elif (shell[2] == direction.Left):
                shell[0] -= shellSpeed
            if(shell[1] + shellr >= 500 or shell[1]  - shellr <= 0 or shell[0] + shellr >= 500 or shell[0] - shellr <= 0):
                tankshells.remove(shell)
    else:
        return False
    DrawShells(tankshells)

def WinOrLose():
    global tankshells
    global tank1
    global tank2
    for shell in tankshells:
        if(shell[2] == direction.Up and shell[1] - shellr <= tank1[1] + 20 and shell[1] - shellr > tank1[1] - 20 and shell[0] + shellr < tank1[0] + 20 and shell[0] - shellr > tank1[0] - 20):
            DeleteTank(tank1)
            end = 1
            WinOrLoseDialog(end)
            return True
        elif(shell[2] == direction.Up and shell[1] - shellr <= tank2[1] + 20 and shell[1] - shellr > tank2[1] - 20 and shell[0] + shellr < tank2[0] + 20 and shell[0] - shellr > tank2[0] - 20):
            DeleteTank(tank2)
            end = 2
            WinOrLoseDialog(end)
            return True
        elif(shell[2] == direction.Right and shell[0] + shellr >= tank1[0] - 20 and shell[0] + shellr < tank1[0] + 20 and shell[1] + shellr < tank1[1] + 20 and shell[1] - shellr > tank1[1] - 20):
            DeleteTank(tank1)
            end = 1
            WinOrLoseDialog(end)
            return True
        elif(shell[2] == direction.Right and shell[0] + shellr >= tank2[0] - 20 and shell[0] + shellr < tank2[0] + 20) and shell[1] + shellr < tank2[1] + 20 and shell[1] - shellr > tank2[1] - 20:
            DeleteTank(tank2)
            end = 2
            WinOrLoseDialog(end)
            return True
        elif(shell[2] == direction.Down and shell[1] + shellr >= tank1[1] - 20 and shell[1] - shellr < tank1[1] + 20 and shell[0] + shellr < tank1[0] + 20 and shell[0] - shellr > tank1[0] - 20):
            DeleteTank(tank1)
            end = 1
            WinOrLoseDialog(end)
            return True
        elif(shell[2] == direction.Down and shell[1] + shellr >= tank2[1] - 20 and shell[1] - shellr < tank2[1] + 20 and shell[0] + shellr < tank2[0] + 20 and shell[0] - shellr > tank2[0] - 20):
            DeleteTank(tank2)
            end = 2
            WinOrLoseDialog(end)
            return True
        elif(shell[2] == direction.Left and shell[0] - shellr <= tank1[0] + 20 and shell[0] - shellr > tank1[0] - 20 and shell[1] + shellr < tank1[1] + 20 and shell[1] - shellr > tank1[1] - 20):
            DeleteTank(tank1)
            end = 1
            WinOrLoseDialog(end)
            return True
        elif(shell[2] == direction.Left and shell[0] - shellr <= tank2[0] + 20 and shell[0] - shellr > tank2[0] - 20 and shell[1] + shellr < tank2[1] + 20 and shell[1] - shellr > tank2[1] - 20):
            DeleteTank(tank2)
            end = 2
            WinOrLoseDialog(end)
            return True
        return False

def WinOrLoseDialog(end):
    if(end == 1):
        mb.showinfo(title = 'Game over!', message = 'Player 2 WIN!')
    elif(end == 2):
        mb.showinfo(title = 'Game over!', message = 'Player 1 WIN!')

def TankMove(tank, WhereGo):
    DeleteTank(tank)
    if(WhereGo == "up" and tank[3] - 12 > 10):
        tank[1] -= 10
        tank[2] = tank[0]
        tank[3] = tank[1] - 32
        tank[4] = direction.Up
    elif(WhereGo == "right" and tank[2] + 12 < 490):
        tank[0] += 10
        tank[2] = tank[0] + 32
        tank[3] = tank[1]
        tank[4] = direction.Right
    elif(WhereGo == "down" and tank[3] + 12  < 490):
        tank[1] += 10
        tank[2] = tank[0]
        tank[3] = tank[1] + 32
        tank[4] = direction.Down
    elif(WhereGo == "left" and tank[2] - 12 > 10):
        tank[0] -= 10
        tank[2] = tank[0] - 32
        tank[3] = tank[1]
        tank[4] = direction.Left
    DrawTank(tank)

def DrawTank(tank):
    c.create_rectangle(tank[0] - 20, tank[1] - 20, tank[0] + 20, tank[1] + 20)
    if(tank[4] == direction.Up or tank[4] == direction.Down):
        c.create_rectangle(tank[2] - 5, tank[3] - 12, tank[2] + 5, tank[3] + 12)
    else:
        c.create_rectangle(tank[2] - 12, tank[3] - 5, tank[2] + 12, tank[3] + 5)

def DeleteTank(tank):
    c.create_rectangle(tank[0] - 20, tank[1] - 20, tank[0] + 20, tank[1] + 20, outline = 'white')
    if (tank[4] == direction.Up or tank[4] == direction.Down):
        c.create_rectangle(tank[2] - 5, tank[3] - 12, tank[2] + 5, tank[3] + 12, outline = 'white')
    else:
        c.create_rectangle(tank[2] - 12, tank[3] - 5, tank[2] + 12, tank[3] + 5, outline = 'white')

def DrawShells(tankshells):
    for shell in tankshells:
        c.create_oval(shell[0] - shellr, shell[1] - shellr, shell[0] + shellr, shell[1] + shellr, fill = 'red')

def DeleteShells(tankshells):
    for shell in tankshells:
        c.create_oval(shell[0] - shellr, shell[1] - shellr, shell[0] + shellr, shell[1] + shellr, outline = 'white', fill = 'white')

root = Tk()
root.title('Tanks')
c = Canvas(root, width=500, height=500, bg='white')
c.pack()

#Make tanks
class direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4
tank1 = [65, 445, 65, 413, direction.Up]
tank2 = [445, 65, 445, 97, direction.Down]
DrawTank(tank1)
DrawTank(tank2)

#Make click W, S, A, D, up, down, right, left, space and enter
root.bind('<Key>', keypress)

t = Timer(0.1, OnTimer)
t.start()

root.mainloop()