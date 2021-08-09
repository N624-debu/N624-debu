from cmu_112_graphics import *
from tkinter import *
import sys

def appStarted(app):
    app.x=-1
    app.y=-1
    (app.x0,app.y0,app.x1,app.y1)=(-1,-1,-1,-1)
    (app.wp1dx,app.wp1dy)=(-1,-1)
    (app.wp2dx,app.wp2dy)=(-1,-1)
    (app.wp3dx,app.wp3dy)=(-1,-1)
    (app.wp4dx,app.wp4dy)=(-1,-1)
    (app.wp5dx,app.wp5dy)=(-1,-1)
    (app.wp6dx,app.wp6dy)=(-1,-1)
    (app.wp7dx,app.wp7dy)=(-1,-1)
    (app.wp8dx,app.wp8dy)=(-1,-1)
    (app.bp1dx,app.bp1dy)=(-1,-1)
    (app.bp2dx,app.bp2dy)=(-1,-1)
    (app.bp3dx,app.bp3dy)=(-1,-1)
    (app.bp4dx,app.bp4dy)=(-1,-1)
    (app.bp5dx,app.bp5dy)=(-1,-1)
    (app.bp6dx,app.bp6dy)=(-1,-1)
    (app.bp7dx,app.bp7dy)=(-1,-1)
    (app.bp8dx,app.bp8dy)=(-1,-1)
    
    (app.wr1dx,app.wr1dy)=(-1,-1)
    (app.wr2dx,app.wr2dy)=(-1,-1)
    
    app.wpmov=[]
    app.bpmov=[]
    app.wrmov=[]
    #All chessmen images collected from --->
    #"https://www.kindpng.com/imgv/hxbhmb_chess-pieces-png-chess-pieces-sprite-sheet-transparent/"
    app.image1 = app.loadImage("pawn.png")
    app.image2 = app.scaleImage(app.image1, 2/3)
    app.image3 = app.loadImage("white pawn.png")
    app.image4 = app.scaleImage(app.image3, 2/3)
    app.image5 = app.loadImage("black queen.png")
    app.image6 = app.scaleImage(app.image5, .55)
    app.image7 = app.loadImage("white queen.png")
    app.image8 = app.scaleImage(app.image7, .55)
    app.image9 = app.loadImage("black knight.png")
    app.image10 = app.scaleImage(app.image9, .6)
    app.image11 = app.loadImage("white knight.png")
    app.image12 = app.scaleImage(app.image11, .6)
    app.image13 = app.loadImage("black bishop.png")
    app.image14 = app.scaleImage(app.image13, .6)
    app.image15 = app.loadImage("white bishop.png")
    app.image16 = app.scaleImage(app.image15, .6)
    app.image17 = app.loadImage("black king.png")
    app.image18 = app.scaleImage(app.image17, .6)
    app.image19 = app.loadImage("white king.png")
    app.image20 = app.scaleImage(app.image19, .6)
    app.image21 = app.loadImage("black rook.png")
    app.image22 = app.scaleImage(app.image21, .6)
    app.image23 = app.loadImage("white rook.png")
    app.image24 = app.scaleImage(app.image23, .6)
    app.chessBoard=[["bRook","bKnight","bBishop","bQueen","bKing","bBishop","bKnight","bRook"],
                    ["bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8"],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8"],
                    ["wRook1","wKnight1","wBishop1","wQueen","wKing","wBishop2","wKnight2","wRook2"]]
    pawnPosition(app)
    chessmenPosition(app)
    
#     app.chessBoard=[["bRook","bKnight","bBishop","bQueen","bKing","bBishop","bKnight","bRook"],
#                     ["bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8"],
#                     [0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8"],
#                     ["wRook1","wKnight1","wBishop1","wQueen","wKing","wBishop2","wKnight2","wRook2"]]
    
def legalWpawn1Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp1dx=app.wpawn1x
    app.wp1dy=app.wpawn1y
    for i in range(2):
        app.wp1dx-=1
        if app.chessBoard[app.wp1dx][app.wp1dy]==0:
           app.wpmov.append((app.wp1dx,app.wp1dy))
def legalWpawn2Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp2dx=app.wpawn2x
    app.wp2dy=app.wpawn2y
    for i in range(2):
        app.wp2dx-=1
        if app.chessBoard[app.wp2dx][app.wp2dy]==0:
           app.wpmov.append((app.wp2dx,app.wp2dy))
