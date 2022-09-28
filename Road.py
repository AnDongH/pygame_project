import pygame, os
from Settings import *

# 길 이미지
class Road(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "tile_N.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"

class Road_Horizontal(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "re_tile_horiz.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"

class Road_Vertical(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "re_tile_vert.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"

#포세이돈(스테이지1)

#하데스(스테이지2)

#디오니소스(스테이지3)

#제우스(스테이지4)
class Conductor0(pygame.sprite.Sprite): #가짜
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_11.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Conductor0"
        
class Conductor1(pygame.sprite.Sprite): #진짜
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_11.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Conductor1"

class AlcoholRoad(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "purple_tile_0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "alcoholRoad"

class EventTile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, event_code):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "tile_N.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "eventRoad"
        self.event_code = event_code
