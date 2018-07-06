# string_helper.py


def extract_0x_6_4(in_str, case=None):
    out_str = ''

    if in_str is not None:
        out_str = '0x{0}***{1}'.format(in_str[2:8], in_str[-4:])

    if case is not None:
        if case.lower() == 'lower':
            out_str = out_str.lower()
        elif case.lower() == 'upper':
            out_str = out_str.upper()
        else:
            out_str = out_str

    return out_str
