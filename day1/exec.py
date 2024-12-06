
list1 = []
list2 = []

f = open("input.txt", "r")
for x in f:
    print(x.strip())
    # Split the line on the tab character
    parts = x.strip().split("   ")
    print(parts)

    # Add the first part to list1
    list1.append(parts[0])

    # Add the second part to list2
    list2.append(parts[1])

# Sort each list, smallest to largest
list1.sort()
list2.sort()

total = 0
# Loop through the lists and find the difference between the two
for count, ele in enumerate(list1):
    diff = abs(int(list2[count]) - int(ele))
    total += diff

# Answer for part 1
print('Total: %s' % total)

similarity_total = 0
# Go through list1 and see how many times a number appears in list2
for ele in list1:
    count = list2.count(ele)
    print('Count: %s' % count)
    similarity = int(ele) * count
    print(similarity)
    similarity_total += similarity

# Answer for part 2
print('Similarity Total: %s' % similarity_total)