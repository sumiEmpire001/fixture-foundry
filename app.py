"""Generate reproducible synthetic records for development and testing."""
import argparse
import csv
import json
import random
import sys

FIRST=("Ada","Grace","Alan","Linus","Katherine","Margaret")
LAST=("Okafor","Smith","Chen","Patel","Garcia","Jones")

def generate(count=10,seed=0):
    if not isinstance(count,int) or isinstance(count,bool) or not 0<=count<=100000:
        raise ValueError("count must be an integer between 0 and 100000")
    rng=random.Random(seed)
    return [{"id":i+1,"name":rng.choice(FIRST)+" "+rng.choice(LAST),"score":rng.randint(0,100),"active":bool(rng.getrandbits(1))} for i in range(count)]

def main(argv=None):
    p=argparse.ArgumentParser(description="Generate reproducible synthetic test data")
    p.add_argument("--count",type=int,default=10)
    p.add_argument("--seed",type=int,default=0)
    p.add_argument("--format",choices=("json","csv"),default="json")
    p.add_argument("--output")
    args=p.parse_args(argv)
    try: rows=generate(args.count,args.seed)
    except ValueError as exc:
        print(str(exc),file=sys.stderr)
        return 2
    if args.format=="json": content=json.dumps(rows,indent=2)+"\n"
    else:
        import io
        buffer=io.StringIO()
        writer=csv.DictWriter(buffer,fieldnames=["id","name","score","active"])
        writer.writeheader()
        writer.writerows(rows)
        content=buffer.getvalue()
    if args.output:
        try:
            with open(args.output,"w",encoding="utf-8",newline="") as f: f.write(content)
        except OSError as exc:
            print(str(exc),file=sys.stderr)
            return 2
    else: print(content,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
