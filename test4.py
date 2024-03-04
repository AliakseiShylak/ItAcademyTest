class Element:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v

    def get_previous(self):
        return self.previous

    def set_previous(self, p):
        self.previous = p

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

class LinkedList:
    def __init__(self):
        self.empty_element = Element(None)
        self.first = self.empty_element
        self.last = self.empty_element

    def print_list(self):
        el = self.first
        while el:
            print(el.get_value())
            el = el.get_next()
        print()

    def push(self, element):
        if self.last is self.empty_element:
            self.last = element
            self.first = element
        else:
            self.last.set_next(element)
            element.set_previous(self.last)
            self.last = element

    def unshift(self, element):
        if self.first is self.empty_element:
            self.last = element
            self.first = element
        else:
            self.first.set_previous(element)
            element.set_next(self.first)
            self.first = element

    def pop(self):
        if self.last is not self.empty_element:
            if self.last.get_previous() == None:
                self.last = self.empty_element
                self.first = self.empty_element
            else:
                self.last = self.last.get_previous()
                self.last.get_next().set_previous(None)
                self.last.set_next(None)

    def shift(self):
        if self.first is not self.empty_element:
            if self.first.get_next() == None:
                self.last = self.empty_element
                self.first = self.empty_element
            else:
                self.first = self.first.get_next()
                self.first.get_previous().set_next(None)
                self.first.set_previous(None)


el1 = Element(1)
el2 = Element(2)
el3 = Element(3)

link_list = LinkedList()
link_list.print_list()
link_list.pop()
link_list.print_list()
link_list.push(el1)
link_list.push(el2)
link_list.unshift(el3)
link_list.print_list()
link_list.pop()
link_list.print_list()
link_list.shift()
link_list.print_list()
link_list.shift()
link_list.print_list()