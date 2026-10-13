import os, re, sys
SP = os.environ.get('AUDIT_SRC', '/tmp/audit-src')  # local copies of the source editions (not committed)
def load():
    d={}
    for ln in open(f'{SP}/sbl/63-Lk-morphgnt.txt',encoding='utf-8'):
        p=ln.split(); c=int(p[0][2:4]); v=int(p[0][4:6])
        d.setdefault((c,v),[]).append(re.sub("[⸀⸁⸂⸃⸄⸅]","",p[3]))
    return {k:' '.join(w) for k,w in d.items()}
if __name__=='__main__':
    S=load()
    for a in sys.argv[1:]:
        c,r=a.split(':'); lo,hi=(r.split('-')+[r])[:2]
        for v in range(int(lo),int(hi)+1):
            if (int(c),v) in S: print(f'{c}:{v}\t{S[(int(c),v)]}')
