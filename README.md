<!--
 * @Date: 2020-06-19 22:44:45
 * @LastEditors: code
 * @Author: code
 * @LastEditTime: 2020-06-23 21:54:51
-->  

# computed-cached-property

A decorator for caching computed properties in classes. like Vue's Computed-Properties

## install

```powershell
pip install computed-cached-property
```

## usage

```python
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

    @property
    @computed_cached_property(typed=Ture)
    # same as @functools.lru_cache(maxsize=1, typed=typed)
    def v5(self):
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
```

## Hint

Not recommended for use in a production environment

## License

MIT
