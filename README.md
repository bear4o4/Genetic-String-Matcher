# 🧬 Genetic String Matcher

This project implements a **Genetic Algorithm** in Python to evolve a population of random strings toward a specified **target string**. The algorithm simulates natural selection by applying **selection**, **crossover**, and **mutation** to evolve better solutions over time.

## 🎯 Target

Evolve a population of 10-character strings to exactly match a target string such as:


---

## 📌 Features

- ✅ Population-based string evolution
- ✅ Fitness score based on correct characters in correct positions
- ✅ Tournament selection (size = 3)
- ✅ Two-point crossover (probability = 0.8)
- ✅ Character-level mutation (probability = 0.05 per character)
- ✅ Fitness progress tracking per generation
- ✅ Live plotting of average and max fitness

---

## 🧪 Parameters

| Parameter        | Value              |
|------------------|--------------------|
| Population Size  | 50                 |
| String Length    | 10                 |
| Target String    | `HELLOGA123`       |
| Generations      | 20 (or until match)|
| Mutation Rate    | 5% per character   |
| Crossover Rate   | 80%                |
| Selection Method | Tournament (size 3)|

---

## 📈 Output Example


A plot will show how the population improves over generations.

---

## 🧰 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/genetic-string-matcher.git
   cd genetic-string-matcher
