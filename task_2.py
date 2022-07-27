# Напишите функцию find_farthest_orbit(orbits), которая среди списка орбит планет (кортеж из длин полуосей ее элипса) 
# найдет ту, по которой вращается самая далекая планета (орбита наибольшей площади S = 𝜋ab, где a и b - длины полуосей
# элипса). Круговые орбиты не учитывать, самая далекая планета только одна. Результатом функции должен быть кортеж.

def find_farthest_orbit(orbits):
    s_orbits = [a * b for (a, b) in orbits if a != b]
    farthest_orbit = [(a, b) for (a, b) in orbits if a != b and a * b == max(s_orbits)]
    return farthest_orbit[0]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
