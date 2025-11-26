from stat import ST_UID

studentInfo = {
    "Eshan":"Is a student", #use for single value
    #USe MUltiple value
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
#Change value
studentInfo["Eshan"]="Software Engineer"
print(studentInfo["Eshan"])
print(studentInfo)


#Update Value
StudentInfo1 = {
    "Haque":"CSE Student"
}
StudentInfo1.update({"Haque":"Haque Is an SOftware Engineer"})
print(StudentInfo1["Haque"])