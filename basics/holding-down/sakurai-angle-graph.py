import matplotlib.pyplot as plt

# axis
x = 80

# data
grounded_angle = []
aerial_angle = []
knockback = [item for item in range(1, x+1)]

for i in range(1, x+1): 
    if i <= 32:
        grounded_angle.append(0)
        aerial_angle.append(45)
    if i > 32:
        grounded_angle.append(44)
        aerial_angle.append(45)


plt.step(knockback, grounded_angle, label="Grounded")
plt.step(knockback, aerial_angle, label="Aerial")

plt.title("Effect of Knockback Dealt on Launch Angle")
plt.xlabel("Knockback")
plt.ylabel("Launch Angle")
plt.xticks([item for item in range(0, x + 1, 8)])
plt.yticks([item for item in range(0, 51, 5)])

plt.legend()
plt.show()