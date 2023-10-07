

import math

def inductance(r, n, l):
    """Calculate inductance of a coil"""
    return (r**2 * n**2) / (9 * r + 10 * l)

def resonance_frequency(L, C):
    """Calculate resonance frequency given inductance and capacitance"""
    return 1 / (2 * math.pi * math.sqrt(L * C))

def tesla_coil_design(r1, n1, l1, C1, r2, n2, l2, C2):
    """Design a Tesla Coil given parameters of primary and secondary coils"""
    # Calculate inductance for primary and secondary coils
    L1 = inductance(r1, n1, l1)
    L2 = inductance(r2, n2, l2)
    
    # Calculate resonance frequencies
    f1 = resonance_frequency(L1, C1)
    f2 = resonance_frequency(L2, C2)
    
    # Check if resonance frequencies match
    if math.isclose(f1, f2, rel_tol=1e-2):  # Tolerance level can be adjusted
        print(f"Design Successful! Resonance Frequency: {f1:.2f} Hz")
    else:
        print(f"Design Failed! Primary Frequency: {f1:.2f} Hz, Secondary Frequency: {f2:.2f} Hz")

# Example usage:
tesla_coil_design(0.1, 10, 0.2, 1e-6, 0.2, 100, 0.4, 1e-9)
