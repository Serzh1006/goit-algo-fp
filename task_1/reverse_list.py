class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self,arr):
        if not arr:
            return None
        self.head = Node(arr[0])
        current = self.head
        for value in arr[1:]:
            current.next = Node(value)
            current = current.next
        return self.head

    def print_linked_list(self,head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_linked_list(self,head):
        prev = None
        current = head
    
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def insertion_sort_linked_list(self,head):
        if not head or not head.next:
            return head

        sorted_head = Node(0)  # створюємо новий список для сортування
        current = head

        while current:
            prev_node = sorted_head
            next_node = sorted_head.next

            # Знайти правильну позицію для поточного елемента
            while next_node:
                if next_node.data > current.data:
                    break
                prev_node = next_node
                next_node = next_node.next

            # Вставляємо поточний вузол у відсортований список
            temp = current.next
            current.next = next_node
            prev_node.next = current
            current = temp

        return sorted_head.next
    
    def mergeTwoLists(self,l1, l2):
        dummy = Node()
        current = dummy
    
        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
    
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
    
        return dummy.next



llist = LinkedList()
head = llist.create_linked_list([10,6,8,2,4])
test_list = llist.create_linked_list([1,3,5,9])

print("Зв'язний список: ")
llist.print_linked_list(head)
prev = llist.reverse_linked_list(head) # Реверсування списку
print("Зворотній список: ")
llist.print_linked_list(prev)
sorted_list = llist.insertion_sort_linked_list(prev) # Сортування списку
print("Відсортований список: ")
llist.print_linked_list(sorted_list)

combined_list = llist.mergeTwoLists(sorted_list, test_list)
print("Об'єднаний  список: ")
llist.print_linked_list(combined_list)