class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    # add node to the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # insert element in the beginning
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # insert after the node
    def insert_after_node(self, previous_node, data):
        if not previous_node:
            print("previous not doesn't not exit")
            return
        new_node = Node(data)

        new_node.next = previous_node.next
        previous_node.next = new_node

    # def insert after the value.
    def insert_after_value(self, value, data):
        curr_node = self.head
        new_node = None
        while curr_node:
            if curr_node.data == value:
                new_node = Node(data)
                new_node.next = curr_node.next
                curr_node.next = new_node
                break
            else:
                curr_node = curr_node.next

        if new_node is None:
            print("value is not exit in the linked list")

    # delete by node
    def deletion_node(self, data):
        cur_node = self.head

        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # delete by pos
    def deletion_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None

            count = 0
            prev_node = None
            while cur_node and count != pos:
                prev_node = cur_node
                cur_node = cur_node.next
                count = count + 1

            if cur_node is None:
                return

            prev_node.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count = count + 1
            cur_node = cur_node.next

        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if self.head:
            return

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.nxt
            cur.nxt = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return  prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = p
                q = s.next

        if not p:
            s.next = q

        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()

        while curr:
            if curr.head in dup_values:
                prev.next = curr.next
                curr = None
            else:
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next

    # solution 1
    def print_nth_from_last(self, n):
        total_len = self.len_iterative()
        curr = self.head
        while curr:
            if total_len == n:
                print(curr.data)
                return curr.data
            total_len -= 1
            curr = curr.next

        if curr is None:
            return

    # solution 2
    def print_nth_from_last_2(self, n):
        p = self.head
        q = self.head

        count = 0
        while q:
            count += 1
            if count >= n:
                break
            q = q.next

        if not q:
            print(str(n) + " is greater than the number of nodes in list.")
            return

        while p and q.next:
            p = p.next
            q = q.next
        return p.data

    def count_occurence_iterative(self, data):
        count = 0
        curr = self.head
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next

        return count

    def count_occurence_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurence_recursive(node.next, data)
        else:
            return self.count_occurence_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < k:
                prev = p.next
                p = p.next
                q = q.next
                count += 1

            p = prev
            while q:
                prev = q
                q = q.next

            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome(self):
        s = ""
        curr = self.head
        while curr:
            s += curr.data
            curr = curr.next
        return s[1] == s[::-1]

    def is_palindrome_2(self):
        # using stack
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_plaindrome_3(self):
        # using two pointers
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1
            while count <= i/2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count+= 1
            return True
        else:
            return False

    def move_tail_to_head(self):
        if self.head and self.head.next:
            curr = self.head
            prev = None

            while curr.next:
                prev = curr
                curr = curr.next
            curr.next = self.head
            self.head = curr
            prev.next = None


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')

print("Original List")
llist.print_list()


llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.print_list()

