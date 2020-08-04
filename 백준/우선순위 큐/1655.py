class minheap:
    def __init__(self):
        self.queue = [None]
    
    def insert(self, n):
        self.queue.append(n)
        lastidx = len(self.queue) - 1
        while lastidx > 1:
            parentidx = lastidx // 2
            if self.queue[parentidx] > self.queue[lastidx]:
                self.queue[parentidx], self.queue[lastidx] = self.queue[lastidx], self.queue[parentidx]
                lastidx = parentidx
            else:
                break
        
    def delete(self):
        retval = self.queue[1]
        self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
        del self.queue[-1]
        parentidx = 1
        while parentidx * 2 <= len(self.queue) - 1:
            left = parentidx * 2
            right = parentidx * 2 + 1
            if left == len(self.queue) - 1:
                childidx = left
            elif self.queue[left] < self.queue[right]:
                childidx = left
            else:
                childidx = right
            
            if self.queue[parentidx] > self.queue[childidx]:
                self.queue[parentidx], self.queue[childidx] = self.queue[childidx], self.queue[parentidx]
                parentidx = childidx
            else:
                break
        return retval

class maxheap:
    def __init__(self):
        self.queue = [None]
    
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
        retval = self.queue[1]
        self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
        del self.queue[-1]
        parentidx = 1
        while parentidx * 2 <= len(self.queue) - 1:
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
        return retval

import sys
input = sys.stdin.readline
minh = minheap()
maxh = maxheap()
for _ in range(int(input())):
    n = int(input())
    if len(maxh.queue) == len(minh.queue):
        maxh.insert(n)
    else:
        minh.insert(n)
    
    if len(minh.queue) != 1 and maxh.queue[1] > minh.queue[1]:
        minval = minh.delete()
        maxval = maxh.delete()
        minh.insert(maxval)
        maxh.insert(minval)
    
    print(maxh.queue[1])        