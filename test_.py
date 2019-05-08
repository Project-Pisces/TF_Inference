"""
    ** This util is solely for testing **

    Run this after running inference to see how many
    of the images that should of made it actually did

"""


import shutil, os
from math import log10, floor

# Return int to 2 significant figures
def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)


def count_correct_imgs():
    count = 0
    input_chinook_img = 60
    abs_path = "/tmp/test_/"
    for file_name in os.listdir(abs_path):
        if (file_name.endswith(".jpg") and file_name.startswith("chinook")):
            count += 1

    ratio_correct = count/input_chinook_img
    ratio_correct = round_sig(ratio_correct)

    print("Images correctly classified= " + str(count))
    print("Ratio of input images/correctly classified images=" + str(ratio_correct))

def main():
    print("python main function")
    count_correct_imgs()

if __name__ == '__main__':
    main()

"""
for i in {1..20}
do touch /tmp/test_/chinook_$i.jpg
done
"""