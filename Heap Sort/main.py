import pygame
import random


def heapify(arr, n, i, rectangles, window):
    largest = i  # root
    l = 2 * i + 1  # left
    r = 2 * i + 2  # right

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        rectangles[i].x, rectangles[largest].x = rectangles[largest].x, rectangles[i].x
        rectangles[i], rectangles[largest] = rectangles[largest], rectangles[i]
        arr[i], arr[largest] = arr[largest], arr[i]
        update_rectangles(rectangles, window)
        # sub-tree
        heapify(arr, n, largest, rectangles, window)


def update_rectangles(rectangles, screen):
    screen.fill((0, 0, 0))
    for rect in rectangles:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.display.flip()


def generate_random_numbers(size, min, max):
    data = []
    for i in range(size):
        data.append(random.randrange(min, max))
    return data


def main():
    size = width, height = 640, 320
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Heap sort visualization")
    pygame.init()

    array = generate_random_numbers(size=100, min=0, max=100)

    size_width = width / len(array)
    x = 0
    rectangles = []
    maximum = max(array)
    for value in array:
        size_length = (value / maximum) * height
        rectangles.append(pygame.Rect(x, height, size_width + 1, -size_length))
        x += size_width

    update_rectangles(rectangles, screen)

    length_of_array = len(array)
    print("Total : ", length_of_array)

    start = (length_of_array // 2) - 1

    for j in range(length_of_array, 0, -1):
        for parent in range(start, -1, -1):
            heapify(array, j, parent, rectangles, screen)
        rectangles[0].x, rectangles[j - 1].x = rectangles[j - 1].x, rectangles[0].x
        rectangles[0], rectangles[j - 1] = rectangles[j - 1], rectangles[0]
        array[0], array[j - 1] = array[j - 1], array[0]
        update_rectangles(rectangles, screen)

    print(array)


if __name__ == '__main__':
    main()
