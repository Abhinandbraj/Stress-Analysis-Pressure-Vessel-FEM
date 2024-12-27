# Stress-Analysis-Pressure-Vessel-FEM

# Stress Analysis of a Thin-Walled Cylindrical Pressure Vessel Using FEM principles in Python

## Objective
This project analyzes the stresses and safety factors in a thin-walled cylindrical pressure vessel subjected to internal pressure. The calculations are performed using the **Finite Element Method (FEM)** in Python, and the results are visualized through graphs.

## Input Parameters
The analysis uses realistic input parameters for aerospace applications:

- **Internal Pressure (P)**: 10 MPa, 20 MPa, 50 MPa  
- **Radius (r)**: 1.5 meters  
- **Wall Thickness (t)**: 0.01 m, 0.015 m, 0.02 m, 0.03 m  
- **Material Properties**:
  - Yield Strength (sigma_y): 350 MPa (2024-T3 Aluminum)
- **Safety Factor**: Minimum acceptable value = 1.5

## Calculations
The following stresses are calculated for different combinations of pressure and wall thickness:

1. **Hoop Stress (sigma_h)**:
sigma_h = (P * r) / t


2. **Longitudinal Stress (sigma_l)**:
sigma_l = (P * r) / (2 * t)


3. **Von Mises Stress (sigma_vm)**:
sigma_vm = sqrt(sigma_h^2 - sigma_h * sigma_l + sigma_l^2)


4. **Safety Factor (SF)**:
SF = sigma_y / sigma_vm



## Results
The results are visualized using graphs:
- **Hoop Stress vs Wall Thickness**
- **Longitudinal Stress vs Wall Thickness**
- **Von Mises Stress vs Wall Thickness**
- **Safety Factor vs Wall Thickness**

These graphs help in understanding the relationship between wall thickness, applied pressure, and material safety.

## How to Run

### Dependencies
Ensure the following Python libraries are installed:
- `numpy`
- `matplotlib`

To install them, use the following commands:
pip install numpy pip install matplotlib


### Steps
1. Clone or download this repository.
2. Open the Python script (`stress_analysis.py`) in your IDE or Pydroid.
3. Run the script.
4. The graphs will be displayed and saved in the working directory.

## Project Files
- **`stress_analysis.py`**: Python script for stress calculations and graph generation.
- **Graphs**: Saved graphs (optional).
- **`README.md`**: Project documentation.

## Validation
The results are based on established formulas for stress analysis in pressure vessels and are validated against real-world parameters.

## Future Improvements
- Add more material options for analysis.
- Automate the input of parameters.
- Extend to 3D FEM analysis using advanced libraries.


