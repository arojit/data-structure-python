import array as arr
import time


class SelectionSort:
    def __init__(self, data_array):
        self.data = arr.array('i', data_array)

    def sort(self):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i] < self.data[j]:
                    temp = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = temp
        print(self.data)


class BubbleSort:
    def __init__(self, data_array):
        self.data = arr.array('i', data_array)

    def sort(self):
        for i in range(len(self.data)):
            for j in range(len(self.data) - (i+1)):
                if self.data[j] > self.data[j+1]:
                    temp = self.data[j]
                    self.data[j] = self.data[j+1]
                    self.data[j + 1] = temp
        print(self.data)


if __name__ == '__main__':
    data = [5, 7, 9, 2, 1]

    selection_sort = SelectionSort(data)
    start = time.time()
    selection_sort.sort()
    end = time.time()

    print("Time Taken :: ", end - start)

    bubble_sort = BubbleSort(data)
    start = time.time()
    bubble_sort.sort()
    end = time.time()

    print("Time Taken :: ", end - start)



