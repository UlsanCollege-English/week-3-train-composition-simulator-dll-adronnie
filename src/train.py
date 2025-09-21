class _Car:
    __slots__ = ("id", "prev", "next")

    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None


class Train:
    def __init__(self):
        self.head = None
        self.tail = None

    def attach_front(self, car_id):
        node = _Car(car_id)
        if not self.head:  # empty
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return True

    def attach_back(self, car_id):
        node = _Car(car_id)
        if not self.tail:  # empty
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return True

    def detach_front(self):
        if not self.head:
            return None
        node = self.head
        if self.head == self.tail:  # only one
            self.head = self.tail = None
        else:
            self.head = node.next
            self.head.prev = None
        return node.id

    def detach_back(self):
        if not self.tail:
            return None
        node = self.tail
        if self.head == self.tail:  # only one
            self.head = self.tail = None
        else:
            self.tail = node.prev
            self.tail.next = None
        return node.id

    def detach(self, car_id):
        node = self.head
        while node:
            if node.id == car_id:
                # fix neighbors
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                return True
            node = node.next
        return False

    def to_list(self):
        res = []
        node = self.head
        while node:
            res.append(node.id)
            node = node.next
        return res
