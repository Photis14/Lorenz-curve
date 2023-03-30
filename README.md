# Lorenz-curve

In this project, I used NumPy and matplotlib to create a Lorenz curve for the population data of over 200 countries and territories in 2010.

The Lorenz curve showed the contribution to the common "wealth" (in this case, population) of the bottom x "people" (in this case, countries). For example, y(1) represented the contribution of the smallest country, y(2) represented the contribution of the two smallest countries, and y(N) represented the total contribution, which was equal to either 1.0 or 100%.

I normalized both the X and Y dimensions to the range of 0.0 to 1.0, without using any loops or non-array arithmetic operations. The resulting plot had axes labels and a title, and was saved as population-lorenz.png with a resolution of 200dpi.

All of this was accomplished through a complete Python program that read the data from the provided pop2010.npy file and produced the PNG file without any human interaction.

Thank you for joining me on this project, and I hope you found it informative and enjoyable!





