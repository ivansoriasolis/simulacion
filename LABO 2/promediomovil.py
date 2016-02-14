def predecir(val):
    def prom(val, vent=2):
        det = {'vent':vent, 'prom':[], 'pred':0, 'err':[], 'mse':0}
        for i in range(vent,len(val)):
            prom = sum(val[i-vent:i])/vent
            det['prom'] += [prom]
            det['err'] += [ (val[i]-prom)**2 ]
        det['pred'] = sum(val[len(val)-vent:len(val)])/vent
        det['mse'] = sum(det['err'])/len(det['err'])
        return det
    preds = [ prom(val,i) for i in range(2,len(val))]
    mses = [ (item['mse'],item['pred'],item['vent']) for item in preds]
    return sorted(mses)
        
