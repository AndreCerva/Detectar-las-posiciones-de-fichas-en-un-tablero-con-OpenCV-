"""
author: Cervantes Loyola Carlos Andrés
created: 10/06/2021
1. Aplicar una máscara para que sepa qué piezas son blancas y qué piezas son cafés
2. Contar el número de piezas blancas y cafés en el tablero y poner el numero en la imagen
3. A cada pieza blanca se le coloca su posición con texto sobre la misma pieza con texto color azul
5. A cada pieza café se le coloca su posición con texto sobre la misma pieza con texto color verde
"""
#Importamos librerias utiles
import cv2
import numpy as np
import pandas as pd
#Creamos variables globales para ingresarlas entre funciones
global c,cx,cy,bx,by,ax,ay,A8
cx=0
cy=0
ax=0
ay=0
bx=0
by=0
#----------------------------------------------------------------------Posiciones según tablero
"""'['A8','B8','C8','D8','E8','F8','G8,H8]
    ['A7','B7','C7','D7','E7','F7','G7,H7]
    ['A6','B6','C6','D6','E6','F6','G6',H6]
    ['A5','B5','C5','D5','E5','F5','G5',H5]
    ['A4','B4','C4','D4','E4','F4','G4',H4]
    ['A3','B3','C3','D3','E3','F3','G3',H3]
    ['A2','B2','C2','D2','E2','F2','G2',H2]
    ['A1','B1','C1','D1','E1','F1','G1',H1]"""
#----------------------------------------------------------------------Colores
azul=[255,0,0]
verde=[0,255,0]
rojo=[0,0,255]
blanco=[255,255,255]
negro=[0]
#-----------------------------------------------------------------------Deteccion de posición por lineas en el tablero
def posicion(cx,cy,bx,by):
    global A8
    inte=cx-bx
    intey=cy-by
    #*****************LINEA 1**********************
    if intey>0 and intey<40:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A8'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B8'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C8'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D8'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E8'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F8'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G8'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H8'), (cx-8, cy+5), 2, 0.5, azul)
    # *****************LINEA 2**********************
    elif intey > 40 and intey < 120:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A7'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B7'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C7'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D7'),(cx-8, cy+5), 2, 0.5, azul)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E7'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F7'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G7'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H7'), (cx-8, cy+5), 2, 0.5, azul)
    # *****************LINEA 3**********************
    elif intey > 120 and intey < 190:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A6'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B6'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C6'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D6'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E6'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F6'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G6'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H6'), (cx-8, cy+5), 2, 0.5, azul)
    # *****************LINEA 4**********************
    elif intey > 190 and intey < 270:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A5'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B5'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C5'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D5'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E5'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F5'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G5'), (cx-8, cy+5), 2, 0.5, azul)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H5'), (cx-8, cy+5), 2, 0.5, azul)
    # *****************LINEA 5**********************
    elif intey > 270 and intey < 350:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A4'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B4'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C4'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D4'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E4'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F4'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G4'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H4'), (cx-8, cy+5), 2, 0.5, verde)
    # *****************LINEA 6**********************
    elif intey > 350 and intey < 420:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A3'), (cx-8, cy+5), 2, 0.5,verde)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B3'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C3'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D3'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E3'), (cx-8, cy+5), 2, 0.5,verde)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F3'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G3'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H3'), (cx-8, cy+5), 2, 0.5, verde)
    # *****************LINEA 7**********************
    elif intey > 420 and intey < 500:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A2'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B2'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C2'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D2'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E2'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F2'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G2'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H2'), (cx-8, cy+5), 2, 0.5, verde)
    # *****************LINEA 8**********************
    elif intey > 500 and intey < 600:
        if inte>0 and inte<40:
            cv2.putText(imagen,('A1'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>40 and inte<160:
            cv2.putText(imagen,('B1'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>160 and inte<200:
            cv2.putText(imagen,('C1'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>200 and inte<300:
            cv2.putText(imagen,('D1'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>300 and inte<350:
            cv2.putText(imagen,('E1'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>350 and inte<440:
            cv2.putText(imagen,('F1'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>440 and inte<500:
            cv2.putText(imagen,('G1'), (cx-8, cy+5), 2, 0.5, verde)
        elif inte>500 and inte<600:
            cv2.putText(imagen,('H1'), (cx-8, cy+5), 2, 0.5, verde)
#----------------------------------------------------------------------Detección de contornos
def detection2(mask,color):
    global c,cx,bx,cy,by
    c=0
    contorns, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for i in contorns:
        area = cv2.contourArea(i)
        if area > 3000:
            momentos = cv2.moments(i)
            if momentos['m00'] == 0: momentos['m00'] = 1
            cx = int(momentos['m10'] / momentos['m00'])
            cy = int(momentos['m01'] / momentos['m00'])
            _, radio = cv2.minEnclosingCircle(i)
            radio = int(radio)
            cv2.circle(imagen, (cx, cy), radio, color, 3)
            posicion(cx,cy,bx,by)
            c=c+1
#----------------------------------------------------------------------Limites para las mascaras
blancoligh=np.array([23,0,0],np.uint8)
blacohigh=np.array([30,120,240],np.uint8)
cafeligh=np.array([10,170,0],np.uint8)
cafehigh=np.array([20,255,150],np.uint8)
#---------------------------------------------------------------------Lectura de imagen y transformacion a hsv
imagen=cv2.imread('tablero3.png')
imahsv=cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
#---------------------------------------------------------------------Esquinas tablero
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 5, 3, 0.04)
ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
#imagen[dst > 0.4 * dst.max()] = [0, 0, 255]
for i in corners:
    i[0] = np.round(i[0])
    i[1] = np.round(i[1])
df2 = pd.DataFrame( data = corners, columns=["x","y"])
ymax=df2.max()
ymin=df2.min()
ax=ymax[0]
ay=ymax[1]
bx=ymin[0]
by=ymin[1]
#----------------------------------------------------------------------Mascaras fichas blancas y cafes
maskbla=cv2.inRange(imahsv,blancoligh,blacohigh)
maskcaf=cv2.inRange(imahsv,cafeligh,cafehigh)
maskCavis = cv2.bitwise_and(imagen,imagen,mask=maskcaf)
maskBlavis = cv2.bitwise_and(imagen,imagen,mask=maskbla)
detection2(maskbla,azul)
cv2.putText(imagen, ("Fichas blancas:" + str(c)), (10, 30), 0, 0.9,azul, 2)
detection2(maskcaf,verde)
cv2.putText(imagen, ("Fichas cafes:" + str(c)), (10, 680), 0, 0.9, verde, 2)
#---------------------------------------------------------------------Visualización de resultados
#cv2.imshow('maskcafvis', maskCavis)
cv2.imshow('Resultado', imagen)
#cv2.imshow('Tablero',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()