"""
{
    "value": 4,
    "next": None
}

"""




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
       
    def print_values(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
                return temp
            return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        temp = self.head
        counter = 0
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            False

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


            



            

    # def append(self, value):

    # def prepend(self, value):

    # def insert(self, index, value):

class LinkedListTwo:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif self.length == 1:
            pre = self.head
            temp = self.head
        else:
            self.tail = new_node
            self.tail.next = new_node
        self.length += 1






    def print_head(self):
        temp = self.head
        while temp is not None:
            temp = temp.next
        return True
    
   

my_linked_list = LinkedList(4)
my_linked_list.append(2)
# my_linked_list.pop()
# my_linked_list.pop()
my_linked_list.prepend(9)
my_linked_list.prepend(7)
my_linked_list.prepend(2)
# my_linked_list.pop_first()



my_linked_list.insert(2, 9)

my_linked_list.print_values()


# my_linked_list.set_value(4, 8)

# print(f"new value is {my_linked_list.get(4)}")


