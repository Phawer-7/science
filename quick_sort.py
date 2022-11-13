def qs(arr: list) -> list:
    if not len(arr) > 2:
        return arr
    else:
        if len(arr) == 2:
            if arr[0] > arr[1]:
                return [arr[0], arr[1]]
            else:
                return [arr[1], arr[0]]
        elif len(arr) > 2:
            x = arr[0]

            bigger = []
            smaller = []
            for i in arr:
                if i > x:
                    bigger.append(i)
                elif i < x:
                    smaller.append(i)

            return qs(bigger) + [x] + qs(smaller)
