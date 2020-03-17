Progress in completing the Ladders
==========================================================
![](static/dragonMaid.gif)

#### Mar 9
- [x] Followup ladders 
- [x] DP II 

follow up questions.<br>
segment tree要再看一遍<br>
博弈类dp太难了:scream: 还是滚动数组好<br>

#### Mar 10
- [x] Data Structure II - Stack, Deque, Heap video 
- [x] AD Ladder 3
- [x] DP I Video 
<br>
Mar 10. 3刷 Heap/Stack tag. <br>
Monotonic Stack： 递增递减判断。<br>
PriorityQueue / heapq：需要remove就用Java写，python override sift好烦

堆：     
>1. 解决动态求最大/最小值问题
>2. 动态第K大/小的问题
>3. 双堆解决动态中位数

栈：
>1. 实现非递归
>2. 单调栈解决找一个值左/有第一个比它大/小的值的问题 

#### Mar 11
- [x] DP I Video review
- [x] DP I Ladder
- [x] Binary Tree - Divide Conquer & Traverse

DP:
1. 滚动数组优化
2. 博弈问题， 必胜和必败
3. 区间型动态规划， 消去型问题: 按长度枚举。长度从小到大，每次固定长度从左到右计算
coins in a Line II
Scramble String: DFS + 剪枝
DPI review in 3 days 

#### Mar 12
- [x] Sweep Line + Binary Search video 
- [x] AD Ladder 4
- [x] Binary Tree Ladder 

扫描线：区间需要排序 => 扫描线
	   build events
双端队列：维护一个候选可能的最大值集合

#### Mar 13
- [x] Sweep Line + Binary Search video 
- [x] AD Ladder 4
- [x] Binary Search Ladder 
- [x] Breadth First Search Ladder 

rotated array problems 33, 153, 154, (leetcode)

#### Mar 14
- [x]CLEAN OVERLEFT LADDERS - all clear. 

Gym is closed. Sad :sob: 
No more fun. Just LC

#### Mar 15
- [x] ladder - 7 Hash & Heap
- [x] ladder - 6 DFS 


#### Mar 16
- [ ] ladder - 8 Memoization search
- [ ] ladder - 9 DP
- [ ] AD ladder - DP

啥玩意啊写的 一顿debug
真的动态规划你做成这样，就祈祷倒时候遇不到dp吧

消去型的动态规划，要逆折题意想。 Burst Balloon, guess Number Higher or LowerII, <br>
这道题里首先考虑最后一个被扎破的气球。
o xxxxxx X xxxxx o <br>

两边的o是我自己加的，相当于在nums首尾各加一个1， 为了保证所有气球被扎破的时候都有得分。这样最后一个也可以用 1 * num * 1 计算
X是最后一个被扎破的气球。 X左右的得分互不相关，因为X没被扎破的时候把两边都分开了。左右两边就是两个小区间<br>
所以f[i][j]就可以表示出来， i，j是不包括在区间内的，因为刚才加在首位的两个1就不包含在区间内。
所以f[i][j]代表的就是从i+1到j-1这个区间内能得到的最大值。<br>
转移方程就是f[i][j] = max(f[i][j], f[i][k] + f[k][j] + balloons[i] * balloons[k] * balloons[j])<br>
初始条件就是i, j相邻时候f[i][j] = 0. 因为区间的两个边界相邻，中间没有能扎的气球。
这道题我做的最差的地方是计算顺序。以后就固定计算顺序：
- 第一层循环：按照区间长度length从小到大
- 第二层循环：固定长度，区间的start从0取到len(balloons)-length，所以start循环的范围是for i in range(len(balloons) - length + 1). 对应的end： j = i + length - 1
- 第三层循环：i，j是不能扎破的两个气球，k就是i到j之间的某个最后一个扎破的气球。 for k in range(i + 1, j)
这题不能再写错了，三遍了都。。

