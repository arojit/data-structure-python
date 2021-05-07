import array as arr
import time


class BinarySearch:
    item = []

    def add(self, number):
        self.item.append(number)

    def search(self, number):
        lb = 0
        ub = len(self.item) - 1
        while lb < ub:
            mid = (lb + ub) // 2
            if self.item[mid] == number:
                print("Found")
                return
            if number > self.item[mid]:
                lb = mid
            else:
                ub = mid
        print("Not Found")


class LinearSearch:
    item = arr.array('i')

    def add(self, number):
        self.item.append(number)

    def search(self, number):
        for num in self.item:
            if number == num:
                print("found")
                return
        print("Not Found")


if __name__ == '__main__':
    binary_search = BinarySearch()

    binary_search.add(2)
    binary_search.add(5)
    binary_search.add(8)
    binary_search.add(9)
    binary_search.add(11)
    binary_search.add(14)

    start = time.time()
    binary_search.search(1)
    end = time.time()

    print("Time Taken : ", end - start)

    linear_search = LinearSearch()

    linear_search.add(2)
    linear_search.add(5)
    linear_search.add(8)
    linear_search.add(9)
    linear_search.add(11)
    linear_search.add(14)

    start = time.time()
    linear_search.search(11)
    end = time.time()
    print("Time Taken : ", end - start)
