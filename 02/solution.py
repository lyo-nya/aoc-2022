import fileinput


def calculate_score(signs: str) -> int:
    score = ord(signs[-1]) - 87
    opponent = ord(signs[0]) - 64
    sign_diff = score - opponent
    if sign_diff in {1, -2}:
        score += 6
    elif not sign_diff:
        score += 3
    return score


def get_fake_signs(signs: str) -> str:
    if signs[-1] == "X":
        opponent_sign = ord(signs[0]) + 22
        if opponent_sign < 88:
            opponent_sign += 3
        return signs.replace(signs[-1], chr(opponent_sign))
    if signs[-1] == "Y":
        return signs.replace(signs[-1], chr(ord(signs[0]) + 23))
    if signs[-1] == "Z":
        opponent_sign = ord(signs[0]) + 24
        if opponent_sign > 90:
            opponent_sign -= 3
        return signs.replace(signs[-1], chr(opponent_sign))


score1 = 0
score2 = 0
for line in fileinput.input(files="input.txt"):
    value = line.strip()
    score1 += calculate_score(value)
    score2 += calculate_score(get_fake_signs(value))

print(f"First part answer: {score1}")
print(f"Second part answer: {score2}")
