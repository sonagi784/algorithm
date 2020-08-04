import sys

class Stack:
  def __init__(self):
    self.num = []
  
  def insert(self, data):
    if data == 0:
      del self.num[-1]
    else:
      self.num.append(data)
  
s = Stack()
for _ in range(int(input())):
  data = sys.stdin.readline().rstrip('\n')
  s.insert(int(data))

print(sum(s.num))
