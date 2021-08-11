from cmu_112_graphics import *
from tkinter import *
import sys

def appStarted(app):
    app.player2={"bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8","bRook1","bKnight1","bBishop1","bQueen","bKing","bBishop2","bKnight2","bRook2"}
    app.player1={"wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8","wRook1","wKnight1","wBishop1","wQueen","wKing","wBishop2","wKnight2","wRook2"}
    app.move=False
    app.player1chance=True
    app.player2chance=False
    app.tokill=[]
    app.tokillpiece=[]
    app.m=[]
    app.movingplaces=[]
    app.allMovingPlaces=[]
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
    (app.br1dx,app.br1dy)=(-1,-1)
    (app.br2dx,app.br2dy)=(-1,-1)
    
    (app.wk1dx,app.wk1dy)=(-1,-1)
    (app.wk2dx,app.wk2dy)=(-1,-1)
    (app.bk1dx,app.bk1dy)=(-1,-1)
    (app.bk2dx,app.bk2dy)=(-1,-1)
    
    (app.wb1dx,app.wb1dy)=(-1,-1)
    (app.wb2dx,app.wb2dy)=(-1,-1)
    (app.bb1dx,app.bb1dy)=(-1,-1)
    (app.bb2dx,app.bb2dy)=(-1,-1)
    
    (app.wqx,app.wqy)=(-1,-1)
    (app.bqx,app.bqy)=(-1,-1)
    (app.wkx,app.wky)=(-1,-1)
    (app.bkx,app.bky)=(-1,-1)
    (app.checkx,app.checky)=(8,7)
    app.message=""
    
    app.pmov=[]
    app.wrmov=[]
    chessplayerimage(app)
    app.chessBoard=[["bRook1","bKnight1","bBishop1","bQueen",0,"bBishop2","bKnight2","bRook2"],
                    ["bpawn1","bpawn2","bpawn3","bpawn4","bpawn5","bpawn6","bpawn7","bpawn8"],
                    [0,0,0,0,0,0,0,0],
                    [0,0,"bKing",0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    ["wpawn1","wpawn2","wpawn3","wpawn4","wpawn5","wpawn6","wpawn7","wpawn8"],
                    ["wRook1","wKnight1","wBishop1","wQueen","wKing","wBishop2","wKnight2","wRook2"],
                    [0,0,0,0,0,0,0,0]]
    pawnPosition(app)
    chessmenPosition(app)
    if app.player1chance==True:
        app.message="Player 1: It's your turn"
    if app.player2chance==True:
        app.message="Player 2: It's your turn"
def chessplayerimage(app):
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
def legalpawnMov(app,x,y,a,b,c):

    app.pmov=[]
    a,b=x,y
    for i in range(2):
        if c=="w":
            a-=1
        elif c=="b":
            a+=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
    a,b=x,y
    if c=="w" and a>0 and b<7:
        a-=1
        b+=1
        if app.chessBoard[a][b] in app.player2:
           app.tokill.append((a,b))
           app.tokillpiece.append(app.chessBoard[a][b])
    
    if c=="w" and a>0 and b>0:
        a,b=x,y
        a-=1
        b-=1
        if app.chessBoard[a][b] in app.player2:
           app.tokill.append((a,b))
           app.tokillpiece.append(app.chessBoard[a][b])
    if c=="b" and a<7 and b>0:
        a,b=x,y
        a+=1
        b-=1
        if app.chessBoard[a][b] in app.player1:
           app.tokill.append((a,b))
           app.tokillpiece.append(app.chessBoard[a][b])
    a,b=x,y
    if c=="b" and b<7 and a<7:
        a+=1
        b+=1
        if app.chessBoard[a][b] in app.player1:
           app.tokill.append((a,b))
           app.tokillpiece.append(app.chessBoard[a][b])
    
def attackOpponent(app,a,b,c):
    if c=="w":
       if app.chessBoard[a][b] in app.player2:
          app.tokill.append((a,b))
          app.tokillpiece.append(app.chessBoard[a][b])
    if c=="b":
       if app.chessBoard[a][b] in app.player1:
          app.tokill.append((a,b))
          app.tokillpiece.append(app.chessBoard[a][b])
       
def legalrookMov(app,x,y,a,b,c):
    app.pmov=[]
    a,b=x,y
    while a<7:
        a+=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break
    a,b=x,y
    while a>0:
        a-=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
            break
    a,b=x,y
    while b<7:
        b+=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
            break
    a,b=x,y
    while b>0:
        b-=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
            break
#app.whiteKnight1x,app.whiteKnight1y,app.wk1dx,app.wk1dy
def legalknightMov(app,x,y,a,b,c):
    app.pmov=[]
    a,b=x,y
    while b<6 and a>0:  
        b+=2
        a-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b<6 and a<0:
        b+=2
        a+=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b<7 and a>1:  
        b+=1
        a-=2
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b>0 and a>1:  
        b-=1
        a-=2
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break   
    a,b=x,y
    while b>1 and a<6:  
        a+=1
        b-=2
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b>0 and a>0:
        b-=2
        a-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b<7 and a<6:  
        b+=1
        a+=2
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b>0 and a<6:  
        b-=1
        a+=2
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
def legalbishopMov(app,x,y,a,b,c):
    app.pmov=[]
    (a,b)=(x,y)
    while a<7 and b>0:
        a+=1
        b-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break
    (a,b)=(x,y)
    while b<7 and a>0:
        b+=1
        a-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
            break
    (a,b)=(x,y)
    while a>0 and b>0:
        a-=1
        b-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break
    (a,b)=(x,y)
    while a<7 and b<7:
        a+=1
        b+=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break

def legalqueenMov(app,x,y,a,b,c):
    legalrookMov(app,x,y,a,b,c)
    (a,b)=(x,y)
    while a<7 and b>0:
        a+=1
        b-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break
    (a,b)=(x,y)
    while b<7 and a>0:
        b+=1
        a-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break
    (a,b)=(x,y)
    while a>0 and b>0:
        a-=1
        b-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break
    (a,b)=(x,y)
    while a<7 and b<7:
        a+=1
        b+=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        if app.chessBoard[a][b]!=0:
           break
def legalkingMov(app,x,y,a,b,c):
    (a,b)=(x,y)
    while a<7 and b>0:
        a+=1
        b-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    (a,b)=(x,y)
    while b<7 and a>0:
        b+=1
        a-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    (a,b)=(x,y)
    while a>0 and b>0:
        a-=1
        b-=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    (a,b)=(x,y)
    while a<7 and b<7:
        a+=1
        b+=1
        if app.chessBoard[a][b]==0:
           app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while a<7:
        a+=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while a>0:
        a-=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b<7:
        b+=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
    a,b=x,y
    while b>0:
        b-=1
        if app.chessBoard[a][b]==0:
            app.pmov.append((a,b))
        attackOpponent(app,a,b,c)
        break
def checkByKnight(app,p,q,c):
        m,n=p,q
        if m<6 and n<7:
            n-=1
            m-=2
            #print(a,b)
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)
        m,n=p,q
        if n<7 and m>1:
            n+=1
            m-=2
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)
        m,n=p,q
        if m<7 and n<6:
            m+=1
            n+=2
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)
        m,n=p,q
        if m>0 and n<6:
            m-=1
            n+=2
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)
        m,n=p,q
        if n>0 and m<6:
            n-=1
            m+=2
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)
        m,n=p,q
        if n<7 and m<6:
            n+=1
            m+=2
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)       
        m,n=p,q
        if m<7 and n>1:
            m+=1
            n-=2
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)
        m,n=p,q
        if m>0 and n>1:
            m-=1
            n-=2
            if app.chessBoard[m][n]==c:
                app.checkx,app.checky=(m,n)
