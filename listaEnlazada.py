class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.First = None
        self.Size = 0

    def Append(self, value):
        Mynode = Node(value)
        if self.Size == 0:
            self.First = Mynode
        else:
            current = self.First  # primer nodo es current
            while current.next is not None:
                current = current.next
            current.next = Mynode
        self.Size += 1
        return Mynode

    def Remove(self, value):
        if self.Size == 0:
            return False
        else:
            current = self.First
            # Si el primer nodo contiene el valor
            if current.value == value:
                self.First = current.next
                self.Size -= 1
                return True

            while current.next is not None:
                if current.next.value == value:
                    deletedNode = current.next
                    current.next = deletedNode.next
                    self.Size -= 1
                    return True
                current = current.next
        return False

    def __len__(self):
        return self.Size

    def __str__(self):
        string = "["
        current = self.First
        while current is not None:
            string += str(current)
            if current.next is not None:
                string += ", "
            current = current.next
        string += "]"
        return string


Mylist = LinkedList()
Mylist.Append(1)
Mylist.Append(2)
Mylist.Append(3)
Mylist.Append(4)

Mylist.Remove(1)
print(Mylist)
