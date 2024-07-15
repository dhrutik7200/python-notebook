Number = 204
def AddNumber():
    # accessing the global namespace
    global Number
    Number = Number

print( Number )
AddNumber()
print( Number)