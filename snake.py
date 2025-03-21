import pygame
import random

ENDGAMEEVENT = pygame.event.Event(pygame.USEREVENT+1,{"Fin del juego":"Serpiente ha chocado con la pared"})
BODYCRASH = pygame.event.Event(pygame.USEREVENT+1,{"Fin del juego":"Serpiente ha chocado con su cuerpo"})

LEFT = pygame.Vector2(-1,0)
RIGHT = pygame.Vector2(1,0)
UP = pygame.Vector2(0,-1)
DOWN=pygame.Vector2(0,+1)


class GameOverException(Exception):
    pass


class Snake:

    #nota usar vectores para la posicion, mejor que pares que no se pueden operar con ellos
    def __init__(self,head):

        self.body = []
        self.head = head    #es un vector2 (x,y)
        self.tail = head    # es un vector2 (x,y)
        self.body.append(head)  #lista de pares
        self.body.append(head+LEFT)
        self.body.append(head+LEFT+LEFT)
        self.length = 3
        self.direction = RIGHT 
    

    def changeDirection(self,direction):
        self.direction = direction

    
    def eat(self,newTail): 
      
       self.body.append(newTail)
       self.tail = newTail
       self.length +=1
       

    def move(self):
        newhead = self.head +self.direction
        self.body = [newhead]+self.body[:-1]
        self.head = self.body[0]
        self.tail = self.body[-1]


class Tablero:

    def __init__(self,rows,cols,snake):
        self.rows = rows
        self.cols = cols
        self.snake = snake
        self.apple = self.generateApple()

        self.snakeMustEat = False
        self.lastTail =snake.tail 

    def generateApple(self):
        newApple = pygame.Vector2(random.randint(0,self.cols-1),random.randint(0,self.rows-1))

        while newApple in self.snake.body:
             newApple = pygame.Vector2(random.randint(0,self.cols-1),random.randint(0,self.rows-1))
        
        return newApple
    
    def snakeChangeDirection(self,direction):
        if not self.checkDirection(direction):
            self.snake.changeDirection(direction)

    def checkDirection(self,direction): #comprueba si la direccion es valida
        return (self.snake.direction == RIGHT and direction == LEFT) or (self.snake.direction == LEFT and direction ==RIGHT) or (self.snake.direction == UP and direction ==DOWN) or (self.snake.direction == DOWN and direction ==UP)
            
      
    def snakeMoves(self):

        """
        La idea es que la serpiente crezca al comer la manzana. Sin embargo, es mejor no hacerlo al instante; sino esperar un turno. Es decir:
        La serpiente alcanza la manzana
        Se mueve
        Al final de este movimiento es cuando crece

        De esta manera el espacio libre que ha dejado la cola al moverse, lo vamos a ocupar como el nuevo miebro del cuerpo de la serpiente y asi no hay que calcular
        posibles huecos libres etc

        """
        if self.snake.head == self.apple: 
            self.snakeMustEat = True #Esperamos al siguiente ciclo para que crezca
            self.lastTail = self.snake.tail #Guardamos la celda libre que va a dejar tras moverse
            self.apple = self.generateApple()

        self.snake.move()
        
        if self.bodyOutOfBoard(self.snake.head) :
            pygame.event.post(ENDGAMEEVENT)
            raise GameOverException()
        if self.bodyCrash(self.snake.head):
            pygame.event.post(BODYCRASH)
            raise GameOverException()


    def snakeEats(self):
        
        if self.snakeMustEat:
            self.snakeMustEat = False
            self.snake.eat(self.lastTail)
            return 1
        
        return 0
      

    def bodyOutOfBoard(self,pos):
         return pos[0] >= self.cols or pos[0] <0  or pos[1] >= self.rows or pos[1] < 0 
    
    def bodyCrash(self,pos):
        return pos in self.snake.body[1:]
           

     

    
    

        
            
   
           

     

    
    

        
            
   