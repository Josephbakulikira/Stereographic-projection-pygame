width, height = 1000, 1000
resolution = (width, height)
white, black = (255, 255, 255), (0, 0, 0)

def Translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2) * ((value-min1)/(max1-min1))
