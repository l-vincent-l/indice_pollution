from importlib import import_module
from itertools import chain

regions = [
    'auvergne-rhone-alpes',
    'bretagne',
    'corse',
    'pays_de_la_loire',
    'centre_val_de_loire',
    'nouvelle_aquitaine',
    'haut_de_france',
    'grand-est',
    'occitanie'
]

def epci_list():
    return list(chain(*[
        import_module(f'.{region_name}', 'indice_pollution.regions').Forecast.epci_list
        for region_name in regions
    ]))

def insee_list():
    return list(chain(*[
        import_module(f'.{region_name}', 'indice_pollution.regions').Forecast.insee_list()
        for region_name in regions
    ]))

def forecast(epci=None, insee=None):
    for region_name in regions:
        region = import_module(f'.{region_name}', 'indice_pollution.regions').Forecast
        if epci in region.epci_list or insee in region.insee_list():
            return region.get
    raise KeyError("Unable to find epci")