def legalWpawn3Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp3dx=app.wpawn3x
    app.wp3dy=app.wpawn3y
    for i in range(2):
        app.wp3dx-=1
        if app.chessBoard[app.wp3dx][app.wp3dy]==0:
           app.wpmov.append((app.wp3dx,app.wp3dy))
def legalWpawn4Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp4dx=app.wpawn4x
    app.wp4dy=app.wpawn4y
    for i in range(2):
        app.wp4dx-=1
        if app.chessBoard[app.wp4dx][app.wp4dy]==0:
           app.wpmov.append((app.wp4dx,app.wp4dy))
def legalWpawn5Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp5dx=app.wpawn5x
    app.wp5dy=app.wpawn5y
    for i in range(2):
        app.wp5dx-=1
        if app.chessBoard[app.wp5dx][app.wp5dy]==0:
           app.wpmov.append((app.wp5dx,app.wp5dy))
def legalWpawn6Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp6dx=app.wpawn6x
    app.wp6dy=app.wpawn6y
    for i in range(2):
        app.wp6dx-=1
        if app.chessBoard[app.wp6dx][app.wp6dy]==0:
           app.wpmov.append((app.wp6dx,app.wp6dy))
def legalWpawn7Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp7dx=app.wpawn7x
    app.wp7dy=app.wpawn7y
    for i in range(2):
        app.wp7dx-=1
        if app.chessBoard[app.wp7dx][app.wp7dy]==0:
           app.wpmov.append((app.wp7dx,app.wp7dy))
def legalWpawn8Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.wp8dx=app.wpawn8x
    app.wp8dy=app.wpawn8y
    for i in range(2):
        app.wp8dx-=1
        if app.chessBoard[app.wp8dx][app.wp8dy]==0:
           app.wpmov.append((app.wp8dx,app.wp8dy))
def legalBpawn1Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp1dx=app.bpawn1x
    app.bp1dy=app.bpawn1y
    for i in range(2):
        app.bp1dx+=1
        if app.chessBoard[app.bp1dx][app.bp1dy]==0:
           app.bpmov.append((app.bp1dx,app.bp1dy))
def legalBpawn2Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp2dx=app.bpawn2x
    app.bp2dy=app.bpawn2y
    for i in range(2):
        app.bp2dx+=1
        if app.chessBoard[app.bp2dx][app.bp2dy]==0:
           app.bpmov.append((app.bp2dx,app.bp2dy))
def legalBpawn3Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp3dx=app.bpawn3x
    app.bp3dy=app.bpawn3y
    for i in range(2):
        app.bp3dx+=1
        if app.chessBoard[app.bp3dx][app.bp3dy]==0:
           app.bpmov.append((app.bp3dx,app.bp3dy))
def legalBpawn4Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp4dx=app.bpawn4x
    app.bp4dy=app.bpawn4y
    for i in range(2):
        app.bp4dx+=1
        if app.chessBoard[app.bp4dx][app.bp4dy]==0:
           app.bpmov.append((app.bp4dx,app.bp4dy))
def legalBpawn5Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp5dx=app.bpawn5x
    app.bp5dy=app.bpawn5y
    for i in range(2):
        app.bp5dx+=1
        if app.chessBoard[app.bp5dx][app.bp5dy]==0:
           app.bpmov.append((app.bp5dx,app.bp5dy))
def legalBpawn6Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp6dx=app.bpawn6x
    app.bp6dy=app.bpawn6y
    for i in range(2):
        app.bp6dx+=1
        if app.chessBoard[app.bp6dx][app.bp6dy]==0:
           app.bpmov.append((app.bp6dx,app.bp6dy))
def legalBpawn7Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp7dx=app.bpawn7x
    app.bp7dy=app.bpawn7y
    for i in range(2):
        app.bp7dx+=1
        if app.chessBoard[app.bp7dx][app.bp7dy]==0:
           app.bpmov.append((app.bp7dx,app.bp7dy))
def legalBpawn8Mov(app):
    app.wpmov=[]
    app.bpmov=[]
    app.bp8dx=app.bpawn8x
    app.bp8dy=app.bpawn8y
    for i in range(2):
        app.bp8dx+=1
        if app.chessBoard[app.bp8dx][app.bp8dy]==0:
           app.bpmov.append((app.bp8dx,app.bp8dy))
