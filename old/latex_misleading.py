import json

with open('misleading.json','r') as f:
    results = json.load(f)
"""
res = {
    'margins':list(margins),
    'min_round_sizes':list(round_sizes),
    'prov_sprobs':list(prov_sprobs),
    'so_sprobs':list(so_sprobs),
    'eor_sprobs':list(eor_sprobs)
}
"""
s = "\\begin{tabular}{ |c|c|c|c|c| } \n\\hline \n misleading & margin & $n$ & Prov & SO & EOR \\\\\n\hline\n"

for i in range(len(results['misleading_limits'])):
    misleading_limit = results['misleading_limits'][i]
    
    s += str(misleading_limit)

    res = results['results'][i]
    margins = res['margins']
    min_round_sizes = res['min_round_sizes']
    prov_sprobs = res['prov_sprobs']
    so_sprobs = res['so_sprobs']
    eor_sprobs = res['eor_sprobs']

    for i in range(len(margins)):
        #print('margin:'+str(margins[i]))
        #print('min round size:'+str(min_round_sizes[i]))
        #print('prov sprob:'+str(prov_sprobs[i]))
        m = str(margins[i])
        r = str(min_round_sizes[i])
        t = 1000
        p = str(int(prov_sprobs[i] * t) / t)
        so = str(int(so_sprobs[i] * t) / t)
        eor = str(int(eor_sprobs[i] * t) / t)
        #s+=str(margins[i])+'&'+str()+'&'+str(prov_sprobs[i])+'&'+str(so_sprobs[i])+'&'+str(eor_sprobs[i])+'\\\\\n'
        s+='&'+m+'&'+r+'&'+p+'&'+so+'&'+eor+'\\\\\n'
        
s+="\hline\n\end{tabular}"


print(s)
