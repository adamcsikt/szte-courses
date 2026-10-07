# 🌳 Git Subtree – külső repository beemelése a sajátba

> Külső Git repository tartalmának beemelése a saját repositoryba `git subtree`-vel, majd későbbi frissítése és eltávolítása.

## 📑 Tartalom

1. [Mikor használjunk subtree-t?](#1-mikor-használjunk-git-subtree-t)
2. [Telepítés](#2-telepítés)
3. [Első beállítás lépésről lépésre](#3-első-beállítás-lépésről-lépésre)
4. [Frissítés](#4-frissítés)
5. [Alias a hosszú parancshoz](#5-alias-a-hosszú-parancshoz)
6. [Eltávolítás](#6-eltávolítás)
7. [Teljes példa](#7-teljes-példa)
8. [Cheat sheet](#8-cheat-sheet)
9. [Tipikus hibák](#9-tipikus-hibák)

---

## 1. Mikor használjunk `git subtree`-t?

Akkor hasznos, ha egy **másik repository tartalmát** a saját repositorynk egy alkönyvtárában szeretnénk tárolni.

```text
sajat-repo/
└── courses/
    └── targy/
        └── anyagok/     ← ez egy másik repositoryból származik
```

### ✅ Előnyök

- A fájlok **ténylegesen bekerülnek** a saját repositoryba.
- Klónozáskor a fájlok automatikusan elérhetők, nem kell külön `git clone`.
- A külső repositoryból később **frissíthető**.
- Nem kell `git submodule`.
- Az alkönyvtár a saját repóban **normál könyvtárként** jelenik meg.

### 🆚 Gyors összehasonlítás

| | `git subtree` | `git submodule` |
|---|---|---|
| Fájlok a saját repóban | ✅ igen | ❌ csak hivatkozás |
| Külön `clone` / `init` kell | ❌ nem | ✅ igen |
| Normál könyvtárként látszik | ✅ igen | ⚠️ nem igazán |
| Frissítés | `git subtree pull` | `git submodule update` |

---

## 2. Telepítés

Először nézzük meg, elérhető-e:

```bash
git subtree --version
```

Ha ezt kapod:

```text
git: 'subtree' is not a git command
```

akkor telepíteni kell:

| Disztró | Parancs |
|---|---|
| **Fedora** | `sudo dnf install git-subtree` |
| **Debian / Ubuntu** | `sudo apt install git-subtree` |

Telepítés után ellenőrzés:

```bash
git subtree --version
```

---

## 3. Első beállítás lépésről lépésre

### 3.1 Külső repo hozzáadása remote-ként

Lépj be a saját repository gyökerébe:

```bash
cd /path/to/sajat-repo
```

Add hozzá a külső repót remote-ként:

```bash
git remote add <remote-nev> <kulso-repo-url>
```

Például:

```bash
git remote add kulso-repo https://example.com/group/project.git
```

Ellenőrzés:

```bash
git remote -v
```

```text
kulso-repo  https://example.com/group/project.git (fetch)
kulso-repo  https://example.com/group/project.git (push)
origin      https://github.com/user/sajat-repo.git (fetch)
origin      https://github.com/user/sajat-repo.git (push)
```

> [!TIP]
> A remote neve tetszőleges: `kulso-repo`, `egyetemi`, `anyagok`, `orai-anyagok`, `upstream`...

### 3.2 Ha a külső repót már korábban clone-oltad

Ha már lefuttattad ezt:

```bash
git clone https://example.com/group/project.git
```

és a clone a saját repón **belül** van:

```text
sajat-repo/
└── courses/
    └── targy/
        └── anyagok/
            ├── .git/      ← ez a gond
            └── ...
```

akkor a subtree hozzáadása előtt **ideiglenesen nevezd át**:

```bash
mv courses/targy/anyagok courses/targy/anyagok-temp
```

> [!NOTE]
> A `-temp` könyvtárat még **ne töröld**, csak a subtree sikeres létrehozása után.

### 3.3 Tiszta working tree ellenőrzése

A subtree hozzáadásához **tiszta working tree** kell:

```bash
git status
```

Ha vannak saját módosításaid, három lehetőséged van:

| Mit szeretnél? | Parancs |
|---|---|
| Commitolni | `git add .` majd `git commit -m "Save current changes"` |
| Ideiglenesen félretenni | `git stash` |
| Egy módosítást eldobni | `git restore <fajl>` |

### 3.4 Subtree hozzáadása

Szintaxis:

```bash
git subtree add --prefix=<cel-konyvtar> <remote-nev> <branch> --squash
```

Példa:

```bash
git subtree add --prefix=courses/targy/anyagok kulso-repo main --squash
```

Siker esetén valami ilyesmit kapsz:

```text
Added dir 'courses/targy/anyagok'
```

<details>
<summary><b>🤔 Mit jelent a <code>--squash</code>?</b></summary>

<br>

A `--squash` miatt a külső repository **teljes commit history-ja nem kerül be** a saját repository történetébe. Csak a külső repo aktuális állapota kerül be egyetlen subtree commitként.

Általában akkor érdemes használni, ha a tartalom:

- egyetemi órai anyag,
- dokumentáció,
- jegyzet,
- vagy általában külső projekt tartalma.

</details>

### 3.5 Ideiglenes clone törlése

Ha a subtree sikeresen létrejött, a régi clone már nem kell:

```bash
rm -rf courses/targy/anyagok-temp
git status
```

### 3.6 Push

A subtree hozzáadása commitot hoz létre, ezt pusholni kell:

```bash
git push origin main
```

---

## 4. Frissítés

Ha a külső repóban új változások jelentek meg:

> [!WARNING]
> **Ne** használj sima `git pull`-t!
>
> ```bash
> git pull kulso-repo main    # ❌ NEM ajánlott
> ```

Helyette:

```bash
git subtree pull --prefix=courses/targy/anyagok kulso-repo main --squash
git push
```

Ez azt mondja a Gitnek:

> A `kulso-repo` `main` branchének új változásait integráld a saját repository `courses/targy/anyagok` könyvtárába.

### Miért nem jó a sima `git pull`?

A saját és a külső repository **külön Git historyval** rendelkezik. A sima `git pull` a két külön történetet próbálná normál módon összeilleszteni, ami ilyen hibához vezethet:

```text
hint: You have divergent branches and need to specify how to reconcile them.
```

A `git subtree pull` kifejezetten erre készült.

---

## 5. Alias a hosszú parancshoz

A `subtree pull` parancs hosszú, ezért érdemes aliast csinálni:

```bash
git config alias.update-materials 'subtree pull --prefix=courses/targy/anyagok kulso-repo main --squash'
```

> [!IMPORTANT]
> Az alias parancsában **nem kell `git`-tel kezdeni**.
>
> ```bash
> # ✅ Helyes
> git config alias.update-materials 'subtree pull --prefix=... '
>
> # ❌ Helytelen
> git config alias.update-materials 'git subtree pull ...'
> ```
>
> A helytelen változatból a Git ezt futtatná: `git git subtree pull ...`

### Használat

```bash
git update-materials
git push
```

### Alias ellenőrzése

```bash
git config alias.update-materials
```

Ennek ezt kell visszaadnia:

```text
subtree pull --prefix=courses/targy/anyagok kulso-repo main --squash
```

---

## 6. Eltávolítás

### 6.1 Subtree törlése a saját repóból

```bash
git rm -r courses/targy/anyagok
git commit -m "Remove external repository subtree"
git push
```

### 6.2 Remote eltávolítása

Ha a külső repót remote-ként sem szeretnéd megtartani:

```bash
git remote remove kulso-repo
git remote -v
```

> [!CAUTION]
> A `git remote remove` **csak a remote kapcsolatot** törli. A subtree fájljai a saját repóban **megmaradnak**!
> A fájlok törléséhez a 6.1 lépés (`git rm -r ...`) kell.

---

## 7. Teljes példa

**Adatok:**

| | Érték |
|---|---|
| Külső repo | `https://example.com/group/materials.git` |
| Remote neve | `materials` |
| Célmappa | `courses/example/materials` |

### ▶️ Első beállítás

```bash
git remote add materials https://example.com/group/materials.git
git subtree add --prefix=courses/example/materials materials main --squash
git push
```

### 🔄 Későbbi frissítés

```bash
git subtree pull --prefix=courses/example/materials materials main --squash
git push
```

### ⚡ Alias

```bash
git config alias.materials-update 'subtree pull --prefix=courses/example/materials materials main --squash'
```

Ezután elég ennyi:

```bash
git materials-update
git push
```

### 🗑️ Eltávolítás

```bash
git rm -r courses/example/materials
git commit -m "Remove materials subtree"
git push
git remote remove materials
```

---

## 8. Cheat sheet

| Feladat | Parancs |
|---|---|
| Telepítés (Fedora) | `sudo dnf install git-subtree` |
| Remote hozzáadása | `git remote add <remote> <url>` |
| Subtree létrehozása | `git subtree add --prefix=<cel> <remote> <branch> --squash` |
| Subtree frissítése | `git subtree pull --prefix=<cel> <remote> <branch> --squash` |
| Push | `git push` |
| Alias létrehozása | `git config alias.<nev> 'subtree pull --prefix=<cel> <remote> <branch> --squash'` |
| Alias használata | `git <nev>` majd `git push` |
| Subtree eltávolítása | `git rm -r <cel>` → `git commit -m "Remove external subtree"` → `git push` |
| Remote eltávolítása | `git remote remove <remote>` |

### 🧭 Teljes folyamat röviden

**Első alkalommal:**

```bash
sudo dnf install git-subtree                                   # ha még nincs
git remote add <remote> <url>
git subtree add --prefix=<cel> <remote> main --squash
git push
```

**Később:**

```bash
git subtree pull --prefix=<cel> <remote> main --squash
git push
```

**Ha már nem kell:**

```bash
git rm -r <cel>
git commit -m "Remove external subtree"
git push
git remote remove <remote>
```

---

## 9. Tipikus hibák

### ❌ `git: 'subtree' is not a git command`

Nincs telepítve. Fedorán:

```bash
sudo dnf install git-subtree
```

---

### ❌ `fatal: working tree has modifications`

A working tree nem tiszta. Nézd meg a `git status`-szal, majd:

```bash
git add .
git commit -m "Save changes"
```

vagy:

```bash
git stash
```

---

### ❌ `You have divergent branches`

Valószínűleg sima `git pull <remote> <branch>`-et használtál subtree esetén. Helyette:

```bash
git subtree pull --prefix=<cel> <remote> <branch> --squash
```

---

### ❌ `adding embedded git repository`

Egy másik Git repót próbáltál normál könyvtárként hozzáadni. Megoldás:

1. Vedd ki az embedded repót.
2. Az eredeti clone-t ideiglenesen nevezd át vagy told el.
3. Használd:

```bash
git subtree add --prefix=<cel> <remote> <branch> --squash
```
