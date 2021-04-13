import numpy as np
import pandas as pd

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('max_columns', None)

# Join
## 2개의 dataframe을 하나의 dataframe으로 합칠 때 사용 됨

## 예제 1
print("\n# example 01")
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 
print(left)

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
print(right)                      

"""
1. calling object(left)의 column은 "on" 파라메터로 명시.
2. 명시되어있지 않으므로 calling object의 index를 기준
3. called object(right)는 index가 target이 됨
4. right 에서 left의 index와 일치하는 row만 join 함
"""
print("\n>> left.join(right)")
print(left.join(right))

print("\n>> left.join(right, how='outer')")
print(left.join(right, how='outer'))

## 예제 2
print("\n# example 02")

left = pd.DataFrame(
    {
        'A':['A0', 'A1', 'A2', 'A3'],
        'B':['B0', 'B1', 'B2', 'B3'],
        'key':['K0', 'K1', 'K0', 'K1'],
    }
)
right = pd.DataFrame(
    {
        'C':['C0', 'C1', 'C2'],
        'D':['D0', 'D1', 'D2']
    },
    index=['K0', 'K1', 'K2']
)
print("\n>> left")
print(left)

print("\n>> right")
print(right)

"""
1. left obejct에서 key를 기준으로 join을 진행
2. join 후, index를 key로 설정 함
"""
print("\n>> left.join(right, on='key').set_index('key')")
print(left.join(right, on='key').set_index('key'))


print("\n>> left.set_index('key').join(right) ")
print(left.set_index('key').join(right))

