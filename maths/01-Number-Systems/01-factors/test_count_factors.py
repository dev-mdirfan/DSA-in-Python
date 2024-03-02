import pytest
from count_factors import FactorCounter

# Test for count_factors method
@pytest.mark.parametrize("input_value, expected_output, test_id", [
    (1, 1, 'happy_1'),  # Test with the smallest positive integer
    (6, 4, 'happy_2'),  # Test with a composite number
    (13, 2, 'happy_3'),  # Test with a prime number
    (28, 6, 'happy_4'),  # Test with a perfect number
    (0, 0, 'edge_1'),  # Test with zero, should handle gracefully
    (-1, 0, 'error_1'),  # Test with a negative number, should handle or raise an error
    (25, 3, 'happy_5'),  # Test with a perfect square number
    (36, 9, 'happy_6'),  # Test with another perfect square number
])
def test_count_factors(input_value, expected_output, test_id, capsys):
    # Arrange
    factor_counter = FactorCounter(input_value)

    # Act
    factor_counter.count_factors()
    captured = capsys.readouterr()

    # Assert
    assert int(captured.out.split('\n')[-2]) == expected_output

# Test for count_factors1 method
@pytest.mark.parametrize("input_value, expected_output, test_id", [
    (1, 1, 'happy_1'),
    (6, 4, 'happy_2'),
    (13, 2, 'happy_3'),
    (28, 6, 'happy_4'),
    (0, 0, 'edge_1'),
    (-1, 0, 'error_1'),
    (25, 3, 'happy_5'),
    (36, 9, 'happy_6'),
])
def test_count_factors1(input_value, expected_output, test_id):
    # Arrange
    factor_counter = FactorCounter(input_value)

    # Act
    result = factor_counter.count_factors1()

    # Assert
    assert result == expected_output

# Test for count_factors2 method
@pytest.mark.parametrize("input_value, expected_output, test_id", [
    (1, 1, 'happy_1'),
    (6, 4, 'happy_2'),
    (13, 2, 'happy_3'),
    (28, 6, 'happy_4'),
    (0, 0, 'edge_1'),
    (-1, 0, 'error_1'),
    (25, 3, 'happy_5'),
    (36, 9, 'happy_6'),
])
def test_count_factors2(input_value, expected_output, test_id):
    # Arrange
    factor_counter = FactorCounter(input_value)

    # Act
    result = factor_counter.count_factors2()

    # Assert
    assert result == expected_output

# Test for count_factors3 method
@pytest.mark.parametrize("input_value, expected_output, test_id", [
    (1, 1, 'happy_1'),
    (6, 4, 'happy_2'),
    (13, 2, 'happy_3'),
    (28, 6, 'happy_4'),
    (0, 0, 'edge_1'),
    (-1, 0, 'error_1'),
    (25, 3, 'happy_5'),
    (36, 9, 'happy_6'),
])
def test_count_factors3(input_value, expected_output, test_id):
    # Arrange
    factor_counter = FactorCounter(input_value)

    # Act
    result = factor_counter.count_factors3()

    # Assert
    assert result == expected_output

# Run the tests
if __name__ == "__main__":
    pytest.main()
