from datetime import datetime
import numpy as np

nemo = ["nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]
large = np.random.choice(everyone, size=100000, replace=True)


def find_nemo(array):
    t0 = datetime.now()
    nemo_found = 0
    for i in array:
        if i == "nemo":
            # print("Found NEMO!")
            nemo_found += 1
    t1 = datetime.now()
    total = t1 - t0
    print("Call to find Nemo took " + str(total.microseconds) + " microseconds")


find_nemo(large)

boxes = [0, 1, 2, 3, 4, 5]


def log_first_two_boxes(boxess):
    print(boxess[0])  # O(1)
    print(boxess[1])  # O(1)


log_first_two_boxes(boxes)  # O(2)
