class MyQueue:
    def __init__(self, len_queue=None):
        self.queue = []
        self.len_queue = len_queue

    def append(self, item):
        if len(self.queue) == self.len_queue:
            self.queue = self.queue[1:]
        self.queue.append(item)

    def complete(self):
        return len(self.queue) == self.len_queue

    def set(self):
        return set(self.queue)


def encryption_queue(text, template):
    template_set = set(template)
    len_temp = len(template)
    cnt = 0
    queue = MyQueue(len_temp)

    for i in text:
        queue.append(i)
        if queue.complete():
            set_queue = queue.set()
            if set_queue == template_set:
                cnt += 1
    return cnt


s = 'aaaa'
temp = 'aaa'
print(encryption_queue(s, temp))