def checkByBishop(app,p,q,c):
    m,n=p,q
    while m<7 and n>0:
        m+=1
        n-=1        
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
    m,n=p,q
    while m>0 and n<7:
        m-=1
        n+=1        
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
    m,n=p,q
    while m>0 and n>0:
        m-=1
        n-=1        
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
    m,n=p,q
    while m<7 and n<7:
        m+=1
        n+=1       
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
def checkByRook(app,p,q,c):
    m,n=p,q
    while m<7 and m>0:
        m+=1    
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
    m,n=p,q
    while m<7 and n>0:
        n-=1
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
    m,n=p,q
    while m>0 and n>0:
        m-=1
        
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
    m,n=p,q
    while m<7 and n<7:
        n+=1       
        if app.chessBoard[m][n]==c:
           app.checkx,app.checky=(m,n)
           break
        if app.chessBoard[m][n]!=0:
            break
def checkByQueen(app,p,q,c):
    checkByBishop(app,p,q,c)
    checkByRook(app,p,q,c)
def checkByPawn(app,p,q,c):
    m,n=p,q
    if c=="w" and m>0 and n<7:
        m-=1
        n+=1
        if app.chessBoard[m][n] == "bKing":
           app.checkx,app.checky=(m,n)
           
    m,n=p,q
    if c=="w" and m>0 and n>0:
        m-=1
        n-=1
        if app.chessBoard[m][n]=="bKing":
           app.checkx,app.checky=(m,n)
    m,n=p,q
    if c=="b" and m<7 and n>0:
        m+=1
        n-=1
        if app.chessBoard[m][n]=="wKing":
           app.checkx,app.checky=(m,n)
    m,n=p,q
    if c=="b" and m<7 and n<7:
        m+=1
        n+=1
        if app.chessBoard[m][n]=="wKing":
           app.checkx,app.checky=(m,n)
