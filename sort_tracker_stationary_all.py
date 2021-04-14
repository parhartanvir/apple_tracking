from sort.sort import *
import cv2
import csv
from glob import glob
import  os

mot_tracker = Sort(max_age=100, iou_threshold=0.1, min_hits=4)
colors = {}
all_boxes = {}
counts = []

def get_key(fp):
    filename = os.path.splitext(os.path.basename(fp))[0]
    int_part = filename.split()[0]
    print("int_part ", int_part)
    # int_part = int_part[int_part.find('im')+2:]
    int_part = int_part[int_part.find('left') + 4:]

    print("int_part ", int_part)
    return int(int_part)


def get_boxes(csv_name):
    boxes1 = []
    with open(csv_name, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for i in range(len(row)):
                row[i] = float(row[i])
            row[2] = row[0] + row[2]
            row[3] = row[1] + row[3]
            row.append(None)
            boxes1.append(row)
    return boxes1


def show_matches(boxes1, im1, im_name):
    for i in range(len(boxes1)):
        idx_1 = int(boxes1[i][4])
        print(boxes1[i], idx_1)
        all_boxes[idx_1] = boxes1[i]

    for idx_1 in all_boxes.keys():
        if (idx_1 not in colors):
            colors[idx_1] = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        color = colors[idx_1]
        pts1 = all_boxes[idx_1]
        cv2.rectangle(img=im1, pt1=(int(pts1[0]), int(pts1[1])),
                      pt2=(int(pts1[2]), int(pts1[3])),
                      thickness=15, color=color)
        im1 = cv2.putText(im1, str(idx_1), (int(pts1[0]), int(pts1[1])), cv2.FONT_HERSHEY_SIMPLEX,
                          fontScale=2, color=(255, 255, 255), thickness=5)

    im1 = cv2.putText(im1, "Total number of boxes ", (50, 1500), cv2.FONT_HERSHEY_SIMPLEX,
                      fontScale=2, color=(255, 255, 255), thickness=5)
    im1 = cv2.putText(im1, str(len(all_boxes)), (850, 1500), cv2.FONT_HERSHEY_SIMPLEX,
                      fontScale=2, color=(255, 255, 255), thickness=5)

    cv2.namedWindow('im1', cv2.WINDOW_NORMAL)
    cv2.imshow("im1", im1)
    #cv2.imwrite('/media/frcvision2/8ac9713c-aa2f-4f4c-9fbd-ff15beb3269e1/2018_9_10_APPLE_CA_LEAF_BLOWER/moving/train_data/stationary_images/tracked/' + im_name+'.jpg', im1)
    cv2.waitKey(50)
    counts.append(len(all_boxes))


images = glob(os.path.curdir+'/stationary/processed/*.jpg')
images.sort()
images = sorted(images, key=get_key)
print(images)

cv2.namedWindow('im1', cv2.WINDOW_NORMAL)
x=input("start?")

for i in range(len(images)):
    im = cv2.imread(images[i])
    im_name = images[i][images[i].find('/processed') + 10:]
    print(im_name)
    csv_name = os.path.curdir+'/stationary/processed/' + im_name + '.csv'

    boxes = get_boxes(csv_name)
    track_bbs_ids = mot_tracker.update(np.array(boxes))
    show_matches(track_bbs_ids, im, im_name)

with open('counts.csv','w') as file:
    for c in counts:
        file.write(str(c))
        file.write('\n')