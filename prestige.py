import math

rankUpCosts = {"A": 150, "B": 300, "C": 700, "D": 1530, "E": 3150, "G": 4500, "H": 9750, "I": 22500, "J": 36000, "K": 90000, "L": 120000,"M": 135000, "N": 225000, "O": 607500,
               "P": 742500, "Q": 1575000, "R": 5175000, "S": 8325000, "T": 24750000, "U": 45000000, "V": 60750000, "W": 213750000, "X": 261000000, "Y": 722250000, "Z": 2000000000}
#Gives raw costs for the rankup in each mine, e.g. in mine A, it costs 150 sapphires to rankup to B. 

mineAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



mineInfo = {"A": {"Ores": ["S","C","none"],    "Abundances": [95, 5, 0],   "Prices": [2, 2, 0],          "Uniques": {"Pick": ["Gold", 100], "Eff": ["1", 150], "Fortune": []}},
            "B": {"Ores": ["S","C","none"],    "Abundances": [80, 20, 0],  "Prices": [2.52, 3.24, 0],    "Uniques": {"Pick": [], "Eff": [], "Fortune": ["1.33", 300]}},
            "C": {"Ores": ["S","C","none"],    "Abundances": [50, 50, 0],  "Prices": [4.79, 5.85, 0],    "Uniques": {"Pick": [], "Eff": ["2", 400], "Fortune": []}},
            "D": {"Ores": ["S","C","I"],       "Abundances": [10, 80, 10], "Prices": [5.5, 6.05, 13.19], "Uniques": {"Pick": [], "Eff": [], "Fortune": ["1.75", 1000]}},
            "E": {"Ores": ["S","C","I"],       "Abundances": [5, 80, 15],  "Prices": [10.29, 14, 20],    "Uniques": {"Pick": ["Stone", 3500], "Eff": [], "Fortune": []}},
            "F": {"Ores": ["C","I","none"],    "Abundances": [50, 50, 0],  "Prices": [18, 27, 0],        "Uniques": {"Pick": [], "Eff": ["3", 4000], "Fortune": []}},
            "G": {"Ores": ["C","I","G"],       "Abundances": [45, 50, 5],  "Prices": [18, 30, 70],       "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "H": {"Ores": ["C","I","G"],       "Abundances": [5, 75, 20],  "Prices": [37, 75, 75],       "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "I": {"Ores": ["I","G","none"],    "Abundances": [75, 25, 0],  "Prices": [85, 135, 0],       "Uniques": {"Pick": [], "Eff": ["4", 35000], "Fortune": []}},
            "J": {"Ores": ["I","G","none"],    "Abundances": [50, 50, 0],  "Prices": [110, 170, 0],      "Uniques": {"Pick": ["Iron", 50000], "Eff": [], "Fortune": []}},
            "K": {"Ores": ["G","R","none"],    "Abundances": [95, 5, 0],   "Prices": [170, 248, 0],      "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "L": {"Ores": ["G","R","none"],    "Abundances": [75, 25, 0],  "Prices": [180, 248, 0],      "Uniques": {"Pick": [], "Eff": ["5", 115000], "Fortune": []}},
            "M": {"Ores": ["G","R","none"],    "Abundances": [50, 50, 0],  "Prices": [203, 248, 0],      "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "N": {"Ores": ["G","R","L"],       "Abundances": [40, 55, 5],  "Prices": [203, 280, 430],    "Uniques": {"Pick": [], "Eff": [], "Fortune": ["2.20", 220000]}},
            "O": {"Ores": ["G","R","L"],       "Abundances": [10, 45, 45], "Prices": [210, 315, 430],    "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "P": {"Ores": ["R","L","none"],    "Abundances": [50, 50, 0],  "Prices": [315, 471, 0],      "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "Q": {"Ores": ["R","L","D"],       "Abundances": [40, 55, 5],  "Prices": [315, 678, 1251],   "Uniques": {"Pick": ["Diamond", 1500000], "Eff": [], "Fortune": []}},
            "R": {"Ores": ["R","L","D"],       "Abundances": [5, 65, 30],  "Prices": [965, 1950, 2000],  "Uniques": {"Pick": [], "Eff": ["6", 5000000], "Fortune": []}},
            "S": {"Ores": ["L","D","none"],    "Abundances": [75, 25, 0],  "Prices": [2065, 3213, 0],    "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "T": {"Ores": ["L","D","none"],    "Abundances": [50, 50, 0],  "Prices": [4760, 7403, 0],    "Uniques": {"Pick": [], "Eff": ["7", 10000000], "Fortune": []}},
            "U": {"Ores": ["D","none","none"], "Abundances": [100, 0, 0],  "Prices": [12510, 0, 0],      "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "V": {"Ores": ["D","E","none"],    "Abundances": [95, 5, 0],   "Prices": [12510, 41500, 0],  "Uniques": {"Pick": [], "Eff": ["8", 200000000], "Fortune": []}},
            "W": {"Ores": ["D","E","none"],    "Abundances": [60, 40, 0],  "Prices": [40000, 42600, 0],  "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "X": {"Ores": ["D","E","none"],    "Abundances": [50, 50, 0],  "Prices": [41200, 54600, 0],  "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "Y": {"Ores": ["D","E","none"],    "Abundances": [10, 90, 0],  "Prices": [50000, 78000, 0],  "Uniques": {"Pick": [], "Eff": [], "Fortune": []}},
            "Z": {"Ores": ["E","none","none"], "Abundances": [100, 0, 0],  "Prices": [86000, 0, 0],      "Uniques": {"Pick": [], "Eff": ["9", 700000000], "Fortune": []}}}
#Gives information regarding each mine. "Ores" elucidates ores in the mine, with S = stone, C = coal, I = iron, G = gold, R = redstone, L = lapis, D = diamond, and E = emerald. Abundances provide estimates for the relative abundances of the ores in the mine out of 100.
#Prices gives exact sell prices for each respective ore. Uniques are upgrades that are attainable in the mine and their respective costs. For example, in Mine E, there is stone, coal, iron, with abundances of 5%, 80%, 15%, with sell prices of 10.29, 14, and 20, respectively.

mineTime = {

    "Wood": {
        "haste 0": {
            "S": [1.15,0.6,0.35,0.2,0.15,0.1,0.1,0.05,0.05,0.05],
            "C": [2.25,1.15,0.65,0.4,0.25,0.2,0.15,0.1,0.1,0.1],
            "I": [7.5,3.75,2.15,1.25,0.8,0.55,0.4,0.3,0.25,0.2],
            "L": [7.5,3.75,2.15,1.25,0.8,0.55,0.4,0.3,0.25,0.2],
            "G": [7.5,3.75,2.15,1.25,0.8,0.55,0.4,0.3,0.25,0.2],
            "R": [7.5,3.75,2.15,1.25,0.8,0.55,0.4,0.3,0.25,0.2],
            "D": [7.5,3.75,2.15,1.25,0.8,0.55,0.4,0.3,0.25,0.2],
            "E": [7.5,3.75,2.15,1.25,0.8,0.55,0.4,0.3,0.25,0.2]},


        "haste 6": {
            "S": [0.55,0.3,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05],
            "C": [1.05,0.55,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05],
            "I": [3.45,1.75,1,0.6,0.4,0.25,0.2,0.15,0.15,0.1],
            "L": [3.45,1.75,1,0.6,0.4,0.25,0.2,0.15,0.15,0.1],
            "G": [3.45,1.75,1,0.6,0.4,0.25,0.2,0.15,0.15,0.1],
            "R": [3.45,1.75,1,0.6,0.4,0.25,0.2,0.15,0.15,0.1],
            "D": [3.45,1.75,1,0.6,0.4,0.25,0.2,0.15,0.15,0.1],
            "E": [3.45,1.75,1,0.6,0.4,0.25,0.2,0.15,0.15,0.1]
        },

        "haste 19": {
            "S": [0.25,0.15,0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.5,0.25,0.15,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "I": [1.6,0.8,0.45,0.3,0.2,0.15,0.1,0.1,0.05,0.05],
            "L": [1.6,0.8,0.45,0.3,0.2,0.15,0.1,0.1,0.05,0.05],
            "G": [1.6,0.8,0.45,0.3,0.2,0.15,0.1,0.1,0.05,0.05],
            "R": [1.6,0.8,0.45,0.3,0.2,0.15,0.1,0.1,0.05,0.05],
            "D": [1.6,0.8,0.45,0.3,0.2,0.15,0.1,0.1,0.05,0.05],
            "E": [1.6,0.8,0.45,0.3,0.2,0.15,0.1,0.1,0.05,0.05]
        }
    },

    "Gold": {
        "haste 0": {
            "S": [0.2,0.2,0.15,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "C": [0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.1,0.1,0.05],
            "I": [1.25,1.1,0.9,0.7,0.55,0.4,0.35,0.25,0.2,0.2],
            "L": [1.25,1.1,0.9,0.7,0.55,0.4,0.35,0.25,0.2,0.2],
            "G": [1.25,1.1,0.9,0.7,0.55,0.4,0.35,0.25,0.2,0.2],
            "R": [1.25,1.1,0.9,0.7,0.55,0.4,0.35,0.25,0.2,0.2],
            "D": [1.25,1.1,0.9,0.7,0.55,0.4,0.35,0.25,0.2,0.2],
            "E": [1.25,1.1,0.9,0.7,0.55,0.4,0.35,0.25,0.2,0.2]
        },

        "haste 6": {
            "S": [0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.2,0.15,0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05],
            "I": [0.6,0.5,0.45,0.35,0.25,0.2,0.15,0.15,0.1,0.1],
            "L": [0.6,0.5,0.45,0.35,0.25,0.2,0.15,0.15,0.1,0.1],
            "G": [0.6,0.5,0.45,0.35,0.25,0.2,0.15,0.15,0.1,0.1],
            "R": [0.6,0.5,0.45,0.35,0.25,0.2,0.15,0.15,0.1,0.1],
            "D": [0.6,0.5,0.45,0.35,0.25,0.2,0.15,0.15,0.1,0.1],
            "E": [0.6,0.5,0.45,0.35,0.25,0.2,0.15,0.15,0.1,0.1]
        },

        "haste 19": {
            "S": [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
            "I": [0.3,0.25,0.2,0.15,0.15,0.1,0.1,0.1,0.05,0.05],
            "L": [0.3,0.25,0.2,0.15,0.15,0.1,0.1,0.1,0.05,0.05],
            "G": [0.3,0.25,0.2,0.15,0.15,0.1,0.1,0.1,0.05,0.05],
            "R": [0.3,0.25,0.2,0.15,0.15,0.1,0.1,0.1,0.05,0.05],
            "D": [0.3,0.25,0.2,0.15,0.15,0.1,0.1,0.1,0.05,0.05],
            "E": [0.3,0.25,0.2,0.15,0.15,0.1,0.1,0.1,0.05,0.05]
        }
    },

    "Stone": {
        "haste 0": {
            "S": [0.6,0.4,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05],
            "C": [1.15,0.75,0.5,0.35,0.25,0.15,0.15,0.1,0.1,0.1],
            "I": [1.15,0.75,0.5,0.35,0.25,0.15,0.15,0.1,0.1,0.1],
            "L": [1.15,0.75,0.5,0.35,0.25,0.15,0.15,0.1,0.1,0.1],
            "G": [3.75,2.5,1.7,1.1,0.75,0.5,0.4,0.3,0.25,0.2],
            "R": [3.75,2.5,1.7,1.1,0.75,0.5,0.4,0.3,0.25,0.2],
            "D": [3.75,2.5,1.7,1.1,0.75,0.5,0.4,0.3,0.25,0.2],
            "E": [3.75,2.5,1.7,1.1,0.75,0.5,0.4,0.3,0.25,0.2]
        },

        "haste 6": {
            "S": [0.3,0.2,0.15,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.55,0.35,0.25,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "I": [0.55,0.35,0.25,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "L": [0.55,0.35,0.25,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "G": [1.75,1.15,0.8,0.5,0.35,0.25,0.2,0.15,0.1,0.1],
            "R": [1.75,1.15,0.8,0.5,0.35,0.25,0.2,0.15,0.1,0.1],
            "D": [1.75,1.15,0.8,0.5,0.35,0.25,0.2,0.15,0.1,0.1],
            "E": [1.75,1.15,0.8,0.5,0.35,0.25,0.2,0.15,0.1,0.1]
        },

        "haste 19": {
            "S": [0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.25,0.2,0.15,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "I": [0.25,0.2,0.15,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "L": [0.25,0.2,0.15,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "G": [0.8,0.55,0.35,0.25,0.15,0.15,0.1,0.1,0.05,0.05],
            "R": [0.8,0.55,0.35,0.25,0.15,0.15,0.1,0.1,0.05,0.05],
            "D": [0.8,0.55,0.35,0.25,0.15,0.15,0.1,0.1,0.05,0.05],
            "E": [0.8,0.55,0.35,0.25,0.15,0.15,0.1,0.1,0.05,0.05]
        }
    },

    "Iron": {
        "haste 0": {
            "S": [0.4,0.3,0.25,0.15,0.1,0.1,0.1,0.05,0.05,0.05],
            "C": [0.75,0.6,0.45,0.3,0.2,0.15,0.15,0.1,0.1,0.1],
            "I": [0.75,0.6,0.45,0.3,0.2,0.15,0.15,0.1,0.1,0.1],
            "L": [0.75,0.6,0.45,0.3,0.2,0.15,0.15,0.1,0.1,0.1],
            "G": [0.75,0.6,0.45,0.3,0.2,0.15,0.15,0.1,0.1,0.1],
            "R": [0.75,0.6,0.45,0.3,0.2,0.15,0.15,0.1,0.1,0.1],
            "D": [0.75,0.6,0.45,0.3,0.2,0.15,0.15,0.1,0.1,0.1],
            "E": [0.75,0.6,0.45,0.3,0.2,0.15,0.15,0.1,0.1,0.1]
        },

        "haste 6": {
            "S": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.35,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "I": [0.35,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "L": [0.35,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "G": [0.35,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "R": [0.35,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "D": [0.35,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "E": [0.35,0.3,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05]
        },

        "haste 19": {
            "S": [0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "I": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "L": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "G": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "R": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "D": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "E": [0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05]
        }
    },

    "Diamond": {
        "haste 0": {
            "S": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "C": [0.6,0.45,0.35,0.25,0.2,0.15,0.1,0.1,0.1,0.05],
            "I": [0.6,0.45,0.35,0.25,0.2,0.15,0.1,0.1,0.1,0.05],
            "L": [0.6,0.45,0.35,0.25,0.2,0.15,0.1,0.1,0.1,0.05],
            "G": [0.6,0.45,0.35,0.25,0.2,0.15,0.1,0.1,0.1,0.05],
            "R": [0.6,0.45,0.35,0.25,0.2,0.15,0.1,0.1,0.1,0.05],
            "D": [0.6,0.45,0.35,0.25,0.2,0.15,0.1,0.1,0.1,0.05],
            "E": [0.6,0.45,0.35,0.25,0.2,0.15,0.1,0.1,0.1,0.05]
        },

        "haste 6": {
            "S": [0.15,0.15,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "I": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "L": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "G": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "R": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "D": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05],
            "E": [0.3,0.25,0.2,0.15,0.1,0.1,0.05,0.05,0.05,0.05]
        },

        "haste 19": {
            "S": [0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
            "C": [0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "I": [0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "L": [0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "G": [0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "R": [0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "D": [0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05],
            "E": [0.15,0.1,0.1,0.1,0.05,0.05,0.05,0.05,0.05,0.05]
        }
    }
}
#Provides raw data for how many seconds it takes to mine a block in the given category for different efficiency levels in ascending order left to right of efficiency 0 to efficiency 9. 0.05 represents instant mining (20 blocks/second).

mineIndex = mineAlphabet.index(input("What mine are you in? Enter a capital letter: "))
sellBonus = float(input("What is your ore sell rate bonus? Enter as a single integer value representing the percent bonus (do not divide by 100): ")) / 100
discriminality = float(input("What is your discriminality factor? 0 denotes no discriminality, 1 is max discriminality: "))

def pickMineTable(haste):
    
    Picks = [['Wood', 0]]
    pickSpeeds = {"Wood": {}}
    for index in range(0, mineIndex + 1):
        if mineInfo[mineAlphabet[index]]["Uniques"]["Eff"] != []:            #Finds the maximum efficiency given the current rank and its associated cost.
            maxEfficiency = mineInfo[mineAlphabet[index]]["Uniques"]["Eff"]
        if mineInfo[mineAlphabet[index]]["Uniques"]["Pick"] != []:
            Picks += [(mineInfo[mineAlphabet[index]]["Uniques"]["Pick"])]    #Finds the available picks given the current rank and their associated costs.
            pickSpeeds[(mineInfo[mineAlphabet[index]]["Uniques"]["Pick"][0])] = {"S": 0, "C": 0, "I": 0, "L": 0, "G": 0, "R": 0, "D": 0, "E": 0}        #Finds the available picks given the current rank and constructs the pickSpeeds dictionary, which is used to elucidate block break times at a given haste level.
    #print(Picks)

    for pickIndex in pickSpeeds:                                             #Fills in specific data for block break times in the pickSpeeds dictionary given a haste and max efficiency level as determined by the given rank. 
        pickSpeeds[pickIndex]["S"] = mineTime[pickIndex][haste]["S"][int(maxEfficiency[0])]
        pickSpeeds[pickIndex]["C"] = mineTime[pickIndex][haste]["C"][int(maxEfficiency[0])]
        pickSpeeds[pickIndex]["I"] = mineTime[pickIndex][haste]["I"][int(maxEfficiency[0])]
        pickSpeeds[pickIndex]["L"] = mineTime[pickIndex][haste]["L"][int(maxEfficiency[0])]
        pickSpeeds[pickIndex]["G"] = mineTime[pickIndex][haste]["G"][int(maxEfficiency[0])]
        pickSpeeds[pickIndex]["R"] = mineTime[pickIndex][haste]["R"][int(maxEfficiency[0])]
        pickSpeeds[pickIndex]["D"] = mineTime[pickIndex][haste]["D"][int(maxEfficiency[0])]
        pickSpeeds[pickIndex]["E"] = mineTime[pickIndex][haste]["E"][int(maxEfficiency[0])]

    return pickSpeeds


#This function takes in an abundance list created in moneyRateTable(haste) and skews the values according to the value of the ore and relative abundance. It has input variable d (discriminality) which is set by the player, effectively representing how much they are
#"paying attention" to their mining. A discriminality value of 1 means they place a higher priority on mining high-value items (technically this should be calculated by taking the money rates per pick...but this is less complicated and should approximate it fine) and thus
#skews the abundance to reflect that for the purposes of the later calculations. A discriminality of 0 means that if there is 10% oreA and 90% oreB, the player will mine 1 oreA for every 9 oreB. It should be noted that if the player expects to insta-mine blocks, the discriminality
#should be set to zero since you effectively can't control what blocks you're mining at that point. 
#
#Some further notes: Discriminality as a concept is completely arbitrary. None of the values been tested so I'm not sure if it's realistic...I just knew that when mining, you are going to preferentially target high value ores, hence discriminality.
#I would use maybe 0.5 discriminality max. Further, this function was created entirely by ChatGPT so I don't know how it works and do not want to learn since I wasn't sure how to do this math. The rest of this program was written by myself. 
def adjust_row(row, prices, d):
    ores = row[:3]
    abundances = [x / 100 for x in row[3:]]

    raw = []
    value = []

    for ore, p in zip(ores, abundances):
        if ore == 'none' or p == 0:
            continue

        v = prices.get(ore, 1)

        raw.append((ore, p))
        value.append((ore, p * v))

    raw_sum = sum(p for _, p in raw)
    value_sum = sum(w for _, w in value)

    weighted = []

    for (ore, p_raw), (_, p_val) in zip(raw, value):
        p_raw = p_raw / raw_sum if raw_sum else 0
        p_val = p_val / value_sum if value_sum else 0

        w = (1 - d) * p_raw + d * p_val
        weighted.append((ore, w))

    total = sum(w for _, w in weighted)

    if total == 0:
        return [ores[0], ores[1], ores[2], 0, 0, 0]

    adjusted = {
        ore: round((w / total) * 100, 3)
        for ore, w in weighted
    }

    return [
        ores[0], ores[1], ores[2],
        adjusted.get(ores[0], 0),
        adjusted.get(ores[1], 0),
        adjusted.get(ores[2], 0)
    ]

        
def moneyRateTable(haste):
    moneyRates = {}
    mineOreCostRectified = {}
    maxFortune = []
    
    for index in range(0, mineIndex + 1):
        pickList = {}
        for oreIndex in range(len(mineInfo[mineAlphabet[index]]["Ores"])):
            if mineInfo[mineAlphabet[index]]["Ores"][oreIndex] not in mineOreCostRectified and mineInfo[mineAlphabet[index]]["Ores"][oreIndex] != 'none':
                mineOreCostRectified[mineInfo[mineAlphabet[index]]["Ores"][oreIndex]] = 0
            for oreIdentity in mineOreCostRectified:
                if mineInfo[mineAlphabet[index]]["Prices"][oreIndex] > mineOreCostRectified[oreIdentity]:
                    mineOreCostRectified[mineInfo[mineAlphabet[index]]["Ores"][oreIndex]] = mineInfo[mineAlphabet[index]]["Prices"][oreIndex] * (1 + sellBonus)          #mineOreCostRectified represents the maximum value an ore will sell for given your current rank; for example, if you mined coal
                                                                                                                                                                         #in B mine but were rank G you could sell it for $18 instead of only $3.24.                                                                                                                                              
  
        for picks in pickMineTable(haste):
            pickList[picks] = 0
        moneyRates[mineAlphabet[index]] = pickList                               #Constructs and initializes the moneyRates dictionary given the current rank. 
        if mineInfo[mineAlphabet[index]]["Uniques"]["Fortune"] != []:     #Finds the maximum fortune given the current rank and its associated cost.
            maxFortune = mineInfo[mineAlphabet[index]]["Uniques"]["Fortune"]
    
    pickTimeTable = pickMineTable(haste)
    
    #The following for loop packages the relevant ore abundances according to the input mine level as a list with the format [(mine A): [ore1, ore2, ore3, abundance1, abundance2, abundance 3], (mine B): ...]
    abundance = []
    for mine in moneyRates:
        tempAbundance = []
        for attribute in mineInfo[mine]:
            if attribute == "Uniques" or attribute == "Prices":
                continue
            for oreIndex in range(len(mineInfo[mine][attribute])):
                tempAbundance += [mineInfo[mine][attribute][oreIndex]]
        tempAbundance = adjust_row(tempAbundance, mineOreCostRectified, discriminality)
        abundance += [tempAbundance]
    
    #The following for loop packages the mine, ore, ore abundance, and pick bread speed of that ore in a list with the format:
    #[[mine1, ore1, abundance1, [[pick 1, pick1 break speed of ore 1], [pick2 break speed of ore 1...], ...], ore2, abundance2, ...], [mine2, ore1...]]
    #This list packages all relevant information (and ONLY the relevant information) according to the current mine rank which is used to carry out the calculations in the next loop.
    minePackage = []
    for mine in range(len(abundance)):
        minePackage.append([mineAlphabet[mine]])
        for index in range(len(abundance[index])-3):
            if abundance[mine][index] == 'none':
                continue
            minePackage[mine].append(abundance[mine][index])
            minePackage[mine].append(abundance[mine][index+3])
            miniPickPackage = []
            for pick in pickTimeTable:
                miniPickPackage.append([pick, pickTimeTable[pick][abundance[mine][index]]])
            minePackage[mine].append(miniPickPackage)
    
    #The following for loop calculates the money rates possible in each mine using the best pickaxe enchantments available for each pickaxe and best sell prices for each ore. This is useful for determining if it is worth it to get a pickaxe upgrade in a certain mine or save money for later. 
    #Note that it does NOT calculate the rates for the pickaxe available in each mine, i.e. if you input that you're in mine Z, the best pickaxe is a pickaxe with efficiency 9 and fortune 3; the rates for mine A, B, C, D... are calculated using those enchantments. 
    for mine in range(len(minePackage)):
        for pick in range(len(minePackage[0][3])):
            pickMoney1 = 0
            if minePackage[mine][1] in ['S','I','G']:
    #running total of money rate = relative abundance of ore 1 * pick break speed against ore 1 * maximum sell price for ore 1 * maximum fortune level (= 1 for stone, iron, and gold)
                pickMoney1 += (minePackage[mine][2] / 100) * (1 / minePackage[mine][3][pick][1]) * mineOreCostRectified[minePackage[mine][1]]
            else:
                pickMoney1 += (minePackage[mine][2] / 100) * (1 / minePackage[mine][3][pick][1]) * mineOreCostRectified[minePackage[mine][1]] * float(maxFortune[0])
            try: 
                if minePackage[mine][4] in ['S','I','G']:
                    pickMoney1 += (minePackage[mine][5] / 100) * (1 / minePackage[mine][6][pick][1]) * mineOreCostRectified[minePackage[mine][4]]
                else:
                    pickMoney1 += (minePackage[mine][5] / 100) * (1 / minePackage[mine][6][pick][1]) * mineOreCostRectified[minePackage[mine][4]] * float(maxFortune[0])
            except IndexError:   #This try/except block is necessary since not all mines have 3 or even 2 ores. 
                pass
            try: 
                if minePackage[mine][7] in ['S','I','G']:
                    pickMoney1 += (minePackage[mine][8] / 100) * (1 / minePackage[mine][9][pick][1]) * mineOreCostRectified[minePackage[mine][7]]
                else:
                    pickMoney1 += (minePackage[mine][8] / 100) * (1 / minePackage[mine][9][pick][1]) * mineOreCostRectified[minePackage[mine][7]] * float(maxFortune[0])
            except IndexError:
                pass
            moneyRates[mineAlphabet[mine]][minePackage[mine][3][pick][0]] = round(pickMoney1, 1)
    print(moneyRates)
                        
moneyRateTable("haste 0")


