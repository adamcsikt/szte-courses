import pytest
from mukincs import mukincsek_atpakolasa, sikeres_betores

# ===========================================================================
# sikeres_betores() tesztek
# ===========================================================================


def test_settenkedő_1_hus_2_orkutya():
    """1 hús, 2 őrkutya – a második kutyához nincs hús, visszatér False."""
    eredmeny = sikeres_betores("settenkedő", ["hús"], ["őrkutya", "őrkutya"])
    assert eredmeny == False


def test_settenkedő_2_hus_1_orkutya_1_or():
    """2 hús, 1 őrkutya + 1 őr – settenkedőnek az őr nem akadály, 1 hús elég."""
    eredmeny = sikeres_betores("settenkedő", ["hús", "hús"], ["őrkutya", "őr"])
    assert eredmeny == True


def test_akrobata_2_hus_2_spray_1_orkutya_2_lezer():
    """Akrobata, 2 hús + 2 spray, 1 őrkutya + 2 lézer – akrobatának nincs szükség hacker eszközre."""
    eredmeny = sikeres_betores(
        "akrobata", ["hús", "hús", "spray", "spray"], ["őrkutya", "lézer", "lézer"]
    )
    assert eredmeny == True


def test_settenkedő_2_hus_2_spray_1_orkutya_2_lezer():
    """Settenkedő, 2 hús + 2 spray, 1 őrkutya + 2 lézer – lézerhez hacker eszköz is kell, nincs, False."""
    eredmeny = sikeres_betores(
        "settenkedő", ["hús", "hús", "spray", "spray"], ["őrkutya", "lézer", "lézer"]
    )
    assert eredmeny == False


# ===========================================================================
# mukincsek_atpakolasa() tesztek
# ===========================================================================


def test_alap_eset_queen_diadem():
    """Csak a Queen Diadem (1300) esik az 1000–1400 sávba."""
    eredmeny = mukincsek_atpakolasa(
        ["Old Painting", "Faberget Egg", "Queen Diadem", "Old Pot"], []
    )
    assert eredmeny == ["Queen Diadem"]


def test_nincs_erteke_ures_taska():
    """Egyik tárgy sem éri el az 1000-et, a táska üres marad."""
    eredmeny = mukincsek_atpakolasa(["Old Painting", "Faberget Egg", "Old Pot"], [])
    assert eredmeny == []


def test_mar_teli_taska_bovul():
    """A táskában már van 'Old Pot', mellé kerül a Queen Diadem."""
    eredmeny = mukincsek_atpakolasa(
        ["Old Painting", "Faberget Egg", "Queen Diadem", "Old Pot"], ["Old Pot"]
    )
    assert eredmeny == ["Old Pot", "Queen Diadem"]


def test_mona_lisa_tul_ertékes():
    """Mona Lisa (1500) meghaladja az 1400-as határt, csak Queen Diadem kerül a táskába."""
    eredmeny = mukincsek_atpakolasa(
        ["Painting: Mona Lisa", "Faberget Egg", "Queen Diadem"], []
    )
    assert eredmeny == ["Queen Diadem"]


def test_csak_queen_diadem_a_muzeumban():
    """Egyetlen értékes tárgy a múzeumban, az kerül a táskába."""
    eredmeny = mukincsek_atpakolasa(["Queen Diadem", "Old Pot"], [])
    assert eredmeny == ["Queen Diadem"]
