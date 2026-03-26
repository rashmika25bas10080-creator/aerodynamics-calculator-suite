"""
Wing Loading and related calculations
"""


def calculate_wing_loading(weight, wing_area):
    """
    Calculate wing loading
    Formula: W/S = Weight / Wing Area
    """
    if wing_area <= 0:
        raise ValueError("Wing area must be positive")
    
    if weight <= 0:
        raise ValueError("Weight must be positive")
    
    return weight / wing_area


def calculate_stall_speed(wing_loading, density, max_lift_coefficient):
    """
    Calculate stall speed from wing loading
    Formula: V_stall = √(2 × (W/S) / (ρ × C_Lmax))
    """
    if any(x <= 0 for x in [wing_loading, density, max_lift_coefficient]):
        raise ValueError("All inputs must be positive")
    
    stall_speed = ((2 * wing_loading) / (density * max_lift_coefficient)) ** 0.5
    
    return stall_speed
