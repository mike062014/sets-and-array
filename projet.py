snack_set1 = {"apples", "pizza", "milk"}
snack_set2 = {"pizza", "banana", "soda"}
snack_set1.add("ice_cream")
common_items = snack_set1.intersection(snack_set2)
print(common_items)
print(snack_set1)
print(snack_set2)
import array as arr
snacks = arr.array("i", ["apples", "kiwi", "carrot"])
print(snacks)