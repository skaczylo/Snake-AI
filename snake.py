import pygame
import random

ENDGAMEEVENT = pygame.event.Event(pygame.USEREVENT+1,{"Fin del juego":"Serpiente ha chocado"})


LEFT = pygame.Vector2(-1,0)
RIGHT = pygame.Vector2(1,0)
UP = pygame.Vector2(0,-1)
DOWN=pygame.Vector2(0,+1)

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


    def eat(self,newTail): 
      
       self.body.append(newTail)
       self.tail = newTail
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
        self.apple = self.generateApple()

    def snakeEats(self):
        """
       
       Para crecer la cola de la serpiente nos vamos a basar en el anterior elemento a tail:

       si compartes misma coordenada y => se añade a la izquierda o a la derecha 
       si comparten misma coordenada x => se añade arriba o abajo

       Caso particular : solo hay cabeza => se añade en direccion contraria a la que vaya la serpiente
       """
        
        if self.snake.length == 1:

            if self.snake.toward == RIGHT:
                newTailToward = LEFT
            if self.snake.toward == LEFT:
                newTailToward = RIGHT
            if self.snake.toward == UP:
                newTailToward = DOWN
            if self.snake.toward == DOWN:
                newTailToward =UP
            
            self.snake.eat(self.snake.head+newTailToward)

        elif self.snake.length >1:
            subTail = self.snake.body[self.snake.length-2]
            tail = self.snake.tail

            #Miramos que coordenada comparten
            if subTail[0] == tail[0]: #comparten coordenada x
                if subTail[1]<tail[1]: #Se anyade ARRIBA
                    newTail = tail +UP
                else:
                    newTail = tail +DOWN
            elif subTail[1] == tail[1]: #comparten coordenada y
                if subTail[1]<tail[1]: #Se anyade a la derecha
                    newTail = tail+RIGHT
                else:
                    newTail = tail+LEFT
            
                
            self.snake.eat(newTail)


    def generateApple(self):
        newApple = pygame.Vector2(random.randint(0,self.cols-1),random.randint(0,self.rows-1))

        while newApple in self.snake.body:
             newApple = pygame.Vector2(random.randint(0,self.cols-1),random.randint(0,self.rows-1))
        
        return newApple
    
    def snakeChangesToward(self,toward):
        self.snake.changeToward(toward)


    def snakeMoves(self):
        self.snake.move()

        if self.bodyOutOfBoard(self.snake.head) :
            pygame.event.post(ENDGAMEEVENT)

        if self.snake.head == self.apple: 
            self.apple = self.generateApple()
            self.snakeEats()
    

    def bodyOutOfBoard(self,pos):
         return pos[0] > self.cols or pos[0] <0  or pos[1] > self.rows or pos[1] < 0 
           

     

    
    

        
            
   