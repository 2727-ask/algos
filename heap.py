class Heap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        self.heapify(len(self.arr)-1)

    def replace(self, val):
        if(len(self.arr) > 0):
            self.arr = self.arr[1:len(self.arr)]
            print(self.arr)
            self.trickle(0)
       
        
    def trickle(self, i):
        parent = i
        left = 2*i + 1
        right = 2*i + 2




    def heapify(self, i):
        parent = (i-1) // 2
        while(i > 0 and self.arr[parent] < self.arr[i]):
            temp = self.arr[parent]
            self.arr[parent] = self.arr[i]
            self.arr[i] = temp
            i = parent
            parent = (i-1) // 2

    
    def display(self):
        for x in self.arr:
            print(x)

heap = Heap() #[3, 1 , 2]


heap.insert(10)  # Add 10
heap.insert(20)  # Add 20
heap.insert(5)   # Add 5
heap.insert(30)  # Add 30
heap.insert(15)
heap.insert(100)
heap.insert(0)
heap.insert(1)
heap.insert(0)
heap.display()

print(20 * "--")


heap.display()
        