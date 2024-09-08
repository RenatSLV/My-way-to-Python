class ChessBoard:
    def _init_(self):
        self.size = 8  # Размер шахматной доски 8x8

    def is_valid_position(self, position):
        """Проверяет, находится ли позиция на шахматной доске"""
        if len(position) != 2:
            return False
        column, row = position
        if column not in 'abcdefgh' or row not in '12345678':
            return False
        return True

    def position_to_indices(self, position):
        """Преобразует позицию из формата 'a1' в индексы (x, y)"""
        column, row = position
        x = ord(column) - ord('a')
        y = int(row) - 1
        return x, y

    def can_queen_move(self, start, end):
        """Проверяет, может ли ферзь переместиться с start на end одним ходом"""
        x1, y1 = self.position_to_indices(start)
        x2, y2 = self.position_to_indices(end)
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

    def can_knight_move(self, start, end):
        """Проверяет, может ли конь переместиться с start на end одним ходом"""
        x1, y1 = self.position_to_indices(start)
        x2, y2 = self.position_to_indices(end)
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

def main():
    board = ChessBoard()

    try:
        start = input("Введите начальную позицию (например, 'e2'): ").strip().lower()
        end = input("Введите конечную позицию (например, 'e4'): ").strip().lower()

        if not board.is_valid_position(start) or not board.is_valid_position(end):
            raise ValueError("Недопустимая позиция. Введите значения в формате 'a1'-'h8'.")

        if board.can_queen_move(start, end):
            print(f"Ферзь может переместиться с {start} на {end} одним ходом.")
        else:
            print(f"Ферзь не может переместиться с {start} на {end} одним ходом.")

        if board.can_knight_move(start, end):
            print(f"Конь может переместиться с {start} на {end} одним ходом.")
        else:
            print(f"Конь не может переместиться с {start} на {end} одним ходом.")

    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()