def get_ground_cost(w):
  """Calculate the cost of shipping a package weighing w lbs by ground."""
  flat_fee = 20
  price_per_pound = None
  if w <= 2.0:
    price_per_pound = 1.50
  elif 2 < w <= 6:
    price_per_pound = 3.00
  elif 6 < w <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return w * price_per_pound + flat_fee

def get_ground_premium_cost(w):
  """Calculate the cost of shipping a package weighing w lbs by premium ground."""
  flat_fee = 125
  return flat_fee

def get_drone_cost(w):
  """Calculate the cost of shipping a package weighing w lbs by drone."""
  price_per_pound = None
  if w <= 2.0:
    price_per_pound = 4.50
  elif 2 < w <= 6:
    price_per_pound = 9.00
  elif 6 < w <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return w * price_per_pound

if __name__ == '__main__':
    weight = 4.8
    ground_cost = get_ground_cost(weight)
    ground_premium_cost = get_ground_premium_cost(weight)
    drone_cost = get_drone_cost(weight)
    #print(f'Ground Shipping: ${ground_cost:.2f}')
    #print(f"Ground Shipping Premium: ${ground_premium_cost:.2f}")
    #print(f'Drone Shipping: ${drone_cost:.2f}')

    costs = [("Ground Shipping", ground_cost),
          ("Ground Shipping Premium", ground_premium_cost),
          ("Drone Shipping", drone_cost),
    ]

    method, cost = min(costs, key=lambda x: x[1])
    print(f'{method}: ${cost:.2f}')
