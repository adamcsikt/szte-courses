# AI: Claude (claude.ai), 2026.05.03, cél: pytest tesztesetek generálása a Mentés/Betöltés feature-höz
# prompt: "write tests for the save/load feature"

import json
import os

import pytest
import szinozon


# ── Segéd fixture: ideiglenesen átírja a SAVE_FILE útvonalát ─────────────────
@pytest.fixture(autouse=True)
def isolated_save_file(monkeypatch, tmp_path):
    """
    Minden teszt saját tmp könyvtárban dolgozik,
    hogy ne szennyezzék egymást és a valódi mentésfájlt.
    """
    tmp_save = str(tmp_path / "test_szinozon_save.json")
    monkeypatch.setattr(szinozon, "SAVE_FILE", tmp_save)
    yield tmp_save


# ── load_game() tesztek ───────────────────────────────────────────────────────
def test_load_game_returns_none_when_no_save_file_exists():
    """
    Ha nincs mentésfájl, a load_game() None-t kell visszaadjon,
    és nem szabad kivételt dobnia.
    """
    assert not os.path.exists(szinozon.SAVE_FILE), "A fájlnak nem kellene létezni"
    result = szinozon.load_game()
    assert result is None


def test_load_game_returns_correct_data_from_valid_save(isolated_save_file):
    """
    Érvényes mentésfájl esetén load_game() helyesen rekonstruálja
    a titkos kódot, a history-t, a kísérletszámot és a folyamatban lévő tippet.
    """
    save_data = {
        "secret": ["R", "G", "B", "Y"],
        "history": [[["R", "G", "B", "Y"], 2, 1]],
        "attempt": 3,
        "current_guess": ["R", "G"],
    }
    with open(isolated_save_file, "w", encoding="utf-8") as f:
        json.dump(save_data, f)

    result = szinozon.load_game()

    assert result is not None
    secret, history, attempt, current_guess = result
    assert secret == ["R", "G", "B", "Y"]
    assert len(history) == 1
    assert history[0] == (["R", "G", "B", "Y"], 2, 1)
    assert attempt == 3
    assert current_guess == ["R", "G"]


def test_load_game_returns_none_on_corrupt_save_file(isolated_save_file):
    """
    Sérült / érvénytelen JSON tartalmú mentésfájl esetén
    load_game() None-t kell visszaadjon, nem szabad crashelnie.
    """
    with open(isolated_save_file, "w", encoding="utf-8") as f:
        f.write("{ ez nem valid json @@@ ")

    result = szinozon.load_game()
    assert result is None


def test_load_game_handles_missing_current_guess_key(isolated_save_file):
    """
    Ha a mentésfájlból hiányzik a 'current_guess' kulcs (régebbi mentés),
    load_game() üres listát adjon vissza helyette, ne dobjon kivételt.
    """
    save_data = {
        "secret": ["M", "C"],
        "history": [],
        "attempt": 1,
    }
    with open(isolated_save_file, "w", encoding="utf-8") as f:
        json.dump(save_data, f)

    result = szinozon.load_game()
    assert result is not None
    _, _, _, current_guess = result
    assert current_guess == []


# ── save_game() tesztek ───────────────────────────────────────────────────────
def test_save_game_creates_file_with_correct_content(monkeypatch, isolated_save_file):
    """
    Ha a felhasználó 'y'-t ad meg, save_game() létrehozza a fájlt,
    és abba a helyes adatokat írja bele.
    """
    monkeypatch.setattr("builtins.input", lambda _prompt: "y")

    secret = ["R", "G", "B", "Y"]
    history = [(["R", "G", "B", "Y"], 2, 1)]
    attempt = 3
    current_guess = ["R"]

    szinozon.save_game(secret, history, attempt, current_guess)

    assert os.path.exists(isolated_save_file)
    with open(isolated_save_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["secret"] == secret
    assert data["attempt"] == attempt
    assert data["current_guess"] == current_guess
    assert len(data["history"]) == 1


def test_save_game_does_not_create_file_when_user_declines(
    monkeypatch, isolated_save_file
):
    """
    Ha a felhasználó 'n'-t válaszol a mentés kérdésére,
    a fájl nem jön létre.
    """
    monkeypatch.setattr("builtins.input", lambda _prompt: "n")

    szinozon.save_game(["R", "G", "B", "Y"], [], 1, [])

    assert not os.path.exists(isolated_save_file)


# ── delete_save() tesztek ─────────────────────────────────────────────────────
def test_delete_save_removes_existing_file(isolated_save_file):
    """
    Ha a mentésfájl létezik, delete_save() törli azt.
    """
    with open(isolated_save_file, "w") as f:
        f.write("{}")

    assert os.path.exists(isolated_save_file)
    szinozon.delete_save()
    assert not os.path.exists(isolated_save_file)


def test_delete_save_does_not_raise_when_file_missing():
    """
    Ha a mentésfájl nem létezik, delete_save() nem dob kivételt.
    """
    assert not os.path.exists(szinozon.SAVE_FILE)
    szinozon.delete_save()  # nem kell kivétel
