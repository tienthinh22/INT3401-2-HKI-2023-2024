studentIDs = {"knuth": 42.0, "turing": 56.0, "nash": 92.0}
print(studentIDs["turing"])
studentIDs["nash"] = "ninety-two"
del studentIDs["knuth"]
print(studentIDs)
print(studentIDs.keys())
print(studentIDs.values())
print(studentIDs.items())
print(len(studentIDs))