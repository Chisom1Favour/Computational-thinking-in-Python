"""A program that solves the 0/1 knapsack problem by exploring algorithms from the corrrect one to the most optimal one. Here, the 0/1 knapsack problem is demonstarted by a calorie constraint, which involves the decison to include a food from the menu or not."""
import random
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    """names, values, calories lists of same length,
        name a list of strings
        values and calories lists of numbers
        returns lists of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu
# Greedy algorithm for the 0/1 knapsack problem
def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0, keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('  ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)

# Algorithm for search/decision tree 
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a wight
        Returns a tuple of the total value of a solution to 0/1 knapsack problem and the items of that solution."""
    # toConsider: Those items that nodes higher up in the tree (corresponding to earlier calls in the recursive call stack) have not yet considered.
    # avail: The amount of space still available
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getUnits())
        withoutVal += nextItem .getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print("Use search tree to allocate", maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print("Total value of items taken ", val)
    if printItems:
        for item in taken:
            print('  ', item)

import random

def buildLargeMenu(numItems, maxVal, maxCost):
    build = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
        Returns fibonacci of n"""
        if n == 0 or n == 1:
            return 1
        try:
            return memo[n]
        except KeyError:
            result = fastFib(n-1, memo) +\
                    fastFib(n-2, memo)
            memo[n] = result
            return result
    
for numItems in (5, 10, 15, 10, 25, 30, 35, 40, 45):`
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)

names = ['wine', 'pizza', 'burger', 'cake', 'fries', 'beer', 'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 98, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
print(' ')
testMaxVal(foods, 750)
