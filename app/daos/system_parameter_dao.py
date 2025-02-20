from ..models.system_parameter_model import SystemParameterModel


class SystemParameterDao():
    def get_time_limit(self, level):
        time_limit = SystemParameterModel.query.filter_by(
            key=f"level_{level}_time_limit").first()

        return time_limit

    def get_quantity_limit(self, level):
        quantity_limit = SystemParameterModel.query.filter_by(
            key=f"level_{level}_quantity_limit").first()

        return quantity_limit
