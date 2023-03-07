class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None

    def set_next_elem(self, nextElem):
        self.nextElem = nextElem

    def get_next_elem(self):
        return self.nextElem

    def get_obj(self):
        return self.obj

class EinfachVerketteteListe:
    def __init__(self):
        self.startElem = ListElement("0")

    def add_last(self, o):
        newElem = ListElement(o)
        lastElem = self.get_last_elem()
        lastElem.set_next_elem(newElem)

    def insert_after(self, prevItem, newItem):
        newElem = ListElement(newItem)
        pointerElem = self.startElem.get_next_elem()
        while pointerElem is not None and pointerElem.get_obj() != prevItem:
            pointerElem = pointerElem.get_next_elem()
        nextElem = pointerElem.get_next_elem()
        pointerElem.set_next_elem(newElem)
        newElem.set_next_elem(nextElem)

    def delete(self, o):
        le = self.startElem
        while le.get_next_elem() is not None and le.get_obj() != o:
            if le.get_next_elem().get_obj() == o:
                if le.get_next_elem().get_next_elem() is not None:
                    le.set_next_elem(le.get_next_elem().get_next_elem())
                else:
                    le.set_next_elem(None)
                    break
            le = le.get_next_elem()

    def find(self, o):
        le = self.startElem
        while le is not None:
            if le.get_obj() == o:
                return True
            le = le.nextElem
        return False

    def get_first_elem(self):
        return self.startElem

    def get_last_elem(self):
        le = self.startElem
        while le.get_next_elem() is not None:
            le = le.get_next_elem()
        return le

    def write_list(self):
        le = self.startElem
        while le is not None:
            print(le.get_obj())
            le = le.get_next_elem()

    def length(self):
        le = self.startElem
        count = 0
        while le is not None:
            count += 1
            le = le.get_next_elem()
        print(count)

if __name__ == '__main__':
    list = EinfachVerketteteListe()
    list.add_last("1")
    list.add_last("2")
    list.add_last("3")
    list.add_last("4")
    list.add_last("5")
    list.insert_after("2", "neu")
    list.delete("3")
    list.write_list()
    print("Lentgth:")
    list.length()

