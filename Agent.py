"""
En esta clase se definen los agentes que controlarán el juego. Hay 2 agentes:
- Ser humano
- Inteligencia Artificial

"""
import pygame
import snakeGame
import snake
import numpy as np
import model
from collections import deque
import random
import torch

STATE_DIM = 11
STATE_OUPUT = 4
MEMORY_SIZE = 10000
BATCH_SIZE = 10

class PlayerAgent:
    def __init__(self,game):
        self.game = game
    
    def run(self):
         # pygame setup
        pygame.init()
        clock = pygame.time.Clock()
        self.game.update_graphics()
        gameOver = False
        while not gameOver:

            direction = self.game.handle_events()
            self.game.next_step(direction)
            self.game.update_graphics()
            clock.tick(snakeGame.SPEED)
            gameOver = self.game.gameOver(game.snake.head) 


class AIAgent:

    def __init__(self,game):
        self.game = game
        self.epsilon = 0 #Por defecto elige explotacion
        self.gamma = 0.99 #Factor de descuento : recompensas a largo plazo (aprox 1); recompensas a corto plazo (aprox 0)
        self.model = model.DQN(STATE_DIM,STATE_OUPUT)
        self.memory = deque(maxlen = MEMORY_SIZE)
    
    def decideAction(self,state):

        action = self.game.snake.direction
        
        if random.random() < self.epsilon: #Movimiento aleaotorio
            options = [snake.UP,snake.RIGHT,snake.LEFT,snake.DOWN]
            x = options[random.randint(0,3)] 
            action = x if game.board.checkDirection(x) else action
        else:
            state_tensor = torch.tensor(state)
            prediction = self.model(state_tensor) #resultado de la red neuronal


            

            

    def train(self):
        self.epsilon = 1 #E
        while True:
            old_state = self.getState()

    def getState(self):
        """
        Representar estado solo como las direcciones que no se pueden tomar y las que si; ademas de la manzana
        
        """

        head = game.snake.head
        apple = game.board.apple

        point_r = head +snake.RIGHT
        point_l = head +snake.LEFT
        point_u = head +snake.UP
        point_d = head +snake.DOWN

        dir_r = game.snake.direction == snake.RIGHT
        dir_l= game.snake.direction == snake.LEFT
        dir_u= game.snake.direction == snake.UP
        dir_d= game.snake.direction == snake.DOWN

        state = [
            #4 primeros elementos indican la direccion de la serpiente
            dir_r,
            dir_l,
            dir_u,
            dir_d,

            #Direcciones peligrosas:
            #Tener en cuenta que la cabeza puede continuar su direccion o girar derecha o izquierda(suponer que estas en los ojos de la serpiente)
            #Continuar en la misma direccion => colision
            (dir_r and game.gameOver(point_r) or
             dir_l and game.gameOver(point_l) or
             dir_u and game.gameOver(point_u) or
             dir_d and game.gameOver(point_d)),

            #Girar hacia la derecha => colision
            (dir_u and game.gameOver(point_r) or
             dir_d and game.gameOver(point_l) or
             dir_r and game.gameOver(point_d) or
             dir_l and game.gameOver(point_u)),

             #Girar hacia la izquierda => colision
            (dir_u and game.gameOver(point_l) or
             dir_d and game.gameOver(point_r) or
             dir_r and game.gameOver(point_u) or
             dir_l and game.gameOver(point_d)),

             #Tenemos que indicar mas o menos donde esta la manzana
             head[0]<apple[0], #manzana esta a la derecha
             head[0] >apple[0], #manzana esta a la izquierda
             head[1] > apple[1], #manzana esta mas abajo
             head[1] < apple[1] #manza esta mas arriba
        ]
        return np.array(state,dtype=int) #es un vector de booleanos luego lo convertimos a 1 y 0s


if __name__ == "__main__":
    game = snakeGame.Game()
    jugador = PlayerAgent(game)
    jugador.run()