def checkByAll(app):
    for i in range(len(app.chessBoard)):
        for j in range(len(app.chessBoard[i])):
            if app.chessBoard[i][j]=="wKnight2" or app.chessBoard[i][j]=="wKnight1":              
               checkByKnight(app,i,j,"bKing")
            elif app.chessBoard[i][j]=="bKnight2" or app.chessBoard[i][j]=="bKnight1":
               checkByKnight(app,i,j,"wKing")
            elif app.chessBoard[i][j]=="wBishop1" or app.chessBoard[i][j]=="wBishop2":
               checkByBishop(app,i,j,"bKing")
            elif app.chessBoard[i][j]=="bBishop1" or app.chessBoard[i][j]=="bBishop2":
               checkByBishop(app,i,j,"wKing")
            elif app.chessBoard[i][j]=="bRook1" or app.chessBoard[i][j]=="bRook2":
               checkByRook(app,i,j,"wKing")
            elif app.chessBoard[i][j]=="wRook1" or app.chessBoard[i][j]=="wRook2":
               checkByRook(app,i,j,"bKing")
               
            elif app.chessBoard[i][j]=="bQueen":
               checkByQueen(app,i,j,"wKing")
            elif app.chessBoard[i][j]=="wQueen":
               checkByQueen(app,i,j,"bKing")
            elif (app.chessBoard[i][j]=="wpawn1" or app.chessBoard[i][j]=="wpawn2" or app.chessBoard[i][j]=="wpawn3" or app.chessBoard[i][j]=="wpawn4" or app.chessBoard[i][j]=="wpawn5" or app.chessBoard[i][j]=="wpawn6" or app.chessBoard[i][j]=="wpawn7" or app.chessBoard[i][j]=="wpawn8"):
               checkByPawn(app,i,j,"w")
            elif (app.chessBoard[i][j]=="bpawn1" or app.chessBoard[i][j]=="bpawn2" or app.chessBoard[i][j]=="bpawn3" or app.chessBoard[i][j]=="bpawn4" or app.chessBoard[i][j]=="bpawn5" or app.chessBoard[i][j]=="bpawn6" or app.chessBoard[i][j]=="bpawn7" or app.chessBoard[i][j]=="bpawn8"):
               checkByPawn(app,i,j,"b")
# def kingCheckIdentifier(app,x,y,a,b):
#     (a,b)=(x,y)
#     b+=1
#     while a<7 and b>0:
#         a+=1
#         b-=1
#         if app.chessBoard[a][b]!=0:
#             if app.chessBoard[a][b]=="wBishop1" or app.chessBoard[a][b]=="wBishop2" :
#                break      
#     (a,b)=(x,y)
#     
#     while b<7 and a>0:
#         b+=1
#         a-=1
#         if app.chessBoard[a][b]==0:
#            app.pmov.append((a,b))
#         attackOpponent(app,a,b,c)
#         if app.chessBoard[a][b]!=0:
#             break
#     (a,b)=(x,y)
#     while a>0 and b>0:
#         a-=1
#         b-=1
#         if app.chessBoard[a][b]==0:
#            app.pmov.append((a,b))
#         attackOpponent(app,a,b,c)
#         if app.chessBoard[a][b]!=0:
#            break
#     (a,b)=(x,y)
#     while a<7 and b<7:
#         a+=1
#         b+=1
#         if app.chessBoard[a][b]==0:
#            app.pmov.append((a,b))
#         attackOpponent(app,a,b,c)
#         if app.chessBoard[a][b]!=0:
#             break
def pawnAttack(app):
    app.wp1dx,app.wp1dy=app.wpawn1x,app.wpawn1y
    app.wp1dx-=1
    app.wp1dy-=1
    #if app.chessBoard[app.wp1dx][app.wp1dy] in app.player2:
        
    
    
def mousePressed(app,event):
    #pawnModifiedPosition(app)
#     if app.player1chance==True:
#         app.message="Player 1: It's your turn"
#     if app.player2chance==True:
#         app.message="Player 2: It's your turn"
    (app.x,app.y)=getCell(app, event.x, event.y)
    app.allMovingPlaces.append((app.x,app.y))
    #print(app.allMovingPlaces)
    if app.chessBoard[app.x][app.y]!=0:
        app.m.append(app.chessBoard[app.x][app.y])
        app.movingplaces.append((app.x,app.y))
    if (app.x,app.y) in app.pmov:
        app.checkx,app.checky=(8,6)
        #changeValAbsent(app)
        app.move=True
        app.tokill=[]
        app.chessBoard[app.x][app.y]=app.m[-1]
        a=app.movingplaces[-1]
        app.chessBoard[a[0]][a[1]]=0
        pawnModifiedPosition(app)
        chessmenModifiedPosition(app)
        #print(app.chessBoard)
        #print(app.chessBoard[5][7])
        #print(app.movingplaces[-1])
