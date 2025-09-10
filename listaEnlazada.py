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
    def intercambiarAdyacente(self):
        if self.First is None or self.First.next is None:
            return
        prev = None
        current = self.First
        self.First = current.next
        while current and current.next:
            siguienteNodo = current.next
            siguientePar = siguienteNodo.next

            siguienteNodo.next = current
            current.next = siguientePar

            if prev: 
                prev.next = siguienteNodo
            prev = current
            current = siguientePar

    def __len__(self):
        return self.Size

    def __str__(self):
        string = "["
        current = self.First
        while current is not None:
            string += str(current)
            if current.next is not None:
                string += "-> "
            current = current.next
        string += "]"
        return string


