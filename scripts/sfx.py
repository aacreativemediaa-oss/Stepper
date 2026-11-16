import numpy as np, wave, sys, os
SR=48000; out=sys.argv[1]; rng=np.random.default_rng(7)
def save(name,x,peak=0.9):
    x=np.asarray(x,dtype=np.float64); x=x/ (np.max(np.abs(x))+1e-9)*peak
    st=np.stack([x,x],1); d=(st*32767).astype(np.int16)
    with wave.open(os.path.join(out,name),'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(d.tobytes())
def t(d): return np.arange(int(SR*d))/SR
def lp(x,a):  # one-pole lowpass, a may be array
    y=np.zeros_like(x); s=0.0; a=np.broadcast_to(a,x.shape)
    for i in range(len(x)): s+= a[i]*(x[i]-s); y[i]=s
    return y
def bp_sweep(n,f0,f1,dur,q=4):
    # simple state-variable bandpass with swept cutoff
    N=len(n); f=np.geomspace(f0,f1,N); y=np.zeros(N); low=band=0.0
    for i in range(N):
        F=2*np.sin(np.pi*f[i]/SR); hp=n[i]-low-band/q*1.0; band+=F*hp; low+=F*band; y[i]=band
    return y
# whoosh
d=0.45; tt=t(d); n=rng.standard_normal(len(tt)); env=np.sin(np.pi*np.clip(tt/d,0,1))**2
save('whoosh.wav', bp_sweep(n,300,4000,d,q=2)*env, 0.8)
# swoosh down (reverse-ish)
d=0.35; tt=t(d); n=rng.standard_normal(len(tt)); env=np.sin(np.pi*tt/d)**1.5
save('swoosh.wav', bp_sweep(n,5000,600,d,q=2)*env, 0.7)
# pop
d=0.12; tt=t(d); f=np.geomspace(900,300,len(tt)); ph=2*np.pi*np.cumsum(f)/SR
save('pop.wav', np.sin(ph)*np.exp(-tt*35), 0.85)
# ding (bell)
d=1.2; tt=t(d); x=sum(a*np.sin(2*np.pi*f*tt)*np.exp(-tt*k) for f,a,k in [(1760,1,3.5),(2637,.5,5),(3520,.3,7),(5274,.15,9)])
x*=np.minimum(1,tt/0.003); save('ding.wav',x,0.6)
# impact / boom
d=0.9; tt=t(d); f=np.geomspace(120,38,len(tt)); ph=2*np.pi*np.cumsum(f)/SR
x=np.sin(ph)*np.exp(-tt*4.5)+0.6*lp(rng.standard_normal(len(tt)),0.08)*np.exp(-tt*14)
save('impact.wav',x,0.95)
# cha-ching: noise click + two bells
d=1.0; tt=t(d); x=np.zeros(len(tt)); cl=rng.standard_normal(int(SR*0.04))*np.exp(-np.arange(int(SR*0.04))/SR*120); x[:len(cl)]+=cl*0.6
for st,base in [(0.0,2349),(0.09,3136)]:
    i=int(st*SR); tb=tt[:len(tt)-i]; x[i:]+=sum(a*np.sin(2*np.pi*base*m*tb)*np.exp(-tb*k) for m,a,k in [(1,1,5),(2.01,.4,8),(2.76,.25,10)])
save('cash.wav',x,0.6)
# tick
d=0.03; tt=t(d); save('tick.wav', np.sin(2*np.pi*2400*tt)*np.exp(-tt*250),0.5)
# riser
d=1.2; tt=t(d); f=np.geomspace(200,1400,len(tt)); ph=2*np.pi*np.cumsum(f)/SR
n=rng.standard_normal(len(tt)); x=(0.5*np.sign(np.sin(ph))*0.3+ bp_sweep(n,400,6000,d,q=3))*(tt/d)**2
save('riser.wav',x,0.6)
# glitch/ zap for "naik"
d=0.35; tt=t(d); f=np.geomspace(300,2000,len(tt)); ph=2*np.pi*np.cumsum(f)/SR
save('zap.wav', np.sign(np.sin(ph))*0.5*np.exp(-tt*6)*np.minimum(1,tt/0.005), 0.4)
