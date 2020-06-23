'''
@Date: 2020-06-23 21:23:00
@LastEditors: code
@Author: code
@LastEditTime: 2020-06-23 21:35:10
'''

import functools
import ast
import inspect
import textwrap
from typing import List


def computed_cached_property(typed: bool = False):
    '''creat a function

    :param user_function: a funtion

    :return: a new function
    '''
    def decorator(user_function):
        '''creat a function

        :param user_function: a funtion

        :return: a new function
        '''
        code_str = inspect.getsource(user_function)
        code_str = textwrap.dedent(code_str)

        root_node = ast.parse(code_str)
        def_node: ast.FunctionDef = root_node.body[0]
        arg_name = def_node.args.args[0].arg
        attr_name_list: List[str] = []
        for attr_node in ast.walk(def_node):
            attr_node: ast.Attribute
            attr_node.value: ast.Name
            if not (isinstance(attr_node, ast.Attribute)
                    and isinstance(attr_node.value, ast.Name)
                    and attr_node.value.id == arg_name):
                continue
            attr_name_list.append(attr_node.attr)

        instance = {}

        @functools.lru_cache(maxsize=1, typed=typed)
        def decorator1(*args1):
            return user_function(instance[0])

        @functools.wraps(user_function)
        def decorator2(*args2):
            instance[0] = args2[0]

            args0: List[object] = []
            for attr_name in attr_name_list:
                args0.append(getattr(instance[0], attr_name))
            return decorator1(*args0)

        return decorator2
    
    if callable(typed):
        return decorator(typed)
    
    return decorator