#         if app.m[-1]=="wKnight2" or app.m[-1]=="wKnight1":
#            b=app.allMovingPlaces[-1]
#            checkByKnight(app,b[0],b[1],"bKing")
#         elif app.m[-1]=="bKnight2" or app.m[-1]=="bKnight1":
#            b=app.allMovingPlaces[-1]
#            checkByKnight(app,b[0],b[1],"wKing")
#         elif app.m[-1]=="wBishop1" or app.m[-1]=="wBishop2":
#            b=app.allMovingPlaces[-1]
#            checkByBishop(app,b[0],b[1],"bKing")
#         elif app.m[-1]=="bBishop1" or app.m[-1]=="bBishop2":
#            b=app.allMovingPlaces[-1]
#            checkByBishop(app,b[0],b[1],"wKing")
#         elif app.m[-1]=="bRook1" or app.m[-1]=="bRook2":
#            b=app.allMovingPlaces[-1]
#            checkByRook(app,b[0],b[1],"wKing")
#         elif app.m[-1]=="wRook1" or app.m[-1]=="wRook2":
#            b=app.allMovingPlaces[-1]
#            checkByRook(app,b[0],b[1],"bKing")
#            
#         elif app.m[-1]=="bQueen":
#            b=app.allMovingPlaces[-1]
#            checkByQueen(app,b[0],b[1],"wKing")
#         elif app.m[-1]=="wQueen":
#            b=app.allMovingPlaces[-1]
#            checkByQueen(app,b[0],b[1],"bKing")
#         elif (app.m[-1]=="wpawn1" or app.m[-1]=="wpawn2" or app.m[-1]=="wpawn3" or app.m[-1]=="wpawn4" or app.m[-1]=="wpawn5" or app.m[-1]=="wpawn6" or app.m[-1]=="wpawn7" or app.m[-1]=="wpawn8"):
#            b=app.allMovingPlaces[-1]
#            checkByPawn(app,b[0],b[1],"w")
#         elif (app.m[-1]=="bpawn1" or app.m[-1]=="bpawn2" or app.m[-1]=="bpawn3" or app.m[-1]=="bpawn4" or app.m[-1]=="bpawn5" or app.m[-1]=="bpawn6" or app.m[-1]=="bpawn7" or app.m[-1]=="bpawn8"):
#            b=app.allMovingPlaces[-1]
#            checkByPawn(app,b[0],b[1],"b")
        #print(app.chessBoard)
        
        checkByAll(app)
        app.player1chance=not app.player1chance
        app.player2chance=not app.player2chance
        if app.player1chance==True:
            app.message="Player 1: It's your turn"
        if app.player2chance==True:
            app.message="Player 2: It's your turn"       
        
    elif (app.x,app.y) in app.tokill:
        app.checkx,app.checky=(8,6)
        app.tokill=[]
        b=app.movingplaces[-1]
        app.chessBoard[b[0]][b[1]]=0
        a=app.movingplaces[-2]
        app.chessBoard[a[0]][a[1]]=0
        app.chessBoard[app.x][app.y]=app.m[-2]
        #app.chessBoard[app.x][app.y]=app.m[-1]
        changeValAbsent(app)
        pawnModifiedPosition(app)
        chessmenModifiedPosition(app)
        app.player1chance=not app.player1chance
        app.player2chance=not app.player2chance
        checkByAll(app)
    elif app.move==False:
        if ((app.player1chance==True and app.chessBoard[app.x][app.y] in app.player1) 
                         or (app.player2chance==True and app.chessBoard[app.x][app.y] in app.player2)):    
                app.pmov=[]
                if app.chessBoard[app.x][app.y]=="wpawn1":
                   legalpawnMov(app,app.wpawn1x,app.wpawn1y,app.wp1dx,app.wp1dy,"w")
                elif app.chessBoard[app.x][app.y]=="wpawn2":
                   legalpawnMov(app,app.wpawn2x,app.wpawn2y,app.wp2dx,app.wp2dy,"w")
                elif app.chessBoard[app.x][app.y]=="wpawn3":
                    legalpawnMov(app,app.wpawn3x,app.wpawn3y,app.wp3dx,app.wp3dy,"w")
                elif app.chessBoard[app.x][app.y]=="wpawn4":
                   legalpawnMov(app,app.wpawn4x,app.wpawn4y,app.wp4dx,app.wp4dy,"w")
                elif app.chessBoard[app.x][app.y]=="wpawn5":
                    legalpawnMov(app,app.wpawn5x,app.wpawn5y,app.wp5dx,app.wp5dy,"w")
                elif app.chessBoard[app.x][app.y]=="wpawn6":
                   legalpawnMov(app,app.wpawn6x,app.wpawn6y,app.wp6dx,app.wp6dy,"w")
                elif app.chessBoard[app.x][app.y]=="wpawn7":
                    legalpawnMov(app,app.wpawn7x,app.wpawn7y,app.wp7dx,app.wp7dy,"w")
                elif app.chessBoard[app.x][app.y]=="wpawn8":
                    legalpawnMov(app,app.wpawn8x,app.wpawn8y,app.wp8dx,app.wp8dy,"w")
                
                elif app.chessBoard[app.x][app.y]=="bpawn1":
                    legalpawnMov(app,app.bpawn1x,app.bpawn1y,app.bp1dx,app.bp1dy,"b")
                elif app.chessBoard[app.x][app.y]=="bpawn2":
                    legalpawnMov(app,app.bpawn2x,app.bpawn2y,app.bp2dx,app.bp2dy,"b")
                elif app.chessBoard[app.x][app.y]=="bpawn3":
                    legalpawnMov(app,app.bpawn3x,app.bpawn3y,app.bp3dx,app.bp3dy,"b")
                elif app.chessBoard[app.x][app.y]=="bpawn4":
                    legalpawnMov(app,app.bpawn4x,app.bpawn4y,app.bp4dx,app.bp4dy,"b")
                elif app.chessBoard[app.x][app.y]=="bpawn5":
                    legalpawnMov(app,app.bpawn5x,app.bpawn5y,app.bp5dx,app.bp5dy,"b")
                elif app.chessBoard[app.x][app.y]=="bpawn6":
                    legalpawnMov(app,app.bpawn6x,app.bpawn6y,app.bp6dx,app.bp6dy,"b")
                elif app.chessBoard[app.x][app.y]=="bpawn7":
                    legalpawnMov(app,app.bpawn7x,app.bpawn7y,app.bp7dx,app.bp7dy,"b")
                elif app.chessBoard[app.x][app.y]=="bpawn8":
                    legalpawnMov(app,app.bpawn8x,app.bpawn8y,app.bp8dx,app.bp8dy,"b")
                
                
                
                elif app.chessBoard[app.x][app.y]=="wRook1":
                   legalrookMov(app,app.whiteRook1x,app.whiteRook1y,app.wr1dx,app.wr1dy,"w")
                elif app.chessBoard[app.x][app.y]=="wRook2":
                   legalrookMov(app,app.whiteRook2x,app.whiteRook2y,app.wr2dx,app.wr2dy,"w")
                elif app.chessBoard[app.x][app.y]=="bRook1":
                   legalrookMov(app,app.blackRook1x,app.blackRook1y,app.br1dx,app.br1dy,"b")
                elif app.chessBoard[app.x][app.y]=="bRook2":
                   legalrookMov(app,app.blackRook2x,app.blackRook2y,app.br2dx,app.br2dy,"b")

                elif app.chessBoard[app.x][app.y]=="wBishop1":
                    legalbishopMov(app,app.whiteBishop1x,app.whiteBishop1y,app.wb1dx,app.wb1dy,"w")
                elif app.chessBoard[app.x][app.y]=="wBishop2":
                    legalbishopMov(app,app.whiteBishop2x,app.whiteBishop2y,app.wb2dx,app.wb2dy,"w")
                elif app.chessBoard[app.x][app.y]=="bBishop1":
                    legalbishopMov(app,app.blackBishop1x,app.blackBishop1y,app.bb1dx,app.bb1dy,"b")
                elif app.chessBoard[app.x][app.y]=="bBishop2":
                    legalbishopMov(app,app.blackBishop2x,app.blackBishop2y,app.bb2dx,app.bb2dy,"b")
                    
                elif app.chessBoard[app.x][app.y]=="wQueen":   
                    legalqueenMov(app,app.whiteQueenx,app.whiteQueeny,app.wqx,app.wqy,"w")
                elif app.chessBoard[app.x][app.y]=="bQueen":   
                    legalqueenMov(app,app.blackQueenx,app.blackQueeny,app.bqx,app.bqy,"b")
                elif app.chessBoard[app.x][app.y]=="wKing":
                    legalkingMov(app,app.whiteKingx,app.whiteKingy,app.wkx,app.wky,"w")
                elif app.chessBoard[app.x][app.y]=="bKing":
                    legalkingMov(app,app.blackKingx,app.blackKingy,app.bkx,app.bky,"b")
                    
                elif app.chessBoard[app.x][app.y]=="wKnight1":
                    legalknightMov(app,app.whiteKnight1x,app.whiteKnight1y,app.wk1dx,app.wk1dy,"w")
                elif app.chessBoard[app.x][app.y]=="wKnight2":
                    legalknightMov(app,app.whiteKnight2x,app.whiteKnight2y,app.wk2dx,app.wk2dy,"w")
                elif app.chessBoard[app.x][app.y]=="bKnight1":
                    legalknightMov(app,app.blackKnight1x,app.blackKnight1y,app.bk1dx,app.bk1dy,"b")
                elif app.chessBoard[app.x][app.y]=="bKnight2":
                    legalknightMov(app,app.blackKnight2x,app.blackKnight2y,app.bk2dx,app.bk2dy,"b")
                
