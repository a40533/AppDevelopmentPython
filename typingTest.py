from typing import List, Dict, Tuple, Set, Callable, Union, Any, Optional

def test_function(a: int, b: Optional[int]) -> Union[int, float, None]:
    if b is None:
        return a
    if b != 0:
        return a / b
    
    return

def test_function2(input_val:list[str],index: int) -> Union[str, int]:
    return (input_val[index],index)
    

return_val = test_function(1, 2)
print(return_val)

return_val2 = test_function2(["a","b","c"],2)
print(return_val2)