class PointDatabase:

    class tree:
        class node:
            """Creating a Node class having data and pointer to its left and right node"""
            data = None
            left = None
            right = None

            def __str__(self):
                return str(self.data)
        "a 2D range tree which has all the points on its leaf for searching purpose"
        Root = None

        def __init__(self, store: list) -> None:
            self.Root = self.maketree(store, self.Root)

        def maketree(self, store, curr, var='y'):
            """maketree function to organize the tree in the sorted way , it will return the root of the tree."""
            if len(store) == 1:
                curr = store[0]
                return curr
            if var == 'x':
                pivot = self.median(store, 0)[0]
            else:
                pivot = self.median(store, 1)[1]

            curr = PointDatabase.tree.node()
            curr.data = (var, pivot)
            store1 = []
            store2 = []
            for _ in store:
                if var == 'x':

                    if _[0] <= pivot:
                        store1.append(_)
                    else:
                        store2.append(_)
                else:
                    if _[1] <= pivot:
                        store1.append(_)
                    else:
                        store2.append(_)
            if var == 'x':
                curr.left = self.maketree(store1, curr.left, 'y')
                curr.right = self.maketree(store2, curr.right, 'y')
            else:
                curr.left = self.maketree(store1, curr.left, 'x')
                curr.right = self.maketree(store2, curr.right, 'x')

            return curr

        def median(self, lst: list, z, k=0, delta=0):
            n = len(lst)

            if n == 1:
                return lst[0]

            if k == 0:
                k = n//2 if n % 2 == 0 else n//2+1
            # i=n//2-delta if boool == True else n//2+delta
            # print("n is ",n)
            i = n//2
            if delta == 1:
                if i == 0:
                    i += 1
                else:
                    if n % 2 != 0:
                        i = 2*i
                    else:
                        if n == 2:
                            i = 0
                        else:
                            i = 2*i-1
            else:
                i = n//2

            pivot = lst[i][z]
            lst1 = []
            lst2 = []
            for item in lst:
                if item[z] <= pivot:
                    lst1.append(item)
                else:
                    lst2.append(item)
            # print("i =", i, "delta =", delta, "k =", k, "z =", z, "pivot =", pivot)
            if lst1 == lst or lst2 == lst:
                delta += 1

            else:

                delta = 0

            if delta == 1:

                return self.median(lst, z, k, delta)

            if len(lst1) >= k:

                return self.median(lst1, z, k, delta)
            else:
                return self.median(lst2, z, k-len(lst1), delta)
    Datastructtree: tree = None

    def find(self, root: tree.node, q, d, temp: list):
        """This is a helper function for the searchnearby function, 
        it starts from the root of the tree and checks if its a node or not 
        till it reaches the leaf which is of the datatype tuple
        after that it checks if it satisfies the distance relation or not
        """
        if type(root) == self.tree.node:
            a = root.data
            if a[0] == 'x':
                if q[0]+d <= a[1]:
                    temp += self.find(root.left, q, d, [])
                elif q[0]-d > a[1]:
                    temp += self.find(root.right, q, d, [])
                else:
                    temp += self.find(root.left, q, d, [])
                    temp += self.find(root.right, q, d, [])
            else:
                if q[1]+d <= a[1]:
                    temp += self.find(root.left, q, d, [])
                elif q[1]-d > a[1]:
                    temp += self.find(root.right, q, d, [])
                else:
                    temp += self.find(root.left, q, d, [])
                    temp += self.find(root.right, q, d, [])

        else:
            a = root
            if q[0]-d <= a[0] <= q[0]+d and q[1]-d <= a[1] <= q[1]+d:

                temp.append(a)
        a = temp.copy()
        temp = []
        return a

    def __init__(self, store: list) -> None:
        """constructor part, which constructs a appropriate tree for searching"""
        if store == []:
            self.Datastructtree = None
            return
        self.Datastructtree = PointDatabase.tree(store)

    def searchNearby(self, q: tuple, d: float | int) -> list:
        """the main function which returns the list containing all the nearby points within 
        the range"""
        if self.Datastructtree == None:
            return []
        a = self.Datastructtree.Root
        return self.find(a, q, d, [])