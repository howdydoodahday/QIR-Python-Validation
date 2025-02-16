import numpy as np
import matplotlib.pyplot as plt

# Function that runs the gravitational lensing model
def lensing_effect(mass, distance, alpha):
    return (4 * mass / distance) + alpha  # Placeholder equation

# Define parameters
mass = 1.0  # Solar masses
distance = 100  # Arbitrary units
alpha = 0.05  # QIR correction term

# Run the model
lensing_result = lensing_effect(mass, distance, alpha)

# Print basic output
print(f"Lensing effect: {lensing_result}")

# Optional: Save results to file and generate plot
save_output = True  # Change to False to disable file output

if save_output:
    # Save numerical results to a text file
    with open("output_lensing.txt", "w") as file:
        file.write(f"Mass: {mass} Solar masses\n")
        file.write(f"Distance: {distance} units\n")
        file.write(f"QIR Correction (alpha): {alpha}\n")
        file.write(f"Lensing Effect: {lensing_result}\n")
    
    # Generate and save plot
    distances = np.linspace(50, 150, 100)
    lensing_values = [lensing_effect(mass, d, alpha) for d in distances]
    
    plt.plot(distances, lensing_values, label="QIR-Modified Lensing")
    plt.xlabel("Distance")
    plt.ylabel("Lensing Effect")
    plt.title("QIR Gravitational Lensing Simulation")
    plt.legend()
    plt.savefig("output_lensing.png")

    print("Results saved as 'output_lensing.txt' and 'output_lensing.png'")
