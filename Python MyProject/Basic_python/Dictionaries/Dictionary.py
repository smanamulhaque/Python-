from stat import ST_UID

studentInfo = {
    "Eshan":"Is a student", #use for single value
    "Anamul":{
    "location":"Dhaka",
    "Study":"SWE",
     "roll":285,
},
    "Anam":{
    "location":"Dhaka",
    "Study":"CSE",
     "roll":288,
}
}
print(studentInfo["Anam"])
print("\n")
print(studentInfo["Anam"]["Study"])
print("\n")
print(studentInfo)