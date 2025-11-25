#!/usr/bin/env python3
"""
Simple command-line calculator that supports the four basic arithmetic operations.
"""

from __future__ import annotations

from typing import Callable, Dict, Tuple

Number = float
Operation = Callable[[Number, Number], Number]


def add(x: Number, y: Number) -> Number:
    return x + y


def subtract(x: Number, y: Number) -> Number:
    return x - y


def multiply(x: Number, y: Number) -> Number:
    return x * y


def divide(x: Number, y: Number) -> Number:
    if y == 0:
        raise ZeroDivisionError("Không thể chia cho 0")
    return x / y


OPERATIONS: Dict[str, Tuple[str, Operation]] = {
    "1": ("Cộng", add),
    "2": ("Trừ", subtract),
    "3": ("Nhân", multiply),
    "4": ("Chia", divide),
}


def get_number(prompt: str) -> Number:
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")


def main() -> None:
    print("=== Máy tính đơn giản ===")
    while True:
        for key, (label, _) in OPERATIONS.items():
            print(f"{key}. {label}")
        print("q. Thoát")

        choice = input("Chọn phép tính: ").strip().lower()
        if choice == "q":
            print("Tạm biệt!")
            break

        if choice not in OPERATIONS:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
            continue

        a = get_number("Nhập số thứ nhất: ")
        b = get_number("Nhập số thứ hai: ")

        label, operation = OPERATIONS[choice]
        try:
            result = operation(a, b)
            print(f"Kết quả {label.lower()}: {result}")
        except ZeroDivisionError as exc:
            print(exc)


if __name__ == "__main__":
    main()
