import Help
import random
import sys
import copy


class Hill:
    def __init__(self, r, no_colors, pic, threshold=10, max_iter=30):
        self.r = r
        self.init_r = r
        self.no_colors = no_colors
        self.pic = pic
        self.threshold = threshold
        self.max_iter = max_iter
        self.curr = self.init_state()
        self.perm = Help.gen_permutations(2, 3)
        return

    def evaluation(self, element):
        sum = 0
        for i in range(len(self.pic)):
            for j in range(len(self.pic[i])):
                min_distance = sys.maxsize
                for l in range(self.no_colors):
                    min_distance = min(min_distance, Help.euclidean_distance(element[0][l], self.pic[i][j]))
                sum += min_distance
        return round(sum / (len(self.pic) * len(self.pic[0])), 15)

    def init_state(self):
        lst = [[random.randint(0, 255) for _ in range(3)] for _ in range(self.no_colors)]
        a = [lst, 0]
        # print(self.evaluation(a))
        a[1] = self.evaluation(a)
        return a

    def find_neighbour(self, lst):
        ngb = list()
        # valid_values = [-1, 1]
        for i in range(self.no_colors):
            for perm in self.perm:
                tmp = copy.deepcopy(lst)
                for j in range(3):
                    if perm[j] == 0:
                        tmp[0][i][j] -= self.r
                        if tmp[0][i][j] < 0:
                            tmp[0][i][j] = 0
                    elif perm[j] == 1:
                        tmp[0][i][j] += self.r
                        if tmp[0][i][j] > 255:
                            tmp[0][i][j] = 255
                tmp[1] = self.evaluation(tmp)
                ngb.append(tmp)
        return ngb

    def update_r(self):
        if self.r == self.threshold:
            self.r = 5
            return
        self.r -= 1
        return

    def run(self):
        ngb = self.find_neighbour(self.curr)
        self.update_r()
        return ngb

    # def main_loop(self):
    #     iteration = 0
    #     while iteration < self.max_iter:
    #         ngb = self.find_neighbour(self.curr)
    #         self.update_r()
    #         if ngb[0][1] <= self.curr[1]:
    #             self.curr = copy.deepcopy(ngb[0])
    #         iteration += 1
    #         print("iteration =", iteration, "| best value =", round(self.curr[1] / (len(self.pic) * len(self.pic[0])), 1),
    #                          "error per pixel", "| Solution =", self.curr[0])
    #     return self.curr
