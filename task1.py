from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера.

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """
    # Сортуємо завдання спочатку за пріоритетами (1 - найвищий), а потім за об'ємом
    sorted_jobs = sorted(print_jobs, key=lambda x: (x["priority"]))

    print_order = []
    total_time = 0
    total_volume = 0
    items_count = 0

    # Додаємо моделі до черги відповідно до обмежень
    for job in sorted_jobs:
        if total_volume + job["volume"] <= constraints["max_volume"] \
                and items_count < constraints["max_items"]:
            print_order.append(job["id"])
            total_time = max(total_time, job["print_time"])
            total_volume += job["volume"]
            items_count += 1
        else:
            print_order.append(job["id"])
            total_time += job["print_time"]

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Тестування

def test_printing_optimization():
    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    test_cases = [
        (
            "Тест 1 (однаковий пріоритет)",
            [
                {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
                {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
            ]
        ),
        (
            "Тест 2 (різні пріоритети)",
            [
                {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
                {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
            ]
        ),
        (
            "Тест 3 (перевищення обмежень)",
            [
                {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
                {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
                {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
            ]
        )
    ]

    for test_name, jobs in test_cases:
        print(f"{test_name}:")
        result = optimize_printing(jobs, constraints)
        print(f"Порядок друку: {result['print_order']}")
        print(f"Загальний час: {result['total_time']} хвилин\n")

if __name__ == "__main__":
    test_printing_optimization()
