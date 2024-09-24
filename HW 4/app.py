import pandas as pd
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure, curdoc
from bokeh.io import show

df = pd.read_csv('preprocessed_response_time.csv')

# convert month back to datetime for plotting
df['month'] = pd.to_datetime(df['month'].astype(str))

# ColumnDataSource for plotting the 'ALL' zip codes initially
source_all = ColumnDataSource(data=dict(month=[], response_time_hours=[]))

# ColumnDataSource for zip1 and zip2
source_zip1 = ColumnDataSource(data=dict(month=[], response_time_hours=[]))
source_zip2 = ColumnDataSource(data=dict(month=[], response_time_hours=[]))

# figure for the line plot
p = figure(x_axis_type='datetime', height=400, width=800, title="Monthly Average Response Time (in hours)",
           x_axis_label='Month', y_axis_label='Response Time (hours)')

# plot the three curves:
line_all = p.line('month', 'response_time_hours', source=source_all, color='blue', legend_label='All Zipcodes')
line_zip1 = p.line('month', 'response_time_hours', source=source_zip1, color='green', legend_label='Zipcode 1')
line_zip2 = p.line('month', 'response_time_hours', source=source_zip2, color='red', legend_label='Zipcode 2')

# dropdown menus for selecting zip codes
zipcodes = df['incident_zip'].unique().tolist()
zipcodes.remove('ALL')  # ALL is not a zipcode
zip_select1 = Select(title="Select Zipcode 1", value=zipcodes[0], options=zipcodes)
zip_select2 = Select(title="Select Zipcode 2", value=zipcodes[1], options=zipcodes)

# update the plot based on selected zip codes
def update_plot(attr, old, new):
    zip1 = zip_select1.value
    zip2 = zip_select2.value

    # Filter data
    df_all = df[df['incident_zip'] == 'ALL']
    df_zip1 = df[df['incident_zip'] == zip1]
    df_zip2 = df[df['incident_zip'] == zip2]

    # Update the data source for 'ALL'
    source_all.data = dict(
        month=df_all['month'],
        response_time_hours=df_all['response_time_hours']
    )

    # Update the data source for zip1
    source_zip1.data = dict(
        month=df_zip1['month'],
        response_time_hours=df_zip1['response_time_hours']
    )

    # Update the data source for zip2
    source_zip2.data = dict(
        month=df_zip2['month'],
        response_time_hours=df_zip2['response_time_hours']
    )

# callback to the dropdowns
zip_select1.on_change('value', update_plot)
zip_select2.on_change('value', update_plot)

# Set up layout
layout = column(zip_select1, zip_select2, p)

# default values
update_plot(None, None, None)

curdoc().add_root(layout)
curdoc().title = "NYC 311 Dashboard"
