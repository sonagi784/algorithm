class Maxheap:
    def __init__(self):
        self.queue = [0]
        
    def insert(self, n):
        self.queue.append(n)
        lastidx = len(self.queue) - 1
        while lastidx > 1:
            parentidx = lastidx // 2
            if self.queue[parentidx] < self.queue[lastidx]:
                self.queue[parentidx], self.queue[lastidx] = self.queue[lastidx], self.queue[parentidx]
                lastidx = parentidx
            else:
                break
    
    def delete(self):
        if len(self.queue) == 1:
            print('0')
            return;
        self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
        print(self.queue[-1])
        self.queue.pop()
        parentidx = 1
        while parentidx*2 <= len(self.queue) - 1:
            left = parentidx * 2
            right = parentidx * 2 + 1
            if left == len(self.queue) - 1:
                childidx = left
            elif self.queue[left] > self.queue[right]:
                childidx = left
            else:
                childidx = right
            
            if self.queue[parentidx] < self.queue[childidx]:
                self.queue[parentidx], self.queue[childidx] = self.queue[childidx], self.queue[parentidx]
                parentidx = childidx
            else:
                break

import sys

h = Maxheap()
for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0:
        h.delete()
    else:
        h.insert(x)