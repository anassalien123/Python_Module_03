import sys

if __name__ == "__main__":

    print("=== Player Score Analytics ===")

    scores = []

    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for i in range(1, len(sys.argv)):
                scores.append(int(sys.argv[i]))
        except ValueError as error:
            print(f"Error {error}")
        else:
            Total_players = len(scores)
            Total_score = sum(scores)
            High_score = max(scores)
            Low_score = min(scores)

            print(f"Total players: {Total_players}")
            print(f"Total score: {Total_score}")
            print(f"Average score: {Total_score / Total_players}")
            print(f"High score: {High_score}")
            print(f"Low score: {Low_score}")
            print(f"Score range: {High_score - Low_score}")
