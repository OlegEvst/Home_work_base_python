from user_interface import temperature_view, preassure_view, wind_spead_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body> \n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Spead_wind: {} m</p>\n'\
        .format(style, wind_spead_view(device))
    html += '   <p {}>Preassure: {} mmHg</p>\n'\
        .format(style, preassure_view(device))
    html += '   </body>\n</html >'

    with open('index.html', 'w') as page:
        page.write(html)

    return html

def new_create(data, device = 1):
    t,p,w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body> \n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '   <p {}>Spead_wind: {} m</p>\n'\
        .format(style, w)
    html += '   <p {}>Preassure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   </body>\n</html >'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data
