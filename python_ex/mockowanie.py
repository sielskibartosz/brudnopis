from unittest.mock import Mock

# Tworzymy mocka ręcznie
mock_funkcja = Mock()

# Możemy ustawić co ma zwracać
mock_funkcja.return_value = 42

print(mock_funkcja())  # -> 42
print(mock_funkcja(10, 20))  # -> 42, argumenty są ignorowane jeśli nie ustawimy inaczej

# Sprawdzanie wywołań
mock_funkcja.assert_called()  # sprawdza, że mock był wywołany
mock_funkcja.assert_called_with(10, 20)  # sprawdza, że był wywołany z tymi argumentami
