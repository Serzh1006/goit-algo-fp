def greedy_algorithm(items, budget):
    item_ratios = {item: value['calories'] / value['cost'] for item, value in items.items()}
    sorted_items = sorted(item_ratios.items(), key=lambda x: x[1], reverse=True)
    
    total_calories = 0
    total_cost = 0
    selected_items = []
    
    for item, ratio in sorted_items:
        cost = items[item]['cost']
        calories = items[item]['calories']
        
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_calories += calories
            total_cost += cost
    
    return selected_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", selected_items)
print("Total calories:", total_calories)