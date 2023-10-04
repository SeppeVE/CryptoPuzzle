import streamlit as st
from simpleai.search import CspProblem, backtrack

word1 = input("First word: ")
word2 = input("Second word: ")
word3 = input("Solution word: ")

letters = []

domains = {}

for i in word1:
    if i == word1[0]:
        domains[i] = list(range(1, 10))
        letters.append(i);
    else:
        domains[i] = list(range(0, 10))
        letters.append(i);

for j in word2:
    if j == word2[0]:
        domains[j] = list(range(1, 10))
        letters.append(j);
    else:
        domains[j] = list(range(0, 10))
        letters.append(j);

for k in word3:
    if k == word3[0]:
        domains[k] = list(range(1, 10))
        letters.append(k);
    else:
        domains[k] = list(range(0, 10))
        letters.append(k);

letters = list(set(letters))


def constraint_unique(letters, values):
    return len(values) == len(set(values))  # remove repeated values and count

def constraint_add(letters, values):
    factor1 = ""
    factor2 = ""
    solution = ""

    for char in word1:
        pos = letters.index(char)
        factor1 += str(values[pos])
    
    for char in word2:
        pos = letters.index(char)
        factor2 += str(values[pos])
    
    for char in word3:
        pos = letters.index(char)
        solution += str(values[pos])

    factor1 = int(factor1)
    factor2 = int(factor2)
    solution = int(solution)
    
    return (factor1 + factor2) == solution

constraints = [
    (letters, constraint_unique),
    (letters, constraint_add),
]

problem = CspProblem(letters, domains, constraints)

output = backtrack(problem)
print('\nSolutions:', output)
