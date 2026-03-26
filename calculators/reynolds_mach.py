"""
Reynolds Number and Mach Number calculators
"""

from utils.constants import AIR_VISCOSITY, SEA_LEVEL_SPEED_OF_SOUND


def calculate_reynolds_number(density, velocity, characteristic_length, viscosity=None):
    """
    Calculate Reynolds number
    Formula: Re = ρ × V × L / μ
    """
    if any(x <= 0 for x in [density, velocity, characteristic_length]):
        raise ValueError("Density, velocity, and length must be positive")
    
    if viscosity is None:
        viscosity = AIR_VISCOSITY
    
    reynolds = (density * velocity * characteristic_length) / viscosity
    
    return reynolds


def calculate_mach_number(velocity, speed_of_sound=None):
    """
    Calculate Mach number
    Formula: M = V / a
    """
    if velocity < 0:
        raise ValueError("Velocity cannot be negative")
    
    if speed_of_sound is None:
        speed_of_sound = SEA_LEVEL_SPEED_OF_SOUND
    
    mach = velocity / speed_of_sound
    
    return mach


def classify_flow_regime(reynolds_number):
    """
    Classify flow regime based on Reynolds number
    """
    if reynolds_number < 2000:
        return "Laminar Flow"
    elif reynolds_number < 4000:
        return "Transitional Flow"
    else:
        return "Turbulent Flow"
