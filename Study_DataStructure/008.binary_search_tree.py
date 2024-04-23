class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, root, target):
        if root is None:
            return False
        if root.data == target:
            return True
        elif target < root.data:
            return self._search_recursive(root.left, target)
        else:
            return self._search_recursive(root.right, target)

    def pre_order(self, root):
        if root:
            print(root.data, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=' ')
            self.in_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=' ')


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(9)
    bst.insert(1)
    bst.insert(4)
    bst.insert(3)

    print("Pre-order traversal:")
    bst.pre_order(bst.get_root())
    print("\nIn-order traversal:")
    bst.in_order(bst.get_root())
    print("\nPost-order traversal:")
    bst.post_order(bst.get_root())

    print("\nSearch for 9:", bst.search(9))
    print("Search for 2:", bst.search(2))
