#!/usr/bin/env python3
"""
Aerodynamics Calculator Suite
Main entry point with interactive menu system
"""

from utils.constants import SEA_LEVEL_DENSITY, AIR_VISCOSITY, SEA_LEVEL_SPEED_OF_SOUND
from utils.validators import validate_positive_float, validate_coefficient
from calculators.lift_drag import calculate_lift, calculate_drag, lift_to_drag_ratio
from calculators.reynolds_mach import calculate_reynolds_number, calculate_mach_number, classify_flow_regime
from calculators.wing_loading import calculate_wing_loading, calculate_stall_speed


def print_header():
    """Print application header"""
    print("=" * 50)
    print("     AERODYNAMICS CALCULATOR SUITE")
    print("=" * 50)
    print()


def print_menu():
    """Display main menu"""
    print("\nSelect a calculator:")
    print("-" * 40)
    print("1. Lift Force Calculator")
    print("2. Drag Force Calculator")
    print("3. Lift-to-Drag Ratio")
    print("4. Reynolds Number")
    print("5. Mach Number")
    print("6. Wing Loading")
    print("7. Stall Speed")
    print("0. Exit")
    print("-" * 40)


def lift_calculator():
    """Lift force calculator"""
    print("\n--- LIFT FORCE CALCULATOR ---")
    try:
        velocity = validate_positive_float(input("Enter velocity (m/s): "), "Velocity")
        area = validate_positive_float(input("Enter wing area (m²): "), "Area")
        cl = validate_coefficient(input("Enter lift coefficient: "), "Lift coefficient")
        
        lift = calculate_lift(SEA_LEVEL_DENSITY, velocity, area, cl)
        print(f"\nLift Force: {lift:,.2f} N")
    except ValueError as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to continue...")


def drag_calculator():
    """Drag force calculator"""
    print("\n--- DRAG FORCE CALCULATOR ---")
    try:
        velocity = validate_positive_float(input("Enter velocity (m/s): "), "Velocity")
        area = validate_positive_float(input("Enter area (m²): "), "Area")
        cd = validate_coefficient(input("Enter drag coefficient: "), "Drag coefficient")
        
        drag = calculate_drag(SEA_LEVEL_DENSITY, velocity, area, cd)
        print(f"\nDrag Force: {drag:,.2f} N")
    except ValueError as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to continue...")


def ldr_calculator():
    """Lift-to-drag ratio calculator"""
    print("\n--- LIFT-TO-DRAG RATIO ---")
    try:
        lift = validate_positive_float(input("Enter lift force (N): "), "Lift")
        drag = validate_positive_float(input("Enter drag force (N): "), "Drag")
        
        ratio = lift_to_drag_ratio(lift, drag)
        print(f"\nL/D Ratio: {ratio:.2f}")
    except ValueError as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to continue...")


def reynolds_calculator():
    """Reynolds number calculator"""
    print("\n--- REYNOLDS NUMBER ---")
    try:
        velocity = validate_positive_float(input("Enter velocity (m/s): "), "Velocity")
        length = validate_positive_float(input("Enter characteristic length (m): "), "Length")
        
        reynolds = calculate_reynolds_number(SEA_LEVEL_DENSITY, velocity, length)
        regime = classify_flow_regime(reynolds)
        
        print(f"\nReynolds Number: {reynolds:,.2e}")
        print(f"Flow Regime: {regime}")
    except ValueError as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to continue...")


def mach_calculator():
    """Mach number calculator"""
    print("\n--- MACH NUMBER ---")
    try:
        velocity = validate_positive_float(input("Enter velocity (m/s): "), "Velocity")
        
        mach = calculate_mach_number(velocity)
        print(f"\nMach Number: {mach:.3f}")
    except ValueError as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to continue...")


def wing_loading_calculator():
    """Wing loading calculator"""
    print("\n--- WING LOADING ---")
    try:
        weight = validate_positive_float(input("Enter aircraft weight (N): "), "Weight")
        area = validate_positive_float(input("Enter wing area (m²): "), "Area")
        
        loading = calculate_wing_loading(weight, area)
        print(f"\nWing Loading: {loading:.2f} N/m²")
    except ValueError as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to continue...")


def stall_calculator():
    """Stall speed calculator"""
    print("\n--- STALL SPEED ---")
    try:
        weight = validate_positive_float(input("Enter weight (N): "), "Weight")
        area = validate_positive_float(input("Enter wing area (m²): "), "Area")
        cl_max = validate_coefficient(input("Enter max lift coefficient: "), "Max lift coefficient")
        
        wing_loading = calculate_wing_loading(weight, area)
        stall_speed = calculate_stall_speed(wing_loading, SEA_LEVEL_DENSITY, cl_max)
        
        print(f"\nStall Speed: {stall_speed:.2f} m/s")
        print(f"Stall Speed: {stall_speed * 3.6:.2f} km/h")
    except ValueError as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to continue...")


def main():
    """Main program loop"""
    while True:
        print_header()
        print_menu()
        
        choice = input("\nEnter your choice (0-7): ")
        
        if choice == '1':
            lift_calculator()
        elif choice == '2':
            drag_calculator()
        elif choice == '3':
            ldr_calculator()
        elif choice == '4':
            reynolds_calculator()
        elif choice == '5':
            mach_calculator()
        elif choice == '6':
            wing_loading_calculator()
        elif choice == '7':
            stall_calculator()
        elif choice == '0':
            print("\nThank you for using the Aerodynamics Calculator Suite!")
            break
        else:
            print("\nInvalid choice. Please enter 0-7.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
