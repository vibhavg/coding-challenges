# Day 1 of the Advent of Code Challenge

def getFuelForMass(mass):
  return int(mass / 3.) - 2

def getFuelForModule(module_mass):
    fuel = getFuelForMass(module_mass)
    total_fuel = fuel
    while (fuel > 0):
        fuel = getFuelForMass(fuel)
        total_fuel += fuel if fuel > 0 else 0

    return total_fuel

if __name__ == "__main__":

    with open("shield_masses.txt") as mass_file:
        masses = [float(mass) for mass in mass_file]

    total_fuel = 0
    for mass in masses:
        total_fuel += getFuelForMass(mass)

    print("Total Fuel without fuel as mass: {}".format(total_fuel))

    total_fuel = 0
    for mass in masses:
        total_fuel += getFuelForModule(mass)

    print("Total fuel including fuel for fuel: {}".format(total_fuel))

