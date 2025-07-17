def model_to_dict(obj):
    data = obj.__dict__.copy()
    data.pop("_sa_instance_state", None)
    return data