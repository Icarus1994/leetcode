# -*- coding: utf-8 -*-
# @Time : 2019-08-25 15:50
# @Author : icarusyu
# @FileName: LCS.py.py
# @Software: PyCharm
class Solution:
    # 空间复杂度2*len(A)
    def findLength(self, A, B):
        if not A or not B or len(A) == 0 or len(B) == 0:
            return 0
        up = [0 for i in range(len(A) + 1)]
        down = [0 for i in range(len(A) + 1)]
        # B作为二维数组的列
        for i in range(1, len(B) + 1):
            for j in range(1, len(A) + 1):
                if B[i - 1] == A[j - 1]:
                    down[j] = up[j - 1] + 1
                else:
                    down[j] = max(down[j - 1], up[j])
            up = down
            down = [0 for i in range(len(A) + 1)]
        return up[-1]

    # 空间复杂度len(A) * len(B)
    def LCS(self,A,B):
        if not A or not B:
            return 0
        # 考虑长度为1的边界条件
        # 两个细节：用来统计LCS长度的二维数组，长和宽都要比输入的两个数组的长度大1；
        # 遍历A，B数组时设置从1开始，因为从0开始时和存储LCS的数组下标冲突
        a = [0] * (len(B)+1)
        c = [a for i in range(len(A)+1)]
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1] == B[j-1]:
                    c[i][j] = c[i-1][j-1] +1
                else:
                    c[i][j] = max(c[i-1][j],c[i][j-1])
        return c[-1][-1]

A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
ans = Solution().findLength(A, B)
print(ans)

# 原理参考
# https://blog.csdn.net/hrn1216/article/details/51534607

