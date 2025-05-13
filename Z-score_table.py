import csv

def main():
    try:
        age = int(input("Age(in month): "))
        if 6<= age < 24 :
            pass
        elif 24<=age < 60:
            above_two_year()
        else: 
            print("Please select age between 6-59 month")
    except ValueError:
        print("Error :Please enter integer number between 6-59 month")

def above_two_year():
    sex = input("Select sex (M/F): ").strip().upper()
    
    if sex == "F":
        result = calculate_girls_Zscore()
    elif sex == "M":
        result = calculate_boys_Zscore()
    else:
        result = "Invalid input. Please enter 'M' for male and 'F' for female."
    
    print(result)  # Make sure to print the result

def calculate_girls_Zscore():        
    try:
        height = float(input("Enter Height (71–120 cm): "))
        if not (71 <= height <= 120):
            return "Height must be between 71 and 120 cm."
        weight = float(input("Enter Weight (kg): "))
    except ValueError:
        return "Please enter valid numbers for height and weight."
    
    with open("Zscore.csv", "r") as file:
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

def calculate_boys_Zscore():
    try:
        height = float(input("Enter Height (71–120 cm): "))
        if not (71 <= height <= 120):
            return "Height must be between 71 and 120 cm."
        weight = float(input("Enter Weight (kg): "))
    except ValueError:
        return "Please enter valid numbers for height and weight."
    
    with open("Zscore.csv", "r") as file:
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

if __name__=="__main__":
    main(
