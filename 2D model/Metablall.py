import pygame
import random
pygame.init()


WIDTH = 800
HEIGH = 800
TIME = 0.4
REZ = 20
CONTOUR_EN = 1.5
Lightblue = "#23e8e8"
WIN = pygame.display.set_mode((WIDTH,HEIGH))
pygame.display.set_caption("METABALL")

#-------------
def calculate(e0,a0,e1,a1):
    x = (CONTOUR_EN-e0)*(a1-a0)/(e1-e0) + a0
    return x

def distance(ob1,ob2):
    dx = ob1[0] - ob2[0]
    dy = ob1[1] - ob2[1]
    distance = (dx**2 + dy**2)**0.5
    return distance


#-------------
def draw_link(corner_0, corner_1, corner_2, corner_3):
    x1 = []
    x2 = []
    if corner_0[0][0] == corner_1[0][0]:
        x1 = [corner_0[0][0], calculate(corner_0[1], corner_0[0][1], corner_1[1], corner_1[0][1])]
    else: 
        x1 = [calculate(corner_0[1], corner_0[0][0], corner_1[1], corner_1[0][0]), corner_0[0][1]]
    if corner_2[0][0] == corner_3[0][0]:
        x2 = [corner_2[0][0], calculate(corner_2[1], corner_2[0][1], corner_3[1], corner_3[0][1])]
    else: 
        x2 = [calculate(corner_2[1], corner_2[0][0], corner_3[1], corner_3[0][0]), corner_2[0][1]]
    pygame.draw.line(WIN, Lightblue, x1, x2, 3)

def state_case(corner_po, balls):
    square_state = []
    c = 0
    for corner in corner_po:
        energy = 0
        for ball in balls:
            d = distance(ball.position, corner[0])
            if d!= 0: energy += ball.radius/d
        corner_po[c].append(energy)
        c+=1
        
        if energy > CONTOUR_EN:
            square_state.append(1)
        else:
            square_state.append(0)  
    state_case = square_state[0] + square_state[1]*2 + square_state[2]*4 + square_state[3]*8
    return state_case

def state(balls):
    rows = int(HEIGH / REZ)
    cols = int(WIDTH / REZ)
    for i in range(0,cols, 1):
        for j in range(0,rows, 1):
            corner_po = [[[i*REZ, j*REZ]], 
                        [[i*REZ + REZ, j*REZ]], 
                        [[i*REZ + REZ, j*REZ + REZ]],
                        [[i*REZ, j*REZ + REZ]]]
           
            
            ball_case = state_case(corner_po,balls)

            match ball_case:
                case 0|15:
                    pass
                case 1|14:
                    draw_link(corner_po[0], corner_po[1], corner_po[0], corner_po[3])
                case 2|13:
                    draw_link(corner_po[0], corner_po[1], corner_po[1], corner_po[2])
                case 3|12:
                    draw_link(corner_po[1], corner_po[2], corner_po[0], corner_po[3])
                case 4|11:
                    draw_link(corner_po[1], corner_po[2], corner_po[2], corner_po[3])
                case 5:
                    draw_link(corner_po[0], corner_po[1], corner_po[1], corner_po[2])
                    draw_link(corner_po[2], corner_po[3], corner_po[0], corner_po[3])
                case 6|9:
                    draw_link(corner_po[0], corner_po[1], corner_po[2], corner_po[3])
                case 7|8:
                    draw_link(corner_po[2], corner_po[3], corner_po[0], corner_po[3])
                case 10:
                    draw_link(corner_po[0], corner_po[1], corner_po[0], corner_po[3])
                    draw_link(corner_po[1], corner_po[2], corner_po[2], corner_po[3])
                case _ : pass
            

#-------------
def energy_net(balls):
    for i in range(0,HEIGH + REZ, REZ):
        for j in range(0,WIDTH + REZ, REZ):
            energy = 0
            for ball in balls:
                energy += ball.radius/distance(ball.position, (j,i))
            if energy >= 0.5 and energy <= 2:
                c = (150)*energy - 75
                d = (-60)*energy + 315
                pygame.draw.circle(WIN, (0,0,c), (j,i), 2)
            elif energy > 2:
                pygame.draw.circle(WIN, (255,255,255), (j,i),2)


