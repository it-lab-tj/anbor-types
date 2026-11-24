from anbor_types import ListQuery
from src.app.shared_kernel.types.base_types import ID_T


class CityListQuery(ListQuery):
    country_id: ID_T
