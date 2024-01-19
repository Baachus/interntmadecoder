''' Algorithms for sorting visualizer '''
class Algorithm():
    '''Class for algorithms'''

    @staticmethod
    def bubble_sort(data):
        '''Bubble sort algorithm'''
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                yield data

    @staticmethod
    def merge_sort(data, start=0, end=None):
        '''Merge sort algorithm'''
        if end is None:
            end = len(data) - 1

        if end - start < 1:
            return

        mid = start + (end - start) // 2

        yield from Algorithm.merge_sort(data, start, mid)
        yield from Algorithm.merge_sort(data, mid + 1, end)

        left = data[start:mid + 1]
        right = data[mid + 1:end + 1]

        i = j = 0

        for k in range(start, end + 1):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1

            yield data

    @staticmethod
    def merge(left, right):
        '''Merge helper function'''
        merged = []
        left_index = 0
        right_index = 0

        # Merge smaller elements first
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

            # Yield the merged list
            yield merged

        # If there are remaining elements in left or right half, append them to the result
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1
            yield merged

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1
            yield merged

    @staticmethod
    def quick_sort(data, start=0, end=None):
        '''Quick sort algorithm'''
        if end is None:
            end = len(data) - 1

        if start >= end:
            return

        pivot = data[end]
        low = start
        high = end - 1

        while low <= high:
            if data[low] <= pivot:
                low += 1
            else:
                data[low], data[high] = data[high], data[low]
                high -= 1

            yield data

        data[end], data[low] = data[low], data[end]

        yield data

        yield from Algorithm.quick_sort(data, start, low - 1)
        yield from Algorithm.quick_sort(data, low + 1, end)
