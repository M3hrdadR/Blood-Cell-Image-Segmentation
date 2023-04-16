import cv2
import Beam
import Help
import time

start = time.time()
path = "ALL_IDB2/img/"
name = "Im008_1.tif"
result_path = "Results/"
img = cv2.imread(path + name)
resize_img = Help.resize(img)
no_colors = 5
no_agents = 5
initial_r = 20
beam = Beam.Beam(initial_r, no_colors, no_agents, resize_img, threshold=5, max_iter=40)
solution = beam.main_loop()
# solution = [[[53, 83, 53], [81, 99, 4], [158, 154, 159], [126, 115, 142], [118, 26, 84]], 0]
matrix = Help.make_pic(solution, img)
# PSNR
img_gray = cv2.imread(path + name, cv2.IMREAD_GRAYSCALE)
gray_matrix = Help.convert_to_gray_scale(matrix)
psnr = Help.psnr(img_gray, gray_matrix)
print("PSNR =", psnr)
print("time = ", round((time.time() - start) / 60, 2))

cv2.imwrite(result_path + name[:-4] + " " + str(no_colors) + ".jpg", matrix)
cv2.imshow("rgb", matrix)
cv2.waitKey(0)

