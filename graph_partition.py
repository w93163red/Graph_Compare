import numpy as np

class Graph(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def cal_weight(self, list, task_no):
        summ = 0
        for num in list:
            summ += self.matrix[num][task_no]
        return summ


    def find_list(self, divide_list, task_no):
        for i in range(0, len(divide_list)):
            if task_no in divide_list[i]:
                return i
        return -1


    def run(self):

        core = 4
        max_vertices = 10

        divide_list = []
        for _ in range(core):
            divide_list.append([])
        divide_list[0] = [0, 1]
        divide_list[1] = [2, 3, 4]
        divide_list[2] = [5, 6, 7]
        divide_list[3] = [8, 9]

        flag = True
        while (flag):
            flag = False
            for i in range(0, 10):
                for j in range(0, 10):
                    if i != j:
                        i_no = int(self.find_list(divide_list, i))
                        j_no = int(self.find_list(divide_list, j))
                        ii = len(divide_list[i_no]) * (self.cal_weight(divide_list[i_no], i) - self.cal_weight(divide_list[i_no], j))
                        jj = len(divide_list[j_no]) * (self.cal_weight(divide_list[j_no], i) - self.cal_weight(divide_list[j_no], j))
                        ii = np.float64(ii).item()
                        jj = np.float64(jj).item()
                        if ii > jj:
                            flag = True
                            divide_list[i_no].remove(i)
                            divide_list[j_no].remove(j)
                            divide_list[i_no].append(j)
                            divide_list[j_no].append(i)

        sum = 0
        for i in range(len(divide_list)):
            for j in range(0, len(divide_list[i])):
                for k in range(j, len(divide_list[i])):
                    sum += self.matrix[j][k]

        return divide_list, sum
