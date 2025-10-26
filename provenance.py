# provenance.py
def make_provenance(dataset_name, resource_url, filters):
    return {
        "dataset": dataset_name,
        "resource": resource_url,
        "filters": filters
    }
