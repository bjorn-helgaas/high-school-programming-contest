import sys
 
lines = sys.stdin.readlines()
num_cases = int(lines[0])
 
case = 1
while case < num_cases + 1:
    gallons, density_lb_gal = lines[case].split()
    weight_lb = float(gallons) * float(density_lb_gal)
    weight_kg = weight_lb / 2.2
    print("%.2f" % weight_kg)
    case = case + 1

