from hashlib import sha1
import numpy as np
import pandas as pd
import re

def hasher(solution):
    print(solution)
    return sha1(solution.encode("utf8")).hexdigest()

def ex1_1_1(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "015b8dcbc023be1734f726ca9af614fbb5b87611"
        else False
    )

def ex1_1_2(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "fbccebab4a05483ba1b7ce5c12688ac8f69ec024"
        else False
    )

def ex1_2_1(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "1b390cd54a0c0d4f27fa7adf23e3c45536e9f37c"
        else False
    )

def ex1_2_2(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "a1fca854f9cf2577cf14dd55c8c38dd79e4c4bf2"
        else False
    )

def ex1_2_3(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "0cf1aeac0372e10da230a32e74c9b6e68dca7342"
        else False
    )

def ex1_2_4(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "34a2d78560e4fc44dd67495c6ced9688f42dca1d"
        else False
    )

def ex1_2_5(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "e8dc057d3346e56aed7cf252185dbe1fa6454411"
        else False
    )

def ex1_2_6(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "34a2d78560e4fc44dd67495c6ced9688f42dca1d"
        else False
    )

def ex1_2_7(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "bdedc3fe4985c37a90969413100c6d0faccb1f1b"
        else False
    )

def ex1_2_8(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "1b390cd54a0c0d4f27fa7adf23e3c45536e9f37c"
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