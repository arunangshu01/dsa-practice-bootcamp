"""

Sum Lists

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

"""

from linked_list_class import LinkedList


def sumLists(first_linked_list, second_linked_list):
    temp1, temp2, carry = first_linked_list.head, second_linked_list.head, 0
    sum_linked_list = LinkedList()

    while temp1 or temp2:
        result = carry
        if temp1:
            result += temp1.value
            temp1 = temp1.next
        if temp2:
            result += temp2.value
            temp2 = temp2.next
        sum_linked_list.add(value=int(result % 10))
        carry = result / 10
    if carry > 0:
        sum_linked_list.add(value=int(carry))
    return sum_linked_list


if __name__ == "__main__":
    first_linked_list = LinkedList()
    first_linked_list.add(value=7)
    first_linked_list.add(value=1)
    first_linked_list.add(value=6)

    second_linked_list = LinkedList()
    second_linked_list.add(value=5)
    second_linked_list.add(value=9)
    second_linked_list.add(value=8)

    print(first_linked_list)
    print(second_linked_list)

    print(sumLists(first_linked_list=first_linked_list, second_linked_list=second_linked_list))
