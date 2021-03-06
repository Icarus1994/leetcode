# -*- coding: utf-8 -*-
# @Time : 2019-10-18 16:32
# @Author : icarusyu
# @FileName: dp.py.py
# @Software: PyCharm


'''
5 Longest Palindromic Substring
状态转移：
dp[i][j]表示的是s[i:j+1]是否是回文串
dp[i][j] = 1 if dp[i] == dp[j] and dp[i+1][j-1]==1
细节：遍历时顺序和大小应该是：
for i in range(1,len):
    for j in range(1,i+1):
即需要先控制回文串的终点从小到大先更新完，否则更新dp[i][j]时的dp[i+1][j-1]没有被先更新，就得不到正确结果了


10 Regular Expression Matching
题目：
给定字符串s和模式p,s中只包含小写字母，p包含小写字母和. *
.表示匹配任意单个字符
*可匹配它的前一个字符0次到多次，如有a*时可以匹配空字符串
注意.*结合可以表示任意字符串

【循环第一层(i)为p】,第二层(j)为s,分情况讨论
当p[i]=='*'时，可以匹配前面的字符0次，1次，多次.
【匹配多次时，状态转移方程中只要考虑p[i]和s[j-1]是否能匹配即可】，因为随着j的增大，就能匹配到多个*前的字符
匹配多次时又分为*前的字符是否等于.两种情况,如果是.*组合那么可以匹配任意字符串


44 Wildcard Matching
题目：
给定字符串s和模式p,s中只包含小写字母，p包含小写字母和. *
？表示匹配单个字符，*表示匹配任意字符串，包括空字符串

外层先遍历p,当第i个字符是*时，for j in range(1,len(s)+1),dp[i][j] = 1 if dp[i-1][j] ==1 or dp[i][j-1]==1(匹配多次。传递性)


53 maximum subarray 数据结构课程第一道算法题
方法一：分治法,O(nlogn),注意分治法只有当合并的这一步骤时间复杂度为线性时最后才能得到O(nlogn)
方法二：在线，先遍历找到数组中最小的，指针i从左到右遍历一次，sum+=当前元素值，当sum为负数时另sum为0，每加一次更新Max  x


72 edit distance
dp[i][j] = dp[i-1][j-1] if A[i-1] == B[i-1]
         = min(dp[i][j-1],dp[i-1][j], dp[i-1][j-1]) +1
记得初始化第一行第一列，dp大小为(len(A) +1) * (len(B) +1)


121 买股票-最多买一次
分治法，归并排序
1、在合并阶段，左子数组内部已经找到了子数组内买卖股票能挣到的最多的前，右子数组也是，又因为左右子数组已经排好序了，那么只要考虑
在左右子数组之间买卖股票能挣到的最多的前即可，然后合并左右子数组
2、合并阶段，左右子数组（是新创建的）下标分别为i,j,更新后的数组是对函数传进来的参数prices数组进行修改。
【更新prices数组时使用i+j作为下标】

变种题：买股票，至少买一次
双指针，下标i,j，j往前遍历，当第一次出现prices[j]>prices[j+1]时，买一次股票，i = j+1,j继续前进


139 判断字符串是否能正好由词典中的词分割
一维dp数组
for j in range(1,len(s)+1)
    for i in range(j-1,-1,-1),判断s[i:j]是否在字典中，如果存在且dp[i]==1则dp[j]==1


【注意】动态规划中两个要注意遍历dp数组时顺序的题
判断回文串，for j in range(1,n+1) for i in range(1,j+1)
139 字符串能否由词典的词分割 for j,for i

140 hard

322 coin change背包
给定面额，求用硬币组成该面额的最小数量
dp = [sys.maxsize] * (amount+1)
        for coin in coins: # ！！！
            if coin <= amount:
                dp[coin] =1
            for i in range(coin+1,amount+1,1):
                if dp[i-coin] != sys.maxsize:
                    dp[i] = min(dp[i], dp[i-coin] +1) # ！！！
        return -1 if dp[-1] == sys.maxsize else dp[-1]
'''
