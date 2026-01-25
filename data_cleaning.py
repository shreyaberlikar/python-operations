import pandas as pd
import numpy as np

# Sample data
data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}

# Create DataFrame
energy_df = pd.DataFrame(data)

print("Original DataFrame:")
print(energy_df)

# Forward fill missing values
forward_filled_df = energy_df.ffill()
print("\nData After Forward Filling:")
print(forward_filled_df)

# Backward fill missing values
backward_filled_df = energy_df.bfill()
print("\nData After Backward Filling:")
print(backward_filled_df)

#output
Original DataFrame:
  Energy Source  Energy Consumption (MWh)  Cost (Million $)
0         Solar                     1200.0             200.0
1          Wind                        NaN             400.0
2    Hydropower                     2900.0               NaN
3    Geothermal                        NaN             150.0
4        Biomass                     2500.0             250.0
5        Nuclear                     3200.0               NaN

Data After Forward Filling:
  Energy Source  Energy Consumption (MWh)  Cost (Million $)
0         Solar                     1200.0             200.0
1          Wind                     1200.0             400.0
2    Hydropower                     2900.0             400.0
3    Geothermal                     2900.0             150.0
4        Biomass                     2500.0             250.0
5        Nuclear                     3200.0             250.0

Data After Backward Filling:
  Energy Source  Energy Consumption (MWh)  Cost (Million $)
0         Solar                     1200.0             200.0
1          Wind                     2900.0             400.0
2    Hydropower                     2900.0             150.0
3    Geothermal                     2500.0             150.0
4        Biomass                     2500.0             250.0
5        Nuclear                     3200.0               NaN
