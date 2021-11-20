size = 4
ani = 1
base = 250

worldX = size * base
worldY = size * base
fps = 60

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)


def legal(value):
    return (value // base) * base
