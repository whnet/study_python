# -*- coding: utf-8 -*-
'''
增长量级
O(1)       : 常数级（constant）
O(logb^n)  : 对象级(logarithmic)(对于任意b)
O(n)       : 线性级(linear)
O(nlogb^n) : 线性对数级(linearithmic)
O(n^2)     : 二次方级(quadratic)
O(n^3)     : 三次方级(cubic)
O（c^n）   : 指数级(exponential)（对于任意c）
[(\log n)^{c}  多对数
O(n!)      :  阶乘
对于对数级数  【O(logb^n)】， 对数的基数并不影响增长量级。改变阶数等价于乘以一个常熟， 其不改变增长量级。
所有的指数级别 【O（c^n）】，都属于相同的增长量级，而无需考虑指数的基数大小（指数量级增长的非常快，因此指数级算法只用于小规模）

大O符号在分析算法效率的时候非常有用
举个例子：
解决一个规模为 {\displaystyle n} n的问题所花费的时间（或者所需步骤的数目）可以表示为：
 T(n)=4n^{2}-2n+2。当 n增大时， {\displaystyle n^{2}} n^{2}项将开始占主导地位，而其他各项可以被忽略。
 举例说明：当  n=500， 4n^{2}项是 2n项的1000倍大，
因此在大多数场合下，省略后者对表达式的值的影响将是可以忽略不计的。
进一步看，如果我们与任一其他级的表达式比较， {\displaystyle n^{2}} n^{2}项的系数也是无关紧要的。

'''
l = [14,10,9,13,34,26,11,7]
# 插入排序
'''
先假设list[min_index]处的值最小，再跟后面的值依次比较，
当发现list[j]比list[min_index]值小时，这时的min_index替换为j，
再跟后面的进行比较，指导找到最小的那个list[j]，
将j付给min_index，这时l[min_index]就是遍历过程中的最小值了
'''


def insert_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            min = l[ min_index]
            next = l[j]
            if min > next:
                min_index = j
        tmp = l[i]
        l[i] = l[min_index]
        l[min_index] = tmp
        print(str(l))

'''
它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。
'''
def bub_sort(l):
    # 冒泡排序, 相邻的两个数进行比较
    count = len(l)
    for i in range(0, count):
        for j in range(i + 1, count):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

print(bub_sort(l))