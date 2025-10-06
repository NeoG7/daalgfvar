# Queue класс – First In First Out (FIFO)
class Queue:
    def __init__(self):
        # TODO: хоосон жагсаалт үүсгэх
        self.items = []

    # Элемент нэмэх (enqueue)
    def enqueue(self, data):
        # TODO: element-г жагсаалтын төгсгөлд нэмнэ
        pass

    # Элемент гаргах (dequeue)
    def dequeue(self):
        # TODO: хэрвээ хоосон биш бол эхний элементийг авна
        # TODO: хоосон бол мэдэгдэх
        pass

    # Хоосон эсэх
    def is_empty(self):
        # TODO: Queue хоосон эсэхийг шалгах
        pass

    # Queue-г хэвлэх
    def print_queue(self):
        # TODO: Queue-г хэвлэх
        pass

# Туршилт
if __name__ == "__main__":
    q = Queue()
    # TODO: enqueue функцээр хэд хэдэн элемент нэмэх
    # TODO: dequeue функцээр элементийг гаргаж үзэх
    # TODO: print_queue-г ашиглан Queue-г хэвлэх
