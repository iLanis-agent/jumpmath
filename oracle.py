import json, math

def pos(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>0
def num(x): return isinstance(x,(int,float)) and math.isfinite(x)
def jround(x): return math.floor(x+0.5)
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)
def r10(x): return jround(x/10)*10
def r5(x): return jround(x/5)*5

def crank_plan(liters,fuel):
    if not pos(liters): return {"error":"the engine size must be above zero"}
    if fuel not in ("gas","diesel"): return {"error":"pick gas or diesel"}
    raw=liters*(240 if fuel=="diesel" else 110)
    return {"amps":r10(raw),"fuel":fuel}

def render_crank(r,liters,fuel):
    return ("Your "+jsnum(liters)+" L "+r["fuel"]+" engine wants about "+jsnum(r["amps"])
            +" honest cranking amps - a labeled norm; the battery plate and the manual name the real number.")

def decode_plan(peak):
    if not pos(peak): return {"error":"the peak amps must be above zero"}
    raw=peak/3.5
    working=r10(raw)
    if raw<150: verdict="a phone charger with ambition"
    elif raw<300: verdict="small engines only"
    elif raw<600: verdict="most gas cars"
    elif raw<1000: verdict="trucks and diesels in fair weather"
    else: verdict="shop-grade"
    return {"working":working,"verdict":verdict}

def render_decode(r,peak):
    return ("The "+jsnum(peak)+" peak amps on the box figure about "+jsnum(r["working"])
            +" honest cranking amps - "+r["verdict"]+". The peak is a pulse, not a crank.")

def need_factor(t):
    if t>=50: return 1
    if t>=32: return 1.25
    if t>=0: return 1.6
    return 2
def pack_factor(t):
    if t>=50: return 1
    if t>=32: return 0.85
    if t>=0: return 0.7
    return 0.55

def cold_plan(amps,tempF):
    if not pos(amps): return {"error":"the amps must be above zero"}
    if not num(tempF): return {"error":"the temperature must be a number"}
    return {"need":r5(amps*need_factor(tempF)),"packPct":jround(pack_factor(tempF)*100)}

def render_cold(r,amps,tempF):
    return ("At "+jsnum(tempF)+" F the engine wants about "+jsnum(r["need"])+" honest amps and the cold pack keeps "
            +jsnum(r["packPct"])+"% of its room-temperature best - check the margin before the morning.")

cases=[]
def add(tool,args):
    if tool=="crank": r=crank_plan(*args); fn=render_crank
    elif tool=="decode": r=decode_plan(*args); fn=render_decode
    else: r=cold_plan(*args); fn=render_cold
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(2.0,"gas"),(1.4,"gas"),(3.5,"gas"),(5.7,"gas"),(6.7,"diesel"),(3.0,"diesel"),(0.9,"gas"),(2.4,"gas"),(4.0,"diesel"),(1.6,"gas")]:
    add("crank",a)
for a in [(2000,),(400,),(1000,),(600,),(3500,),(800,),(520,),(1500,)]:
    add("decode",a)
for a in [(220,10),(300,0),(450,32),(250,70),(600,-10),(180,45),(520,20),(300,-20)]:
    add("cold",a)
add("crank",[0,"gas"]); add("crank",[2.0,"hybrid"]); add("decode",[0]); add("cold",[0,10])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
