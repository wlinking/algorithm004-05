# NOTE
总结第一周
学习内容：本周学习一维线性数据结构数组，链表，跳表，栈的基本特征，学习队列（含优先队列，双端队列）源码的搜索及分析方法。
学习了数组3个、栈2个题目的精讲。

学到什么：
1、解决算法问题，归纳的能力很重要，例如：《70爬楼梯》对于台阶数>2而言，都有差2个台阶，差1个台阶的2套爬楼梯的方法。
2、双指针思想：在数据两侧向中间移动
左指针坐标left = 0，右指针rigth = len(nums)-1。通过规则选择左指针或右指针移动，达到移动过程中处理数据的效果。主要应用在数组中元素与其他元素关系（大小，包夹面积等）中。
3、快慢指针思想：
a、快指针匀速，如每次移动2个元素，应用场景【环形链表】
b、快指针不匀速，根据条件移动元素个数不确定，如跳过重复元素，应用场景【移动特定相同元素，删除重复元素】

遇到问题：
1、“五毒神掌”一般只能执行完前2步，第三步感觉没有时间操作；
2、眼高手低情况严重，想到的思路写不出来，本以为if,for,while很简单，组合起来才发现如此复杂。
3、第一周的视频课中的“预习题目”“实战题目”无法在4天内完成，本人每题目耗时都很久，主要是在分析答案上，请问如何破解呢？
4、双端循环队列，我写的程序通过了提交，但我没感觉是循环了。


CodeReview:
# 755
leetcode_1:two_sum
不明白为什么要用"hashmap"这个词表示类型为dict的结果集，是hashmap有特殊含义还是随意起的名字，感觉会产生误导。
# 525
leetcode_189:rotate
代码真简洁，学习。
# 535
每段代码都有注释，一目了然。看其他同学都是代码一扔就完事了。
# 040
绝对是IDE编写的Python代码，有测试程序。
# 25
提交的代码十分工整，还分析了时间、空间复杂度，值得学习。