def returnPixelValue(app,a):
    if a=="bpawn1":
        return [app.bpawn1x,app.bpawn1y]
    
    
def getPixelForChessmen(app,row,col):
    x=340.625+61.25*col
    y=100+61.25*.5224+61.25*(row)
    return (x,y)
def pawnModifiedPosition(app):
    app.pmov=[]
    for i in range(len(app.chessBoard)):
        for j in range(len(app.chessBoard[i])):
            if app.chessBoard[i][j]=="bpawn1":
                app.bpawn1x,app.bpawn1y=(i,j)
                
            elif app.chessBoard[i][j]=="bpawn2":
                app.bpawn2x,app.bpawn2y=(i,j)
            elif app.chessBoard[i][j]=="bpawn3":
                app.bpawn3x,app.bpawn3y=(i,j)
            elif app.chessBoard[i][j]=="bpawn4":
                app.bpawn4x,app.bpawn4y=(i,j)
            elif app.chessBoard[i][j]=="bpawn5":
                app.bpawn5x,app.bpawn5y=(i,j)
            elif app.chessBoard[i][j]=="bpawn6":
                app.bpawn6x,app.bpawn6y=(i,j)
            elif app.chessBoard[i][j]=="bpawn7":
                app.bpawn7x,app.bpawn7y=(i,j)
            elif app.chessBoard[i][j]=="bpawn8":
                app.bpawn8x,app.bpawn8y=(i,j)
                
            elif app.chessBoard[i][j]=="wpawn1":
                app.wpawn1x,app.wpawn1y=(i,j)
            elif app.chessBoard[i][j]=="wpawn2":
                app.wpawn2x,app.wpawn2y=(i,j)
            elif app.chessBoard[i][j]=="wpawn3":
                app.wpawn3x,app.wpawn3y=(i,j)
            elif app.chessBoard[i][j]=="wpawn4":
                app.wpawn4x,app.wpawn4y=(i,j)
            elif app.chessBoard[i][j]=="wpawn5":
                app.wpawn5x,app.wpawn5y=(i,j)
            elif app.chessBoard[i][j]=="wpawn6":
                app.wpawn6x,app.wpawn6y=(i,j)
            elif app.chessBoard[i][j]=="wpawn7":
                app.wpawn7x,app.wpawn7y=(i,j)
            elif app.chessBoard[i][j]=="wpawn8":
                app.wpawn8x,app.wpawn8y=(i,j)
                
    
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
def chessmenModifiedPosition(app):
    app.pmov=[]
    for i in range(len(app.chessBoard)):
        for j in range(len(app.chessBoard[i])):
            if app.chessBoard[i][j]==0:
                continue
            elif app.chessBoard[i][j]=="bRook1":
               app.blackRook1x,app.blackRook1y=(i,j)
            elif app.chessBoard[i][j]=="bKnight1":
               app.blackKnight1x,app.blackKnight1y=(i,j)
            elif app.chessBoard[i][j]=="bBishop1":
               app.blackBishop1x,app.blackBishop1y=(i,j)
            elif app.chessBoard[i][j]=="bQueen":
               app.blackQueenx,app.blackQueeny=(i,j)
            elif app.chessBoard[i][j]=="bKing":
               app.blackKingx,app.blackKingy=(i,j)
            elif app.chessBoard[i][j]=="bBishop2":
               app.blackBishop2x,app.blackBishop2y=(i,j)
            elif app.chessBoard[i][j]=="bKnight2":
               app.blackKnight2x,app.blackKnight2y=(i,j)
            elif app.chessBoard[i][j]=="bRook2":
               app.blackRook2x,app.blackRook2y=(i,j)
               
            
            elif app.chessBoard[i][j]=="wRook1":
               app.whiteRook1x,app.whiteRook1y=(i,j)
            elif app.chessBoard[i][j]=="wKnight1":
               app.whiteKnight1x,app.whiteKnight1y=(i,j)
            elif app.chessBoard[i][j]=="wBishop1":
               app.whiteBishop1x,app.whiteBishop1y=(i,j)
            elif app.chessBoard[i][j]=="wQueen":
               app.whiteQueenx,app.whiteQueeny=(i,j)
            elif app.chessBoard[i][j]=="wKing":
               app.whiteKingx,app.whiteKingy=(i,j)
            elif app.chessBoard[i][j]=="wBishop2":
               app.whiteBishop2x,app.whiteBishop2y=(i,j)
            elif app.chessBoard[i][j]=="wKnight2":
               app.whiteKnight2x,app.whiteKnight2y=(i,j)
            elif app.chessBoard[i][j]=="wRook2":
               app.whiteRook2x,app.whiteRook2y=(i,j)

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
    app.move=False
    
