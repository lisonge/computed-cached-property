'''
@Date: 2020-06-23 21:23:51
@LastEditors: code
@Author: code
@LastEditTime: 2020-06-23 21:46:07
'''
from computed_cached_property import computed_cached_property
from dataclasses import dataclass


@dataclass
class A:
    v1: int = 1
    v2: str = 'fuck'
    v3: bool = False

    @property
    @computed_cached_property
    def v4(self):
        print('run code in v4 function')
        return f'v1:{self.v1}, v2:{self.v2}, v3:{self.v3}'


a1 = A(v1=99)
print(a1.v4)
print(a1.v4)
a1.v2 = 'xxoo'
print(a1.v4)

# output
# run code in v4 function
# v1:99, v2:fuck, v3:False
# v1:99, v2:fuck, v3:False
# run code in v4 function
# v1:99, v2:xxoo, v3:False
