from typing import Tuple
import math

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    # 頑張って！
    target_aspect_ratio: float = 16/9
    new_x : int = math.ceil(y * target_aspect_ratio)
    new_y: int = y
    return (new_x, new_y)