import panda as pd


def jury():
    try:
        data = pd.read_csv("notes.csv", sep=';')
        data["Moyenne"] = data["median"] * 0.3 + data["TP"] * 0.25 + data["final"]* 0.45
        data.sort_values(by="moyenne", ascending=False, inplace=True)
        data.to_csv("juryINF2.csv", sep=";", index=False)
    except OSError as e:
        print(e)