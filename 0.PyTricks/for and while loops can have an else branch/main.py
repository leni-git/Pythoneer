#  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# Latest 22-May-2019
# Made by Leni ♡
# From. Dan at Real Python

# I  translate a subscribe script from `Real Python`
# `Real Python`에서 제공해주는 스크립트를 해석한 내용입니다.
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +


# Python's `for` and `while` loops
# support an `else` clause that executes
# only if the loops terminates without
# hitting a `break` statement.

# 파이썬의 `for`와 `while` 루프는
# 'else' 문을 지원합니다.
# ` break` 문구를 만나지 않고 루프가 종료되면
# 'else' 문이 실행됩니다.
def contains(haystack, needle):
    """
    Throw a ValueError if `needle` not
    in `haystack`.

    만약 `needle` 이 `haystack`의 멤버가 아니라면
    ValueError를 발생시킵니다.
    """
    for item in haystack:
        if item == needle:
            break
    else:
        # The `else` here is a
        # "completion clause" that runs
        # only if the loop ran to completion
        # without hitting a `break` statement.

        #  `else` 문은 루프가 `break` 문구를 만나지 않고
        # 반복 동작을 마친 경우에만 실행되는
        # "completion clause" 입니다.
        raise ValueError('Needle not found')


# Command lines ( 명령문)
contains([23, 'needle', 0xbadc0ffee], 'needle')  # None
contains([23, 42, 0xbadc0ffee], 'needle')  # ValueError: "Needle not found"
# end [ contains ] + + + + + + + + + + + + + + + + + + + +


# Personally, I'm not a fan of the `else`
# "completion clause" in loops because
# I find it confusing. I'd rather do
# something like this:

# 루프에 있는 "completion clause"는 혼란을 주기 때문에
# 개인적으로, 나는 `else` 의 팬이 아니다.
# 차라리 이렇게 하는게 낫다.
def better_contains(haystack, needle):
    for item in haystack:
        if item == needle:
            return
    raise ValueError('Needle not found')
# end [ better_contains ] + + + + + + + + + + + + + + + + + + + +


# Note: Typically you'd write something
# like this to do a membership test,
# which is much more Pythonic:

# 참고: 일반적으로 멤버 변수인지 테스트 할 때
# 다음과 같이 작성합니다.
# 이것이 훨씬 Pythonic 하다.
if needle not in haystack:
    raise ValueError('Needle not found')
# end  + + + + + + + + + + + + + + + + + + + +  + + + + + + + + + +
