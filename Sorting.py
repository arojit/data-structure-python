import array as arr


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


if __name__ == '__main__':
    data = [5, 7, 9, 2, 1]

    selection_sort = SelectionSort(data)
    selection_sort.sort()


