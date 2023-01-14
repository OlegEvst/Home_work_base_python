from user_interface import temperature_view, preassure_view,wind_spead_view

def create(device = 1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_spead_view units = "c">{}</temperature>\n'\
        .format(wind_spead_view(device))
    xml += '    < preassure units = "c">{}</temperature>\n'\
        .format( preassure_view(device))
    
    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml

def new_create(data, device = 1):
    t,p,w = data
    t = t *1.8 + 32
    xml = '<xml>\n'
    xml += '    <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '    <wind_spead_view units = "m/s">{}</temperature>\n'\
        .format(w)
    xml += '    < preassure units = "c">{}</temperature>\n'\
        .format(p)
    
    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data