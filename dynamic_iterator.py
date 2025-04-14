# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def f(l):
    for element in l:
        print(f'{element} ', end = '')
    print('')

def main():
    letters = ['a', 'b', 'c']
    directions = ['up', 'down']
    numbers = range(10)
    colors = ['red', 'orange', 'yellow', 'green']

    dyn_iter(f, [letters, colors, directions, numbers])

def dyn_iter(f, iterator_sets, realized_elements = None):
    assert isinstance(iterator_sets, list)

    if not realized_elements:
        realized_elements = []

    iters = iterator_sets.pop()
    for element in iters:
        realized_elements.append(element)
        if iterator_sets:
            dyn_iter(f, iterator_sets, realized_elements)
        else:
            f(realized_elements)
        realized_elements.pop()
    iterator_sets.append(iters)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