def legalWrook1Mov(app):
    app.bpmov=[]
    app.wpmov=[]
    app.wr1dx,app.wr1dy=(app.whiteRook1x,app.whiteRook1y)
    while app.wr1dx<7:
        app.wr1dx+=1
        if app.chessBoard[app.wr1dx][app.wr1dy]==0:
            app.wrmov.append((app.wr1dx,app.wr1dy))
        elif app.chessBoard[app.wr1dx][app.wr1dy]!=0:
           break
    app.wr1dx,app.wr1dy=(app.whiteRook1x,app.whiteRook1y)
    while app.wr1dx>0:
        app.wr1dx-=1
        if app.chessBoard[app.wr1dx][app.wr1dy]==0:
            app.wrmov.append((app.wr1dx,app.wr1dy))
        elif app.chessBoard[app.wr1dx][app.wr1dy]!=0:
            break
    app.wr1dx,app.wr1dy=(app.whiteRook1x,app.whiteRook1y)
    while app.wr1dy<7:
        app.wr1dy+=1
        if app.chessBoard[app.wr1dx][app.wr1dy]==0:
            app.wrmov.append((app.wr1dx,app.wr1dy))
        elif app.chessBoard[app.wr1dx][app.wr1dy]!=0:
            break
    app.wr1dx,app.wr1dy=(app.whiteRook1x,app.whiteRook1y)
    while app.wr1dy>0:
        app.wr1dy-=1
        if app.chessBoard[app.wr1dx][app.wr1dy]==0:
            app.wrmov.append((app.wr1dx,app.wr1dy))
        elif app.chessBoard[app.wr1dx][app.wr1dy]!=0:
            break
    print(app.wrmov)
def legalWrook2Mov(app):
    app.bpmov=[]
    app.wpmov=[]
    app.wr2dx,app.wr2dy=(app.whiteRook2x,app.whiteRook2y)
    while app.wr2dx<7:
        app.wr2dx+=1
        if app.chessBoard[app.wr2dx][app.wr2dy]==0:
            app.wrmov.append((app.wr2dx,app.wr2dy))
        elif app.chessBoard[app.wr2dx][app.wr2dy]!=0:
           break
    app.wr2dx,app.wr2dy=(app.whiteRook2x,app.whiteRook2y)
    while app.wr2dx>0:
        app.wr2dx-=1
        if app.chessBoard[app.wr2dx][app.wr2dy]==0:
            app.wrmov.append((app.wr2dx,app.wr2dy))
        elif app.chessBoard[app.wr2dx][app.wr2dy]!=0:
            break
    app.wr2dx,app.wr2dy=(app.whiteRook2x,app.whiteRook2y)
    while app.wr2dy<7:
        app.wr2dy+=1
        if app.chessBoard[app.wr2dx][app.wr2dy]==0:
            app.wrmov.append((app.wr2dx,app.wr2dy))
        elif app.chessBoard[app.wr2dx][app.wr2dy]!=0:
            break
    app.wr2dx,app.wr2dy=(app.whiteRook2x,app.whiteRook2y)
    while app.wr2dy>0:
        app.wr2dy-=1
        if app.chessBoard[app.wr2dx][app.wr2dy]==0:
            app.wrmov.append((app.wr2dx,app.wr2dy))
        elif app.chessBoard[app.wr2dx][app.wr2dy]!=0:
            break
    
    