def findInBoard(app,x):
    for i in range(len(app.chessBoard)):
        if x in app.chessBoard[i]:
            return True
    return False
def changeValAbsent(app):
    if findInBoard(app,"wpawn1")==False:
        app.wpawn1x,app.wpawn1y=(8,7)
    if findInBoard(app,"wpawn2")==False:
        app.wpawn2x,app.wpawn2y=(8,7)
    if findInBoard(app,"wpawn3")==False:
        app.wpawn3x,app.wpawn3y=(8,7)
    if findInBoard(app,"wpawn4")==False:
        app.wpawn4x,app.wpawn4y=(8,7)
    if findInBoard(app,"wpawn5")==False:
        app.wpawn5x,app.wpawn5y=(8,7)
    if findInBoard(app,"wpawn6")==False:
        app.wpawn6x,app.wpawn6y=(8,7)
    if findInBoard(app,"wpawn7")==False:
        app.wpawn7x,app.wpawn7y=(8,7)
    if findInBoard(app,"wpawn8")==False:
        app.wpawn8x,app.wpawn8y=(8,7)
        
    
    if findInBoard(app,"bpawn1")==False:
        app.bpawn1x,app.bpawn1y=(8,7)
    if findInBoard(app,"bpawn2")==False:
        app.bpawn2x,app.bpawn2y=(8,7)
    if findInBoard(app,"bpawn3")==False:
        app.bpawn3x,app.bpawn3y=(8,7)
    if findInBoard(app,"bpawn4")==False:
        app.bpawn4x,app.bpawn4y=(8,7)
    if findInBoard(app,"bpawn5")==False:
        app.bpawn5x,app.bpawn5y=(8,7)
    if findInBoard(app,"bpawn6")==False:
        app.bpawn6x,app.bpawn6y=(8,7)
    if findInBoard(app,"bpawn7")==False:
        app.bpawn7x,app.bpawn7y=(8,7)
    if findInBoard(app,"bpawn8")==False:
        app.bpawn8x,app.bpawn8y=(8,7)
    
    if findInBoard(app,"wRook1")==False:
       app.whiteRook1x,app.whiteRook1y=(8,7)
    if findInBoard(app,"wRook2")==False:
       app.whiteRook2x,app.whiteRook2y=(8,7)
    if findInBoard(app,"wKnight1")==False:  
        app.whiteKnight1x,app.whiteKnight1y=(8,7)
    if findInBoard(app,"wKnight2")==False:
        app.whiteKnight2x,app.whiteKnight2y=(8,7)
    if findInBoard(app,"wBishop1")==False:  
        app.whiteBishop1x,app.whiteBishop1y=(8,7)
    if findInBoard(app,"wBishop2")==False:
        app.whiteBishop2x,app.whiteBishop2y=(8,7)
    if findInBoard(app,"wQueen")==False:  
        app.whiteQueenx,app.whiteQueeny=(8,7)
    if findInBoard(app,"wKing")==False:
        app.whiteKingx,app.whiteKingy=(8,7)
        
    if findInBoard(app,"bRook1")==False:
       app.blackRook1x,app.blackRook1y=(8,7)
    if findInBoard(app,"bRook2")==False:
       app.blackRook2x,app.blackRook2y=(8,7)
    if findInBoard(app,"bKnight1")==False:  
        app.blackKnight1x,app.blackKnight1y=(8,7)
    if findInBoard(app,"bKnight2")==False:
        app.blackKnight2x,app.blackKnight2y==(8,7)
    if findInBoard(app,"bBishop1")==False:  
        app.blackBishop1x,app.blackBishop1y=(8,7)
    if findInBoard(app,"bBishop2")==False:
        app.blackBishop2x,app.blackBishop2y=(8,7)
    if findInBoard(app,"bQueen")==False:  
        app.blackQueenx,app.blackQueeny=(8,7)
    if findInBoard(app,"bKing")==False:
        app.blackKingx,app.blackKingy=(8,7)

