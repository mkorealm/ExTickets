class Queue:
    List = [1, 2, 3, 4, 5]


def swap(List):
    one = List[0]
    two = List[-1]
    List.pop(0)
    List.insert(0, two)
    List.pop(-1)
    List.append(one)
    print(List)
