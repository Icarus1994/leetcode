# -*- coding: utf-8 -*-
# @Time : 2019-08-23 16:00
# @Author : icarusyu
# @FileName: 2019_秋招_丢失的序列.py.py
# @Software: PyCharm

import sys



# 题目
# 有一个含有n个数字的序列，每个数字的大小是不超过200的正整数，同时这个序列满足以下条件：
# 1. a_1<=a_2
# 2. a_n<=a_(n-1) （当n>2时，最后两个数组元素满足的条件）
# 3. a_i<=max(a_{i-1},a_{i+1}) （除了首尾元素，其他数组元素应满足的条件）
# 在序列保存的过程中，有些数字丢失了，计算可能有多少种不同的序列可以满足以上条件。