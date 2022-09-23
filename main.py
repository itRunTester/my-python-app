print("Hello Piorun")

name = "Bum"
name = "Bum2"
age = 20
pi = 3.14
number = [1, 2, 3, 4]

print(name)
print(age)
print(pi)
print(number)

comment = """
dfdgfdg {},
dfgdfgd
dfg,fdgdfg"""

print(comment.format(pi))

#
comment = f"""
dfdgfdg {number},
dfgdfgd
dfgf{age}dgdfg"""

print(comment)