def pawnPosition(app):
    for i in range(len(app.chessBoard)):
        for j in range(len(app.chessBoard[i])):
            if app.chessBoard[i][j]=="bpawn1":
                app.bpawn1x,app.bpawn1y=(i,j)
            elif app.chessBoard[i][j]=="bpawn2":
                app.bpawn2x,app.bpawn2y=(i,j)
            elif app.chessBoard[i][j]=="bpawn3":
                app.bpawn3x,app.bpawn3y=(i,j)
            elif app.chessBoard[i][j]=="bpawn4":
                app.bpawn4x,app.bpawn4y=(i,j)
            elif app.chessBoard[i][j]=="bpawn5":
                app.bpawn5x,app.bpawn5y=(i,j)
            elif app.chessBoard[i][j]=="bpawn6":
                app.bpawn6x,app.bpawn6y=(i,j)
            elif app.chessBoard[i][j]=="bpawn7":
                app.bpawn7x,app.bpawn7y=(i,j)
            elif app.chessBoard[i][j]=="bpawn8":
                app.bpawn8x,app.bpawn8y=(i,j)
                
            elif app.chessBoard[i][j]=="wpawn1":
                app.wpawn1x,app.wpawn1y=(i,j)
            elif app.chessBoard[i][j]=="wpawn2":
                app.wpawn2x,app.wpawn2y=(i,j)
            elif app.chessBoard[i][j]=="wpawn3":
                app.wpawn3x,app.wpawn3y=(i,j)
            elif app.chessBoard[i][j]=="wpawn4":
                app.wpawn4x,app.wpawn4y=(i,j)
            elif app.chessBoard[i][j]=="wpawn5":
                app.wpawn5x,app.wpawn5y=(i,j)
            elif app.chessBoard[i][j]=="wpawn6":
                app.wpawn6x,app.wpawn6y=(i,j)
            elif app.chessBoard[i][j]=="wpawn7":
                app.wpawn7x,app.wpawn7y=(i,j)
            elif app.chessBoard[i][j]=="wpawn8":
                app.wpawn8x,app.wpawn8y=(i,j)
                
    
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
def chessmenPosition(app):
    for i in range(len(app.chessBoard)):
        for j in range(len(app.chessBoard[i])):
            if app.chessBoard[i][j]==0:
                continue
            elif app.chessBoard[i][j]=="bRook1":
               app.blackRook1x,app.blackRook1y=(i,j)
            elif app.chessBoard[i][j]=="bKnight1":
               app.blackKnight1x,app.blackKnight1y=(i,j)
            elif app.chessBoard[i][j]=="bBishop1":
               app.blackBishop1x,app.blackBishop1y=(i,j)
            elif app.chessBoard[i][j]=="bQueen":
               app.blackQueenx,app.blackQueeny=(i,j)
            elif app.chessBoard[i][j]=="bKing":
               app.blackKingx,app.blackKingy=(i,j)
            elif app.chessBoard[i][j]=="bBishop2":
               app.blackBishop2x,app.blackBishop2y=(i,j)
            elif app.chessBoard[i][j]=="bKnight2":
               app.blackKnight2x,app.blackKnight2y=(i,j)
            elif app.chessBoard[i][j]=="bRook2":
               app.blackRook2x,app.blackRook2y=(i,j)
               
            
            elif app.chessBoard[i][j]=="wRook1":
               app.whiteRook1x,app.whiteRook1y=(i,j)
            elif app.chessBoard[i][j]=="wKnight1":
               app.whiteKnight1x,app.whiteKnight1y=(i,j)
            elif app.chessBoard[i][j]=="wBishop1":
               app.whiteBishop1x,app.whiteBishop1y=(i,j)
            elif app.chessBoard[i][j]=="wQueen":
               app.whiteQueenx,app.whiteQueeny=(i,j)
            elif app.chessBoard[i][j]=="wKing":
               app.whiteKingx,app.whiteKingy=(i,j)
            elif app.chessBoard[i][j]=="wBishop2":
               app.whiteBishop2x,app.whiteBishop2y=(i,j)
            elif app.chessBoard[i][j]=="wKnight2":
               app.whiteKnight2x,app.whiteKnight2y=(i,j)
            elif app.chessBoard[i][j]=="wRook2":
               app.whiteRook2x,app.whiteRook2y=(i,j)

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
        #for j in range(8):
        for j in range(9):
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
            if j==8:            
               canvas.create_rectangle(310+(490/8)*i,100+(490/8)*j,
                                        310+(490/8)*(i+1),100+(490/8)*(j+1),fill="brown")  
    
