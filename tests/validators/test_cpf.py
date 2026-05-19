import pytest

from app.core.validators.cpf import validate


def test_cpf_validator():
    test_cpf_good = ["52998224725"]
    test_cpf_bad = [
        "12345678900",
        "12345678900123123123",
        "123456",
        "12345699900",
        "11111111111",
        "22222222222",
        "",
        "aaaaaaaaaaa"
    ]

    for cpf in test_cpf_good:
        assert validate(cpf)

    with pytest.raises(ValueError):
        for cpf in test_cpf_bad:
            assert validate(cpf)
