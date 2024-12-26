import pygame
import random

ENDGAMEEVENT = pygame.event.Event(pygame.USEREVENT+1,{"Fin del juego":"Serpiente ha chocado"})


LEFT = pygame.Vector2(-1,0)
RIGHT = pygame.Vector2(1,0)
UP = pygame.Vector2(0,1)
DOWN=pygame.Vector2(0,-1)

class Snake:

    #nota usar vectores para la posicion, mejor que pares que no se pueden operar con ellos
    def __init__(self,head):

        self.body = []
        self.head = head    #es un vector2 (x,y)
        self.tail = head    # es un vector2 (x,y)
        self.body.append(head)  #lista de pares
        self.length = 1
        self.toward = RIGHT 
        
    def changeToward(self,toward):
        self.toward = toward


    def eat(self): 
       """
       
       Para crecer la cola de la serpiente nos vamos a basar en el anterior elemento a tail:

       si compartes misma coordenada y => se añade a la izquierda o a la derecha 
       si comparten misma coordenada x => se añade arriba o abajo

       Caso particular : solo hay cabeza => se añade en direccion contraria a la que vaya la serpiente
       """
       newTail = pygame.Vector2(0,0)

       if self.length == 1:
            newTail = self.head
            self.tail = newTail
            self.body.append(newTail)
            self.length +=1

    def move(self):
        newhead = self.head +self.toward
        self.body = [newhead]+self.body[:-1]
        self.head = self.body[0]
        self.tail = self.body[-1]

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

        return pygame.Vector2(random.randint(0,self.cols),random.randint(0,self.rows))
    
    def snakeChangesToward(self,toward):
        self.snake.changeToward(toward)

    def snakeMoves(self):
        self.snake.move()

        if self.snake.head[0] >= self.cols or self.snake.head[0] <=0  or self.snake.head[1] == self.rows or self.snake.head[1] <= 0 :
            pygame.event.post(ENDGAMEEVENT)

        if self.snake.head == self.apple: 
            self.snake.eat()
            self.apple = self.generateApple()

     

    
    

        
            
   