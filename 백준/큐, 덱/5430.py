class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.reverse = False
        
    def isempty(self):
        if self.head == self.tail == None:
            return True
        return False
        
    def push(self, data):
        newNode = Node(data)
        if self.isempty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def R(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        self.reverse = not self.reverse
    
    def D(self):
        if self.isempty():
            raise IndexError('D from empty deque')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if self.reverse:
                self.head = self.head.prev
                self.head.next = None
            else:
                self.head = self.head.next
                self.head.prev = None
                
    def printall(self):
        result = []
        temp = self.head
        while(temp != None):
            result.append(temp.data)
            if self.reverse:
                temp = temp.prev
            else:
                temp = temp.next
        print('[' + ','.join(result) + ']')
    
for _ in range(int(input())):
    q = Deque()
    func = list(input())
    n = int(input())
    if n == 0: 
        input()
        error = (func[0] == 'D')
    else:
        arr = input()[1:-1].split(',')
        for num in arr:
            q.push(num)
        error = False
        
        for i in range(len(func)):
            if func[i] == 'R':
                q.R()
            elif q.isempty():
                error = True
                break;
            else: # func[i] == 'D"  O(N)
                q.D()
                
    if error:
        print('error')
    else:
        q.printall()