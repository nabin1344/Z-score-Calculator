import csv

def main():
 while True:
    try:
        age = int(input("Age(in month): "))
        if 0 <= age < 24:
            below_two_year()
            break
        elif 24 <= age < 60:
            above_two_year()
            break
        else:
            print("Please select age between 0-59 month")
            continue
    except ValueError:
        print("Error: Please enter integer number between 0-59 month")
        continue

# =================================== Below 2 year baby ==========================================
def below_two_year():
    while True:
        sex = input("Select sex (M/F): ").strip().upper()

        if sex == "F":
            result = calculate_girls_Zscore1()
            break
        elif sex == "M":
            result = calculate_boys_Zscore1()
            break
        else:
            result = "Invalid input. Please enter 'M' for male and 'F' for female."
            continue

    print(result)

def calculate_girls_Zscore1():        
    try:
        height = float(input("Enter Height (50–100 cm): "))
        if not (50 <= height <= 100):
            return "Height must be between 50 and 100 cm."
        weight = float(input("Enter Weight (kg): "))
    except ValueError:
        return "Please enter valid numbers for height and weight."

    with open("Z-score_below_2year.csv", "r") as file:
        reader = csv.DictReader(file)
        height_str = str(int(height))

        for data in reader:
            if data['Height (cm)'].strip() == height_str:
                median = float(data['Median (G)'].strip())
                sd1 = float(data['-1 SD (G)'].strip())
                sd2 = float(data['-2 SD (G)'].strip())
                sd3 = float(data['-3 SD (G)'].strip())

                if weight > median:
                    return 'Overweight'
                elif sd1 < weight <= median:
                    return "Normal Weight"
                elif sd2 <= weight <= sd1:
                    return '-1 SD (Slightly Low Weight)'
                elif sd3 <= weight < sd2:
                    return '-2 SD (Moderate Malnutrition)'
                elif weight < sd3:
                    return '-3 SD (Severe Acute Malnutrition)'
                else:
                    return "Error"
        return "Height not found in the data."

def calculate_boys_Zscore1():
    try:
        height = float(input("Enter Height (50–100 cm): "))
        if not (50 <= height <= 100):
            return "Height must be between 50 and 100 cm."
        weight = float(input("Enter Weight (kg): "))
    except ValueError:
        return "Please enter valid numbers for height and weight."

    with open("Z-score_below_2year.csv", "r") as file:
        reader = csv.DictReader(file)
        height_str = str(int(height))

        for data in reader:
            if data['Height (cm)'].strip() == height_str:
                median = float(data['Median (B)'].strip())
                sd1 = float(data['-1 SD (B)'].strip())
                sd2 = float(data['-2 SD (B)'].strip())
                sd3 = float(data['-3 SD (B)'].strip())

                if weight > median:
                    return 'Overweight'
                elif sd1 < weight <= median:
                    return "Normal Weight"
                elif sd2 <= weight <= sd1:
                    return '-1 SD (Slightly Low Weight)'
                elif sd3 <= weight < sd2:
                    return '-2 SD (Moderate Malnutrition)'
                elif weight < sd3:
                    return '-3 SD (Severe Acute Malnutrition)'
                else:
                    return "Unable to categorize"
        return "Height not found in the data."

# =================================== Above 2 year baby ==========================================
def above_two_year():
    sex = input("Select sex (M/F): ").strip().upper()

    if sex == "F":
        result = calculate_girls_Zscore2()
    elif sex == "M":
        result = calculate_boys_Zscore2()
    else:
        result = "Invalid input. Please enter 'M' for male and 'F' for female."

    print(result)

def calculate_girls_Zscore2():        
    try:
        height = float(input("Enter Height (71–120 cm): "))
        if not (71 <= height <= 120):
            return "Height must be between 71 and 120 cm."
        weight = float(input("Enter Weight (kg): "))
    except ValueError:
        return "Please enter valid numbers for height and weight."

    with open("Z-score_above_2year.csv", "r") as file:
        reader = csv.DictReader(file)
        height_str = str(int(height))

        for data in reader:
            if data['Height (cm)'].strip() == height_str:
                median = float(data['Median (G)'].strip())
                sd1 = float(data['-1 SD (G)'].strip())
                sd2 = float(data['-2 SD (G)'].strip())
                sd3 = float(data['-3 SD (G)'].strip())

                if weight > median:
                    return 'Overweight'
                elif sd1 < weight <= median:
                    return "Normal Weight"
                elif sd2 <= weight <= sd1:
                    return '-1 SD (Slightly Low Weight)'
                elif sd3 <= weight < sd2:
                    return '-2 SD (Moderate Malnutrition)'
                elif weight < sd3:
                    return '-3 SD (Severe Acute Malnutrition)'
                else:
                    return "Unable to categorize"
        return "Height not found in the data."

def calculate_boys_Zscore2():
    try:
        height = float(input("Enter Height (71–120 cm): "))
        if not (71 <= height <= 120):
            return "Height must be between 71 and 120 cm."
        weight = float(input("Enter Weight (kg): "))
    except ValueError:
        return "Please enter valid numbers for height and weight."

    with open("Z-score_above_2year.csv", "r") as file:  # Fixed file name here
        reader = csv.DictReader(file)
        height_str = str(int(height))

        for data in reader:
            if data['Height (cm)'].strip() == height_str:
                median = float(data['Median (B)'].strip())
                sd1 = float(data['-1 SD (B)'].strip())
                sd2 = float(data['-2 SD (B)'].strip())
                sd3 = float(data['-3 SD (B)'].strip())

                if weight > median:
                    return 'Overweight'
                elif sd1 < weight <= median:
                    return "Normal Weight"
                elif sd2 <= weight <= sd1:
                    return '-1 SD (Slightly Low Weight)'
                elif sd3 <= weight < sd2:
                    return '-2 SD (Moderate Malnutrition)'
                elif weight < sd3:
                    return '-3 SD (Severe Acute Malnutrition)'
                else:
                    return "Unable to categorize"
        return "Height not found in the data."

# =================================== Run Program ==========================================
if __name__ == "__main__":
    main()
