import data_provider as prov
import logger as log 

def temperature_view(sensor):
    data = prov.get_temperature(sensor)
    log.temperature_logger(data)
    return data

def preassure_view(sensor):
    data = prov.get_preassure(sensor)
    log.preassure_logger(data)
    return data

def wind_spead_view(sensor):
    data = prov.get_wind_spead(sensor)
    log.wind_spead_logger(data)
    return data   