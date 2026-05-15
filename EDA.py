import pandas as pd
import matplotlib.pyplot as plt

# Dataset
space_data = {
    "Company": ["ISRO", "NASA", "SpaceX", "Roscosmos", "ESA"],
    "Mission_Cost": [75, 500, 200, 150, 180],
    "Success_Rate": [95, 98, 97, 85, 90],
    "Launches": [120, 300, 250, 220, 150]
}

data = pd.DataFrame(space_data)


# Graph 1 : Bar Chart

plt.figure(1)

plt.bar(data["Company"], data["Launches"])

plt.title("Company vs Launches")
plt.xlabel("Company")
plt.ylabel("Launches")

plt.show()


# Graph 2 : Scatter Plot

plt.figure(2)

plt.scatter(data["Mission_Cost"],
            data["Success_Rate"])

plt.title("Mission Cost vs Success Rate")
plt.xlabel("Mission Cost")
plt.ylabel("Success Rate")

plt.show()

# Graph 3 : Pie Chart

plt.figure(3)

plt.pie(data["Launches"],
        labels=data["Company"],
        autopct='%1.1f%%')

plt.title("Launch Distribution")

plt.show()