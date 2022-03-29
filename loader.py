import pygame.image

tractor = pygame.image.load("resources/tractor.jpg")

grass = pygame.image.load("resources/gleby/trawka.jpg")
dry_soil = pygame.image.load("resources/gleby/sucha_gleba.jpg")
normal_soil = pygame.image.load("resources/gleby/zwykła_gleba.jpg")
wet_soil = pygame.image.load("resources/gleby/mokra_gleba.jpg")

beetroots = [pygame.image.load("resources/buraki/burak_ćwikłowy.png"),
             pygame.image.load("resources/buraki/burak_liściasty.png"),
             pygame.image.load("resources/buraki/burak_cukrowy.png"),
             pygame.image.load("resources/buraki/burak_pastewny.png")]

obstacles = [pygame.image.load("resources/przeszkody/słup.png"),
             pygame.image.load("resources/przeszkody/drzewo.png"),
             pygame.image.load("resources/przeszkody/kamyki.jpg")]
