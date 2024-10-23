# task 1:

# script with argparse:
import argparse

def main():
    pass
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help="This is the input file")
    parser.add_argument('-o', '--output', required=True, help="This is the output")
    
    args = parser.parse_args
    script_func(args.input)
    
def script_func(input):
    pass

if __name__ == '__main__':
    main()
    
# Jupyter setup:
 
# call jupyter notebook

# Bokeh App: remember it must be naked code
from bokeh.plotting import figure, curdoc
from bokeh.models import Select
from bokeh.layouts import column
# Create the figure
p = figure(title="", x_axis_type="", height="", width="",)

# dropdown menu:
dropdown_option = Select(title="Select first dropdown", value="Default value to display", options="Values in dataframe")
# Create the lines
line = p.line('x_data', 'y_data', source="If Needed", color="color", legend_label="Little Label in the Corner" )
    # add more as needed
    
def update_plot(attr, old, new):
    new_attr = dropdown_option.value
    # get all data for new dropdown value
    data_new_attr = "df[df[dataframe] == new_attr]"
    
    # update line on graph to display new value
    line.datasource.data = { 'x': data_new_attr['label'], 'y': data_new_attr['otherdata']}
    
    # .
    # .
    # .
    
# callback:
dropdown_option.on_change('value', update_plot)

# Define layout:
layout = column("Dropdown1", "Dropdown2", "p (from figure)")

# Add layout to document
curdoc().addroot(layout)
curdoc().title = "Dashboard"

# bokeh serve --show {bokeh_app}.py --port 8080

