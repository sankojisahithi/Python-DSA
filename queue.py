class Queue:
  def __init__(self,cap=5):
    self._a=[None for _ in range(cap)]
    self._front=0
    self._rare=-1
    self._c=0
  def peek(self):
    if self._c==0:
      return "no elements"
    return self._a[self._front]
  def enqueue(self,data):
    if self._c==len(self._a):
      print('overflow')
      return
    self._a[self._c]=data
    self._c+=1
  def rear(self):
    if self._c==0:
      return "no elements"
    return self._a[self._c-1]
  def dequeue(self):
    if self._c==0:
      print('underflow')
      return
    ar=[None for _ in range(len(self._a))]
    for i in range(1,self._c):
      ar[i-1]=self._a[i]
    self._c-=1
    temp=self._a[self._front]
    self._a=ar
    return temp
  def is_empty(self):
    return self._c==0
  def is_full(self):
    return self._c==len(self._a)
    
    


que=Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.dequeue()
print("Front:",que.peek())
print("Rear:",que.rear())
print(que.is_empty())
print(que.is_full())
print(que.rear())