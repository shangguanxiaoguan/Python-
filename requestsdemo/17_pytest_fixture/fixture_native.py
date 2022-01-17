def first_var():
    return ["a"]


def test_case02(var):
    var.append("b")
    print(var)


var_temp = first_var()
test_case02(var_temp)
