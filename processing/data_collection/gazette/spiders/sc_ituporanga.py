from gazette.spiders.base import FecamGazetteSpider


class ScItuporangaSpider(FecamGazetteSpider):
    name = "sc_ituporanga"
    FECAM_QUERY = "cod_entidade:134"
    TERRITORY_ID = "4208500"
