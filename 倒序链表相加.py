# -*- coding: utf-8 -*-
'''
@Description: 
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

@Date: 2019-09-06 15:19:17
@Author: CRAZYShimakaze
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        new = ListNode(0)
        temp = new
        while l1 != None or l2 != None or flag != 0:
            if flag == 1:
                su = 1
                flag = 0
            else:
                su = 0
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val
            su += a + b
            if su > 9:
                flag = 1
                su -= 10
            newNode = ListNode(su)
            new.next = newNode
            new = newNode
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return temp.next
