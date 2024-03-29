import pygame
from PIL import Image, ImageFilter
import sys


class Chronometre:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 24)

    def get_elapsed_time(self):
        return pygame.time.get_ticks() - self.start_time

    def draw(self, screen):
        time_elapsed = self.get_elapsed_time() // 1000
        text = self.font.render("Temps écoulé : " + str(time_elapsed), True, (255, 255, 255))
        screen.blit(text, (10, 10))


class Jeu:
    def __init__(self, nom, mdp):
        self.nom = nom
        self.mdp = mdp

    def enregistrer(self):
        self.dic = {}
        self.dic[self.nom] = self.mdp

    def login(self):
        if self.nom in self.dic:
            mdp = 0
            self.dic[self.nom] = mdp
            if self.mdp == mdp:
                return True
            else:
                return False
        else:
            return False

    def fenetre(self, chronometre):
        largeur = 1920
        hauteur = 1080
        taille_fenetre = (largeur, hauteur)

        fenetre = pygame.display.set_mode(taille_fenetre)
        pygame.display.set_caption("Arche_02.jpeg")

        image_arche = pygame.image.load("Arche_02.jpeg")
        image_lion = pygame.image.load("SGT 240-B_0.jpg")
        image_chien = pygame.image.load("SGT 240-H_0.jpg")
        image_chat = pygame.image.load("SGT 240-G_0.jpg")

        position_lion = (300, 300)
        position_chien = (100, 200)
        position_chat = (200, 300)

        animal_selectionne = False
        animal_en_cours = None

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if image_chien.get_rect(topleft=position_chien).collidepoint(event.pos):
                        animal_selectionne = True
                        animal_en_cours = 'chien'
                    elif image_chat.get_rect(topleft=position_chat).collidepoint(event.pos):
                        animal_selectionne = True
                        animal_en_cours = 'chat'
                    elif image_lion.get_rect(topleft=position_lion).collidepoint(event.pos):
                        animal_selectionne = True
                        animal_en_cours = 'lion'

                elif event.type == pygame.MOUSEBUTTONUP:
                    animal_selectionne = False

                if animal_selectionne and event.type == pygame.MOUSEMOTION:
                    if animal_en_cours == 'chien':
                        position_chien = event.pos
                    elif animal_en_cours == 'chat':
                        position_chat = event.pos
                    elif animal_en_cours == 'lion':
                        position_lion = event.pos

            fenetre.fill((255, 255, 255))

            fenetre.blit(image_arche, (0, 0))

            fenetre.blit(image_chien, position_chien)
            fenetre.blit(image_chat, position_chat)
            fenetre.blit(image_lion, position_lion)

            chronometre.draw(fenetre)  # Affichage du chronomètre

            pygame.display.flip()

        pygame.quit()


pygame.init()

# Initialisation du chronomètre
chronometre = Chronometre()

# Initialisation de la classe de jeu
partie = Jeu('marcel', 'lol')

# Initialisation de la fenêtre
largeur = 960
hauteur = 540
taille_fenetre = (largeur, hauteur)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Menu d'Accueil")

# Chargement de l'image
image_jeu = pygame.image.load("Arche_02.jpeg")

# Flou gaussien sur l'image
pil_image = Image.open("Arche_02.jpeg")
pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius=10))
image_floue = pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode)

# Définition des éléments de la fenêtre
font = pygame.font.Font(None, 64)
titre_text = font.render("Bienvenue au jeu", True, (255, 255, 255))
titre_rect = titre_text.get_rect(center=(largeur // 2, 100))
bouton_jouer_rect = pygame.Rect(largeur // 2 - 100, 300, 200, 50)
bouton_quitter_rect = pygame.Rect(largeur // 2 - 100, 400, 200, 50)
blanc = (255, 255, 255)
noir = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_jouer_rect.collidepoint(event.pos):
                partie.fenetre(chronometre)  # Lancement du jeu avec le chronomètre
            elif bouton_quitter_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Affichage de l'image floue en arrière-plan
    fenetre.blit(image_floue, (0, 0))

    # Dessin du titre
    fenetre.blit(titre_text, titre_rect)

    # Dessin des boutons
    pygame.draw.rect(fenetre, noir, bouton_jouer_rect)
    pygame.draw.rect(fenetre, noir, bouton_quitter_rect)

    # Texte des boutons
    font_bouton = pygame.font.Font(None, 32)
    jouer_text = font_bouton.render("Jouer", True, blanc)
    quitter_text = font_bouton.render("Quitter", True, blanc)

    # Positionnement des textes des boutons
    jouer_rect = jouer_text.get_rect(center=bouton_jouer_rect.center)
    quitter_rect = quitter_text.get_rect(center=bouton_quitter_rect.center)

    # Affichage des textes des boutons
    fenetre.blit(jouer_text, jouer_rect)
    fenetre.blit(quitter_text, quitter_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
