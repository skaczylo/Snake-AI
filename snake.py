import pygame
import random

class Snake:

    #nota usar vectores para la posicion, mejor que pares que no se pueden operar con ellos
    def __init__(self,head):

        self.body = []
        self.head = head    #es un vector2 (x,y)
        self.tail = head    # es un vector2 (x,y)
        self.body.append(head)  #lista de pares
        self.length = 1
        

    def eat(self, pos): 
        #cuando come le aumenta la cola
        #El juego se encarga de la direccion en la que aumenta
        self.tail = pos
        self.body.append(pos)
        self.length +=1
    
    def move(self,toward):
        self.head = self.head + toward
        self.body[0] = self.head
        self.tail = self.head #Si el cuerpo es mayor que 1 se actualiza adecuadamente

        if self.length>1 :
            self.body.pop()
            self.tail = self.body[self.length-1]


class Tablero:

    def __init__(self,rows,cols,snake):
        self.rows = rows
        self.cols = cols
        self.snake = snake
        self.apple = pygame.Vector2(random.randint(0,self.cols),random.randint(0,self.rows))

    def snakeEats(self,towards):
        if self.snake.head == self.apple:
            self.snake.eat(self.snake.tail + towards)

    def generateApple(self):

        pygame.Vector2(random.randint(0,self.cols),random.randint(0,self.rows))
    
    

        
            
   