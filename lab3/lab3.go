package main

import (
    "fmt"
    "math"
    "os"
    "sort"
    "strconv"
)

// SquareRoots структура для хранения коэффициентов и корней уравнения
type SquareRoots struct {
    coefA, coefB, coefC float64
    numRoots            int
    rootsList           map[float64]bool
}

// getCoef пытается получить коэффициент из аргумента командной строки или с помощью ввода с клавиатуры
func (sr *SquareRoots) getCoef(index int, prompt string) float64 {
    if len(os.Args) > index {
        coefStr := os.Args[index]
        coef, err := strconv.ParseFloat(coefStr, 64)
        if err == nil {
            return coef
        }
    }
    // Если аргумент командной строки не предоставлен, спрашиваем с клавиатуры
    fmt.Println(prompt)
    var coefStr string
    fmt.Scanln(&coefStr)
    coef, err := strconv.ParseFloat(coefStr, 64)
    if err != nil {
        fmt.Println("Ошибка ввода. Пожалуйста, введите число.")
        os.Exit(1)
    }
    return coef
}

// getCoefs считывает все коэффициенты
func (sr *SquareRoots) getCoefs() {
    sr.coefA = sr.getCoef(1, "Введите коэффициент A:")
    sr.coefB = sr.getCoef(2, "Введите коэффициент B:")
    sr.coefC = sr.getCoef(3, "Введите коэффициент C:")
}

// calculateRoots вычисляет корни уравнения и заполняет rootsList
func (sr *SquareRoots) calculateRoots() {
    a := sr.coefA
    b := sr.coefB
    c := sr.coefC

    // Инициализация map для хранения корней
    sr.rootsList = make(map[float64]bool)

    // Вычисление дискриминанта
    D := b*b - 4*a*c

    if D > 0 {
        t1 := (-b + math.Sqrt(D)) / (2 * a)
        t2 := (-b - math.Sqrt(D)) / (2 * a)

        // Для t1 и t2 вычисляем корни
        if t1 >= 0 {
            sr.rootsList[math.Sqrt(t1)] = true
            sr.rootsList[-math.Sqrt(t1)] = true
        }
        if t2 >= 0 {
            sr.rootsList[math.Sqrt(t2)] = true
            sr.rootsList[-math.Sqrt(t2)] = true
        }

    } else if D == 0 {
        t := -b / (2 * a)
        if t >= 0 {
            sr.rootsList[math.Sqrt(t)] = true
            sr.rootsList[-math.Sqrt(t)] = true
        }
    }

    // Устанавливаем количество уникальных корней
    sr.numRoots = len(sr.rootsList)
}

// printRoots выводит корни уравнения
func (sr *SquareRoots) printRoots() {
    // Преобразуем map в срез и сортируем корни
    var roots []float64
    for root := range sr.rootsList {
        roots = append(roots, root)
    }
    // Сортируем корни для удобства вывода
    sort.Float64s(roots)

    // Печать корней
    if len(roots) == 0 {
        fmt.Println("Нет действительных корней")
    } else {
        fmt.Printf("Корни: ")
        for i, root := range roots {
            if i > 0 {
                fmt.Print(", ")
            }
            fmt.Print(root)
        }
        fmt.Println()
    }
}

func main() {
    // Создаем объект структуры
    r := SquareRoots{}
    // Получаем коэффициенты
    r.getCoefs()
    // Вычисляем корни
    r.calculateRoots()
    // Печатаем корни
    r.printRoots()
}

