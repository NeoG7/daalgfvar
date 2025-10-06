# Node класс – нэг зангилаа
class Node:
    def __init__(self, data):
        # энэ Node-ийн утга буюу өгөгдөл
        self.data = data  

        # дараагийн Node-руу заагч, эхлээд None
        self.next = None  

# LinkedList класс – зангилааг удирдана
class LinkedList:
    def __init__(self):
        # эхний зангилаа (head), эхлээд хоосон
        self.head = None  

    # Эхэнд node нэмэх
    def insert_at_beginning(self, data):
        # шинэ node үүсгэх
        new_node = Node(data)

        # шинэ node-ийн дараагийн заагчийг одоогийн head болгох
        new_node.next = self.head

        # head-г шинэ node болгох
        self.head = new_node
        # иймээс энэ node одоо эхэндээ байна

    # Төгсгөлд node нэмэх
    def insert_at_end(self, data):
        # шинэ node үүсгэх
        new_node = Node(data)

        # хэрвээ Linked List хоосон бол шинэ node-г шууд head болгох
        if self.head is None:
            self.head = new_node
            return

        # Linked List төгсгөлд очиж нэмэх
        last = self.head
        while last.next:  # хамгийн сүүлийн node-г олох хүртэл
            last = last.next
        last.next = new_node  # сүүлийн node-ийн дараагийн заагч шинэ node боллоо

    # Дурын байрлалд node нэмэх (0-с эхэлнэ)
    def insert_at_position(self, position, data):
        # хэрвээ байрлал 0 бол эхэнд нэмэх
        if position == 0:
            self.insert_at_beginning(data)
            return

        # шинэ node үүсгэх
        new_node = Node(data)

        # байрлалд хүрэхэд гүйлгэнэ
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        # хэрвээ байрлал Linked List-ийн уртнаас их бол мэдэгдэх
        if not current:
            print("Байрлал хэтэрсэн байна!")
            return

        # шинэ node-г байрлуулах
        new_node.next = current.next
        current.next = new_node

    # Linked List-г хэвлэх
    def print_list(self):
        current = self.head
        while current:
            # node-ийн өгөгдлийг хэвлэх
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Linked List төгсгөл

# -----------------------------
# Туршилт
# -----------------------------
if __name__ == "__main__":
    # Linked List үүсгэх
    ll = LinkedList()

    # Төгсгөлд node нэмэх
    ll.insert_at_end(10)  # Linked List: 10
    ll.insert_at_end(20)  # Linked List: 10 -> 20
    ll.insert_at_end(30)  # Linked List: 10 -> 20 -> 30

    # Эхэнд node нэмэх
    ll.insert_at_beginning(5)  # Linked List: 5 -> 10 -> 20 -> 30

    # Дурын байрлалд node нэмэх (2-р байрлалд 15)
    ll.insert_at_position(2, 15)  # Linked List: 5 -> 10 -> 15 -> 20 -> 30

    # Linked List-г хэвлэх
    print("Linked List:")
    ll.print_list()