def mousePressed(app,event):
    app.apmov=[]
    app.bpmov=[]
    app.wrmov=[]
    (app.x,app.y)=getCell(app, event.x, event.y)
    (app.x0,app.y0,app.x1,app.y1)=getCellBounds(app,app.x,app.y)
    if app.chessBoard[app.x][app.y]=="wpawn1":
       legalWpawn1Mov(app)
    elif app.chessBoard[app.x][app.y]=="wpawn2":
       legalWpawn2Mov(app)
    elif app.chessBoard[app.x][app.y]=="wpawn3":
       legalWpawn3Mov(app)
    elif app.chessBoard[app.x][app.y]=="wpawn4":
       legalWpawn4Mov(app)
    elif app.chessBoard[app.x][app.y]=="wpawn5":
       legalWpawn5Mov(app)
    elif app.chessBoard[app.x][app.y]=="wpawn6":
       legalWpawn6Mov(app)
    elif app.chessBoard[app.x][app.y]=="wpawn7":
       legalWpawn7Mov(app)
    elif app.chessBoard[app.x][app.y]=="wpawn8":
       legalWpawn8Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn1":
       legalBpawn1Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn2":
       legalBpawn2Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn3":
       legalBpawn3Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn4":
       legalBpawn4Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn5":
       legalBpawn5Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn6":
       legalBpawn6Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn7":
       legalBpawn7Mov(app)
    elif app.chessBoard[app.x][app.y]=="bpawn8":
       legalBpawn8Mov(app)
    elif app.chessBoard[app.x][app.y]=="wRook1":
       legalWrook1Mov(app)
    elif app.chessBoard[app.x][app.y]=="wRook2":
       legalWrook2Mov(app)
       print(app.x,app.y)
    
    
    
    
def getPixelForChessmen(app,row,col):
    x=340.625+61.25*col
    y=100+61.25*.5224+61.25*(row)
    return (x,y)
        
def pawnPosition(app):
    (app.bpawn1x,app.bpawn1y)=(1,0)
    (app.bpawn2x,app.bpawn2y)=(1,1)
    (app.bpawn3x,app.bpawn3y)=(1,2)
    (app.bpawn4x,app.bpawn4y)=(1,3)
    (app.bpawn5x,app.bpawn5y)=(1,4)
    (app.bpawn6x,app.bpawn6y)=(1,5)
    (app.bpawn7x,app.bpawn7y)=(1,6)
    (app.bpawn8x,app.bpawn8y)=(1,7)
    
    (app.wpawn1x,app.wpawn1y)=(6,0)
    (app.wpawn2x,app.wpawn2y)=(6,1)
    (app.wpawn3x,app.wpawn3y)=(6,2)
    (app.wpawn4x,app.wpawn4y)=(6,3)
    (app.wpawn5x,app.wpawn5y)=(6,4)
    (app.wpawn6x,app.wpawn6y)=(6,5)
    (app.wpawn7x,app.wpawn7y)=(6,6)
    (app.wpawn8x,app.wpawn8y)=(6,7)
    
    (app.bpawn1X,app.bpawn1Y)=getPixelForChessmen(app,app.bpawn1x,app.bpawn1y)
    (app.bpawn2X,app.bpawn2Y)=getPixelForChessmen(app,app.bpawn2x,app.bpawn2y)
    (app.bpawn3X,app.bpawn3Y)=getPixelForChessmen(app,app.bpawn3x,app.bpawn3y)
    (app.bpawn4X,app.bpawn4Y)=getPixelForChessmen(app,app.bpawn4x,app.bpawn4y)
    (app.bpawn5X,app.bpawn5Y)=getPixelForChessmen(app,app.bpawn5x,app.bpawn5y)
    (app.bpawn6X,app.bpawn6Y)=getPixelForChessmen(app,app.bpawn6x,app.bpawn6y)
    (app.bpawn7X,app.bpawn7Y)=getPixelForChessmen(app,app.bpawn7x,app.bpawn7y)
    (app.bpawn8X,app.bpawn8Y)=getPixelForChessmen(app,app.bpawn8x,app.bpawn8y)
    
    (app.wpawn1X,app.wpawn1Y)=getPixelForChessmen(app,app.wpawn1x,app.wpawn1y)
    (app.wpawn2X,app.wpawn2Y)=getPixelForChessmen(app,app.wpawn2x,app.wpawn2y)
    (app.wpawn3X,app.wpawn3Y)=getPixelForChessmen(app,app.wpawn3x,app.wpawn3y)
    (app.wpawn4X,app.wpawn4Y)=getPixelForChessmen(app,app.wpawn4x,app.wpawn4y)
    (app.wpawn5X,app.wpawn5Y)=getPixelForChessmen(app,app.wpawn5x,app.wpawn5y)
    (app.wpawn6X,app.wpawn6Y)=getPixelForChessmen(app,app.wpawn6x,app.wpawn6y)
    (app.wpawn7X,app.wpawn7Y)=getPixelForChessmen(app,app.wpawn7x,app.wpawn7y)
    (app.wpawn8X,app.wpawn8Y)=getPixelForChessmen(app,app.wpawn8x,app.wpawn8y)
