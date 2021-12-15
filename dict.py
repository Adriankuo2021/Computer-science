has_pet = {"Mars": False,"henrry" : False,"barbie": True, "Adrian" : True }

student_has_pet = has_pet.get("Mars")
print("the student has a pet:", student_has_pet)

for student in has_pet:
    print(student, 'has a pet', has_pet.get(student))

student_removed = has_pet.pop("Adrian")
print(student_removed)
print(has_pet)
