"""
Vector Similarity Algorithms
"""

from math import sqrt




def cosine_similarity(
    a: list[float],
    b: list[float],
) -> float:
    """
    计算余弦相似度。

    Returns:
        [-1.0, 1.0]
    """

    _validate_vectors(a, b)

    dot = sum(
        x * y
        for x, y in zip(a, b)
    )

    norm_a = sqrt(
        sum(x * x for x in a)
    )

    norm_b = sqrt(
        sum(y * y for y in b)
    )

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)


def dot_product(
    a: list[float],
    b: list[float],
) -> float:
    """
    计算点积。
    """

    _validate_vectors(a, b)

    return sum(
        x * y
        for x, y in zip(a, b)
    )


def euclidean_distance(
    a: list[float],
    b: list[float],
) -> float:
    """
    计算欧氏距离。

    数值越小表示越相似。
    """

    _validate_vectors(a, b)

    return sqrt(
        sum(
            (x - y) ** 2
            for x, y in zip(a, b)
        )
    )


def _validate_vectors(
    a: list[float],
    b: list[float],
) -> None:
    """
    校验两个向量是否合法。
    """

    if len(a) != len(b):
        raise ValueError(
            "Vector dimensions do not match."
        )

    if len(a) == 0:
        raise ValueError(
            "Vector cannot be empty."
        )