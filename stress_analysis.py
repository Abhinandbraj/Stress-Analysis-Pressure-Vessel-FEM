import numpy as np
import matplotlib.pyplot as plt

# Constants ( realistic aerospace parameters)
sigma_y = 350  # Yield strength of material in MPa (2024-T3 Aluminum)
r = 1.5        # Radius of the vessel in meters
t_values = [0.01, 0.015, 0.02, 0.03]  # Wall thickness in meters
P_values = [10, 20, 50]  # Internal pressure in MPa

# Calculate hoop and longitudinal stress for each combination of pressure and thickness
def calculate_stresses(P, t):
    # Hoop stress (σ_h)
    sigma_h = P * r / t
    
    # Longitudinal stress (σ_l)
    sigma_l = P * r / (2 * t)
    
    # Von Mises stress (σ_vm)
    sigma_vm = np.sqrt(sigma_h**2 - sigma_h * sigma_l + sigma_l**2)
    
    # Safety factor (SF)
    safety_factor = sigma_y / sigma_vm
    
    return sigma_h, sigma_l, sigma_vm, safety_factor

# Store results for plotting
results = []

# Loop over pressure and thickness values
for P in P_values:
    for t in t_values:
        sigma_h, sigma_l, sigma_vm, safety_factor = calculate_stresses(P, t)
        results.append((P, t, sigma_h, sigma_l, sigma_vm, safety_factor))

# Plot the results for hoop stress, longitudinal stress, Von Mises stress, and safety factor

# Convert results to numpy array for easier plotting
results_array = np.array(results)

# Create subplots for visualization
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot Hoop Stress
axs[0, 0].plot(results_array[:, 1], results_array[:, 2], 'bo-', label="Hoop Stress (σ_h)")
axs[0, 0].set_xlabel("Wall Thickness (m)")
axs[0, 0].set_ylabel("Hoop Stress (MPa)")
axs[0, 0].set_title("Hoop Stress vs Wall Thickness")
axs[0, 0].legend()

# Plot Longitudinal Stress
axs[0, 1].plot(results_array[:, 1], results_array[:, 3], 'ro-', label="Longitudinal Stress (σ_l)")
axs[0, 1].set_xlabel("Wall Thickness (m)")
axs[0, 1].set_ylabel("Longitudinal Stress (MPa)")
axs[0, 1].set_title("Longitudinal Stress vs Wall Thickness")
axs[0, 1].legend()

# Plot Von Mises Stress
axs[1, 0].plot(results_array[:, 1], results_array[:, 4], 'go-', label="Von Mises Stress (σ_vm)")
axs[1, 0].set_xlabel("Wall Thickness (m)")
axs[1, 0].set_ylabel("Von Mises Stress (MPa)")
axs[1, 0].set_title("Von Mises Stress vs Wall Thickness")
axs[1, 0].legend()

# Plot Safety Factor
axs[1, 1].plot(results_array[:, 1], results_array[:, 5], 'mo-', label="Safety Factor (SF)")
axs[1, 1].set_xlabel("Wall Thickness (m)")
axs[1, 1].set_ylabel("Safety Factor")
axs[1, 1].set_title("Safety Factor vs Wall Thickness")
axs[1, 1].legend()

# Adjust layout and show the plots
plt.tight_layout()
plt.savefig("stress_analysis_graph.png", dpi=300, bbox_inches='tight')
plt.show()
