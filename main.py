import pygame
import sys
import random
from datetime import datetime

pygame.init()

width, height = 800, 600
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('#SAVE PALESTINE')

# Load gambar
image = pygame.image.load('./images/watermelon.png')
image_rect = image.get_rect(center=(width // 2, height // 2))

font = pygame.font.Font(None, 36)
text_save_palestine = font.render('#SAVE PALESTINE', True, (0, 0, 0))
text_rect_save_palestine = text_save_palestine.get_rect(center=(width // 2, height + 50))  # Posisi awal di bawah layar

text_date_location = font.render('', True, (0, 0, 0))
text_rect_date_location = text_date_location.get_rect(center=(width // 2, height - 50))

clock = pygame.time.Clock()

# Efek animasi untuk gambar
image_alpha = 0
image_rotation = 0
rotated_image = image  # Menyimpan gambar yang sudah diputar

# Efek partikel
particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(5, 15)
        self.speed = random.uniform(1, 3)

    def move(self):
        self.y -= self.speed

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    # Tampilkan gambar dengan efek animasi
    if image_alpha < 255:
        image_alpha += 5
        image.set_alpha(image_alpha)
    if image_rotation < 360:
        image_rotation += 2
        rotated_image = pygame.transform.rotate(image, image_rotation)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)
    screen.blit(rotated_image, rotated_rect)

    # Tampilkan tulisan "#SAVE PALESTINE" dengan efek animasi dari bawah ke atas
    if text_rect_save_palestine.y > height // 2 + 150:
        text_rect_save_palestine.y -= 2
    screen.blit(text_save_palestine, text_rect_save_palestine)

    # Tambahkan efek partikel
    if random.random() < 0.1:
        particles.append(Particle(random.randint(0, width), height))
    for particle in particles:
        particle.move()
        pygame.draw.circle(screen, particle.color, (particle.x, int(particle.y)), particle.size)

    # Hapus partikel yang keluar dari layar
    particles = [particle for particle in particles if particle.y > 0]

    # Tampilkan tulisan tanggal dan lokasi
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text_date_location = font.render("Bandung, "+current_date, True, (0, 0, 0))
    text_rect_date_location = text_date_location.get_rect(center=(width // 2, height // 1.2))
    screen.blit(text_date_location, text_rect_date_location)

    # Update layar
    pygame.display.flip()

    # Kontrol kecepatan animasi
    clock.tick(30)
