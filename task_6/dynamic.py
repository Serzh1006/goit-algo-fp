def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_choice = [[] for _ in range(budget + 1)]

    for item, value in items.items():
        cost = value['cost']
        calories = value['calories']
        
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_choice[current_budget] = item_choice[current_budget - cost] + [item]
    
    return item_choice[budget], dp[budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories = dynamic_programming(items, budget)
print("Dynamic Programming:")
print("Selected items:", selected_items)
print("Total calories:", total_calories)