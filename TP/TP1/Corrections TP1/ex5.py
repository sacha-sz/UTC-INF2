import math

def main():
    xA = int(input("Donnez moi Xa: "))
    yA = int(input("Donnez moi Ya: "))
    xB = int(input("Donnez moi Xb: "))
    yB = int(input("Donnez moi Yb: "))

    distance = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)

    print("Bonjour, la distance qui sépare les deux points est de " + str(round(distance, 2)))


if __name__ == '__main__':
    main()
