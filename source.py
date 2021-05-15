print("|-----------------------------------------------------|")
print("  |Press ctrl+c to exit out or just close the window|")
print("|-----------------------------------------------------| \n \n")


def DPIandsenstoeDPI():
    print("What is your DPI")
    DPI = int(input())

    print("What is your sensitivity")
    sens = float(input())

    eDPI = DPI * sens

    print(f"\n Your DPI is {eDPI}\n")
    main()


def eDPIandDPItoSens():
    print("\nWhat is your eDPI")
    eDPI = int(input())

    print("What is your DPI")
    DPI = int(input())

    sens = eDPI/DPI
    print(f"\n Your sens is: {sens} \n")
    main()


def main():
    print("What would you like to calculate \n")
    choice = input()

    if choice == 'dpiandsenstoedpi' or choice == 'DPIandSenstoEDPI' or choice == 'dpiSenseDPI' or choice == 'dpisensedpi':
        DPIandsenstoeDPI()
    elif choice == 'edpianddpitosens' or choice == 'EDPIandDPItoSens' or choice == 'eDPIdpiSens' or choice == 'edpidpisens':
        eDPIandDPItoSens()
    elif choice == 'help':
        print("")
        print("- help")
        print("- dpisensedpi")
        print("- edpidpisens")
        print("- info\n")
        main()
    elif choice == 'info':
        print("\nThis program will help with finding your common sensitivity using eDPI and DPI")
        print("For example, you can use the 'dpisensedpi' command to find your eDPI (with your dpi and sensitivity).")
        print("Then use that eDPI to share with friends or teammates to compare your sensitivity")
        print("Your friends/teammates can then use the 'edpidpisens' command to convert the eDPI to their sens appropriate DPI \n")
        main()
    else:
        print("--------------------------------")
        print("| Please enter a valid command |")
        print("-------------------------------- \n")
        main()

main()
