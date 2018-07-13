def shallow_copy():
    # import copy

    list1 = [
        3,
        "string",
        [1, 0, 0, 4],
        {'a': 'kitty', 'b': 'MAMAMO'}
    ]

    list2 = list1.copy()
    # list2 = copy.copy(list1)

    print('\n00. list1을 list2에 복사했을 때')
    print('{}'.format('- '*10))
    print('list 1 << {} >>\t{}'.format(id(list1), list1))
    for i in list1:
        print('\tid << {} >> : {}'.format(id(i), i))
    print('\nlist 2 << {} >>\t{}'.format(id(list2),list2))
    for i in list2:
        print('\tid << {} >> : {}'.format(id(i), i))
    print('{}'.format('- ' * 10))

    list2[0] = 0
    list2[2][1] = 3
    list2[3]['add_key'] = 'addddd her'

    print('\n01. list2에 대한 값을 변경 시켰을 때')
    print('{}'.format('- '*10))
    print('list 1 << {} >>\t{}'.format(id(list1), list1))
    print('list 2 << {} >>\t{}'.format(id(list2),list2))
    print('{}'.format('- ' * 10))

    print('\n03. list2에 대한 값 변경 후 주소 출력')
    print('{}'.format('- '*10))
    print('list 1 << {} >>\t{}'.format(id(list1), list1))
    for i in list1:
        print('\tid << {} >> : {}'.format(id(i), i))
    print('\nlist 2 << {} >>\t{}'.format(id(list2),list2))
    for i in list2:
        print('\tid << {} >> : {}'.format(id(i), i))
    print('{}'.format('- ' * 10))