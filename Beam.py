import Hill
import Help
import copy


class Beam:
    def __init__(self, r, no_colors, no_agents, pic, threshold=3, max_iter=30):
        self.r = r
        self.no_colors = no_colors
        self.no_agents = no_agents
        self.pic = pic
        self.threshold = threshold
        self.max_iter = max_iter
        self.agents = [Hill.Hill(self.r, self.no_colors, self.pic, self.threshold, self.max_iter)
                       for _ in range(self.no_agents)]
        self.best = [[], 1000]
        self.prevoius_best = [[], 1000]
        return

    def emergency_services(self):
        print()
        print("Emergency call ..............")
        for i in range(self.no_agents):
            self.agents[i].r = self.r
            # for j in range(self.no_colors):
            #     for k in range(3):
            #         p = random.randint(-2, 1)
            #         if p == 0:
            #             p = 2
            #         self.agents[i].curr[0][j][k] = self.best[0][j][k] + p * 30
            #         if self.agents[i].curr[0][j][k] > 255:
            #             self.agents[i].curr[0][j][k] = 255
            #         if self.agents[i].curr[0][j][k] < 0:
            #             self.agents[i].curr[0][j][k] = 0
            # self.agents[i].curr[1] = self.agents[i].evaluation(self.agents[i].curr)
        return

    def main_loop(self):
        no_iter = 0
        stagnancy_no = 0
        while no_iter < self.max_iter:
            ngb = list()
            for i in range(self.no_agents):
                ngb = ngb + self.agents[i].run()
                # ngb.append(self.agents[i].curr)
            ngb.sort(key=lambda x: x[1])

            unique_ngb = Help.unique_neighbours(ngb)
            for i in range(self.no_agents):
                self.agents[i].curr = copy.deepcopy(unique_ngb[i])

            stagnancy_no += 1
            if unique_ngb[0][1] < self.best[1]:
                self.best = unique_ngb[0]
                stagnancy_no = 0

            if stagnancy_no == self.max_iter // 10:
                self.emergency_services()
                stagnancy_no = -3 * self.max_iter // 10
            for i in range(self.no_agents):
                print(self.agents[i].curr, self.agents[i].r)
            no_iter += 1
            print("iteration =", no_iter, "\nbest value =", self.best[1], "error per pixel", "\nSolution =", self.best[0])
            print()
        return self.best