#  app.chessBoard=[["bRook1","bKnight1","bBishop1","bQueen","bKing","bBishop2","bKnight2","bRook2"],
#                     ["bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8"],
#                     [0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8"],
#                     ["wRook1","wKnight1","wBishop1","wQueen","wKing","wBishop2","wKnight2","wRook2"]]    
   
    
def chessmenPosition(app):
    app.blackRook1x,app.blackRook1y=(0,0)
    app.blackKnight1x,app.blackKnight1y=(0,1)
    app.blackBishop1x,app.blackBishop1y=(0,2)
    app.blackQueenx,app.blackQueeny=(0,3)
    app.blackKingx,app.blackKingy=(0,4)
    app.blackBishop2x,app.blackBishop2y=(0,5)
    app.blackKnight2x,app.blackKnight2y=(0,6)
    app.blackRook2x,app.blackRook2y=(0,7)
    
    app.whiteRook1x,app.whiteRook1y=(7,0)#(7,0)
    app.whiteKnight1x,app.whiteKnight1y=(7,1)
    app.whiteBishop1x,app.whiteBishop1y=(7,2)
    app.whiteQueenx,app.whiteQueeny=(7,3)
    app.whiteKingx,app.whiteKingy=(7,4)
    app.whiteBishop2x,app.whiteBishop2y=(7,5)
    app.whiteKnight2x,app.whiteKnight2y=(7,6)
    app.whiteRook2x,app.whiteRook2y=(7,7)


            
    app.blackQueenX,app.blackQueenY=getPixelForChessmen(app,app.blackQueenx,app.blackQueeny)
    app.blackKingX,app.blackKingY=getPixelForChessmen(app,app.blackKingx,app.blackKingy)
    app.blackRook1X,app.blackRook1Y=getPixelForChessmen(app,app.blackRook1x,app.blackRook1y)
    app.blackRook2X,app.blackRook2Y=getPixelForChessmen(app,app.blackRook2x,app.blackRook2y)
    app.blackKnight1X,app.blackKnight1Y=getPixelForChessmen(app,app.blackKnight1x,app.blackKnight1y)
    app.blackKnight2X,app.blackKnight2Y=getPixelForChessmen(app,app.blackKnight2x,app.blackKnight2y)
    app.blackBishop1X,app.blackBishop1Y=getPixelForChessmen(app,app.blackBishop1x,app.blackBishop1y)
    app.blackBishop2X,app.blackBishop2Y=getPixelForChessmen(app,app.blackBishop2x,app.blackBishop2y)
    
    app.whiteQueenX,app.whiteQueenY=getPixelForChessmen(app,app.whiteQueenx,app.whiteQueeny)
    app.whiteKingX,app.whiteKingY=getPixelForChessmen(app,app.whiteKingx,app.whiteKingy)
    app.whiteRook1X,app.whiteRook1Y=getPixelForChessmen(app,app.whiteRook1x,app.whiteRook1y)
    app.whiteRook2X,app.whiteRook2Y=getPixelForChessmen(app,app.whiteRook2x,app.whiteRook2y)
    app.whiteKnight1X,app.whiteKnight1Y=getPixelForChessmen(app,app.whiteKnight1x,app.whiteKnight1y)
    app.whiteKnight2X,app.whiteKnight2Y=getPixelForChessmen(app,app.whiteKnight2x,app.whiteKnight2y)
    app.whiteBishop1X,app.whiteBishop1Y=getPixelForChessmen(app,app.whiteBishop1x,app.whiteBishop1y)
    app.whiteBishop2X,app.whiteBishop2Y=getPixelForChessmen(app,app.whiteBishop2x,app.whiteBishop2y)
    
    (app.bpawn1X,app.bpawn1Y)=getPixelForChessmen(app,app.bpawn1x,app.bpawn1y)
    (app.bpawn2X,app.bpawn2Y)=getPixelForChessmen(app,app.bpawn2x,app.bpawn2y)
    (app.bpawn3X,app.bpawn3Y)=getPixelForChessmen(app,app.bpawn3x,app.bpawn3y)
    (app.bpawn4X,app.bpawn4Y)=getPixelForChessmen(app,app.bpawn4x,app.bpawn4y)
    (app.bpawn5X,app.bpawn5Y)=getPixelForChessmen(app,app.bpawn5x,app.bpawn5y)
    (app.bpawn6X,app.bpawn6Y)=getPixelForChessmen(app,app.bpawn6x,app.bpawn6y)
    (app.bpawn7X,app.bpawn7Y)=getPixelForChessmen(app,app.bpawn7x,app.bpawn7y)
    (app.bpawn8X,app.bpawn8Y)=getPixelForChessmen(app,app.bpawn8x,app.bpawn8y)
    
    (app.wpawn1X,app.wpawn1Y)=getPixelForChessmen(app,app.wpawn1x,app.wpawn1y)
    (app.wpawn2X,app.wpawn2Y)=getPixelForChessmen(app,app.wpawn2x,app.wpawn2y)
    (app.wpawn3X,app.wpawn3Y)=getPixelForChessmen(app,app.wpawn3x,app.wpawn3y)
    (app.wpawn4X,app.wpawn4Y)=getPixelForChessmen(app,app.wpawn4x,app.wpawn4y)
    (app.wpawn5X,app.wpawn5Y)=getPixelForChessmen(app,app.wpawn5x,app.wpawn5y)
    (app.wpawn6X,app.wpawn6Y)=getPixelForChessmen(app,app.wpawn6x,app.wpawn6y)
    (app.wpawn7X,app.wpawn7Y)=getPixelForChessmen(app,app.wpawn7x,app.wpawn7y)
    (app.wpawn8X,app.wpawn8Y)=getPixelForChessmen(app,app.wpawn8x,app.wpawn8y)
    

