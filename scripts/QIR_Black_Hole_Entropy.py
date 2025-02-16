import numpy as np
import matplotlib.pyplot as plt

# Function that models black hole entropy corrections with QIR
def black_hole_entropy_correction(mass, qir_correction):
    return (mass ** 2) * (1 + qir_correction)  # Placeholder equation

# Define parameters
mass = 10  # Solar masses
qir_correction = 0.02  # QIR entropy correction term

# Run the model
entropy_result = black_hole_entropy_correction(mass, qir_correction)

# Print basic output
print(f"Black hole entropy correction: {entropy_result}")

# Optional: Save results to file and generate plot
save_output = True  # Change to False to disable file output

if save_output:
    # Save numerical results to a text file
    with open("output_entropy.txt", "w") as file:
        file.write(f"Mass: {mass} Solar masses\n")
        file.write(f"QIR Correction: {qir_correction}\n")
        file.write(f"Black Hole Entropy Correction: {entropy_result}\n")
    
    # Generate and save plot
    masses = np.linspace(5, 15, 100)
    entropy_values = [black_hole_entropy_correction(m, qir_correction) for m in masses]
    
    plt.plot(masses, entropy_values, label="QIR-Modified Black Hole Entropy")
    plt.xlabel("Mass (Solar Masses)")
    plt.ylabel("Entropy Correction")
    plt.title("QIR Black Hole Entropy Simulation")
    plt.legend()
    plt.savefig("output_entropy.png")

    print("Results saved as 'output_entropy.txt' and 'output_entropy.png'")
