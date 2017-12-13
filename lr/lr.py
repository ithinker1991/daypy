# -*- coding:utf-8 -*-
import numpy
from numpy import *
import random

_author__ = "Intery"


class LR(object):
    @classmethod
    def load_data_set(cls, path):
        data_mat = []
        class_mat = []

        f = open(path, 'r')
        for line in f.readlines():
            line_data = line.strip().split(',')
            data_mat.append([1.0, float(line_data[0]), float(line_data[1])])
            class_mat.append(int(line_data[2]))

        return data_mat, class_mat

    @classmethod
    def sigmoid(cls, intX):
        return 1.0 / (1 + numpy.exp(-intX))

    @classmethod
    def gradAscent(cls, data_mat, class_mat):
        data_matrix = mat(data_mat)
        class_matrix = mat(class_mat).transpose()
        m, n = shape(data_mat)
        alpha = 0.001
        max_iter = 500
        weights = ones((n, 1))
        for k in range(max_iter):
            h = cls.sigmoid(data_matrix * weights)
            error = (class_matrix - h)
            weights += alpha * data_matrix.transpose() * error
        return weights

    @classmethod
    def stocGradAscent(cls, data_mat, class_mat):
        m, n = shape(data_mat)
        alpha = 0.001
        weights = ones(n)
        for i in range(m):
            h = cls.sigmoid(sum(data_mat[i] * weights))
            error = class_mat[i] - h
            belta = (alpha * error)*ones(n)
            weights += belta * data_mat[i]
        return weights

    @classmethod
    def optimizedSGA(cls, data_mat, class_mat, num_iter=150):
        m, n = shape(data_mat)
        weights = ones(n)
        for j in range(num_iter):
            data_index = range(m)
            for i in range(m):
                alpha = 5 / (1.0 + j + i) + 0.01
                rand_index = int(random.uniform(0, len(data_index)))
                h = cls.sigmoid(sum(data_mat[rand_index] * weights))
                error = class_mat[rand_index] - h
                belta = (alpha * error)*ones(n)
                weights += belta * data_mat[rand_index]
                del (data_index[rand_index])
        return weights


if __name__ == "__main__":
    path = "./test.txt"
    data_mat, class_mat = LR.load_data_set(path)
    weights = LR.gradAscent(data_mat, class_mat)
    print "gradAscent weights %s" % weights

    weights = LR.stocGradAscent(data_mat, class_mat)
    print "stocGradAscent weights %s" % weights

    weights = LR.optimizedSGA(data_mat, class_mat)
    print "optimizedSGA weights %s" % weights

    print 'sfsf-fsf-fsd-f'.split('-', 2)
