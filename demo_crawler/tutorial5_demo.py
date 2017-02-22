import json
import math
from collections import Counter
from matplotlib import pyplot as plt


def mean(x):
    return sum(x) / len(x)


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    deviations = de_mean(x)
    variance_x = 0
    for d in deviations:
        variance_x += d**2
    variance_x /= len(x)
    return variance_x


def dot(x, y):
    dot_product = sum(v_i * w_i for v_i, w_i in zip(x, y))
    dot_product /= (len(x))
    return dot_product


def correlation(x, y):
    variance_x = variance(x)
    variance_y = variance(y)
    sd_x = math.sqrt(variance_x)
    sd_y = math.sqrt(variance_y)
    dot_xy = dot(de_mean(x), de_mean(y))
    return dot_xy/(sd_x*sd_y)


def decile(num):
    return (num // 10) * 10


if __name__ == '__main__':
    '''
    with open('example.json', 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        images = []
        pushes = []
        for d in data_list:
            images.append(d['num_image'])
            pushes.append(d['push_count'])
    '''
    images = [3, 7, 1, 12, 9, 1, 2, 13, 0, 5, 27, 5, 1, 8, 0, 1, 14, 2, 3, 2, 1, 25, 3, 14, 27, 2]
    pushes = [18, 20, 0, 0, 3, 6, 2, 12, 1, 13, 11, 5, 0, 20, 1, 7, 6, 2, 2, 0, 0, 32, 10, 13, 9, 2]

    print('Pics:', images, 'Max:', max(images), 'Min:', min(images))
    print('Pushes:', pushes, 'Max:', max(pushes), 'Min:', min(pushes))
    print('Avg Pics:', mean(images), 'Avg Posts:', mean(pushes))
    print('correlation:', correlation(images, pushes))

    # histogram
    histogram = Counter(decile(push) for push in pushes)
    print(histogram)

    # histogram plot
    plt.figure(1)
    plt.bar([x-4 for x in histogram.keys()], histogram.values(), 8)
    plt.axis([-5, 35, 0, 20])
    plt.title('Pushes')
    plt.xlabel('# of pushes')
    plt.ylabel('# of posts')
    plt.xticks([10 * i for i in range(4)])

    # scattering plot
    plt.figure(2)
    plt.scatter(images, pushes)
    plt.title('# of image v.s. push')
    plt.xlabel('# of image')
    plt.ylabel('# of push')
    plt.axis('equal')

    plt.show()
