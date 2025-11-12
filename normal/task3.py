from typing import Dict, List, Tuple
import random
from itertools import permutations

def _compose_permutations(p: Tuple[int, ...], q: Tuple[int, ...]) -> Tuple[int, ...]:
    """Композиция перестановок p ∘ q"""
    return tuple(p[q[i]] for i in range(len(p)))

def _permutation_power(perm: Tuple[int, ...], n: int) -> Tuple[int, ...]:
    """Возведение перестановки в степень n"""
    if n == 0:
        return tuple(range(len(perm)))
    result = perm
    for _ in range(n - 1):
        result = _compose_permutations(result, perm)
    return result

def solve_sigma_power_eq(N: int) -> dict:
    m = 4 + (N % 5)
    n = 2 + (N % 10)
    
    # Целевая перестановка (1 2 3 ... m-1)
    target_perm = tuple((i + 1) % m for i in range(m))
    
    # Генерируем все перестановки S_m
    all_perms = list(permutations(range(m)))
    solutions = []
    
    # Ищем решения уравнения σ^n = target_perm
    for sigma in all_perms:
        sigma_power = _permutation_power(sigma, n)
        if sigma_power == target_perm:
            solutions.append(sigma)
    
    # Выбираем три случайных решения
    random_solutions = []
    if solutions:
        if len(solutions) >= 3:
            random_solutions = random.sample(solutions, 3)
        else:
            random_solutions = solutions.copy()
    
    return {
        "m": m,
        "n": n,
        "target_permutation": target_perm,
        "number_of_solutions": len(solutions),
        "three_random_solutions": random_solutions,
    }

"""Все решения являются перестановками, которые при возведении в степень n дают циклическую перестановку. 
Порядок любого решения делит n * порядок целевой перестановки."""