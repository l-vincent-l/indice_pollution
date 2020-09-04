from . import ForecastMixin
from datetime import datetime, timedelta
from dateutil.parser import parse

class Forecast(ForecastMixin):
    website = 'http://www.ligair.fr/'
    url = 'https://services1.arcgis.com/HzzPcgRsxxyIZdlU/arcgis/rest/services/ind_centre_val_de_loire_agglo_1/FeatureServer/0/query'

    @classmethod
    def params(cls, date_, insee):
        epci = cls.insee_epci[insee]

        day_after = str(parse(date_).date() + timedelta(days=1))
        return {
            'outFields': ",".join(cls.outfields),
            'where': f"(code_zone={epci}) AND (date_ech >= DATE '{date_}')",
            'outSR': 4326,
            'f': 'json'
        }

    @classmethod
    def insee_list(cls):
        return cls.insee_epci.keys()

    insee_epci = {
        "18033": "241800507",
        "18205": "241800507",
        "18141": "241800507",
        "18213": "241800507",
        "18267": "241800507",
        "18050": "241800507",
        "18180": "241800507",
        "18138": "241800507",
        "18028": "241800507",
        "18255": "241800507",
        "18157": "241800507",
        "18218": "241800507",
        "18008": "241800507",
        "18226": "241800507",
        "18288": "241800507",
        "18006": "241800507",
        "18129": "241800507",
        "36044": "243600327",
        "36063": "243600327",
        "36159": "243600327",
        "36005": "243600327",
        "36202": "243600327",
        "36128": "243600327",
        "36101": "243600327",
        "36009": "243600327",
        "36071": "243600327",
        "36057": "243600327",
        "36064": "243600327",
        "36112": "243600327",
        "36211": "243600327",
        "36089": "243600327",
        "28134": "200040277",
        "28404": "200040277",
        "28348": "200040277",
        "28359": "200040277",
        "27230": "200040277",
        "28007": "200040277",
        "27355": "200040277",
        "28089": "200040277",
        "28001": "200040277",
        "27438": "200040277",
        "28393": "200040277",
        "28064": "200040277",
        "28098": "200040277",
        "28059": "200040277",
        "28377": "200040277",
        "28415": "200040277",
        "28223": "200040277",
        "28394": "200040277",
        "28386": "200040277",
        "28293": "200040277",
        "27378": "200040277",
        "28096": "200040277",
        "28405": "200040277",
        "28332": "200040277",
        "28251": "200040277",
        "28371": "200040277",
        "28239": "200040277",
        "28226": "200040277",
        "28360": "200040277",
        "27543": "200040277",
        "28062": "200040277",
        "28171": "200040277",
        "28036": "200040277",
        "28321": "200040277",
        "28124": "200040277",
        "28292": "200040277",
        "28206": "200040277",
        "28369": "200040277",
        "28187": "200040277",
        "28014": "200040277",
        "28082": "200040277",
        "28147": "200040277",
        "28247": "200040277",
        "28055": "200040277",
        "28374": "200040277",
        "28180": "200040277",
        "28322": "200040277",
        "28267": "200040277",
        "28054": "200040277",
        "28120": "200040277",
        "28351": "200040277",
        "28375": "200040277",
        "28037": "200040277",
        "28235": "200040277",
        "28355": "200040277",
        "28323": "200040277",
        "28178": "200040277",
        "28030": "200040277",
        "28170": "200040277",
        "28053": "200040277",
        "28050": "200040277",
        "28117": "200040277",
        "28308": "200040277",
        "28143": "200040277",
        "28289": "200040277",
        "28087": "200040277",
        "28341": "200040277",
        "27376": "200040277",
        "28155": "200040277",
        "28045": "200040277",
        "28076": "200040277",
        "28216": "200040277",
        "28008": "200040277",
        "28231": "200040277",
        "28151": "200040277",
        "28136": "200040277",
        "28003": "200040277",
        "28312": "200040277",
        "28090": "200040277",
        "28346": "200040277",
        "28315": "200040277",
        "45208": "244500203",
        "45004": "244500203",
        "45068": "244500203",
        "45338": "244500203",
        "45247": "244500203",
        "45104": "244500203",
        "45061": "244500203",
        "45092": "244500203",
        "45293": "244500203",
        "45345": "244500203",
        "45249": "244500203",
        "45312": "244500203",
        "45102": "244500203",
        "45185": "244500203",
        "45216": "244500203",
        "37261": "243700754",
        "37122": "243700754",
        "37233": "243700754",
        "37214": "243700754",
        "37208": "243700754",
        "37050": "243700754",
        "37109": "243700754",
        "37195": "243700754",
        "37018": "243700754",
        "37139": "243700754",
        "37172": "243700754",
        "37054": "243700754",
        "37151": "243700754",
        "37203": "243700754",
        "37243": "243700754",
        "37179": "243700754",
        "37152": "243700754",
        "37217": "243700754",
        "37272": "243700754",
        "37219": "243700754",
        "37099": "243700754",
        "37025": "243700754",
        "28085": "200033181",
        "28218": "200033181",
        "28229": "200033181",
        "28220": "200033181",
        "28209": "200033181",
        "28227": "200033181",
        "28110": "200033181",
        "28070": "200033181",
        "28337": "200033181",
        "28380": "200033181",
        "28358": "200033181",
        "28201": "200033181",
        "28006": "200033181",
        "28024": "200033181",
        "28269": "200033181",
        "28122": "200033181",
        "28278": "200033181",
        "28173": "200033181",
        "28022": "200033181",
        "28253": "200033181",
        "28388": "200033181",
        "28309": "200033181",
        "28035": "200033181",
        "28325": "200033181",
        "28158": "200033181",
        "28104": "200033181",
        "28160": "200033181",
        "28034": "200033181",
        "28403": "200033181",
        "28254": "200033181",
        "28052": "200033181",
        "28195": "200033181",
        "28129": "200033181",
        "28084": "200033181",
        "28048": "200033181",
        "28383": "200033181",
        "28047": "200033181",
        "28102": "200033181",
        "28177": "200033181",
        "28286": "200033181",
        "28317": "200033181",
        "28246": "200033181",
        "28281": "200033181",
        "28194": "200033181",
        "28068": "200033181",
        "28301": "200033181",
        "28128": "200033181",
        "28100": "200033181",
        "28365": "200033181",
        "28397": "200033181",
        "28107": "200033181",
        "28419": "200033181",
        "28285": "200033181",
        "28245": "200033181",
        "28162": "200033181",
        "28141": "200033181",
        "28073": "200033181",
        "28366": "200033181",
        "28004": "200033181",
        "28421": "200033181",
        "28095": "200033181",
        "28344": "200033181",
        "28049": "200033181",
        "28060": "200033181",
        "28163": "200033181",
        "28255": "200033181",
        "45234": "244500468",
        "45232": "244500468",
        "45147": "244500468",
        "45284": "244500468",
        "45302": "244500468",
        "45285": "244500468",
        "45075": "244500468",
        "45169": "244500468",
        "45089": "244500468",
        "45286": "244500468",
        "45274": "244500468",
        "45298": "244500468",
        "45235": "244500468",
        "45272": "244500468",
        "45308": "244500468",
        "45282": "244500468",
        "45194": "244500468",
        "45034": "244500468",
        "45197": "244500468",
        "45072": "244500468",
        "45043": "244500468",
        "45100": "244500468",
        "41018": "200030385",
        "41295": "200030385",
        "41047": "200030385",
        "41167": "200030385",
        "41212": "200030385",
        "41067": "200030385",
        "41032": "200030385",
        "41031": "200030385",
        "41055": "200030385",
        "41276": "200030385",
        "41142": "200030385",
        "41147": "200030385",
        "41230": "200030385",
        "41061": "200030385",
        "41029": "200030385",
        "41091": "200030385",
        "41101": "200030385",
        "41045": "200030385",
        "41052": "200030385",
        "41050": "200030385",
        "41233": "200030385",
        "41206": "200030385",
        "41145": "200030385",
        "41288": "200030385",
        "41144": "200030385",
        "41040": "200030385",
        "41109": "200030385",
        "41128": "200030385",
        "41223": "200030385",
        "41009": "200030385",
        "41134": "200030385",
        "41035": "200030385",
        "41137": "200030385",
        "41203": "200030385",
        "41246": "200030385",
        "41189": "200030385",
        "41281": "200030385",
        "41234": "200030385",
        "41093": "200030385",
        "41205": "200030385",
        "41108": "200030385",
        "41208": "200030385",
        "41266": "200030385",
    }
