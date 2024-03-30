import numpy as np

fuel_efficiency = {
    'model': ['Model A', 'Model B', 'Model C', 'Model D', 'Model E', 'Model F', 'Model G', 'Model H', 'Model I', 'Model J'],
    'mpg': [25, 30, 28, 32, 27, 35, 22, 29, 31, 26]
}

models = np.array(fuel_efficiency['model'])
mpg_values = np.array(fuel_efficiency['mpg'])

avg_mpg = np.mean(mpg_values)
print(f"The average fuel efficiency is: {avg_mpg:.2f} mpg")

model_a_mpg = mpg_values[models == 'Model A'][0]
model_h_mpg = mpg_values[models == 'Model H'][0]

percentage_improvement = (model_h_mpg - model_a_mpg) / model_a_mpg * 100
print(f"The percentage improvement in fuel efficiency from Model A to Model H is: {percentage_improvement:.2f}%")
