# Coal Imports Germany

## Project Description
In this project I have analysed the data of Coal Imports in Germany provided publicly from the Database of the Federal Statistical Office of Germany. The data starts from 2004 till 2022 and contains Monthly Data regarding the Quantity and Cost of Coal Imports from categorised sources. The data can be found at [Genesis Online Portal](https://www-genesis.destatis.de/genesis//online?operation=table&code=43511-0002&bypass=true&levelindex=1&levelid=1685794296645#abreadcrumb). I used `Python v3.8.10` along with python libraries `NumPy v1.22.0`, `Pandas v1.3.5` and `Seaborn v0.11.2` for my analysis, calculations and visualization. 

## Package Installation

To install Python, NumPy, and Pandas on Linux, follow these steps:

1. Open a terminal window.

2. Check if Python is already installed by running the following command:
- `python --version`

If Python is not installed, you will need to install it.

3. Install Python by running the appropriate command for your Linux distribution:
- For Debian-based systems (e.g., Ubuntu):
  ```
  sudo apt-get update
  sudo apt-get install python3
  ```

4. Verify that Python is installed correctly by running `python --version` again.

5. Install the `pip` package manager, which is used to install Python packages:

- `sudo -apt-get install python3-pip`

6. Install NumPy by running the following command:
- `pip install numpy`
7. Install Pandas by running the following command:
- `pip install pandas`
8. Install Seaborn by running the following command:
- `pip install seaborn`

9. Verify that NumPy and Pandas are installed correctly by importing them in a Python script or running the following commands in a Python interpreter:
- ```
    python
    import numpy
    import pandas
  ```


If there are no errors, the installation was successful.

## Directory Structure
- `./`: The root directory of your project.

- `README.md`: The README file provides an overview and instructions for your project.

- `data/`: This directory contains various data files used in your project, including:
  - `43511-0002-USPLD1_$F.xlsx`: An Excel file containing data.
  - `CleanedData.csv`: A CSV file containing cleaned data.
  - `Pivot_Tables.xlsx`: An Excel file containing pivot tables.
  - `Sorted_Workbook.xlsx`: An Excel file with sorted data.

- `docs/`: The `docs` directory holds project documentation, including:
  - `Analysis.ipynb`: A Jupyter Notebook file for data analysis.
  - `Report.ipynb`: A Jupyter Notebook file for generating project reports.
  - `cleaning.py`: A Python script for data cleaning.
  - `description.txt`: A text file providing additional project description or documentation.

- `images/`: This directory contains various images related to your project, including:
  - `Country_of_Origin_Comparison.jpg`: An image comparing the country of origin.
  - `Import_hardcoal_yearly.jpg`: An image showing yearly import of hard coal.
  - `Imports_hardcoal_eurospert_month.jpg`: An image showing imports of hard coal in euros per tonne.
  - `Country_of_Origin_TotalEuros.jpg`: An image displaying the total euros based on country of origin.
  - `Imports_hardcoal_tonnes_compared_months.jpg`: An image comparing imports of hard coal in tonnes.
