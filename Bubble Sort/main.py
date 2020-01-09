import random
import pygame
import time


def create_data(size, min, max):
    data = []
    for i in range(size):
        data.append(random.randrange(min, max))
    return data


def show_data(data):
    print("Your data : ")
    for i in data:
        print(i)


def bubble_sort(data, rectangles, screen):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                rectangles[j].x, rectangles[j+1].x = rectangles[j+1].x, rectangles[j].x
                rectangles[j], rectangles[j+1] = rectangles[j+1], rectangles[j]
                update_rectangles(rectangles, screen)

def update_rectangles(rectangles, screen):
    screen.fill((0, 0, 0))
    for rect in rectangles:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.display.flip()


def main():
    size = width, height = 640, 320
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Bubble sort visualization")

    data = create_data(size=100, min=0, max=100)

    x = 0
    rectangles = []
    maximum = max(data)
    size_width = width / len(data)

    for value in data:
        size_length = (value / maximum) * height
        rectangles.append(pygame.Rect(x, height, size_width + 1, -size_length))
        x += size_width

    update_rectangles(rectangles, screen)

    bubble_sort(data, rectangles, screen)


if __name__ == '__main__':
    main()
