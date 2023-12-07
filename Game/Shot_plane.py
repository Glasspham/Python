import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ trò chơi
screen_width = 836
screen_height = 810
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Tải hình ảnh máy bay và tiểu hành tinh
player_img = pygame.image.load("") # Tự kiếm anh chèn vào
asteroid_img = pygame.image.load("") # Tự kiếm anh chèn vào

# Kích thước máy bay và tiểu hành tinh
player_width = 66
player_height = 64
asteroid_width = 32
asteroid_height = 32

# Vị trí ban đầu của máy bay
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10

# Tốc độ di chuyển của máy bay
player_speed = 2

# Danh sách các tiểu hành tinh
asteroids = []

# Hàm để tạo tiểu hành tinh mới
def create_asteroid():
    x = random.randint(0, screen_width - asteroid_width)
    y = random.randint(-screen_height, -asteroid_height)
    asteroids.append([x, y])

# Hàm để vẽ các đối tượng lên màn hình
def draw_objects():
    screen.blit(player_img, (player_x, player_y))
    for asteroid in asteroids:
        screen.blit(asteroid_img, (asteroid[0], asteroid[1]))

# Vòng lặp chính của trò chơi
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xử lý phím di chuyển của máy bay
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < screen_width - player_width:
        player_x += player_speed

    # Di chuyển tiểu hành tinh và kiểm tra va chạm
    for asteroid in asteroids:
        asteroid[1] += 1
        if asteroid[1] > screen_height:
            asteroids.remove(asteroid)
        if (player_x < asteroid[0] + asteroid_width and
            player_x + player_width > asteroid[0] and
            player_y < asteroid[1] + asteroid_height and
            player_y + player_height > asteroid[1]):
            running = False

    # Tạo tiểu hành tinh mới
    if random.randint(0, 100) < 2:
        create_asteroid()

    # Vẽ các đối tượng lên màn hình
    screen.fill((0, 0, 0))
    draw_objects()
    pygame.display.flip()

# Kết thúc trò chơi
pygame.quit()
