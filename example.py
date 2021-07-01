from LinkedList import LinkedList, Node


def main():
    llist = LinkedList(['b', 'c', 'd'])

    for node in llist:
        print(node)

    llist.add_first(Node('a'))
    print(llist)

    llist.add_last(Node('e'))
    print(llist)

    llist.add_after('b', Node('x'))
    print(llist)

    llist.add_before('a', Node('z'))
    print(llist)

    llist.remove_node('x')
    print(llist)

    llist.remove_node('z')
    print(llist)

    llist.get(8)


if __name__ == '__main__':
    main()
