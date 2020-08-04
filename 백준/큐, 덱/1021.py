class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isempty(self):
        if self.head == self.tail == None:
            return True
        return False
    
    def push_front(self, data):
        newNode = Node(data)
        if self.isempty():
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = self.tail
            self.tail.next = newNode
    
    def push_back(self, data):
        newNode = Node(data)
        if self.isempty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            newNode.next = self.head
            self.head.prev = newNode
            
    def pop_front(self):
        if self.isempty(): # 0
            raise IndexError('pop from empty Deque')
            return;
        elif self.head == self.tail: # 1
            ret_data = self.head.data
            self.head = None
            self.tail = None
        else: # 2 이상
            ret_data = self.head.data
            self.head = self.head.next
            self.head.prev = self.tail
        return ret_data
        
    def pop_back(self):
        if self.isempty(): # 0
            raise IndexError('pop from empty Deque')
            return;
        elif self.head == self.tail: # 1
            ret_data = self.tail.data
            self.head = None
            self.tail = None
        else: # 2 이상
            ret_data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = self.head
        return ret_data
        
    def peek_left(self, target): # target == data in deque
        temp = self.head
        count = 0
        while(temp.data != target):
            if temp.prev == None: break;
            temp = temp.prev
            count += 1
        return count
    
    def peek_right(self, target):
        temp = self.head
        count = 0
        while(temp.data != target):
            if temp.next == None: break;
            temp = temp.next
            count += 1
        return count
        
    def rotate_left(self, loop):
        for _ in range(loop):
            self.push_back(self.pop_front())
        
    def rotate_right(self, loop):
        for _ in range(loop):
            self.push_front(self.pop_back())
            
        
N, M = map(int, input().split()) # 1 < M <= N <= 50
pos = list(map(int, input().split()))
q = Deque()
result = 0
for i in range(1, N+1):
    q.push_back(i)
for i in range(M):
    l = q.peek_left(pos[i])
    r = q.peek_right(pos[i])
    if l >= r:
        q.rotate_left(r)
        result += r
    else:
        q.rotate_right(l)
        result += l
    q.pop_front()
print(result)