def getCellBounds(app, row, col):
    cellWidth = 61.25
    cellHeight = 61.25
    x0 = 310 + col * cellWidth
    x1 = 310 + (col+1) * cellWidth
    y0 = 100 + row * cellHeight
    y1 = 100 + (row+1) * cellHeight
    return (x0, y0, x1, y1)
def getCell(app, x, y):
    cellWidth = 61.25
    cellHeight = 61.25
    row = int((y - 100) / cellHeight)
    col = int((x - 310) / cellWidth)
    return (row, col)

def drawPawn(app,canvas):
    canvas.create_image(app.bpawn1X,app.bpawn1Y, image=ImageTk.PhotoImage(app.image2))
    canvas.create_image(app.bpawn2X,app.bpawn2Y, image=ImageTk.PhotoImage(app.image2))
    canvas.create_image(app.bpawn3X,app.bpawn3Y, image=ImageTk.PhotoImage(app.image2))
    canvas.create_image(app.bpawn4X,app.bpawn4Y, image=ImageTk.PhotoImage(app.image2))
    canvas.create_image(app.bpawn5X,app.bpawn5Y, image=ImageTk.PhotoImage(app.image2))
    canvas.create_image(app.bpawn6X,app.bpawn6Y, image=ImageTk.PhotoImage(app.image2))
    canvas.create_image(app.bpawn7X,app.bpawn7Y, image=ImageTk.PhotoImage(app.image2))
    canvas.create_image(app.bpawn8X,app.bpawn8Y, image=ImageTk.PhotoImage(app.image2))
    
    canvas.create_image(app.wpawn1X,app.wpawn1Y, image=ImageTk.PhotoImage(app.image4))
    canvas.create_image(app.wpawn2X,app.wpawn2Y, image=ImageTk.PhotoImage(app.image4))
    canvas.create_image(app.wpawn3X,app.wpawn3Y, image=ImageTk.PhotoImage(app.image4))
    canvas.create_image(app.wpawn4X,app.wpawn4Y, image=ImageTk.PhotoImage(app.image4))
    canvas.create_image(app.wpawn5X,app.wpawn5Y, image=ImageTk.PhotoImage(app.image4))
    canvas.create_image(app.wpawn6X,app.wpawn6Y, image=ImageTk.PhotoImage(app.image4))
    canvas.create_image(app.wpawn7X,app.wpawn7Y, image=ImageTk.PhotoImage(app.image4))
    canvas.create_image(app.wpawn8X,app.wpawn8Y, image=ImageTk.PhotoImage(app.image4))
    
    
    
