from typing import List


# O(n) time | O(k) space, n - number of competitions, k - number of teams
def tournament_winner(competitions: List[List[str]], results: List[int]) -> str:
    current_best_team = ""
    score_board = {current_best_team: 0}

    for (competition, result) in zip(competitions, results):
        home_team, away_team = competition

        winner = home_team if result == 1 else away_team

        if winner not in score_board:
            score_board[winner] = 0

        score_board[winner] += 3

        if score_board[winner] > score_board[current_best_team]:
            current_best_team = winner

    return current_best_team


if __name__ == '__main__':
    competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    expected = "Python"
    res = tournament_winner(competitions, results)
    print(res)
    print(expected == res)
