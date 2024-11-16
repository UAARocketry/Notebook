# Constants for thermal calculations
import math

# Constants
IPA_HEAT_CAPACITY = 2.68  # kJ/kg*K (specific heat capacity of isopropyl alcohol)
IPA_DENSITY = 785  # kg/m^3 (density of isopropyl alcohol at 20°C)
NOZZLE_WALL_THICKNESS = 0.002  # meters (estimated wall thickness for cooling channel)
THERMAL_CONDUCTIVITY_COPPER = 400  # W/m*K (thermal conductivity of copper alloy)
IPA_BOILING_POINT = 82  # Celsius
COOLING_CHANNEL_AREA = 0.0001  # m^2 (cross-sectional area of cooling channel, estimated)
COOLANT_FLOW_RATE = 0.02  # kg/s (initial estimate for IPA flow rate)
NOZZLE_HEAT_FLUX = 1e6  # W/m^2 (estimated heat flux in the nozzle throat region)
NOZZLE_LENGTH = 0.3  # meters (approximate length of nozzle cooling area)

# Heat absorbed by IPA
heat_absorbed_per_second = NOZZLE_HEAT_FLUX * NOZZLE_LENGTH * COOLING_CHANNEL_AREA

# Temperature rise of IPA
mass_flow_rate = COOLANT_FLOW_RATE  # kg/s
temperature_rise = heat_absorbed_per_second / (mass_flow_rate * IPA_HEAT_CAPACITY * 1000)  # Convert kJ to J

# Check if boiling occurs
final_temperature = temperature_rise + 20  # Start temperature at 20°C
boiling_check = "Boiling occurs" if final_temperature >= IPA_BOILING_POINT else "No boiling"

# Thermal stress on nozzle wall
heat_transfer_rate = NOZZLE_HEAT_FLUX * COOLING_CHANNEL_AREA
wall_temperature_rise = (heat_transfer_rate * NOZZLE_WALL_THICKNESS) / THERMAL_CONDUCTIVITY_COPPER

{
    "Heat Absorbed per Second (W)": heat_absorbed_per_second,
    "Final Temperature of IPA (°C)": final_temperature,
    "Boiling Check": boiling_check,
    "Wall Temperature Rise (°C)": wall_temperature_rise
}
