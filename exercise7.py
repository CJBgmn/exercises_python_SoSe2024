def buchstaben_zählen(text):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüß$"
    wort_lower = wort.lower()
    wort_list = list(wort_lower)
    wort_letter = [buchstabe for buchstabe in wort_list if buchstabe in ]
    print(len(wort_letter))
        
(buchstaben_zählen("Hallo, Berlin"))