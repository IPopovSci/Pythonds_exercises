class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # def __repr__(self):
    #     return f'Node object: (Data:{self.data},next:{self.next})'
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
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.getNext()
        yield self.tail

    def isEmpty(self):
        return self.head == None

    def add(self, item):

        temp = Node(item)
        if self.tail==None:
            self.tail = temp
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
                self.tail=current
            elif not found:
                raise Exception('Item not found')
        if previous == None:
            self.head = current.getNext()
        elif found and self.tail:
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
    # def insert(self,position,item):
    #     current = self.head
    #     item_node = Node(item)
    #     list_pos=0
    #     if current:
    #         while list_pos != position:
    #             list_pos+=1
    #             if list_pos != position:
    #                 current = current.getNext()
    #             else:
    #                 #future_node = current.getNext()
    #                 self.head=item_node
    #                 #self.head = future_node
    #
    #     #current.setNext(item_node)




mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(31)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist)
mylist.remove(31)
print('head',mylist.head)
mylist.remove(31)
mylist.remove(54)
#mylist.append(100)
#mylist.insert(1,27)
print(mylist)
print('head',mylist.head)
print('tail',mylist.tail)
