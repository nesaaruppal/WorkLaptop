import math 

def spherical_shell_volume(r1, r2):
    """
    Calculates the volume of a spherical shell given the radii of the inner and outer spheres.

    Args:
        r1 (float): The radius of the inner sphere.
        r2 (float): The radius of the outer sphere.

    Returns:
        float: The volume of the spherical shell.

    Raises:
        ValueError: If the input radii are not positive numbers.

    """
    if r1 <= 0 or r2 <= 0:
        raise ValueError("The input radii must be positive numbers")

    volume = (4/3) * math.pi * (r1**3 - r2**3)

    return round(volume, 3)

Volume_of_Spherical_Shell = (4/3) * (3.1415) * (r1**3 - r2**3)

print(Volume_of_Spherical_Shell(3,3))