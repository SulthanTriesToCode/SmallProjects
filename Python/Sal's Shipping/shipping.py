weight= 1.5

# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
elif weight <= 20:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping: $" + str(cost_ground))

# Ground Shipping Premium
premium_ground = 125.00
print("Ground Shipping Premium: $" + str(premium_ground))

if weight <= 2:
  drone_ground = weight * 4.50
elif weight <= 6:
  drone_ground = weight * 9.00
elif weight <= 10:
  drone_ground = weight * 12.00
elif weight <= 20:
  drone_ground = weight * 14.25

print("Drone Shipping: $" + str(drone_ground))