def drawChessmen(app,canvas):
    canvas.create_image(app.blackKnight1X,app.blackKnight1Y, image=ImageTk.PhotoImage(app.image10))
    canvas.create_image(app.blackKnight2X,app.blackKnight2Y, image=ImageTk.PhotoImage(app.image10))
    canvas.create_image(app.whiteKnight1X,app.whiteKnight1Y, image=ImageTk.PhotoImage(app.image12))
    canvas.create_image(app.whiteKnight2X,app.whiteKnight2Y, image=ImageTk.PhotoImage(app.image12))
    canvas.create_image(app.blackBishop1X,app.blackBishop1Y, image=ImageTk.PhotoImage(app.image14))
    canvas.create_image(app.blackBishop2X,app.blackBishop2Y, image=ImageTk.PhotoImage(app.image14))
    canvas.create_image(app.whiteBishop1X,app.whiteBishop1Y, image=ImageTk.PhotoImage(app.image16))
    canvas.create_image(app.whiteBishop2X,app.whiteBishop2Y, image=ImageTk.PhotoImage(app.image16))
    canvas.create_image(app.blackKingX,app.blackKingY, image=ImageTk.PhotoImage(app.image18))
    canvas.create_image(app.whiteKingX,app.whiteKingY, image=ImageTk.PhotoImage(app.image20))
    canvas.create_image(app.blackQueenX,app.blackQueenY, image=ImageTk.PhotoImage(app.image6))
    canvas.create_image(app.whiteQueenX,app.whiteQueenY, image=ImageTk.PhotoImage(app.image8))
    canvas.create_image(app.blackRook1X,app.blackRook1Y, image=ImageTk.PhotoImage(app.image22))
    canvas.create_image(app.blackRook2X,app.blackRook2Y, image=ImageTk.PhotoImage(app.image22))
    canvas.create_image(app.whiteRook1X,app.whiteRook1Y, image=ImageTk.PhotoImage(app.image24))
    canvas.create_image(app.whiteRook2X,app.whiteRook2Y, image=ImageTk.PhotoImage(app.image24))
    
    
    
def drawBoard(app, canvas):
#colors collected from "https://htmlcolorcodes.com/color-names/"
    canvas.create_rectangle(310,100,800,590)
    for i in range(8):
        for j in range(8):
            if i%2==0 and j%2==0:
                if i==app.x and j==app.y:
                   canvas.create_rectangle(310+(490/8)*i,100+(490/8)*j,
                                        310+(490/8)*(i+1),100+(490/8)*(j+1),fill="#AFEEEE") 
                canvas.create_rectangle(310+(490/8)*i,100+(490/8)*j,
                                        310+(490/8)*(i+1),100+(490/8)*(j+1),fill="#AFEEEE")
            if i%2==1 and j%2==1:
                canvas.create_rectangle(310+(490/8)*i,100+(490/8)*j,
                                        310+(490/8)*(i+1),100+(490/8)*(j+1),fill="#AFEEEE")
            
            if (i%2==0 and j%2==1) or (i%2==1 and j%2==0):
                canvas.create_rectangle(310+(490/8)*i,100+(490/8)*j,
                                        310+(490/8)*(i+1),100+(490/8)*(j+1),fill="#5F9EA0")
    
def drawHighlight(app,canvas):
    canvas.create_rectangle(app.x0,app.y0,app.x1,app.y1,fill="#DEB887")
def drawLegMovwp1(app,canvas):
    for i in app.wpmov:
        (row,col)=(i[0],i[1])
        (x0,y0,x1,y1)=getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill="#D3D3D3") #LightGray
def drawLegMovbp1(app,canvas):
    for i in app.bpmov:
        (row,col)=(i[0],i[1])
        (x0,y0,x1,y1)=getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill="#D3D3D3") #LightGray
def drawLegMovwr(app,canvas):
    for i in app.wrmov:
        (row,col)=(i[0],i[1])
        (x0,y0,x1,y1)=getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill="#D3D3D3") #LightGray
def redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawHighlight(app,canvas)
    drawLegMovwp1(app,canvas)
    drawLegMovbp1(app,canvas)
    drawLegMovwr(app,canvas)
    drawPawn(app,canvas)
    drawChessmen(app,canvas)
    
runApp(width=1300, height=650)
