count = 0
numbers = list()

while True:
    inp = raw_input("Enter number of cards: ")
    if inp.lower() == "done": break
    if len(inp) < 1: break # Checking for empty input
    if inp not in numbers:
        numbers.append(float(inp))
        count = count + 1
print sum(numbers)
bonus = sum(numbers) / 4
print "This student will receive", bonus,"points on the next test."