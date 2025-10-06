# Node класс – өгөгдөл + өмнөх ба дараагийн Node
class Node:
    def __init__(self, data):
        # TODO: өгөгдөл оруулах
        self.data = None
        # TODO: дараагийн Node
        self.next = None
        # TODO: өмнөх Node
        self.prev = None

# Doubly Linked List класс
class DoublyLinkedList:
    def __init__(self):
        # TODO: head-г None болгох
        self.head = None

    # Эхэнд нэмэх
    def insert_at_beginning(self, data):
        # TODO: шинэ Node үүсгэх
        # TODO: хэрвээ хоосон бол head-г шинэ Node болгох
        # TODO: өөр тохиолдолд өмнөх болон дараагийн заагчийг тохируулах
        pass

    # Төгсгөлд нэмэх
    def insert_at_end(self, data):
        # TODO: шинэ Node үүсгэх
        # TODO: хэрвээ хоосон бол head-г шинэ Node болгох
        # TODO: төгсгөлд нэмэх
        pass

    # Linked List хэвлэх
    def print_list(self):
        # TODO: Linked List-г дарааллаар хэвлэх
        pass

# Туршилт
if __name__ == "__main__":
    dll = DoublyLinkedList()
    # TODO: эхэнд болон төгсгөлд хэд хэдэн Node нэмэх
    # TODO: print_list-г ашиглан Linked List-г хэвлэх
