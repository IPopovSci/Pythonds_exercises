class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __repr__(self):
        return f'Node object: (Data:{self.data},next:{self.next})'
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.getNext()
        if self.tail:
            nodes.append(self.tail.data)
        nodes.append("None")
        return str(nodes)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.getNext()
        if self.tail:
            nodes.append(self.tail.data)
        nodes.append("None")
        return [i for i in repr(nodes)]
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.getNext()
        yield self.tail

    #def __contains__(self, item):
    def isEmpty(self):
        return self.head == None

    def add(self, item):

        temp = Node(item)
        if self.tail==None:
            self.tail = temp
            self.length+=1
        else:
            temp.setNext(self.head)
            self.head = temp
            self.length+=1


    def size(self):
        return self.length

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if self.length==0:
            raise Exception("Can't delete last item in an empty list")
        while not found and current!=None:
            if current.getData() == item:
                found = True
            elif current.getNext()!=None:
                previous = current
                current = current.getNext()
            elif self.tail.getData()==item:
                found=True
                self.tail=current #Set tail to last value, meaning item was the last element;
            elif not found:
                raise Exception('Item not found')
        if previous == None: #If the element to remove was the first one
            self.head = current.getNext()
        elif found: #Remove the element found
            previous.setNext(current.getNext())

        self.length-=1
    #Implement append, insert, index, and pop
    #O(n) append:
    def append_on(self,item):
        current = self.head
        item_node = Node(item)
        if current:
            while current.getNext() != None:
                current=current.getNext()
            current.setNext(item_node)
        else:
            current.setNext(item_node)
        self.length+=1
    #O(1) append:
    def append(self,item):
        item_node = Node(item)
        self.tail=item_node
        self.length+=1
    def insert(self,position,item):
        current = self.head
        item_node = Node(item)
        list_pos=0
        if position>self.length:
            raise Exception("Out of bounds")
        while current.getNext()!=None and list_pos<position: #general case for not 0 and not end
            list_pos+=1
            previous=current
            current=current.getNext()
        if position == 0: #For position 0
            item_node.setNext(current)
            self.head = item_node
        elif position == self.length: #Case for tail
            current.setNext(self.tail)
            self.tail=item_node
        else: #General case
            item_node.setNext(current)
            previous.setNext(item_node)
        self.length += 1

    def pop(self,position):
        current = self.head
        future=self.head
        list_pos=0
        if position>self.length:
            raise Exception("Out of bounds")
        while current.getNext()!=None and list_pos<position: #general case for not 0 and not end
            list_pos+=1
            current=future
            future = current.getNext()
        if position == 0: #For position 0
            self.head = self.head.getNext()
        elif position == self.length: #Case for tail
            self.tail = future
        else: #General case
            current.setNext(future.getNext())
        self.length -= 1









mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(31)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist)
#mylist.append(100)
mylist.pop(3)
print(mylist)
print('head',mylist.head)
print('tail',mylist.tail)
