import argparse,json,math

def cosine(a,b):
    if len(a)!=len(b):raise ValueError("Embedding lengths differ")
    dot=sum(x*y for x,y in zip(a,b));na=math.sqrt(sum(x*x for x in a));nb=math.sqrt(sum(x*x for x in b))
    return dot/(na*nb) if na and nb else 0.0

def search(items,query,k):
    vector=items[query]
    return sorted(((name,cosine(vector,value)) for name,value in items.items() if name!=query),key=lambda x:x[1],reverse=True)[:k]

def main():
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("query");p.add_argument("k",type=int);a=p.parse_args()
    items=json.load(open(a.input,encoding="utf-8"))
    for name,score in search(items,a.query,a.k):print(f"{score:.4f}\t{name}")
if __name__=="__main__":main()
