basket1 = {"apple", "banana", "mango", "apple", "grape"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}
print("basket1 :",basket1)
print("basket2 :",basket2)

basket1.add("orange")
print("basket1 after adding orange:",basket1)

common_fruits = basket1.intersection(basket2)
print("Some common fruits in both baskets:",common_fruits)

import array as ar
fruits_counts = ar.array("i", [3, 5, 2, 4])
print("fruit_count array:",fruits_counts)

fruits_counts.insert(0,1)
fruits_counts.append(6)
print("fruit_count after the addition of items:",fruits_counts)

count_of_four = fruits_counts.count(4)
print("Number of times 4 appeared:",count_of_four)

fruits_counts.reverse()
print("reversed fruit_count array:",fruits_counts)

print("")
print("================ CLASS FRUIT BASKET ORGANIZER ================")
print("basket1:",basket1)
print("basket2:",basket2)
print("shared fruits:",common_fruits)
print("fruit counts:",fruits_counts)
print("==============================================================")