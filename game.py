import pygame as pg

pg.init()
font_name = pg.font.match_font('arial') # поиск шрифта arial
size = 18 # размер шрифта
W,H = 600,600
win = pg.display.set_mode((W,H)) # данная команда создает игровое окно
name = ""
def draw_text(surf, text, x,y, size=size, color=(255,255,255)):
  font = pg.font.Font(font_name, size) # определение шрифта
  text_surface = font.render(text, True, color)
  text_rect = text_surface.get_rect()
  text_rect.midtop = (x,y)
  surf.blit(text_surface, text_rect)
def user_name(surf,text, x,y, size):
  font = pg.font.Font(font_name, size)  # определение шрифта
  text_surface = font.render(text, True, color=(255,255,255))
  text_rect = text_surface.get_rect()
  text_rect.midstop = (x, y)
main_loop = True
while main_loop:
  for i in pg.event.get():
    if i.type == pg.QUIT:
      exit()
    elif i.type == pg.KEYDOWN:
      if i.key == pg.K_BACKSPACE:
        name = name[: -1]
      elif i.key == pg.K_RETURN:
        main_loop = False
        break
      else:
        name += i.unicode
  win.fill((0,0,0))
  draw_text(win, 'Введите имя:', W//2,H//2)
  draw_text(win, name, W//2,H//2 +20)
  pg.display.update()

while True:
  for i in pg.event.get():
    if i.type == pg.QUIT:
      exit()
  win.fill((123, 213, 56))
  pg.display.update()
