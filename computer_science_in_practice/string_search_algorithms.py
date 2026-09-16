def Naiv_search():
    text = "aaaabbaaababbabbbaaababbbbbaaabab"
    pattern = "aaabab"

    def find_pattern(text, pattern):
        for start in range(len(text) - len(pattern) + 1):
            match = True

            for offset in range(len(pattern)):
                if text[start + offset] != pattern[offset]:
                    match = False
                    break

            if match:
                return start

        return -1


    print(find_pattern(text, pattern)) 

def Rabin_karp():

    text = "ABCDEF"
    pattern = "CDE"

    pattern_length = len(pattern)
    text_length = len(text)

    if pattern_length > text_length:
        return -1

    pattern_hash = hash(pattern)

    for start in range(text_length - pattern_length + 1):
        window = text[start:start + pattern_length]
        window_hash = hash(window)

        if window_hash == pattern_hash:
            if window == pattern:
                return start

    return -1

def rabin_karp(text, pattern):
    # A teljes szöveg hossza.
    n = len(text)

    # A keresett pattern hossza.
    m = len(pattern)

    # Az üres string minden szöveg elején megtalálható,
    # ezért a kezdőindexe 0.
    if m == 0:
        return 0

    # Ha a pattern hosszabb, mint a text,
    # akkor biztosan nem lehet benne.
    if m > n:
        return -1

    # A hash számítás számrendszerének alapja.
    # A 256 használható, mert egy byte 256 különböző
    # értéket tud felvenni.
    base = 256

    # A hashértékeket ezzel a prímszámmal tartjuk
    # viszonylag kis tartományban.
    prime = 101

    # Ebben tároljuk majd a teljes pattern hashértékét.
    pattern_hash = 0

    # Ebben tároljuk a text aktuális ablakának hashértékét.
    window_hash = 0

    # Ez a bal szélső karakter helyi értéke.
    #
    # Ha a pattern hossza 3, akkor:
    # base ** (3 - 1) = base ** 2
    #
    # A pow harmadik argumentuma miatt rögtön
    # modulo prime értéket számítunk.
    highest_place = pow(base, m - 1, prime)

    # Kiszámoljuk:
    # 1. a pattern hashét,
    # 2. a text első, pattern hosszúságú ablakának hashét.
    for index in range(m):
        # Hozzáadjuk a pattern következő karakterét
        # a pattern hashértékéhez.
        #
        # ord() a karakterből számot készít:
        # ord("A") == 65
        pattern_hash = (
            pattern_hash * base
            + ord(pattern[index])
        ) % prime

        # Ugyanezt megcsináljuk a text első ablakával.
        window_hash = (
            window_hash * base
            + ord(text[index])
        ) % prime

    # Végigmegyünk a text minden lehetséges
    # kezdőpozícióján.
    for start in range(n - m + 1):

        # Ha a pattern és az aktuális ablak hashértéke azonos,
        # akkor lehetséges, hogy megtaláltuk a patternt.
        if window_hash == pattern_hash:

            # Azonos hash nem garantálja azonos stringet,
            # ezért karakterenként is ellenőrizzük.
            if text[start:start + m] == pattern:

                # Visszaadjuk a találat kezdőindexét.
                return start

        # Csak akkor készítünk következő ablakot,
        # ha van még következő ablak.
        if start < n - m:

            # Ez a karakter fog kiesni az ablak bal oldaláról.
            outgoing_character = ord(text[start])

            # Ez a karakter fog belépni az ablak jobb oldalán.
            incoming_character = ord(text[start + m])

            # Kiszámoljuk a következő ablak hashértékét
            # az előző hashből.
            window_hash = (
                # Eltávolítjuk a kieső karakter hozzájárulását.
                (
                    window_hash
                    - outgoing_character * highest_place
                )

                # A megmaradt karaktereket eggyel
                # magasabb helyi értékre toljuk.
                * base

                # Hozzáadjuk az új karaktert.
                + incoming_character

            # Az értéket ismét kis tartományban tartjuk.
            ) % prime

    # Ha egyik ablak sem egyezett a patternnel,
    # akkor nincs találat.
    return -1


text = "ABCDEF"
pattern = "CDE"

result = rabin_karp(text, pattern)

print(result)  # 2