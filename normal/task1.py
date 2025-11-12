from typing import Dict, List, Tuple, Set
import random
from itertools import permutations

Permutation = Tuple[int, ...]
Group = List[Permutation]
Subgroup = Set[Permutation]

def _compose(p: Permutation, q: Permutation) -> Permutation:
    """Композиция двух перестановок: p∘q (сначала применяется q, потом p)"""
    return tuple(p[q[i]] for i in range(len(p)))

def _identity(m: int) -> Permutation:
    """Тождественная перестановка для группы S_m"""
    return tuple(range(m))

def _invert(p: Permutation) -> Permutation:
    """Обратная перестановка"""
    inv = [0] * len(p)
    for i, v in enumerate(p):
        inv[v] = i
    return tuple(inv)

def _all_permutations(m: int) -> Group:
    """Генерирует все перестановки симметрической группы S_m"""
    return list(permutations(range(m)))

def _closure(generators: Subgroup, G: Group) -> Subgroup:
    """Замыкание множества генераторов относительно групповой операции"""
    S = set(generators)
    e = _identity(len(G[0]))
    S.add(e)
    changed = True
    while changed:
        changed = False
        for a in list(S):
            for b in list(S):
                c = _compose(a, b)
                if c not in S:
                    S.add(c)
                    changed = True
    return S

def _left_cosets(G: Group, H: Subgroup) -> List[Subgroup]:
    """Вычисляет левые смежные классы подгруппы H в группе G"""
    cosets, seen = [], set()
    for g in G:
        coset = {_compose(g, h) for h in H}
        key = frozenset(coset)
        if key not in seen:
            seen.add(key)
            cosets.append(coset)
    return cosets

def _right_cosets(G: Group, H: Subgroup) -> List[Subgroup]:
    """Вычисляет правые смежные классы подгруппы H в группе G"""
    cosets, seen = [], set()
    for g in G:
        coset = {_compose(h, g) for h in H}
        key = frozenset(coset)
        if key not in seen:
            seen.add(key)
            cosets.append(coset)
    return cosets

def _is_normal(G: Group, H: Subgroup) -> bool:
    """Проверяет, является ли подгруппа H нормальной в группе G"""
    for g in G:
        left = {_compose(g, h) for h in H}
        right = {_compose(h, g) for h in H}
        if left != right:
            return False
    return True

def subgroups_of_Sm(N: int) -> dict:
    """
    Находит все подгруппы S_m, их количество и случайную подгруппу.
    Для подгруппы с индексом N mod (число подгрупп) строит смежные классы,
    определяет индекс и проверяет нормальность.
    """
    m = 4  # m = 4 + (5 % 5) = 4
    G = _all_permutations(m)
    
    # Находим все подгруппы S_m
    subgroups = []
    subgroups.append({_identity(m)})  # тривиальная подгруппа
    subgroups.append(set(G))           # вся группа
    
    # Добавляем циклические подгруппы, порожденные отдельными элементами
    for g in G:
        H = _closure({g}, G)
        if H not in subgroups:
            subgroups.append(H)
    
    num_subgroups = len(subgroups)
    idx = 5 % num_subgroups  # N = 5
    chosen = subgroups[idx]  # подгруппа для анализа
    
    # Строим смежные классы
    left_cosets = _left_cosets(G, chosen)
    right_cosets = _right_cosets(G, chosen)
    index_val = len(left_cosets)
    is_norm = _is_normal(G, chosen)
    
    return {
        "m": m,
        "num_subgroups": num_subgroups,
        "random_subgroup_size": len(random.choice(subgroups)),
        "chosen_index": idx,
        "index_of_subgroup": index_val,
        "is_normal": is_norm,
        "left_cosets_count": len(left_cosets),
        "right_cosets_count": len(right_cosets)
    }
