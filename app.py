#import libraries
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

#add page options for shiny
ui.page_opts(title="PyShiny App with Plot",fillable=True)

#create a sidebar with a slider input
with ui.sidebar():
    # Add a slide for specifying the number of bins in the histogram.
    #The ui.input_slider function is called with 5 arguments.
    # 1. A string ID ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label ("Number of bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins. 
    # 4. An integer representing the maximum number of bins. 
    # 5. An integer representing the initial value of the slider.
    ui.input_slider("selected_number_of_bins","Number of bins", 0, 100, 20)


@render.plot(alt="A histogram")
def histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int=437
    #set a random see to ensure reproducibility. 
    np.random.seed(3)
    
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    
    x = 100 + 15 * np.random.randn(437)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)

@render.plot(alt="Scatterplot")
def scatterplot():
    count_of_points: int = 437
    np.random.seed(3)
    
    # Generate random data
    x = np.random.randn(count_of_points)
    y = np.random.randn(count_of_points)
    
    # Create scatter plot
    plt.scatter(x, y, color='blue', label='Scatter Plot')
    
    # Add labels and title
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Scatter Plot')
