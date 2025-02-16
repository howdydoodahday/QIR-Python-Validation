import numpy as np
import matplotlib.pyplot as plt

# QIR Lensing Model
def lensing_effect(mass, distance, alpha):
    return (4 * mass / distance) + alpha  # Placeholder equation

# Allow user input of real-world data
use_real_data = input("Use real-world data? (yes/no): ").strip().lower() == "yes"

if use_real_data:
    # Example: Sloan Digital Sky Survey lensing values
    observed_masses = np.array([1.2, 1.5, 1.8])  # Replace with actual dataset values
    observed_distances = np.array([110, 95, 130])  # Replace with actual dataset values
    observed_lensing = np.array([0.08, 0.1, 0.12])  # Replace with real lensing values
    
    predicted_lensing = [lensing_effect(m, d, 0.05) for m, d in zip(observed_masses, observed_distances)]
    
    # Plot real vs. simulated data
    plt.scatter(observed_distances, observed_lensing, color='red', label="Observed Lensing")
    plt.scatter(observed_distances, predicted_lensing, color='blue', label="QIR-Predicted Lensing")
    plt.xlabel("Distance")
    plt.ylabel("Lensing Effect")
    plt.title("QIR Gravitational Lensing vs. Observed Data")
    plt.legend()
    plt.savefig("output_lensing_comparison.png")
    
    print("Comparison plot saved as 'output_lensing_comparison.png'")
else:
    mass = 1.0  # Solar masses
    distance = 100  # Arbitrary units
    alpha = 0.05  # QIR correction term
    print(f"Lensing effect: {lensing_effect(mass, distance, alpha)}")
