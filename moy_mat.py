
def saisir():
    ds = float(input("note DS:\n"))
    exam = float(input("note EXAM:\n"))
    return ds, exam

def moy_mat(ds, exam):
    return ds * 0.3 + exam * 0.7