

class Animaux:
    def __init__ (self):
        self.lion=1
        self.lionne= 2
        self.giraffe=3
        self.girafe=4
        self.hypoM=5
        self.hypoF=6
        self.elephant=7
        self.elephante=8

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur = 1920
hauteur = 1080
taille_fenetre = (largeur, hauteur)

# Création de la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Arche_02.jpeg")

# Charger les images des animaux
image_arche = pygame.image.load("Arche_02.jpeg")
image_lion = pygame.image.load("SGT 240-B_0.jpg")  # Image de l'arche
image_chien = pygame.image.load("SGT 240-H_0.jpg")  # Image du chien
image_chat = pygame.image.load("SGT 240-G_0.jpg")    # Image du chat
# Chargez les images des autres animaux de la même manière...

# Position initiale des animaux
position_lion = (300, 300)
position_chien = (100, 200)
position_chat = (200, 300)
# Définissez les positions initiales des autres animaux de la même manière...

animal_selectionne = False
animal_en_cours = None

# Écran d'accueil
def ecran_accueil():
    fenetre.fill((255, 255, 255))  # Remplir l'écran avec une couleur blanche

    # Texte d'accueil
    font = pygame.font.Font(None, 64)
    jouer_text = font.render("Jouer", True, (0, 0, 0))
    quitter_text = font.render("Quitter", True, (0, 0, 0))

    # Positionnement des textes
    jouer_rect = jouer_text.get_rect(center=(largeur // 2, hauteur // 2 - 50))
    quitter_rect = quitter_text.get_rect(center=(largeur // 2, hauteur // 2 + 50))

    # Dessin des textes sur l'écran
    fenetre.blit(jouer_text, jouer_rect)
    fenetre.blit(quitter_text, quitter_rect)

    pygame.display.flip()

# Boucle pour l'écran d'accueil
ecran_accueil()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if jouer_rect.collidepoint(event.pos):
                running = True
                break
            elif quitter_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
    pygame.display.update()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifiez si un animal est cliqué
            if image_chien.get_rect(topleft=position_chien).collidepoint(event.pos):
                animal_selectionne = True
                animal_en_cours = 'chien'
            elif image_chat.get_rect(topleft=position_chat).collidepoint(event.pos):
                animal_selectionne = True
                animal_en_cours = 'chat'
            elif image_lion.get_rect(topleft=position_lion).collidepoint(event.pos):
                animal_selectionne = True
                animal_en_cours ='lion'

                
            # Ajoutez les autres animaux de la même manière...

        elif event.type == pygame.MOUSEBUTTONUP:
            animal_selectionne = False

        # Mettre à jour la position de l'animal sélectionné
        if animal_selectionne and event.type == pygame.MOUSEMOTION:
            if animal_en_cours == 'chien':
                position_chien = event.pos
            elif animal_en_cours == 'chat':
                position_chat = event.pos
            elif animal_en_cours == 'lion':
                position_lion = event.pos
                
    # Effacer l'écran
    fenetre.fill((255, 255, 255))  # Remplir l'écran avec une couleur blanche

    # Dessiner l'arche
    fenetre.blit(image_arche, (0, 0))

    # Dessiner les animaux
    fenetre.blit(image_chien, position_chien)
    fenetre.blit(image_chat, position_chat)
    fenetre.blit(image_lion, position_lion)
    # Dessinez les autres animaux de la même manière...

    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
