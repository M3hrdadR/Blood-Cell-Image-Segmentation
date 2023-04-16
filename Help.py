import math
import copy
import sys
import numpy as np
import cv2


def resize(img):
    resized_img = cv2.resize(img, dsize=(25, 25), interpolation=cv2.INTER_CUBIC)
    # resized_img2 = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
    return resized_img


def psnr(gray_image, result_image):
    sum = 0
    for i in range(len(gray_image)):
        for j in range(len(gray_image[i])):
            sum += math.pow(int(gray_image[i][j]) - int(result_image[i][j]), 2)
    l = 255
    sum = sum / (len(gray_image) * len(gray_image[0]))
    psnr = math.pow(l, 2) / sum
    psnr = 10 * math.log10(psnr)
    return round(psnr, 4)


def euclidean_distance(lst1, lst2):
    arr1 = np.array(lst1)
    arr2 = np.array(lst2)
    out_num = np.sqrt(np.sum(np.subtract(arr1, arr2) ** 2))
    return out_num


def convert_to_gray_scale(matrix):
    r, g, b = matrix[:, :, 0], matrix[:, :, 1], matrix[:, :, 2]
    gray = 0.33 * r + 0.33 * g + 0.33 * b
    return np.array(gray, dtype=np.uint8)


def make_pic(element, pic_matrix):
    error = 0
    pic = []
    for i in range(len(pic_matrix)):
        pic_row = []
        for j in range(len(pic_matrix[i])):
            min_distance = sys.maxsize
            best_color = element[0][0]
            for l in range(len(element[0])):
                x = euclidean_distance(element[0][l], pic_matrix[i][j])
                if x < min_distance:
                    min_distance = x
                    best_color = element[0][l].copy()
            error += min_distance
            pic_row.append(best_color)
        pic.append(pic_row)
    print("Error in original image (per pixel) =", end=" ")
    print(round(error / (len(pic_matrix)*len(pic_matrix[0])), 2))
    return np.array(pic, dtype=np.uint8)


def gen_permutations(base, length):
    perms = []
    lst = [0 for _ in range(length)]
    k = length - 1
    while k >= 0:
        perms.append(lst.copy())
        k = length - 1
        lst[k] += 1
        while k >= 0 and lst[k] == base:
            lst[k] = 0
            k -= 1
            lst[k] += 1
    return perms


def minimum_distance(element, values):
    for x in values:
        if abs(element - x) < 1:
            return False
    return True


def unique_neighbours(ngb):
    unique_ngb = list()
    values = list()
    for n in ngb:
        if n[1] not in values and minimum_distance(n[1], values):
            values.append(copy.deepcopy(n[1]))
            unique_ngb.append(copy.deepcopy(n))
    return unique_ngb
