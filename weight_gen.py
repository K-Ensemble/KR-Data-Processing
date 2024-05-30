text = "8.108143539512809639e+01"

with open("custom_weight_train.csv", "w") as file:
    for _ in range(3839):
        file.write(text + "\n")