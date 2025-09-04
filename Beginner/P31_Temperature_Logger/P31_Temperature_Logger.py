import os
import csv

def create_csv():
    folder_path = r"C:\Users\Pratyaksh\Desktop\1000+ Projects\1-Python\Beginner\P31_Temperature_Logger" # <- Replace with your path
    file_name = "Patient.csv"
    destination_path = os.path.join(folder_path, file_name)

    if not os.path.exists(destination_path):
        with open(destination_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "age", "temperature"])
    return destination_path


def temp_logger():
    try:
        patient_name = input("Name: ").strip().capitalize()
        age = int(input("Age: "))
        temp = float(input("Temperature in °C: "))

        with open(create_csv(), "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([patient_name, age, temp])
        print("Data saved ✅")

    except ValueError:
        print("Invalid input, please enter correct data.")


def patient_temp_find():
    name_provided = input("Patient name: ").strip()

    with open(create_csv(), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["name"].lower() == name_provided.lower():
                print(f"{row['name']} → {row['temperature']}°C")
                break
        else:
            print("Cannot Find Patient ❌")


# Example usage
# temp_logger()
patient_temp_find()
