# Generated from Tokenize.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,19,250,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,144,8,3,1,4,4,4,147,8,4,11,4,12,4,
        148,1,4,1,4,4,4,153,8,4,11,4,12,4,154,3,4,157,8,4,1,4,1,4,3,4,161,
        8,4,1,4,4,4,164,8,4,11,4,12,4,165,3,4,168,8,4,1,5,1,5,1,5,1,5,4,
        5,174,8,5,11,5,12,5,175,1,6,4,6,179,8,6,11,6,12,6,180,1,6,1,6,4,
        6,185,8,6,11,6,12,6,186,1,6,1,6,4,6,191,8,6,11,6,12,6,192,1,6,1,
        6,4,6,197,8,6,11,6,12,6,198,1,7,1,7,5,7,203,8,7,10,7,12,7,206,9,
        7,1,7,1,7,1,7,5,7,211,8,7,10,7,12,7,214,9,7,1,7,3,7,217,8,7,1,8,
        1,8,5,8,221,8,8,10,8,12,8,224,9,8,1,9,1,9,1,10,1,10,1,11,1,11,1,
        12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,4,17,243,8,
        17,11,17,12,17,244,1,17,1,17,1,18,1,18,0,0,19,1,1,3,2,5,3,7,4,9,
        5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,
        33,17,35,18,37,19,1,0,9,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,
        45,3,0,48,57,65,70,97,102,2,0,39,39,92,92,2,0,34,34,92,92,3,0,65,
        90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,
        269,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,1,39,1,0,0,0,
        3,44,1,0,0,0,5,50,1,0,0,0,7,143,1,0,0,0,9,146,1,0,0,0,11,169,1,0,
        0,0,13,178,1,0,0,0,15,216,1,0,0,0,17,218,1,0,0,0,19,225,1,0,0,0,
        21,227,1,0,0,0,23,229,1,0,0,0,25,231,1,0,0,0,27,233,1,0,0,0,29,235,
        1,0,0,0,31,237,1,0,0,0,33,239,1,0,0,0,35,242,1,0,0,0,37,248,1,0,
        0,0,39,40,5,116,0,0,40,41,5,114,0,0,41,42,5,117,0,0,42,43,5,101,
        0,0,43,2,1,0,0,0,44,45,5,102,0,0,45,46,5,97,0,0,46,47,5,108,0,0,
        47,48,5,115,0,0,48,49,5,101,0,0,49,4,1,0,0,0,50,51,5,110,0,0,51,
        52,5,117,0,0,52,53,5,108,0,0,53,54,5,108,0,0,54,6,1,0,0,0,55,56,
        5,50,0,0,56,57,5,48,0,0,57,58,5,50,0,0,58,59,5,50,0,0,59,60,5,45,
        0,0,60,61,5,48,0,0,61,62,5,53,0,0,62,63,5,45,0,0,63,64,5,50,0,0,
        64,144,5,56,0,0,65,66,5,50,0,0,66,67,5,48,0,0,67,68,5,50,0,0,68,
        69,5,51,0,0,69,70,5,45,0,0,70,71,5,49,0,0,71,72,5,50,0,0,72,73,5,
        45,0,0,73,74,5,51,0,0,74,144,5,50,0,0,75,76,5,50,0,0,76,77,5,48,
        0,0,77,78,5,50,0,0,78,79,5,50,0,0,79,80,5,45,0,0,80,81,5,48,0,0,
        81,82,5,53,0,0,82,83,5,45,0,0,83,84,5,50,0,0,84,85,5,56,0,0,85,86,
        5,84,0,0,86,87,5,48,0,0,87,88,5,49,0,0,88,89,5,58,0,0,89,90,5,48,
        0,0,90,91,5,50,0,0,91,92,5,58,0,0,92,93,5,48,0,0,93,94,5,51,0,0,
        94,95,5,46,0,0,95,96,5,49,0,0,96,97,5,51,0,0,97,98,5,53,0,0,98,99,
        5,49,0,0,99,100,5,54,0,0,100,144,5,52,0,0,101,102,5,50,0,0,102,103,
        5,48,0,0,103,104,5,50,0,0,104,105,5,50,0,0,105,106,5,45,0,0,106,
        107,5,48,0,0,107,108,5,53,0,0,108,109,5,45,0,0,109,110,5,50,0,0,
        110,111,5,56,0,0,111,112,5,84,0,0,112,113,5,48,0,0,113,114,5,49,
        0,0,114,115,5,58,0,0,115,116,5,48,0,0,116,117,5,50,0,0,117,118,5,
        58,0,0,118,119,5,48,0,0,119,144,5,51,0,0,120,121,5,50,0,0,121,122,
        5,48,0,0,122,123,5,50,0,0,123,124,5,50,0,0,124,125,5,45,0,0,125,
        126,5,49,0,0,126,127,5,51,0,0,127,128,5,45,0,0,128,129,5,48,0,0,
        129,130,5,49,0,0,130,131,5,84,0,0,131,132,5,49,0,0,132,133,5,48,
        0,0,133,134,5,34,0,0,134,135,5,34,0,0,135,136,5,50,0,0,136,137,5,
        48,0,0,137,138,5,58,0,0,138,139,5,51,0,0,139,140,5,48,0,0,140,141,
        5,58,0,0,141,142,5,52,0,0,142,144,5,48,0,0,143,55,1,0,0,0,143,65,
        1,0,0,0,143,75,1,0,0,0,143,101,1,0,0,0,143,120,1,0,0,0,144,8,1,0,
        0,0,145,147,7,0,0,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,1,0,
        0,0,148,149,1,0,0,0,149,156,1,0,0,0,150,152,5,46,0,0,151,153,7,0,
        0,0,152,151,1,0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,
        0,0,155,157,1,0,0,0,156,150,1,0,0,0,156,157,1,0,0,0,157,167,1,0,
        0,0,158,160,7,1,0,0,159,161,7,2,0,0,160,159,1,0,0,0,160,161,1,0,
        0,0,161,163,1,0,0,0,162,164,7,0,0,0,163,162,1,0,0,0,164,165,1,0,
        0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,158,1,0,
        0,0,167,168,1,0,0,0,168,10,1,0,0,0,169,170,5,48,0,0,170,171,5,120,
        0,0,171,173,1,0,0,0,172,174,7,3,0,0,173,172,1,0,0,0,174,175,1,0,
        0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,12,1,0,0,0,177,179,7,0,0,
        0,178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,
        0,181,182,1,0,0,0,182,184,5,46,0,0,183,185,7,0,0,0,184,183,1,0,0,
        0,185,186,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,
        0,188,190,5,46,0,0,189,191,7,0,0,0,190,189,1,0,0,0,191,192,1,0,0,
        0,192,190,1,0,0,0,192,193,1,0,0,0,193,194,1,0,0,0,194,196,5,46,0,
        0,195,197,7,0,0,0,196,195,1,0,0,0,197,198,1,0,0,0,198,196,1,0,0,
        0,198,199,1,0,0,0,199,14,1,0,0,0,200,204,5,39,0,0,201,203,8,4,0,
        0,202,201,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,
        0,205,207,1,0,0,0,206,204,1,0,0,0,207,217,5,39,0,0,208,212,5,34,
        0,0,209,211,8,5,0,0,210,209,1,0,0,0,211,214,1,0,0,0,212,210,1,0,
        0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,212,1,0,0,0,215,217,5,34,
        0,0,216,200,1,0,0,0,216,208,1,0,0,0,217,16,1,0,0,0,218,222,7,6,0,
        0,219,221,7,7,0,0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,
        0,222,223,1,0,0,0,223,18,1,0,0,0,224,222,1,0,0,0,225,226,5,43,0,
        0,226,20,1,0,0,0,227,228,5,45,0,0,228,22,1,0,0,0,229,230,5,47,0,
        0,230,24,1,0,0,0,231,232,5,42,0,0,232,26,1,0,0,0,233,234,5,46,0,
        0,234,28,1,0,0,0,235,236,5,58,0,0,236,30,1,0,0,0,237,238,5,44,0,
        0,238,32,1,0,0,0,239,240,5,95,0,0,240,34,1,0,0,0,241,243,7,8,0,0,
        242,241,1,0,0,0,243,244,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,
        245,246,1,0,0,0,246,247,6,17,0,0,247,36,1,0,0,0,248,249,9,0,0,0,
        249,38,1,0,0,0,18,0,143,148,154,156,160,165,167,175,180,186,192,
        198,204,212,216,222,244,1,6,0,0
    ]

class Tokenize(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NULL = 3
    DATE = 4
    NUMBER = 5
    HEX = 6
    IP = 7
    STRING = 8
    SYMBOL = 9
    PLUS = 10
    MINUS = 11
    DIVIDE = 12
    TIMES = 13
    DOT = 14
    COLON = 15
    COMMA = 16
    UNDERSCORE = 17
    WS = 18
    UNKNOWN = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'null'", "'+'", "'-'", "'/'", "'*'", "'.'", 
            "':'", "','", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NULL", "DATE", "NUMBER", "HEX", "IP", "STRING", 
            "SYMBOL", "PLUS", "MINUS", "DIVIDE", "TIMES", "DOT", "COLON", 
            "COMMA", "UNDERSCORE", "WS", "UNKNOWN" ]

    ruleNames = [ "TRUE", "FALSE", "NULL", "DATE", "NUMBER", "HEX", "IP", 
                  "STRING", "SYMBOL", "PLUS", "MINUS", "DIVIDE", "TIMES", 
                  "DOT", "COLON", "COMMA", "UNDERSCORE", "WS", "UNKNOWN" ]

    grammarFileName = "Tokenize.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


