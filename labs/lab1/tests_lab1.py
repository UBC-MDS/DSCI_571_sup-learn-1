from hashlib import sha1
import numpy as np
import pandas as pd
import re

def hasher(solution):
    print(solution)
    return sha1(solution.encode("utf8")).hexdigest()

def ex1_1(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "1469842b4307d36cccb487dc989f21016daadbcc"
        else False
    )

def ex1_2(X,y):    
    if sha1(str(X).encode("utf8")).hexdigest() != "3457744177c14f9603ad3ba55c31421dbd5ea067":
        print('X was not created properly.')
        return False 
    if sha1(str(y).encode("utf8")).hexdigest() != "71e7fdd4b2c23c0934d50d557b3bf6d5a0604fdf": 
        print('y was not created properly.')
        return False 
    return True
         
def ex1_5(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "3978d009748ef54ad6ef7bf851bd55491b1fe6bb"
        else False
    )    
    
def run_all_autograded_tests(tests, results):
    with open("lab1.ipynb", encoding="utf-8") as f:
        total_autogrades = re.findall("rubric={autograde:(\d).*}", f.read())
    print(f"Autograded questions passed: {sum(results)} / {len(total_autogrades)}")
    print(
        f" Autograded points achieved: {sum([int(digit) for r, digit in zip(results, total_autogrades) if r])} / {sum([int(digit) for digit in total_autogrades])}"
    )
    if sum(results) < len(total_autogrades):
        print("")
        [
            print(f"FAILED: {test}")
            for (test, result) in zip(tests, results)
            if not result
        ]