#!/usr/bin/env python3
import csv
import subprocess
from collections import deque

class WarehouseManager:
    def __init__(self):
        # Общие точки для всех операций
        self.entry_point = {'place': 'B2', 'dispenser': 'dispenserTR01'}
        self.exit_point = {'place': 'A2', 'ingestor': 'ingestorTR02'}
        
        # Конфигурация пар устройств
        self.pairs = {
            n: {
                'ingestor_place': f'shelf{n}_in',
                'ingestor_handler': f'ingestor{n}',
                'dispenser_place': f'shelf{n}_out',
                'dispenser_handler': f'dispenser{n}',
                'queue': deque(maxlen=8)
            } for n in range(1, 6)
        }

    def process_tasks(self, filename):
        """Обработка задач из CSV-файла"""
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.handle_task(
                        row['type'].strip().lower(),
                        row['item'].strip()
                    )
                except Exception as e:
                    print(f"Ошибка в задаче {row}: {str(e)}")

    def handle_task(self, task_type, item):
        """Роутер задач"""
        if not item:
            raise ValueError("Пустое название товара")

        if task_type == 'in':
            self.handle_in_task(item)
        elif task_type == 'out':
            self.handle_out_task(item)
        else:
            raise ValueError(f"Неизвестный тип задачи: {task_type}")

    def handle_in_task(self, item):
        """Добавление товара в систему"""
        # Выбор пары с минимальной загрузкой
        target_pair = min(
            self.pairs.values(), 
            key=lambda p: len(p['queue'])
        )
        
        if len(target_pair['queue']) >= 8:
            raise RuntimeError("Все пары переполнены")

        target_pair['queue'].append(item)
        self.send_command(
            src_place=self.entry_point['place'],
            src_handler=self.entry_point['dispenser'],
            dst_place=target_pair['ingestor_place'],
            dst_handler=target_pair['ingestor_handler'],
            item=item
        )

    def handle_out_task(self, target_item):
        """Извлечение товара из системы"""
        for pair_id, pair in self.pairs.items():
            if target_item not in pair['queue']:
                continue

            # Перемещение мешающих товаров
            while pair['queue'] and pair['queue'][0] != target_item:
                self.move_item(pair)

            if not pair['queue']:
                continue

            # Извлечение целевого товара
            pair['queue'].popleft()
            self.send_command(
                src_place=pair['dispenser_place'],
                src_handler=pair['dispenser_handler'],
                dst_place=self.exit_point['place'],
                dst_handler=self.exit_point['ingestor'],
                item=target_item
            )
            return
        
        raise ValueError(f"Товар {target_item} не найден")

    def move_item(self, src_pair):
        """Перемещение товара между парами"""
        if not src_pair['queue']:
            return

        item = src_pair['queue'].popleft()
        
        # Поиск целевой пары с минимальной загрузкой
        target_pair = min(
            (p for p in self.pairs.values() if p != src_pair),
            key=lambda p: len(p['queue']),
            default=None
        )

        if not target_pair or len(target_pair['queue']) >= 8:
            src_pair['queue'].appendleft(item)
            raise RuntimeError("Нет места для перемещения")

        # Отправка команды
        self.send_command(
            src_place=src_pair['dispenser_place'],
            src_handler=src_pair['dispenser_handler'],
            dst_place=target_pair['ingestor_place'],
            dst_handler=target_pair['ingestor_handler'],
            item=item
        )
        target_pair['queue'].append(item)

    def send_command(self, src_place, src_handler, dst_place, dst_handler, item):
        """Отправка команды через ROS 2 CLI"""
        sim_item = "coke"  # Унификация для визуализации
        args = [
            "ros2", "run", "rmf_demos_tasks", "dispatch_delivery",
            "-p", src_place,
            "-pp", f"{sim_item},1",
            "-ph", src_handler,
            "-d", dst_place,
            "-dh", dst_handler,
            "-dp", f"{sim_item},1",
            "--use_sim_time"
        ]
        
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            print(f"✅ Успешно: {item} ({src_place} → {dst_place})")
        except subprocess.CalledProcessError as e:
            error_msg = f"❌ Ошибка: {e.stderr.strip()}" if e.stderr else "Неизвестная ошибка"
            raise RuntimeError(f"Команда не выполнена: {error_msg}")

if __name__ == '__main__':
    manager = WarehouseManager()
    manager.process_tasks("info.csv")
