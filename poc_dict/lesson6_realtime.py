#!/usr/bin/env python
# coding: utf-8

# In[7]:


#---基础---
#创建、访问、修改、删除
#1.创建字典
dic={
    'key1':'hello world',
    'key2':100,
    'key3':0.618,
    'key4':['a','b',1,2,3],
    'key5':('a','b',1,2,3)
}
print(dic)


# In[8]:


#添加键值对 key value-pair
dic['key100'] = 'CAS'
print(dic)


# In[9]:


#2.访问字典
#2.1 通过key读取value
value = dic['key5']
print(value)
#若有两个相同的key，会读取同名的最后一个


# In[10]:


#2.2.1 获取key
list_keys = dic.keys()
print(list_keys)

for k in list_keys:
    print(k)


# In[11]:


#2.2.2 获取values
list_values = dic.values()
print(list_values)

for k in list_values:
    print(k)


# In[12]:


#2.2.3获取键值并以元组形式存入列表
pairs = []
for k,v in dic.items():
    print(k,':\t',v) # \t表示一个tab
    pair = (k,v)
    pairs.append(pair)
print(pairs)


# In[14]:


#3.修改字典
dic['key2'] = 3000
print(dic)

dic['key22'] = 2000 #若key不存在，会新增，但C++等中会报错显示这个key不存在
print(dic)


# In[15]:


#4.删除字典
del dic['key22']
print(dic)


# In[18]:


#---进阶---
#创建、访问、修改、删除
#1.1 创建
dic = {}
seq = ('name','age','sex')
dic = dic.fromkeys(seq)
print(dic)


# In[20]:


#1.2 以默认值创建
dic = dic.fromkeys(seq,10)
print(dic)


# In[ ]:


#2.访问字典
#2.1 
if 'age' in dic:
    print('键 存在')
else:
    print('键 不存在')


# In[21]:


#2.2.1 返回指定键的值
v = dic.get('school')
print(v)


# In[22]:


#2.2.2 返回指定键的值，若不存在则返回默认值
v = dic.get('school','CAS')
print(v)


# In[24]:


v = dic.setdefault('school','CAS')
print(dic)


# In[25]:


#2.3 随机返回并删除字典中的（最后一个）键值对
dic['school'] = 'CSA'
print(dic)
popped = dic.popitem()
print(popped)
print(dic)


# In[ ]:


#堆栈 LIFO --子弹夹 后进先出
#队列 FIFO --消息队列 常用数据结构：微信、游戏等


# In[27]:


#2.4 删除指定key
popped = dic.pop('name','默认值')
#popped = dic.pop('name') 不设置默认值的话若不存在会报错
print(popped)
print(dic)


# In[28]:


#3.修改字典
dic_new = {
    'name':'Mike',
    'height':1.88,
    'weight':70,
    'age':20
}
dic.update(dic_new)
print(dic)
#没有则添加，有则用新字典覆盖


# In[29]:


#4.删除字典
dic.clear() #清空字典
print(dic)


# In[ ]:


del dic #删除字典

