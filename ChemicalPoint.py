from yaml import dump

on_indexes = lambda chemical_point:chemical_point.index
on_elements = lambda chemical_point:chemical_point.element
on_coords = lambda chemical_point: chemical_point.x
on_canonical_rep = lambda chemical_point: chemical_point.canonical_rep


class ChemicalPoint:
    
    def __init__(self, x, index, element=None, flavour=None, grouped_flavours=None):
        self.x = x
        self.index = index
        self.element = element
        self.flavour = flavour
        self.canonical_rep = element if not grouped_flavours else '{element}{group_length}'.format(element=element, group_length=len(grouped_flavours[flavour]))
    
    def __str__(self):
        return '{{index={index}, element={element}, canonical_rep={canonical_rep}}}'.format(
                                        **{   'index':self.index,
                                            'element': self.element,
                                            'canonical_rep': self.canonical_rep
                                        })
    def __repr__(self):
        return self.__str__()


ELEMENT_NUMBERS = {
    "H":1,"HE":2,"LI":3,"BE":4,"B":5,"C":6,"N":7,"O":8,"F":9,"NE":10,"NA":11,"MG":12,
    "AL":13,"SI":14,"P":15,"S":16,"CL":17,"AR":18,"K":19,"CA":20,"SC":21,"TI":22,
    "V":23,"CR":24,"MN":25,"FE":26,"CO":27,"NI":28,"CU":29,"ZN":30,"GA":31,"GE":32,
    "AS":33,"SE":34,"BR":35,"KR":36,"RB":37,"SR":38,"Y":39,"ZR":40,"NB":41,"MO":42,
    "TC":43,"RU":44,"RH":45,"PD":46,"AG":47,"CD":48,"IN":49,"SN":50,"SB":51,"TE":52,
    "I":53,"XE":54,"CS":55,"BA":56,"LA":57,"CE":58,"PR":59,"ND":60,"PM":61,"SM":62,
    "EU":63,"GD":64,"TB":65,"DY":66,"HO":67,"ER":68,"TM":69,"YB":70,"LU":71,"HF":72,
    "TA":73,"W":74,"RE":75,"OS":76,"IR":77,"PT":78,"AU":79,"HG":80,"TL":81,"PB":82,
    "BI":83,"PO":84,"AT":85,"RN":86,"FR":87,"RA":88,"AC":89,"TH":90,"PA":91,"U":92,
    "NP":93,"PU":94,"AM":95,"CM":96,"BK":97,"CF":98,"ES":99,"FM":100,"MD":101,"NO":102,
    "LR":103,"RF":104,"DB":105,"SG":106,"BH":107,"HS":108,"MT":109 }