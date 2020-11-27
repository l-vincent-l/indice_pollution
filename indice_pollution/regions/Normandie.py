from . import ForecastMixin, EpisodeMixin
from dateutil.parser import parse
from json.decoder import JSONDecodeError
import orjson as json
from itertools import takewhile
from string import printable

class Service(object):
    website = 'http://www.atmonormandie.fr/'
    attributes_key = 'properties'
    use_dateutil_parser = True

    insee_list = ['76351', '14366', '76540', '14118', '50502', '27229', '50129', '61001']

class Forecast(Service, ForecastMixin):
    url = 'https://dservices7.arcgis.com/FPRT1cIkPKcq73uN/arcgis/services/ind_normandie_agglo/WFSServer?service=wfs&request=getcapabilities'

    @classmethod
    def params(cls, date_, insee):
        filter_zone = f'<PropertyIsEqualTo><PropertyName>code_zone</PropertyName><Literal>{insee}</Literal></PropertyIsEqualTo>'
        filter_date = f'<PropertyIsGreaterThanOrEqualTo><PropertyName>date_ech</PropertyName><Literal>{date_}T00:00:00.000Z</Literal></PropertyIsGreaterThanOrEqualTo>'
        return {
            'service': 'wfs',
            'request': 'getfeature',
            'typeName': f'ind_normandie_agglo:ind_normandie_agglo',
            'Filter': f"<Filter><And>{filter_zone}{filter_date}</And></Filter>",
            'outputFormat': 'geojson',
        }

    @classmethod
    def features(cls, r):
        r.encoding = 'utf8'
        try:
            return r.json()['features']
        except JSONDecodeError:
            set_printable = set(printable + 'éèàçôêùà')
            clean_string = str("".join(takewhile(lambda c: c in set_printable, r.text)))
            return json.loads(clean_string)['features']


class Episode(Service, EpisodeMixin):
    url = 'https://dservices7.arcgis.com/FPRT1cIkPKcq73uN/arcgis/services/alrt3j_normandie/WFSServer'

    def params(self, date_, insee):
        centre = self.centre(insee)

        return {
            'where': '',
            'outfields': self.outfields,
            'geometry': f'{centre[0]},{centre[1]}',
            'inSR': '4326',
            'outSR': '4326',
            'geometryType': 'esriGeometryPoint',
            'request': 'GetFeature',
            'typeName': 'alrt3j_normandie:alrt3j_normandie',
            'service': 'WFS',
            'outputFormat': 'GEOJSON'
        }