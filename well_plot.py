import altair as alt
from vega_datasets import data

def make_chart(well_df):
    # Read in polygons from topojson
    states = alt.topo_feature(data.us_10m.url, feature='states')

    # US states background
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).properties(
        width=500,
        height=300
    ).project('albersUsa')

    well_chart = alt.Chart(well_df).mark_circle() \
                    .encode(latitude='latitude:Q', longitude='longitude:Q', \
                            color=alt.Color('gradient', scale=alt.Scale(scheme='yelloworangered')), \
                            tooltip=[alt.Tooltip('depth', title='Depth(m)'), 
                                     alt.Tooltip('gradient', title='Gradient (°C/m)', format='0.3f')]
                           )\
                    .properties(title='Abandoned wells')

    return background + well_chart