from gazette.spiders.base import FecamGazetteSpider


class ScArvoredoSpider(FecamGazetteSpider):
    name = "sc_arvoredo"
    FECAM_QUERY = "cod_entidade:25"
    TERRITORY_ID = "4201653"
