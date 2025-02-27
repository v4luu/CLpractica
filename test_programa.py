from programa import es_primo

def test_es_primo():
    assert es_primo(5) is True
    assert es_primo(6) is False
    assert es_primo(8) is False
    assert es_primo(5) is True
    