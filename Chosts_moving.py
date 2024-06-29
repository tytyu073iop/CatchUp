import game


def moving_right(G):
    G.rect.x += game.speed
    G.image = G.move_right[G.index // 5]
    G.Faceid = True

def moving_down(G):
    G.rect.y += game.speed


def moving_left(G):
    G.rect.x -= game.speed
    G.image = G.move_left[G.index // 5]
    G.Faceid = False


def moving_up(G):
    G.rect.y -= game.speed
