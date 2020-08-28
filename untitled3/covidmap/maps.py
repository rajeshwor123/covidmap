import pandas as pd
import numpy as np
import os
import django
from plotly.graph_objs import Layout, Figure

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled3.settings')
django.setup()
from covidmap.models import pandemic
import folium
import plotly.graph_objects as go


class maps:
    total_death = 0
    total_infected = 0
    total_recovered = 0

    def map(self):
        dataObj = pandemic.objects.values_list("death")
        dataTuple = list(dataObj)
        data = []
        death = 0
        for d in dataTuple:
            for x in d:
                data.append(x)

        for i in range(0, len(data)):
            data[i] = int(data[i])
            death = death + data[i]
        maps.total_death = death
        # print(data)

        state_geo = 'assets/nepal.geojson'
        column_names = ['province', 'data']
        plist = [1, 2, 3, 4, 5, 6, 7]
        data = np.column_stack((plist, data))
        df = pd.DataFrame(data, columns=column_names)
        # print(df)

        m = folium.Map(location=[28.3949, 84.1240], zoom_start=7)

        folium.Choropleth(
            geo_data=state_geo,
            name='choropleth',
            data=df,
            columns=['province', 'data'],
            key_on='properties.PROVINCE',
            fill_color='Reds',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='death (%)'
        ).add_to(m)

        folium.LayerControl().add_to(m)

        return m

    def map2(self):
        dataObj = pandemic.objects.values_list("infected")
        dataTuple = list(dataObj)
        data = []
        infected = 0
        for d in dataTuple:
            for x in d:
                data.append(x)

        for i in range(0, len(data)):
            data[i] = int(data[i])
            infected = infected + data[i]
        maps.total_infected = infected
        # print(data)

        state_geo = 'assets/nepal.geojson'
        column_names = ['province', 'data']
        plist = [1, 2, 3, 4, 5, 6, 7]
        data = np.column_stack((plist, data))
        df = pd.DataFrame(data, columns=column_names)
        # print(df)

        m = folium.Map(location=[28.3949, 84.1240], zoom_start=7)

        folium.Choropleth(
            geo_data=state_geo,
            name='choropleth',
            data=df,
            columns=['province', 'data'],
            key_on='properties.PROVINCE',
            fill_color='YlOrBr',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Infected (%)'
        ).add_to(m)

        folium.LayerControl().add_to(m)

        return m

    def map3(self):
        dataObj = pandemic.objects.values_list("recovered")
        dataTuple = list(dataObj)
        data = []
        recovered = 0
        for d in dataTuple:
            for x in d:
                data.append(x)

        for i in range(0, len(data)):
            data[i] = int(data[i])
            recovered = recovered + data[i]
        maps.total_recovered = recovered
        #print(data)
        #print(recovered)

        state_geo = 'assets/nepal.geojson'
        column_names = ['province', 'data']
        plist = [1, 2, 3, 4, 5, 6, 7]
        data = np.column_stack((plist, data))
        df = pd.DataFrame(data, columns=column_names)
        # print(total_recovered)

        m = folium.Map(location=[28.3949, 84.1240], zoom_start=7)

        folium.Choropleth(
            geo_data=state_geo,
            name='choropleth',
            data=df,
            columns=['province', 'data'],
            key_on='properties.PROVINCE',
            fill_color='BuGn',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='recovered (%)'
        ).add_to(m)

        folium.LayerControl().add_to(m)
        return m

    def bar(self):
        recovered = maps.total_recovered
        death = maps.total_death
        infected = maps.total_infected
        labels = ["total_death","total_infected","total_recovered"]
        values =[death,infected,recovered]
        colours = ['crimson','orange','green']

        layout = Layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)'
        )

        fig = go.Figure(data=go.Bar(x=labels,y=values,text=values,textposition='auto',marker_color=colours))
        fig.update_layout(layout)
        config = {
            'displayModeBar': False
        }

        graph = fig.to_html(full_html=False, default_height=500, default_width=850,config=config)


        return graph


