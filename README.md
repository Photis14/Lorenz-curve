# Lorenz Curve for Population Data
In this project, I used NumPy and matplotlib to create a Lorenz curve for the population data of over 200 countries and territories in 2010.

The Lorenz curve shows the contribution to the common "wealth" (in this case, population) of the bottom x "people" (in this case, countries). For example, y(1) represents the contribution of the smallest country, y(2) represents the contribution of the two smallest countries, and y(N) represents the total contribution, which is equal to either 1.0 or 100%.

I normalized both the X and Y dimensions to the range of 0.0 to 1.0, without using any loops or non-array arithmetic operations. The resulting plot had axes labels and a title, and was saved as population-lorenz.png with a resolution of 200dpi.

All of this was accomplished through a complete Python program that read the data from the provided pop2010.npy file and produced the PNG file without any human interaction.

# Technology Stack
The following technologies were used in the development of this project:

NumPy
Matplotlib
Getting Started

To run the program, you must have NumPy and Matplotlib installed on your local machine. Once installed, clone the repository and navigate to the project's root folder in your terminal. Then, run the following command:

bash
Copy code
# Run the Python program
$ python population_lorenz.py
The program will generate the population-lorenz.png file in the same folder.




