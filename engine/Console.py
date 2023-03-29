import pygame


class Console(object):
    """
    Console helps to manage the game
    """

    def __init__(self, screen_width: int, font: pygame.font.Font):
        """

        :param screen_width: main display surface's width (pygame.Surface.get_with()).
        """
        self.font = font
        self.field = pygame.Rect(0, 20, screen_width, 20)
        self.in_active = False
        self.activate = False
        self.inner = ''
        self.inner_parameter = ''
        self.inner_value = ''
        self.text = self.font.render(self.inner, False, (0, 0, 0))
        self.history = []
        self.history_rendered = []

    def log(self, text: str):
        """

        :param text: text to show in console journal
        """
        self.history.insert(0, text)

    def history_update(self):
        """
        Updating console's journal
        :return:
        """
        self.history_rendered = []
        self.log(self.inner)
        for text in self.history:
            text = ">> " + text
            self.history_rendered.append(self.font.render(text, False, (250, 250, 250), (100, 100, 100)))

    def update(self, screen: pygame.Surface, events_list, color: tuple = (200, 200, 200)):
        """
        Checking changes and updating the console. Must be in main cycle
        :param screen: main display surface
        :param events_list: pygame's event list
        :param color: input field's color
        :return:
        """
        if self.in_active:
            pygame.draw.rect(screen, color, self.field)
            screen.blit(self.text, self.field)
            text_number = 1
            for text in self.history_rendered:
                screen.blit(text, (self.field.x, self.field.y + text_number * 20))
                text_number += 1
            for event in events_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.inner += 'a'
                    elif event.key == pygame.K_b:
                        self.inner += 'b'
                    elif event.key == pygame.K_c:
                        self.inner += 'c'
                    elif event.key == pygame.K_d:
                        self.inner += 'd'
                    elif event.key == pygame.K_e:
                        self.inner += 'e'
                    elif event.key == pygame.K_f:
                        self.inner += 'f'
                    elif event.key == pygame.K_g:
                        self.inner += 'g'
                    elif event.key == pygame.K_h:
                        self.inner += 'h'
                    elif event.key == pygame.K_i:
                        self.inner += 'i'
                    elif event.key == pygame.K_j:
                        self.inner += 'j'
                    elif event.key == pygame.K_k:
                        self.inner += 'k'
                    elif event.key == pygame.K_l:
                        self.inner += 'l'
                    elif event.key == pygame.K_m:
                        self.inner += 'm'
                    elif event.key == pygame.K_n:
                        self.inner += 'n'
                    elif event.key == pygame.K_o:
                        self.inner += 'o'
                    elif event.key == pygame.K_p:
                        self.inner += 'p'
                    elif event.key == pygame.K_q:
                        self.inner += 'q'
                    elif event.key == pygame.K_r:
                        self.inner += 'r'
                    elif event.key == pygame.K_s:
                        self.inner += 's'
                    elif event.key == pygame.K_t:
                        self.inner += 't'
                    elif event.key == pygame.K_u:
                        self.inner += 'u'
                    elif event.key == pygame.K_v:
                        self.inner += 'v'
                    elif event.key == pygame.K_w:
                        self.inner += 'w'
                    elif event.key == pygame.K_x:
                        self.inner += 'x'
                    elif event.key == pygame.K_y:
                        self.inner += 'y'
                    elif event.key == pygame.K_z:
                        self.inner += 'z'
                    elif event.key == pygame.K_SPACE:
                        self.inner += ' '
                    elif event.key == pygame.K_0:
                        self.inner += '0'
                    elif event.key == pygame.K_1:
                        self.inner += '1'
                    elif event.key == pygame.K_2:
                        self.inner += '2'
                    elif event.key == pygame.K_3:
                        self.inner += '3'
                    elif event.key == pygame.K_4:
                        self.inner += '4'
                    elif event.key == pygame.K_5:
                        self.inner += '5'
                    elif event.key == pygame.K_6:
                        self.inner += '6'
                    elif event.key == pygame.K_7:
                        self.inner += '7'
                    elif event.key == pygame.K_8:
                        self.inner += '8'
                    elif event.key == pygame.K_9:
                        self.inner += '9'

                    elif event.key == pygame.K_BACKSPACE:
                        self.inner = self.inner[:len(self.inner) - 1]

                    elif event.key == pygame.K_RETURN:
                        self.history_update()
                        for i in self.inner:
                            if i == ' ':
                                break
                            self.inner_parameter += i

                        try:
                            for i in self.inner[::-1]:
                                if i == ' ':
                                    break
                                self.inner_value += i
                            self.inner_value = self.inner_value[::-1]
                        except IndexError:
                            self.log("console is clear, type some")
                        self.inner = ''
                        self.activate = True

                    self.text = self.font.render(self.inner, False, (0, 0, 0))
