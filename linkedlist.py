# -----------------------------
# Node класс – нэг зангилаа
# -----------------------------
class Node:
    def __init__(self, data):
        # TODO: өгөгдөл хадгалах
        self.data = None  

        # TODO: дараагийн Node руу заагч
        self.next = None  

# -----------------------------
# LinkedList класс
# -----------------------------
class LinkedList:
    def __init__(self):
        # TODO: Linked List-ийн эхний зангилаа
        self.head = None  

    # -------------------------
    # Эхэнд node нэмэх
    # -------------------------
    def insert_at_beginning(self, data):
        # TODO: Шинэ node үүсгэх
        # TODO: Шинэ node-г head болгох
        pass

    # -------------------------
    # Төгсгөлд node нэмэх
    # -------------------------
    def insert_at_end(self, data):
        # TODO: Шинэ node үүсгэх
        # TODO: Хэрвээ head хоосон бол шинэ node-г head болгох
        # TODO: Хэрвээ хоосон биш бол төгсгөлд оруулах
        pass

    # -------------------------
    # Дурын байрлалд node нэмэх (0-с эхэлнэ)
    # -------------------------
    def insert_at_position(self, position, data):
        # TODO: Хэрвээ position == 0 бол эхэнд нэмэх
        # TODO: Дурын байрлалд node нэмэх
        pass

    # -------------------------
    # Linked List хэвлэх
    # -------------------------
    def print_list(self):
        # TODO: Linked List-ийг дарааллаар хэвлэх
        pass

# -----------------------------
# Туршилт
# -----------------------------
if __name__ == "__main__":
    # TODO: Linked List үүсгэх
    ll = LinkedList()

    # TODO: Төгсгөлд node нэмэх
    # ll.insert_at_end(...)

    # TODO: Эхэнд node нэмэх
    # ll.insert_at_beginning(...)

    # TODO: Дурын байрлалд node нэмэх
    # ll.insert_at_position(...)

    # TODO: Linked List-г хэвлэх
    # ll.print_list()
