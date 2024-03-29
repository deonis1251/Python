# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.


def nb_year(p0, percent, aug, p):
    result = 0
    while p0 < p:
        p0 = p0 + int(p0 * (percent / 100)) + aug
        result += 1
    return result
    # your code

print(nb_year(1000, 2, 50, 1200))