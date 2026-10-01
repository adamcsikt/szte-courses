# AI: Claude (claude.ai), 2026.05.03, cél: pytest tesztesetek generálása a tippbevitel feature-höz
# prompt: "write tests for the step-by-step guess input feature"
import pytest
import szinozon


# ── Segédfüggvény: több input szimulálása ─────────────────────────────────────
def make_inputs(*values):
    """Iterátor, ami sorban adja vissza az értékeket – input() helyettesítésére."""
    return iter(values)


# ── get_guess() tesztek ───────────────────────────────────────────────────────
def test_get_guess_returns_correct_guess_on_valid_sequential_input(monkeypatch):
    """
    Ha a felhasználó egymás után megadja a CODE_LENGTH színt,
    majd 'rendben'-t ír, get_guess() a helyes listát adja vissza.
    """
    inputs = make_inputs("r", "g", "b", "y", "rendben")
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    result = szinozon.get_guess(1, [])
    assert result == ["R", "G", "B", "Y"]


def test_get_guess_megse_removes_last_color(monkeypatch):
    """
    'megse' hatására az utoljára hozzáadott szín törlődik.
    Pl.: R → G → megse → B → Y → rendben  ⟹  [R, B, Y, ?]
    (CODE_LENGTH == 4 esetén még egy szín kell, itt M-mel egészítjük ki.)
    """
    inputs = make_inputs("r", "g", "megse", "b", "y", "m", "rendben")
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    result = szinozon.get_guess(1, [])
    assert result == ["R", "B", "Y", "M"]


def test_get_guess_rendben_before_full_guess_is_ignored(monkeypatch, capsys):
    """
    Ha 'rendben'-t írnak be a tipp kitöltése előtt,
    a játék Tessék?-kel reagál, és folytatja a bekérést.
    """
    inputs = make_inputs("rendben", "r", "g", "b", "y", "rendben")
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    result = szinozon.get_guess(1, [])
    captured = capsys.readouterr()
    assert "Tessék?" in captured.out
    assert result == ["R", "G", "B", "Y"]


def test_get_guess_extra_color_after_full_guess_is_ignored(monkeypatch, capsys):
    """
    Ha már CODE_LENGTH szín van megadva és a felhasználó még egyet próbál
    hozzáadni, a játék 'Nincs több'-bel reagál, és a tipp nem változik.
    """
    inputs = make_inputs("r", "g", "b", "y", "r", "rendben")
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    result = szinozon.get_guess(1, [])
    captured = capsys.readouterr()
    assert "Nincs több" in captured.out
    assert result == ["R", "G", "B", "Y"]


def test_get_guess_invalid_input_prints_tessek(monkeypatch, capsys):
    """
    Érvénytelen bemenet (pl. 'X', 'alma') esetén a játék 'Tessék?'-et ír ki,
    és nem adja hozzá az érvénytelen értéket a tipphez.
    """
    inputs = make_inputs("x", "alma", "r", "g", "b", "y", "rendben")
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    result = szinozon.get_guess(1, [])
    captured = capsys.readouterr()
    assert captured.out.count("Tessék?") >= 2
    assert result == ["R", "G", "B", "Y"]


def test_get_guess_megse_on_empty_guess_restarts_prompt(monkeypatch, capsys):
    """
    Ha még nincs megadott szín és a felhasználó 'megse'-t ír,
    a tipp bevitele újraindul (a prompt újra megjelenik),
    és a current_guess üres marad egészen az első érvényes színig.
    """
    inputs = make_inputs("megse", "r", "g", "b", "y", "rendben")
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    result = szinozon.get_guess(1, [])
    assert result == ["R", "G", "B", "Y"]


# ── evaluate_guess() tesztek ─────────────────────────────────────────────────
def test_evaluate_guess_all_exact():
    """
    Ha a tipp pontosan megegyezik a titkos kóddal,
    exact == CODE_LENGTH és misplaced == 0.
    """
    secret = ["R", "G", "B", "Y"]
    guess = ["R", "G", "B", "Y"]
    exact, misplaced = szinozon.evaluate_guess(secret, guess)
    assert exact == 4
    assert misplaced == 0


def test_evaluate_guess_all_misplaced():
    """
    Ha az összes szín helyes, de minden rossz pozícióban van.
    """
    secret = ["R", "G", "B", "Y"]
    guess = ["Y", "B", "G", "R"]
    exact, misplaced = szinozon.evaluate_guess(secret, guess)
    assert exact == 0
    assert misplaced == 4


def test_evaluate_guess_no_match():
    """
    Ha a tippben egyetlen helyes szín sem szerepel.
    """
    secret = ["R", "G", "B", "Y"]
    guess = ["M", "M", "C", "C"]
    exact, misplaced = szinozon.evaluate_guess(secret, guess)
    assert exact == 0
    assert misplaced == 0


def test_evaluate_guess_mixed_result():
    """
    Vegyes eset: 1 pontos találat, 1 rossz helyen lévő szín.
    """
    secret = ["R", "G", "B", "Y"]
    guess = ["R", "B", "M", "M"]
    exact, misplaced = szinozon.evaluate_guess(secret, guess)
    assert exact == 1
    assert misplaced == 1


def test_evaluate_guess_duplicate_color_in_guess_not_overcounted():
    """
    Ha a tippben ismétlődő szín van, de a titkos kódban csak egyszer szerepel,
    a misplaced/exact együtt sem haladhatja meg a titkos kódban lévő előfordulások számát.
    """
    secret = ["R", "G", "B", "Y"]
    guess = ["R", "R", "R", "R"]
    exact, misplaced = szinozon.evaluate_guess(secret, guess)
    assert exact == 1
    assert misplaced == 0
    assert exact + misplaced == 1
