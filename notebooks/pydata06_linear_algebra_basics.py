#!/usr/bin/env python
# coding: utf-8

from typing import List

Vector = List[float]

def addV(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)   # 두 벡터의 길이가 같아야 함

    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    """
    인자: 동일한 차원의 벡터들의 리스트
    반환값: 각 항목의 합으로 이루어진 동일한 차원의 벡터
    """
    
    assert vectors                   # 1개 이상의 벡터가 주어져야 함

    num_elements = len(vectors[0])   # 벡터 개수
    
    assert all(len(v) == num_elements for v in vectors)   # 모든 벡터의 크기가 같아야 함

    # 동일한 위치의 항목을 모두 더한 값들로 이루어진 벡터 반환
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

def subtractV(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)   # 두 벡터의 길이가 같아야 함

    return [v_i - w_i for v_i, w_i in zip(v, w)]

def scalar_multV(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multV(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "벡터들의 길이가 동일해야 함"""

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


import math

def sum_of_squares(v: Vector) -> float:

    return dot(v, v)

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtractV(v, w))

# 버전 1
def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))

# 버전 2
def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtractV(v, w))


from typing import Tuple

Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0   # number of elements in first row
    return num_rows, num_cols


# 행벡터 계산
def get_row(A: Matrix, i: int) -> Vector:
    return A[i]             

# 열벡터 계산
def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]


from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [ [entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]   



def zero_matrix(n: int, m:int) -> Matrix:
    return make_matrix(n, m, lambda i, j: 0)


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


def addM(A: Matrix, B: Matrix) -> Matrix:
    assert shape(A) == shape(B)
    
    m, n = shape(A)
    
    return make_matrix(m, n, lambda i, j: A[i][j] + B[i][j])

def subtractM(A: Matrix, B: Matrix) -> Matrix:
    assert shape(A) == shape(B)
    
    m, n = shape(A)
    
    return make_matrix(m, n, lambda i, j: A[i][j] - B[i][j])
