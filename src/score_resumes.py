import os, argparse, glob, json
from pdfminer.high_level import extract_text

def extract_text_from_pdf(path):
    try:
        return extract_text(path)
    except Exception:
        return ''

def heuristic_score(text, jd):
    text_low = text.lower()
    score = 0
    for token in jd.lower().split():
        if token in text_low:
            score += 1
    return score

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--resumes', required=True)
    p.add_argument('--jd', required=True)
    args=p.parse_args()
    files = glob.glob(os.path.join(args.resumes,'*.pdf'))
    results=[]
    for f in files:
        t=extract_text_from_pdf(f)
        s=heuristic_score(t, args.jd)
        results.append({'file':os.path.basename(f),'score':s})
    print(json.dumps(results, indent=2))
