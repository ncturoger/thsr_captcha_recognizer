import os
import matplotlib.pyplot as plt
import cv2
import time
import matplotlib

images = os.listdir("rename")
i = 0

def mypause(interval):
    backend = plt.rcParams['backend']
    if backend in matplotlib.rcsetup.interactive_bk:
        figManager = matplotlib._pylab_helpers.Gcf.get_active()
        if figManager is not None:
            canvas = figManager.canvas
            if canvas.figure.stale:
                canvas.draw()
            canvas.start_event_loop(interval)
            return

isfirst = True
plt.ion()

for img in images:
    img_path = 'rename/{}'.format(img)
    print(img_path)
    img_file = cv2.imread(img_path)
    plt.imshow(img_file)
    if isfirst:
        plt.show(block=False)
        isfirst = False
        print(555)
    # plt.pause(0.1)
    mypause(0.1)
    label = input("label:")
    plt.close()
    id = 1
    rename = 'rename/{}.png'.format(label)
    while os.path.isfile(rename):
        rename = 'rename/{}_{}.png'.format(label, id)
        id += 1
    os.rename(img_path, rename)