#-------------
class Square:
    def __init__ (self, number, corner):
        self.number = number
        self.corner = corner
        
    def corner_energy_cal(self, balls):
        i = 0
        for corner in self.corner:
            energy = 0
            for ball in balls:
                energy += ball.radius/distance(ball.position, corner[0])
            self.corner[i].append(energy)
            i += 1

    def draw_link(self, corner_0, corner_1, corner_2, corner_3):
        x1 = []
        x2 = []
        if corner_0[0][0] == corner_1[0][0]:
            x1 = [corner_0[0][0], calculate(corner_0[1], corner_0[0][1], corner_1[1], corner_1[0][1])]
        else: 
            x1 = [calculate(corner_0[1], corner_0[0][0], corner_1[1], corner_1[0][0]), corner_0[0][1]]
        if corner_2[0][0] == corner_3[0][0]:
            x2 = [corner_2[0][0], calculate(corner_2[1], corner_2[0][1], corner_3[1], corner_3[0][1])]
        else: 
            x2 = [calculate(corner_2[1], corner_2[0][0], corner_3[1], corner_3[0][0]), corner_2[0][1]]

        pygame.draw.line(WIN, Lightblue, x1, x2, 2)


    def marching_square(self, balls):
        self.corner_energy_cal(balls)
        square_state = []
        for i in range(0,4,1):
                if self.corner[i][1] >= 1:
                    square_state.append(1)
                else: 
                    square_state.append(0)
        state_case = square_state[0] + square_state[1]*2 + square_state[2]*4 + square_state[3]*8
        match state_case:
                case 0|15:
                    pass
                case 1|14:
                    self.draw_link(self.corner[0], self.corner[1], self.corner[0], self.corner[3])
                case 2|13:
                    self.draw_link(self.corner[0], self.corner[1], self.corner[1], self.corner[2])
                case 3|12:
                    self.draw_link(self.corner[1], self.corner[2], self.corner[0], self.corner[3])
                case 4|11:
                    self.draw_link(self.corner[1], self.corner[2], self.corner[2], self.corner[3])
                case 5:
                    self.draw_link(self.corner[0], self.corner[1], self.corner[1], self.corner[2])
                    self.draw_link(self.corner[2], self.corner[3], self.corner[0], self.corner[3])
                case 6|9:
                    self.draw_link(self.corner[0], self.corner[1], self.corner[2], self.corner[3])
                case 7|8:
                    self.draw_link(self.corner[2], self.corner[3], self.corner[0], self.corner[3])
                case 10:
                    self.draw_link(self.corner[0], self.corner[1], self.corner[0], self.corner[3])
                    self.draw_link(self.corner[1], self.corner[2], self.corner[2], self.corner[3])

def create_square():
    squares = []
    rows = int(HEIGH / REZ)
    cols = int(WIDTH / REZ)
    for i in range(0,cols, 1):
        for j in range(0,rows, 1):
            squares.append(Square([i,j],
                                  [[[i*REZ, j*REZ]], 
                                   [[i*REZ + REZ, j*REZ]], 
                                   [[i*REZ + REZ, j*REZ + REZ]],
                                   [[i*REZ, j*REZ + REZ]]]))
    return squares


#-------------
class Metaball:

    def __init__(self, position, velocity, radius, color):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def boundary(self):
        if self.position[0] <= self.radius and self.velocity[0] < 0:
            self.velocity[0] *= -1
        if self.position[0] >= WIDTH - self.radius and self.velocity[0] > 0:
            self.velocity[0] *= -1
        if self.position[1] <= self.radius and self.velocity[1] < 0:
            self.velocity[1] *= -1
        if self.position[1] >= HEIGH - self.radius and self.velocity[1] > 0:
            self.velocity[1] *= -1

    def position_update(self):
        
        self.boundary()

        self.position[0] += self.velocity[0] * TIME 
        self.position[1] += self.velocity[1] * TIME
        
        return self.position
    
    def draw_circle(self):
            pygame.draw.circle(WIN, self.color, self.position_update(), self.radius, 1)

def create_circle(color,number):
    balls = []
    for i in range(0, number):
        radius = random.randint(50,80)
        position = [random.randint(0,WIDTH), random.randint(0,HEIGH)]
        velocity = [random.uniform(-10,10), random.uniform(-10,10)]
        balls.append(Metaball(position, velocity, radius, color))
    return balls


#-------------
def main():
    run = True
    clock = pygame.time.Clock()
   
    balls = create_circle(Lightblue, 3)
    #squares = create_square()


    while run:
        clock.tick(100)
        WIN.fill("black")

        state(balls)
        '''energy_net(balls)'''

        for ball in balls:
            #ball.draw_circle()
            ball.position_update()

        '''for square in squares:
            square.marching_square(balls)'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
    pygame.quit()
        
if __name__ == "__main__":
    main()