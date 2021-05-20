def remove_characters(strings):
    strings = strings.replace("_", " ").replace("-", " ").replace("?", "").replace(":", " ")\
    .replace("(", " ").replace(")", " ").replace("/", " ").replace(".", " ").replace("\t", "")

    return strings