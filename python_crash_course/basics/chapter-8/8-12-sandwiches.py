def sandwich_toppings (*toppings):
    for topping in toppings:
        print(f"Adding {topping}")
    print("You can take your sandwichs thanks \n")
sandwich_toppings("jam and cheese")
sandwich_toppings("jam and cheese", "pepper", "mushrooms")
sandwich_toppings("tomatoes", "cheese")