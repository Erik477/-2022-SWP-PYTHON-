
class ArrayNode():
    def __init__(self, content=None):
        super().__init__(content)

    def __str__(self):
        return super().__str__()


class ArrayListIterable():
    def __init__(self, array_list):
        super().__init__(array_list)

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        return super().__next__()


class ArrayList():
    __standard_initiation_size = 25

    def __init__(self, _type=int, size: int = __standard_initiation_size, _list=None):
        self.__initiation_size = size
        self.container = tuple(ArrayNode() for node in range(self.__initiation_size))
        self.__type = _type
        super().__init__(_list)

    def __iter__(self):
        return ListIterableInterface(self)

    def is_empty(self):
        return super().is_empty()

    def __contains__(self, content):
        for node in self.container:
            if content.__eq__(node.content):
                return True
        return False

    def __str__(self):
        return super().__str__() + \
            f"<{self.__type.__name__}>({self.__len__()}/{len(self.container)})" + \
            f":{[node.content for node in self.container if node.content is not None]}"

    def __len__(self):
        return sum(1 for node in self.container if node.content is not None)

    def __resize(self, multiplier=2):
        self.container = tuple(
            ArrayNode(self.container[i].content if i < self.__len__() else None) for i in range(
                len(self.container) * multiplier
            )
        )

    def add(self, content: object):
        if type(content) is not self.__type:
            raise TypeError()
        if self.__len__() == len(self.container):
            self.__resize()
        for node in self.container:
            if node.content is None:
                node.content = content
                return


    def insert(self, index: int, content: object):
        if type(content) is not self.__type:
            raise TypeError
        if self.__len__() == len(self.container):
            self.__resize()
        temp_content = content
        for i in range(index, self.__len__()):
            self.container[i].content, temp_content = temp_content, self.container[i].content
        self.add(temp_content)


    def set(self, index: int, content: object):
        self.container[index].content = content

    def replace(self, lambda_expression, index=None):
        if index is not None:
            if not 0 <= index < self.__len__():
                raise IndexError
        for node in self.container if index is None else [self.container[index]]:
            if node.content is not None:
                node.content = lambda_expression(node.content)

    def clear(self, resize=False):
        if resize:
            self.container = tuple(ArrayNode() for i in range(self.__initiation_size))
        else:
            for node in self.container:
                node.content = None

    def remove(self, content: object):
        if type(content) is not self.__type:
            raise TypeError
        start = False
        for i in range(self.__len__() - 1):
            if not start and content.__eq__(self.container[i].content):
                start = True
            if start:
                self.container[i].content = self.container[i + 1].content
        self.container[self.__len__() - 1].content = None

    def pop(self, index):
        output = self.container[index].content
        for i in range(index, self.__len__() - 1):
            self.container[i].content = self.container[i + 1].content
        self.container[self.__len__() - 1].content = None
        return output
