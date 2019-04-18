# Python3_algorithm
日常记录pyhton3的各种函数用法与技巧

## 1.str.strip()

只要头尾包含有指定字符序列中的字符就删除：

```python
   "12abcrob321" 
   print(str.strip('12'))#字符序列为12
   abcrob3
```

## 2.list()&str()

```python
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

str.find()返回索引，不存在返回-1

str.index()返回索引，不存在报错

str不存在删除，可考虑使用replace

------

list.remove()，del list[index]删除列表元素

list.index()返回索引，不存在报错

## 3.ord()&chr()

ord返回字符的ASCII码

chr返回对应的ASCII字符

## 4.set()

定义：无序的不重复元素序列

set.add()重复则不进行操作

set.update()添加元素

```python
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)
{1, 3, 'Google', 'Taobao', 'Runoob'}
```

set.remove()不存在则报错

set.discard()不存在不报错

## 5.正则表达式

判断素数：

```python
print('yes!') if not re.match(r'1?$|(11+?)\1+$','1'*N) else print('no!')
```

## 6.for ... else ...

```python
for i in range(1,10):
	if i == 1:
		print("Yes")
		break
else:
	print("No")
for i in range(1,10):
	if i == 1:
		print("Yes")
else:
	print("No")
Yes
Yes
No
```

## 7.global
声明变量为全局变量，函数内部也可使用。

## 8.queue
双端队列：
```python
q = queue.deque()
q.popleft()
q.appendleft()
```
