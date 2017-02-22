import json

with open('example.json', 'r', encoding='utf-8') as f:
    data_list = json.load(f)
    images = []
    pushes = []
    for d in data_list:
        images.append(d['num_image'])
        pushes.append(d['push_count'])

print('Pics:', images, 'Max:', max(images), 'Min:', min(images))
print('Pushes:', pushes, 'Max:', max(pushes), 'Min:', min(pushes))

def mean(x):
    return sum(x) / len(x)

print('Avg pics:', mean(images), 'Avg pushes:', mean(pushes))

