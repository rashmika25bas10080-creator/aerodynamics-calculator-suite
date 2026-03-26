"""
Lift and Drag force calculators
"""

from utils.constants import SEA_LEVEL_DENSITY, SEA_LEVEL_PRESSURE


def calculate_lift(density, velocity, area, lift_coefficient):
    """
    Calculate lift force
    Formula: L = 0.5 × ρ × V² × S × C_L
    """
    if any(x <= 0 for x in [density, velocity, area, lift_coefficient]):
        raise ValueError("All inputs must be positive numbers")
    
    dynamic_pressure = 0.5 * density * (velocity ** 2)
    lift = dynamic_pressure * area * lift_coefficient
    
    return lift


def calculate_drag(density, velocity, area, drag_coefficient):
    """
    Calculate drag force
    Formula: D = 0.5 × ρ × V² × S × C_D
    """
    if any(x <= 0 for x in [density, velocity, area, drag_coefficient]):
        raise ValueError("All inputs must be positive numbers")
    
    dynamic_pressure = 0.5 * density * (velocity ** 2)
    drag = dynamic_pressure * area * drag_coefficient
    
    return drag


def lift_to_drag_ratio(lift, drag):
    """
    Calculate lift-to-drag ratio
    """
    if drag <= 0:
        raise ValueError("Drag must be positive")
    
    return lift / drag
