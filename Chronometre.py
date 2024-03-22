import pygame
import sys

class Chronometre:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 36)

    def get_elapsed_time(self):
        return pygame.time.get_ticks() - self.start_time

    def draw(self, screen):
        time_elapsed = self.get_elapsed_time() // 1000
        text = self.font.render("Temps écoulé : " + str(time_elapsed), True, (0, 0, 0))
        screen.blit(text, (10, 10))

class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        # Définition des dimensions de la fenêtre
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 300

        # Création de la fenêtre
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Chronomètre")

        self.chronometre = Chronometre()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  # Remplir la fenêtre avec la couleur blanche

            self.chronometre.draw(self.screen)  # Dessiner le chronomètre en haut de la fenêtre

            pygame.display.flip()  # Mettre à jour l'affichage

        pygame.quit()  # Quitter Pygame
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

    time_elapsed = pygame.time.get_ticks() - start_time

    screen.fill(WHITE)  # Remplir la fenêtre avec la couleur blanche

    draw_timer(time_elapsed)  # Dessiner le chronomètre en haut de la fenêtre

    pygame.display.flip()  # Mettre à jour l'affichage


    def draw_timer(time_elapsed):
        # Afficher le temps écoulé en haut de la fenêtre
        text = font.render("Temps écoulé : " + str(time_elapsed // 1000), True, BLACK)
        screen.blit(text, (10, 10))