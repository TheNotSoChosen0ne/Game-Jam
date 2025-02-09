import colorsys

def next_rainbow_color(color):
    """Prend une couleur (R, G, B) et l'incrémente doucement dans le spectre arc-en-ciel."""
    r, g, b = [c / 255.0 for c in color]  # Normaliser en [0,1]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)  

    if v == 0:  # Si la couleur est noire, on initialise une valeur de base
        h, s, v = 0, 1, 1  # Rouge vif au départ

    h = (h + 0.005) % 1.0
    r, g, b = colorsys.hsv_to_rgb(h, s, v)  
    return (int(r * 255), int(g * 255), int(b * 255))  # Retour en [0,255]
