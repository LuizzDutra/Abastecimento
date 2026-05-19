
def is_valid_cpf(cpf: str) -> bool:
    if len(cpf) != 11:
        return False
    for c in cpf:
        if not c.isdigit():
            return False
    if not check_cpf_validity(cpf):
        return False
    return True


def check_cpf_validity(cpf: str) -> bool:
    # Assume que a formatação foi checkada

    # Checa por números repetidos
    is_repeating = True
    for i in range(1, len(cpf)):
        if cpf[i] != cpf[i - 1]:
            is_repeating = False
    if is_repeating:
        return False

    # Primeira soma do algoritmo
    s = 0
    c = 10
    for i in range(9):
        s += int(cpf[i]) * c
        c -= 1
    s *= 10

    first_digit = s % 11
    # Regra de verificação do dígito
    if first_digit == 10:
        first_digit = 0
    if cpf[-2] != str(first_digit):
        return False

    # Segunda soma
    s = 0
    c = 11
    for i in range(9):
        s += int(cpf[i]) * c
        c -= 1
    s += first_digit * c
    s *= 10

    second_digit = s % 11
    if second_digit == 10:
        second_digit = 0

    if cpf[-1] != str(second_digit):
        return False

    return True


def validate(cpf: str) -> str:
    if not is_valid_cpf(cpf):
        raise ValueError("Invalid CPF")
    return cpf


