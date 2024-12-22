Feature: Проверка работы фигур

  Scenario: Проверка площади прямоугольника
    Given I have a rectangle with width 4 and height 5
    Then the area of the rectangle should be 20

  Scenario: Проверка площади круга
    Given I have a circle with radius 3
    Then the area of the circle should be approximately 28.27

  Scenario: Проверка площади квадрата
    Given I have a square with side 4
    Then the area of the square should be 16
