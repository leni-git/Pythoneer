def typeDICT(*, file_name):
    # Dict type config file load
    import json

    with open(file_name, "rt") as f:
        config = json.load(f)
    return config


def typeYAML(*, file_name):
    # YAML type config file load
    import yaml

    with open(file_name, "rt") as f:
        config = yaml.load(f.read())
    return config
