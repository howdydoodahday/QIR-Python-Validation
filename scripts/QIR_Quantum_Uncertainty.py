import numpy as np
import matplotlib.pyplot as plt

# Function that models quantum uncertainty with QIR
def quantum_uncertainty(position_uncertainty, information_density):
    return (1 / information_density) * position_uncertainty  # Placeholder equation

# Define parameters
position_uncertainty = 1.0  # Arbitrary units
information_density = 0.05  # QIR correction term

# Run the model
uncertainty_result = quantum_uncertainty(position_uncertainty, information_density)

# Print basic output
print(f"Quantum uncertainty effect: {uncertainty_result}")

# Optional: Save results to file and generate plot
save_output = True  # Change to False to disable file output

if save_output:
    # Save numerical results to a text file
    with open("output_uncertainty.txt", "w") as file:
        file.write(f"Position Uncertainty: {position_uncertainty}\n")
        file.write(f"Information Density: {information_density}\n")
        file.write(f"Quantum Uncertainty Effect: {uncertainty_result}\n")
    
    # Generate and save plot
    densities = np.linspace(0.01, 0.1, 100)
    uncertainty_values = [quantum_uncertainty(position_uncertainty, d) for d in densities]
    
    plt.plot(densities, uncertainty_values, label="QIR Quantum Uncertainty")
    plt.xlabel("Information Density")
    plt.ylabel("Uncertainty Effect")
    plt.title("QIR Quantum Uncertainty Simulation")
    plt.legend()
    plt.savefig("output_uncertainty.png")

    print("Results saved as 'output_uncertainty.txt' and 'output_uncertainty.png'")
