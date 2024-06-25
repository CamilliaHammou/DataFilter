

class DataSorter:
    @staticmethod
    def sort_data(data_filter, field: str, reverse: bool = False):
        data_filter.data.sort(key=lambda x: x[field], reverse=reverse)
