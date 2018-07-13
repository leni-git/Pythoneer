from __copy import just_copy
from __shallow_copy import shallow_copy
from __deep_copy import deep_copy

while True:
    print("""
            Copy Test
    
                * 동작을 진행 중일 때 프로그램을 종료하고 싶으시면 강제 종료해 주세요.
    
                1. 단순 복사: 걍 객체 복사
                2. Shallow Copy: 얕은 복사
                3. Deep Copy: 깊은 복사
    
                0. 종료
        """)
    choice = input(' >> ')

    if choice == '1':
        just_copy()
    elif choice == '2':
        shallow_copy()
    elif choice == '3':
        deep_copy()
    elif choice == '0':
        break
    else:
        pass