def drawHighlight(app,canvas):
    canvas.create_rectangle(app.x0,app.y0,app.x1,app.y1,fill="#DEB887")
def drawLegMovwp1(app,canvas):
    for i in app.pmov:
        (row,col)=(i[0],i[1])
        (x0,y0,x1,y1)=getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill="#D3D3D3") #LightGray
def drawAttackPlace(app,canvas):
    for i in app.tokill:
       (row,col)=(i[0],i[1])
       (x0,y0,x1,y1)=getCellBounds(app, row, col)
       canvas.create_rectangle(x0,y0,x1,y1,fill="#FFA07A") #LightSalmon
def drawMessage(app,canvas):
    canvas.create_text(app.width/2,50,text=app.message,fill="darkBlue",font="Times 28 bold")
def drawCheck(app,canvas):
    (x0,y0,x1,y1)=getCellBounds(app, app.checkx,app.checky)
    canvas.create_rectangle(x0,y0,x1,y1,fill="#8B0000")
def redrawAll(app, canvas):
    drawBoard(app, canvas)
    #drawHighlight(app,canvas)
    drawLegMovwp1(app,canvas)
    drawAttackPlace(app,canvas)
    drawCheck(app,canvas)
    drawPawn(app,canvas)
    drawChessmen(app,canvas)
    drawMessage(app,canvas)
    
runApp(width=1300, height=650)

    
