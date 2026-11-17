import sys, numpy as np, subprocess, json
from faster_whisper import WhisperModel
m = WhisperModel("large-v3", device="cpu", compute_type="int8")
out={}
for name,path in zip(sys.argv[2::2], sys.argv[3::2]):
    raw=subprocess.run(["ffmpeg","-v","error","-i",path,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout
    a=np.frombuffer(raw,np.int16).astype(np.float32)/32768
    segs,info=m.transcribe(a,language="ms",word_timestamps=True,vad_filter=True,beam_size=5)
    L=[]
    for s in segs:
        L.append({"start":s.start,"end":s.end,"text":s.text,"nsp":s.no_speech_prob,"words":[{"w":w.word,"s":w.start,"e":w.end} for w in s.words]})
        print(f"{name} [{s.start:5.1f}-{s.end:5.1f}] nsp={s.no_speech_prob:.2f} {s.text}",flush=True)
    if not L: print(name,"(tiada percakapan)",flush=True)
    out[name]=L
json.dump(out,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
