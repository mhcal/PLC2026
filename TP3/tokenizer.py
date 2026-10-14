
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<SKIP>#.*|[ \t]+)|(?P<VAR>\?[a-zA-Z0-9]+)|(?P<LANG>@[a-zA-Z0-9]{2})|(?P<STRING>"[^"]*")|(?P<NUM>\d+)|(?P<LIMIT>\bLIMIT\b)|(?P<SELECT>\bselect\b)|(?P<WHERE>\bwhere\b)|(?P<CONCEITO>[a-zA-Z0-9]+(:[a-zA-Z0-9]*)?)|(?P<DELIMITADOR>[{}.])|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())

        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
    
        elif dic['LANG']:
            t = ("LANG", dic['LANG'], linha, m.span())
    
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
    
        elif dic['NUM']:
            t = ("NUM", dic['NUM'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())
    
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['CONCEITO']:
            t = ("CONCEITO", dic['CONCEITO'], linha, m.span())
    
        elif dic['DELIMITADOR']:
            t = ("DELIMITADOR", dic['DELIMITADOR'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)    

