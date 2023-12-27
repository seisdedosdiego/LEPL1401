import turtle                # module des graphiques tortue
import math                  # module mathématique
tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed("fastest")      # tracé rapide

# les x et y ont été ajoutés par la suite, suite à une découverte. J'ai donc modifié les fonctions mais pas les documentations. 

def square(size, color, x, y):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.penup()
    tortue.goto(x,y)
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

#square(200, "red", -100, 100)

def rectangle(width, height, color):
    """Trace un rectangle plein de largeur `width`, de largeur `height et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du rectangle.
    post: Le rectangle a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

#rectangle(100, 50, "black")

def belgian_flag(width):
    """ Trace le drapeau de la Belgique de largeur `width` et de proportion 3/2."""
    
    rectangle(width/3, 2*width/3, "black")
    tortue.penup()
    tortue.forward(width/3)
    rectangle(width/3, 2*width/3, "yellow")
    tortue.penup()
    tortue.forward(width/3)
    rectangle(width/3, 2*width/3, "red")
    tortue.backward(2*width/3)
    tortue.color("black")
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(2*width/3)
        tortue.right(90)
    tortue.penup()
    
#belgian_flag(300)
    
def three_color_flag_H(width, color1, color2, color3, x, y):
    """ Trace le drapeau un drapeau à 3 couleurs (bandes horizontales) de largeur `width` et de proportion 3/2."""
    
    tortue.penup()
    tortue.goto(x,y)
    tortue.pendown()
    rectangle(width/3, 2*width/3, color1)
    tortue.penup()
    tortue.forward(width/3)
    rectangle(width/3, 2*width/3, color2)
    tortue.penup()
    tortue.forward(width/3)
    rectangle(width/3, 2*width/3, color3)
    tortue.backward(2*width/3)
    tortue.color("black")
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(2*width/3)
        tortue.right(90)
    tortue.penup()

#three_color_flag_H(300, "blue", "white", "red", -150, 100)
    
def three_color_flag_V(width, color1, color2, color3, x, y):
    """ Trace le drapeau un drapeau à 3 couleurs (bandes verticales) de largeur `width` et de proportion 3/2."""
     
    tortue.penup()
    tortue.goto(x,y)
    tortue.pendown()
    rectangle(width, 2*width/9, color1)
    tortue.penup()
    tortue.right(90)
    tortue.forward(2*width/9)
    tortue.left(90)
    rectangle(width, 2*width/9, color2)
    tortue.penup()
    tortue.right(90)
    tortue.forward(2*width/9)
    tortue.left(90)
    rectangle(width, 2*width/9, color3)
    tortue.penup()
    tortue.left(90)
    tortue.forward(4*width/9)
    tortue.right(90)
    tortue.color("black")
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(2*width/3)
        tortue.right(90)
    tortue.penup()
    
#three_color_flag_V(300, "red", "white", "blue", -150, 100)

def draw_star(size, x, y):
    """ Trace une étoile de taille `size`."""
    
    tortue.color("gold")
    tortue.penup()
    tortue.goto(x,y)
    tortue.setheading(72)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(5):
        tortue.forward(size)
        tortue.right(144)
        tortue.forward(size)
        tortue.left(72)
    tortue.end_fill()
    tortue.hideturtle()

#draw_star(30, 0, 0)
    
def draw_circle_of_stars(center_x, center_y, num_stars, radius, star_size):
    angle = 360 / num_stars
    for _ in range(num_stars):
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        draw_star(star_size, x, y)
        angle += 360 / num_stars

#draw_circle_of_stars(0, 0, 12, 100, 20)
        
        
def european_flag(width, x, y):
    """ Trace le drapeau de l'union européenne de largeur `width` avec les proportions suivantes :
        - largeur : width
        - hauteur : 2/3 de width
        - rayon du cercle d'étoile : 2/9 de width
        - rayon d'une étoile : 1/27 de width
        
    """
    tortue.penup()
    tortue.goto(x,y)
    rectangle(width, 2*width/3, "blue")
    draw_circle_of_stars(0, 0, 12, 2*width/9, width/40)
    tortue.hideturtle()
    
european_flag(600, -300, 200)