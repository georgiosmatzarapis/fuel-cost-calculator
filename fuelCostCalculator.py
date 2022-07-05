from helpers import Console, Utilities

def moneyForRouteCalculator(distanceInKm, literPriceInEuros, fuelEfficiencyInLiters):
    totalLiters = (fuelEfficiencyInLiters * distanceInKm) / 100
    return round((totalLiters * literPriceInEuros),2)


def main():
    distanceInKm, literPriceInEuros, fuelEfficiencyInLiters = 0, 0, 0

    while(distanceInKm <= 0):
        strDistanceInKm = input(f"{Console.OKBLUE}Enter the distance of the route in kilometers(km):{Console.ENDC}\n")

        if not strDistanceInKm:
            continue

        if not Utilities.isFloat(strDistanceInKm):
            print(f"{Utilities.invalidInputMessage}\n")
            continue
        else:
            distanceInKm = float(strDistanceInKm)

            if distanceInKm <= 0:
                print(f"{Utilities.invalidInputMessage}\n")

    while(literPriceInEuros <= 0):
        strLiterPriceInEuros = input(f"\n{Console.OKBLUE}Enter the price of the liter in euros(€):{Console.ENDC}\n")

        if not strLiterPriceInEuros:
            continue

        if not Utilities.isFloat(strLiterPriceInEuros):
            print(f"{Utilities.invalidInputMessage}\n")
            continue
        else:
            literPriceInEuros = float(strLiterPriceInEuros)

            if literPriceInEuros <= 0:
                print(f"{Utilities.invalidInputMessage}\n")

    while(fuelEfficiencyInLiters <= 0):
        strFuelEfficiencyInLiters = input(f"\n{Console.OKBLUE}Enter the fuel efficiency (lt/100 km):{Console.ENDC}\n")

        if not strFuelEfficiencyInLiters:
            continue

        if not Utilities.isFloat(strFuelEfficiencyInLiters):
            print(f"{Utilities.invalidInputMessage}\n")
            continue
        else:
            fuelEfficiencyInLiters = float(strFuelEfficiencyInLiters)

            if fuelEfficiencyInLiters <= 0:
                print(f"{Utilities.invalidInputMessage}\n")

    moneyForRoute = moneyForRouteCalculator(distanceInKm, literPriceInEuros, fuelEfficiencyInLiters)
    requiredFuel = round(((fuelEfficiencyInLiters * distanceInKm) / 100),1)

    print("\n---------------")
    print(f"Route distance: {distanceInKm} km")
    print(f"Liter price: {literPriceInEuros} €")
    print(f"Fuel efficiency: {fuelEfficiencyInLiters} lt\n")
    print(f"{Console.OKGREEN}Needed money for the route: {moneyForRoute} €{Console.ENDC}")
    print(f"{Console.OKGREEN}Required liters of fuel: {requiredFuel} lt{Console.ENDC}\n\n")

    input(f"{Console.OKCYAN}Press 'Enter' To Exit...{Console.ENDC}")


if __name__ == "__main__":
    main()
