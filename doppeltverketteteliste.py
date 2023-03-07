class ListElement:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None


    def set_next(self, next):
        self.next = next
    
    def set_prev(self, prev):
        self.prev = prev
    
    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
    
    def get_data(self):
        return self.data

class DoppeltVerketteteListe:
    def __init__(self):
        self.startElem = ListElement("0")
        self.endElem = ListElement("0")
        self.startElem.set_next(self.endElem)
        self.endElem.set_prev(self.startElem)

    def add_last(self, o):
        newElem = ListElement(o)
        lastElem = self.get_last_elem()
        lastElem.set_next(newElem)
        newElem.set_prev(lastElem)
        newElem.set_next(self.endElem)
        self.endElem.set_prev(newElem)

    def insert_after(self, prevItem, newItem):
        newElem = ListElement(newItem)
        pointerElem = self.startElem.get_next()
        while pointerElem is not self.endElem and pointerElem.get_data() != prevItem:
            pointerElem = pointerElem.get_next()
        nextElem = pointerElem.get_next()
        pointerElem.set_next(newElem)
        newElem.set_prev(pointerElem)
        newElem.set_next(nextElem)
        nextElem.set_prev(newElem)

    def delete(self, o):
        le = self.startElem
        while le.get_next() is not self.endElem and le.get_data() != o:
            if le.get_next().get_data() == o:
                if le.get_next().get_next() is not self.endElem:
                    le.set_next(le.get_next().get_next())
                    le.get_next().set_prev(le)
                else:
                    le.set_next(self.endElem)
                    self.endElem.set_prev(le)
                    break
            le = le.get_next()

    def find(self, o):
        le = self.startElem
        while le is not self.endElem:
            if le.get_data() == o:
                return True
            le = le.get_next()
        return False

    def get_first_elem(self):
        return self.startElem

    def get_last_elem(self):
        le = self.startElem
        while le.get_next() is not self.endElem:
            le = le.get_next()
        return le

    def print_list(self):
        le = self.startElem
        while le is not self.endElem:
            print(le.get_data())
            le = le.get_next()

if __name__ == 'main':
    list = DoppeltVerketteteListe()
    list.add_last("1")
    list.add_last("2")
    list.add_last("3")
    list.print_list()
    print("")
    list.delete("2")
    list.print_list()
    print("")
    list.insert_after("1", "neu")
    list.print_list()
