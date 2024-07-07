import glob
from pathlib import Path 
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer as sia

def get_scores():
    filepaths = glob.glob("./myproject8/diary/*.txt")
    dates = []
    positivity = []
    negativity = []
    
    for filepath in sorted(filepaths):
        filename = Path(filepath).stem
        with open(filepath, "r") as my_file:
            diary_input = my_file.read()
        analyzer = sia()
        score = analyzer.polarity_scores(diary_input)
        
        dates.append(filename)
        positivity.append(score["pos"])
        negativity.append(score["neg"])
        
    return dates, positivity, negativity
        
    
if __name__ == "__main__":
    print(get_scores())