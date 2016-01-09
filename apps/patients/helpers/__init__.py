import re


def get_patient_ids(params):
    re1 = '(patient)'  # Word 1
    re2 = '(.)'  # Any Single Character 1
    re3 = '(\\d+)'  # Integer Number 1

    rg = re.compile(re1+re2+re3,re.IGNORECASE | re.DOTALL)
    ids = []
    for param in params:
        m = rg.search(param)
        if m:
            ids.append(m.group(3))

    return ids
