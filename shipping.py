class ShippingMethod:
    """A method of shipping with associated costs."""

    def __init__(self, name, flat_fee=0.00, max_per_pound=0.00, cutoffs=[]):
        self.name = name
        self.flat_fee = flat_fee
        self.max_per_pound = max_per_pound
        self.cutoffs = cutoffs

    def get_cost(self, w):
        """Calculate the cost of shipping a package weighing w lbs by this method."""
        price_per_pound = self.max_per_pound
        for weight, price in self.cutoffs:
            if w <= weight:
                price_per_pound = price
                break
        return self.flat_fee + w * price_per_pound

if __name__ == '__main__':
    weight = 6
    ground = ShippingMethod("Ground Shipping", 20, 4.75, [(2, 1.50), (6, 3.00), (10, 4.00)])
    ground_premium = ShippingMethod("Ground Premium", 125)
    drone = ShippingMethod("Drone Shipping", 0, 14.25, [(2, 4.50), (6, 9.00), (10, 12.00)])
##    print(f"{ground.name}: ${ground.get_cost(weight):.2f}")
##    print(f"{ground_premium.name}: ${ground_premium.get_cost(weight):.2f}")
##    print(f'{drone.name}: ${drone.get_cost(weight):.2f}')
    methods = [ground, ground_premium, drone]
    costs = [(method.name, method.get_cost(weight)) for method in methods]
    method, cost = min(costs, key=lambda x: x[1])
    print(f'{method}: ${cost:.2f}')
