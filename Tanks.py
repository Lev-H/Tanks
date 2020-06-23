from tkinter import *
from tkinter import messagebox as mb
from threading import Timer
from enum import Enum
import pygame

pygame.init()
shellr = 5
shellSpeed = 20
tankSpeed= 10
landscapesize = 30
tankshells = []
sndfile = 'snd/SoundShoot.wav'
SoundShoot = pygame.mixer.Sound(sndfile)
sndfile1 = 'snd/SoundBirst.wav'
SoundBerst = pygame.mixer.Sound(sndfile1)

def keypress(event):
    global tank1
    global tank2
    if(event.keycode == 38):
        TankMove(tank1, direction.Up)
    elif(event.keycode == 87):
        TankMove(tank2, direction.Up)
    elif(event.keycode == 40):
        TankMove(tank1, direction.Down)
    elif(event.keycode == 83):
        TankMove(tank2, direction.Down)
    elif(event.keycode == 39):
        TankMove(tank1, direction.Right)
    elif(event.keycode == 68):
        TankMove(tank2, direction.Right)
    elif(event.keycode == 37):
        TankMove(tank1, direction.Left)
    elif(event.keycode == 65):
        TankMove(tank2, direction.Left)
    if(event.keycode == 13):
        SoundShoot.play()
        Shoot(tank1)
    elif(event.keycode == 32):
        SoundShoot.play()
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
    global landshape
    DeleteShells(tankshells)
    if(WinOrLose() == False):
        for shell in tankshells:
            if CheckMove(shell, shell[2], "shell"):
                if(shell[2] == direction.Up):
                    shell[1] -= shellSpeed
                elif(shell[2] == direction.Down):
                    shell[1] += shellSpeed
                elif (shell[2] == direction.Right):
                    shell[0] += shellSpeed
                elif (shell[2] == direction.Left):
                    shell[0] -= shellSpeed
                if(shell[1] + shellr >= 600 or shell[1]  - shellr <= 0 or shell[0] + shellr >= 600 or shell[0] - shellr <= 0):
                    tankshells.remove(shell)
            else:
                tankshells.remove(shell)
                DrawLevel(landshape)
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
            SoundBerst.play()
            mb.showinfo(title = 'Game over!', message = 'Player 2 WIN!')
        elif(end == 2):
            SoundBerst.play()
            mb.showinfo(title = 'Game over!', message = 'Player 1 WIN!')

def TankMove(tank, WhereGo):
    global landshape
    DeleteTank(tank)
    go = False
    if CheckMove(tank, WhereGo, type = "tank") == True:
        if(WhereGo == direction.Up and tank[3] - 12 > 10 and go == False):
            tank[1] -= tankSpeed
            tank[2] = tank[0]
            tank[3] = tank[1] - 23
            tank[4] = direction.Up
            go = True
        elif(WhereGo == direction.Right and tank[2] + 12 < 590 and go == False):
            tank[0] += tankSpeed
            tank[2] = tank[0] + 23
            tank[3] = tank[1]
            tank[4] = direction.Right
            go = True
        elif(WhereGo == direction.Down and tank[3] + 12  < 590 and go == False):
            tank[1] += tankSpeed
            tank[2] = tank[0]
            tank[3] = tank[1] + 23
            tank[4] = direction.Down
            go = True
        elif(WhereGo == direction.Left and tank[2] - 12 > 10 and go == False):
            tank[0] -= tankSpeed
            tank[2] = tank[0] - 23
            tank[3] = tank[1]
            tank[4] = direction.Left
            go = True
    DrawTank(tank)

def CheckMove(object, WhereGo, type):
    global landshape
    objectx = object[0]
    objecty = object[1]
    if (WhereGo == direction.Up):
        objecty -= tankSpeed
    elif (WhereGo == direction.Down):
        objecty += tankSpeed
    elif (WhereGo == direction.Left):
        objectx -= tankSpeed
    elif (WhereGo == direction.Right):
        objectx += tankSpeed
    diff = landscapesize // 2 + 15
    for i in landshape:
        x = i[0] - landscapesize // 2
        y = i[1] - landscapesize // 2
        if(abs( objecty - y ) < diff  and abs( objectx - x ) < diff):
            if(type == "shell"):
                if(i[2] == 1):
                    DestroyLevel(i)
                    landshape.pop(i)
                    DrawLevel(landshape)
                elif(i[2] == 2):
                    DrawLevel(landshape)
                    return True
                elif(i[2] == 3):
                    DrawLevel(landshape)
                    return True
            elif(type == "tank"):
                if(i[2] == 3):
                    DrawLevel(landshape)
                    return True
            return False
    return True

def LoadLevel(lvl):
    landshape = {}
    f = open('levels/lvl' + str(lvl) + '.txt')
    for line in f:
        line1 = line[:-1]
        line2 = line1.split()
        line3 = int(line2[0]) * landscapesize, int(line2[1]) * landscapesize, int(line2[2])
        if(line2[2] == '0'):
            landshape[line3] = "black"
        elif(line2[2] == '1'):
            landshape[line3] = "red"
        elif(line2[2] == '2'):
            landshape[line3] = "blue"
        elif(line2[2] == '3'):
            landshape[line3] = "green"
    return landshape

def DrawLevel(landshape):
    for i in landshape.keys():
        c.create_rectangle(int(i[0]) - landscapesize, int(i[1]) - landscapesize, int(i[0]), int(i[1]), fill=str(landshape[i]))

def DestroyLevel(elem):
    c.create_rectangle(int(elem[0]) - landscapesize, int(elem[1]) - landscapesize, int(elem[0]), int(elem[1]), fill='white', outline = 'white')

def DrawTank(tank):
    c.create_rectangle(tank[0] - 15, tank[1] - 15, tank[0] + 15, tank[1] + 15)
    if(tank[4] == direction.Up or tank[4] == direction.Down):
        c.create_rectangle(tank[2] - 4, tank[3] - 8, tank[2] + 4, tank[3] + 8)
    else:
        c.create_rectangle(tank[2] - 8, tank[3] - 4, tank[2] + 8, tank[3] + 4)

def DeleteTank(tank):
    c.create_rectangle(tank[0] - 15, tank[1] - 15, tank[0] + 15, tank[1] + 15, outline = 'white')
    if (tank[4] == direction.Up or tank[4] == direction.Down):
        c.create_rectangle(tank[2] - 4, tank[3] - 8, tank[2] + 4, tank[3] + 8, outline = 'white')
    else:
        c.create_rectangle(tank[2] - 8, tank[3] - 4, tank[2] + 8, tank[3] + 4, outline = 'white')

def DrawShells(tankshells):
    for shell in tankshells:
        c.create_oval(shell[0] - shellr, shell[1] - shellr, shell[0] + shellr, shell[1] + shellr, fill = 'red')

def DeleteShells(tankshells):
    for shell in tankshells:
        c.create_oval(shell[0] - shellr, shell[1] - shellr, shell[0] + shellr, shell[1] + shellr, outline = 'white', fill = 'white')

root = Tk()
root.title('Tanks')
c = Canvas(root, width = 600, height = 600, bg = 'white')
c.pack()

#Make tanks
class direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4
tank1 = [65, 545, 65, 522, direction.Up]
tank2 = [545, 65, 545, 88, direction.Down]
DrawTank(tank1)
DrawTank(tank2)

lvl = 1
landshape = LoadLevel(lvl)
DrawLevel(landshape)

#Make click W, S, A, D, up, down, right, left, space and enter
root.bind('<Key>', keypress)

t = Timer(0.1, OnTimer)
t.start()

root.mainloop()