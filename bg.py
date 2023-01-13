import pygame
from pygame.math import Vector2

snd_dir = 'media/snd/'  # Путь до папки со звуками
img_dir = 'media/img/'  # Путь до папки со спрайтами
width = 1366                            # ширина игрового окна
height = 768                            # высота игрового окна

# Создаем класс игрока
class Bg(pygame.sprite.Sprite):
    def __init__(self):  # Специальная функция, где указываем что будет у игрока
        pygame.sprite.Sprite.__init__(self)  # Игрок - спрайт

        self.image = pygame.image.load(img_dir + 'bg.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = [width/2, height/2]
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)       # Изменяем направление взгляда
        self.angle += rotate_speed                    # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)     # Изменение рамки

    def update(self):
        self.rotate(-0.07)