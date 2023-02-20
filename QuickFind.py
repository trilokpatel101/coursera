class QuickFindUF:
    def __init__(self, n):
        self.dataid = []
        for i in range(n):
            self.dataid.append(i)
        print(self.dataid)

    def is_connected(self, p, q):
        return self.dataid[p] == self.dataid[q]

    def union(self,p,q):
        pid =self.dataid[p]
        qid = self.dataid[q]

        for i in range (len(self.dataid)):
            if (self.dataid[i] == pid):
                self.dataid[i] = qid

#
# quick_find = QuickFindUF(5)
# print(quick_find.is_connected(1, 2))
# print(quick_find.union(1, 2))
# print(quick_find.dataid)
# print(quick_find.is_connected(1, 2))

# class QuickFindUF:
#
#     def selfid (n):
#         dataid = []
#         for i in range(n):
#             dataid.append(i)
#         print(dataid)
#     def is_connected (p , q):
#         return QuickFindUF.dataid[p] == QuickFindUF.dataid[q]
#
#
# quick_find = QuickFindUF(5)
# print(quick_find.is_connected(1, 2))


class Quickie ():

    def __init__(self,n):
        self.array = []
        for i in range(n):
            self.array.append(i)
        print (self.array)
    def connection (self, p ,q):
        if (self.array[p] == self.array[q]):
            return True
        return False
        print (self.array)
    def union (self, p , q):
        p = self.array[p]
        q = self.array[q]
        if (p != q):
            self.array[p] = self.array[q]
        return (self.array)

    def unionall (self, p , q):
        p = self.array[p]
        q = self.array[q]
        for i in range( len(self.array)):
            if (self.array[i]== p):
                self.array[i] = q
        print(self.array)


Quick = Quickie(6)
print(Quick.connection (1,2))
print (Quick.union(1,2))
print(Quick.connection (1,2))
print(Quick.union (2,3))
print(Quick.unionall (3,4))


#what is wrong in this code


#
# class Quickie ():
#
#     def __init__(self,n):
#         self.array = []
#         for i in range(n):
#             self.array.append(i)
#         print (self.array)
#
#     def connection (self, p ,q):
#         if (self.array[p] == self.array[q]):
#             return True
#         return False
#         print (self.array)
#
#     def union (self, p , q):
#         p_value = self.array[p]
#         q_value = self.array[q]
#         if (p_value != q_value):
#             self.array[p_value] = self.array[q_value]
#         print(self.array)
#
# Quick = Quickie(5)
# print(Quick.connection(1, 2))

