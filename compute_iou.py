# -*- coding: utf-8 -*-
'''
@Description: 计算iou
@Date: 2019-04-18 17:52:38
@Author: CRAZYShimakaze
'''
def compute_iou(a, b):
    area1 = (a[2] - a[0]) * (a[3] - a[1])
    area2 = (b[2] - b[0]) * (b[3] - b[1])

    left = max(a[1], b[1])
    right = min(a[3], b[3])
    bottom = min(a[0], b[0])
    top = max(a[2], b[2])

    if left >= right or top < bottom:
        return 0
    else:
        area_a = (right - left) * (top - bottom)
        return area_a / (area1 + area2 - area_a)


rect1 = (663, 27, 679, 47)
# (bottom, left, top, right)
rect2 = (661, 22, 677, 45)
iou = compute_iou(rect1, rect2)
print(iou)
