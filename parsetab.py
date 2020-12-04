
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNACIONleftDISTINTOleftMENORMAYORleftMASMENOSleftPORDIVIDIDOleftPOTENCIAleftPAREIZQPAREDERAFN ASIGNACION CADENA CHILLKA CHUMNONE COMA COMENTARIO COMENTARIO_MULTILINEA CONCAT DECIMAL DEUMAN DISTINTO DIVIDIDO ENTERO ID IGUALQUE INCHE KAM KAY KENUN KOM KONME KUDAW LI LLITULUN MAS MAYOR MENOR MENOS MEW NAMEMN NGUEN NON NV NVLI PAREDER PAREIZQ PEKENUN PETULN PONWI POR POTENCIA PVLE RAKIN SHUNUL TUNTEPU WATRON WELTEKUN YAFUNGUELTUNinit            : instruccionesinstrucciones    : instrucciones instrucciondefinicion_instr   : RAKIN ID\n                          | CHILLKA IDinstrucciones    : instruccion instruccion      : pekenun_instr\n                        | definicion_instr\n                        | asignacion_instr\n                        | tuntepu_instr\n                        | li_instr\n                        | nvli_instrpekenun_instr     : PEKENUN PAREIZQ expresion_cadena PAREDERasignacion_instr   : ID ASIGNACION expresion_numerica\n                          | ID ASIGNACION expresion_cadena tuntepu_instr     : TUNTEPU PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFNli_instr           : LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFNnvli_instr      : LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN NVLI LLITULUN instrucciones AFNexpresion_numerica : expresion_numerica MAS expresion_numerica\n                        | expresion_numerica MENOS expresion_numerica\n                        | expresion_numerica POR expresion_numerica\n                        | expresion_numerica DIVIDIDO expresion_numericaexpresion_numerica : expresion_numerica KAY expresion_numerica \n                        | expresion_numerica KAM expresion_numerica \n                        | expresion_numerica NV expresion_numerica \n                        | PAREIZQ expresion_numerica KAY expresion_numerica PAREDER\n                        | PAREIZQ expresion_numerica KAM expresion_numerica PAREDER\n                        | PAREIZQ expresion_numerica NV expresion_numerica PAREDERexpresion_numerica : PAREIZQ expresion_numerica PAREDERexpresion_numerica : ENTERO\n                        | DECIMALexpresion_numerica   : IDexpresion_cadena     : CADENAexpresion_cadena     : expresion_cadena CONCAT expresion_cadenaexpresion_cadena     : expresion_numericaexpresion_logica : expresion_numerica MAYOR expresion_numerica\n                        | expresion_numerica MENOR expresion_numerica\n                        | expresion_numerica IGUALQUE expresion_numerica\n                        | expresion_numerica DISTINTO expresion_numerica'
    
_lr_action_items = {'PEKENUN':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,52,55,56,57,58,59,60,61,62,63,68,72,73,74,75,76,77,78,80,81,82,],[10,10,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-32,-34,-29,-30,-31,-13,-14,-12,-28,-33,-18,-19,-20,-21,-22,-23,-24,10,10,10,10,-25,-26,-27,-15,-16,10,10,-17,]),'RAKIN':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,52,55,56,57,58,59,60,61,62,63,68,72,73,74,75,76,77,78,80,81,82,],[11,11,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-32,-34,-29,-30,-31,-13,-14,-12,-28,-33,-18,-19,-20,-21,-22,-23,-24,11,11,11,11,-25,-26,-27,-15,-16,11,11,-17,]),'CHILLKA':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,52,55,56,57,58,59,60,61,62,63,68,72,73,74,75,76,77,78,80,81,82,],[13,13,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-32,-34,-29,-30,-31,-13,-14,-12,-28,-33,-18,-19,-20,-21,-22,-23,-24,13,13,13,13,-25,-26,-27,-15,-16,13,13,-17,]),'ID':([0,2,3,4,5,6,7,8,9,11,13,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,36,37,38,39,40,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,68,72,73,74,75,76,77,78,80,81,82,],[12,12,-5,-6,-7,-8,-9,-10,-11,18,20,-2,29,-3,29,-4,29,29,29,-32,-34,-29,-30,-31,-13,-14,-12,29,29,29,29,29,29,29,29,29,29,29,29,29,-28,29,29,-33,-18,-19,-20,-21,-22,-23,-24,12,12,12,12,-25,-26,-27,-15,-16,12,12,-17,]),'TUNTEPU':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,52,55,56,57,58,59,60,61,62,63,68,72,73,74,75,76,77,78,80,81,82,],[14,14,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-32,-34,-29,-30,-31,-13,-14,-12,-28,-33,-18,-19,-20,-21,-22,-23,-24,14,14,14,14,-25,-26,-27,-15,-16,14,14,-17,]),'LI':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,52,55,56,57,58,59,60,61,62,63,68,72,73,74,75,76,77,78,80,81,82,],[15,15,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-32,-34,-29,-30,-31,-13,-14,-12,-28,-33,-18,-19,-20,-21,-22,-23,-24,15,15,15,15,-25,-26,-27,-15,-16,15,15,-17,]),'$end':([1,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,52,55,56,57,58,59,60,61,62,74,75,76,77,78,82,],[0,-1,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-32,-34,-29,-30,-31,-13,-14,-12,-28,-33,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-15,-16,-17,]),'AFN':([3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,52,55,56,57,58,59,60,61,62,72,73,74,75,76,77,78,81,82,],[-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-32,-34,-29,-30,-31,-13,-14,-12,-28,-33,-18,-19,-20,-21,-22,-23,-24,77,78,-25,-26,-27,-15,-16,82,-17,]),'PAREIZQ':([10,14,15,17,19,21,22,23,37,38,39,40,41,42,43,44,46,47,48,49,51,53,54,],[17,21,22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'ASIGNACION':([12,],[19,]),'CADENA':([17,19,37,],[25,25,25,]),'ENTERO':([17,19,21,22,23,37,38,39,40,41,42,43,44,46,47,48,49,51,53,54,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'DECIMAL':([17,19,21,22,23,37,38,39,40,41,42,43,44,46,47,48,49,51,53,54,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'PAREDER':([24,25,26,27,28,29,32,34,35,52,55,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[36,-32,-34,-29,-30,-31,45,50,52,-28,-33,-18,-19,-20,-21,-22,-23,-24,-35,-36,-37,-38,74,75,76,-25,-26,-27,]),'CONCAT':([24,25,26,27,28,29,30,31,52,55,56,57,58,59,60,61,62,74,75,76,],[37,-32,-34,-29,-30,-31,-34,37,-28,37,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,]),'MAS':([26,27,28,29,30,33,35,52,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[38,-29,-30,-31,38,38,38,-28,-18,-19,-20,-21,38,38,38,38,38,38,38,38,38,38,-25,-26,-27,]),'MENOS':([26,27,28,29,30,33,35,52,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[39,-29,-30,-31,39,39,39,-28,-18,-19,-20,-21,39,39,39,39,39,39,39,39,39,39,-25,-26,-27,]),'POR':([26,27,28,29,30,33,35,52,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[40,-29,-30,-31,40,40,40,-28,40,40,-20,-21,40,40,40,40,40,40,40,40,40,40,-25,-26,-27,]),'DIVIDIDO':([26,27,28,29,30,33,35,52,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[41,-29,-30,-31,41,41,41,-28,41,41,-20,-21,41,41,41,41,41,41,41,41,41,41,-25,-26,-27,]),'KAY':([26,27,28,29,30,33,35,52,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[42,-29,-30,-31,42,42,51,-28,-18,-19,-20,-21,42,42,42,42,42,42,42,42,42,42,-25,-26,-27,]),'KAM':([26,27,28,29,30,33,35,52,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[43,-29,-30,-31,43,43,53,-28,-18,-19,-20,-21,43,43,43,43,43,43,43,43,43,43,-25,-26,-27,]),'NV':([26,27,28,29,30,33,35,52,56,57,58,59,60,61,62,64,65,66,67,69,70,71,74,75,76,],[44,-29,-30,-31,44,44,54,-28,-18,-19,-20,-21,44,44,44,44,44,44,44,44,44,44,-25,-26,-27,]),'MAYOR':([27,28,29,33,52,56,57,58,59,60,61,62,74,75,76,],[-29,-30,-31,46,-28,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,]),'MENOR':([27,28,29,33,52,56,57,58,59,60,61,62,74,75,76,],[-29,-30,-31,47,-28,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,]),'IGUALQUE':([27,28,29,33,52,56,57,58,59,60,61,62,74,75,76,],[-29,-30,-31,48,-28,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,]),'DISTINTO':([27,28,29,33,52,56,57,58,59,60,61,62,74,75,76,],[-29,-30,-31,49,-28,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,]),'LLITULUN':([45,50,79,],[63,68,80,]),'NVLI':([78,],[79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,63,68,80,],[2,72,73,81,]),'instruccion':([0,2,63,68,72,73,80,81,],[3,16,3,3,16,16,3,16,]),'pekenun_instr':([0,2,63,68,72,73,80,81,],[4,4,4,4,4,4,4,4,]),'definicion_instr':([0,2,63,68,72,73,80,81,],[5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,63,68,72,73,80,81,],[6,6,6,6,6,6,6,6,]),'tuntepu_instr':([0,2,63,68,72,73,80,81,],[7,7,7,7,7,7,7,7,]),'li_instr':([0,2,63,68,72,73,80,81,],[8,8,8,8,8,8,8,8,]),'nvli_instr':([0,2,63,68,72,73,80,81,],[9,9,9,9,9,9,9,9,]),'expresion_cadena':([17,19,37,],[24,31,55,]),'expresion_numerica':([17,19,21,22,23,37,38,39,40,41,42,43,44,46,47,48,49,51,53,54,],[26,30,33,33,35,26,56,57,58,59,60,61,62,64,65,66,67,69,70,71,]),'expresion_logica':([21,22,],[32,34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',187),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',191),
  ('definicion_instr -> RAKIN ID','definicion_instr',2,'p_instruccion_definicion','gramatica.py',196),
  ('definicion_instr -> CHILLKA ID','definicion_instr',2,'p_instruccion_definicion','gramatica.py',197),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',205),
  ('instruccion -> pekenun_instr','instruccion',1,'p_instruccion','gramatica.py',209),
  ('instruccion -> definicion_instr','instruccion',1,'p_instruccion','gramatica.py',210),
  ('instruccion -> asignacion_instr','instruccion',1,'p_instruccion','gramatica.py',211),
  ('instruccion -> tuntepu_instr','instruccion',1,'p_instruccion','gramatica.py',212),
  ('instruccion -> li_instr','instruccion',1,'p_instruccion','gramatica.py',213),
  ('instruccion -> nvli_instr','instruccion',1,'p_instruccion','gramatica.py',214),
  ('pekenun_instr -> PEKENUN PAREIZQ expresion_cadena PAREDER','pekenun_instr',4,'p_instruccion_pekenun','gramatica.py',218),
  ('asignacion_instr -> ID ASIGNACION expresion_numerica','asignacion_instr',3,'p_asignacion_instr','gramatica.py',222),
  ('asignacion_instr -> ID ASIGNACION expresion_cadena','asignacion_instr',3,'p_asignacion_instr','gramatica.py',223),
  ('tuntepu_instr -> TUNTEPU PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN','tuntepu_instr',7,'p_tuntepu_instr','gramatica.py',229),
  ('li_instr -> LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN','li_instr',7,'p_li_instr','gramatica.py',233),
  ('nvli_instr -> LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN NVLI LLITULUN instrucciones AFN','nvli_instr',11,'p_nvli_instr','gramatica.py',237),
  ('expresion_numerica -> expresion_numerica MAS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',241),
  ('expresion_numerica -> expresion_numerica MENOS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',242),
  ('expresion_numerica -> expresion_numerica POR expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',243),
  ('expresion_numerica -> expresion_numerica DIVIDIDO expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',244),
  ('expresion_numerica -> expresion_numerica KAY expresion_numerica','expresion_numerica',3,'p_expresion_booleana','gramatica.py',252),
  ('expresion_numerica -> expresion_numerica KAM expresion_numerica','expresion_numerica',3,'p_expresion_booleana','gramatica.py',253),
  ('expresion_numerica -> expresion_numerica NV expresion_numerica','expresion_numerica',3,'p_expresion_booleana','gramatica.py',254),
  ('expresion_numerica -> PAREIZQ expresion_numerica KAY expresion_numerica PAREDER','expresion_numerica',5,'p_expresion_booleana','gramatica.py',255),
  ('expresion_numerica -> PAREIZQ expresion_numerica KAM expresion_numerica PAREDER','expresion_numerica',5,'p_expresion_booleana','gramatica.py',256),
  ('expresion_numerica -> PAREIZQ expresion_numerica NV expresion_numerica PAREDER','expresion_numerica',5,'p_expresion_booleana','gramatica.py',257),
  ('expresion_numerica -> PAREIZQ expresion_numerica PAREDER','expresion_numerica',3,'p_expresion_agrupacion','gramatica.py',266),
  ('expresion_numerica -> ENTERO','expresion_numerica',1,'p_expresion_number','gramatica.py',270),
  ('expresion_numerica -> DECIMAL','expresion_numerica',1,'p_expresion_number','gramatica.py',271),
  ('expresion_numerica -> ID','expresion_numerica',1,'p_expresion_id','gramatica.py',275),
  ('expresion_cadena -> CADENA','expresion_cadena',1,'p_expresion_cadena','gramatica.py',279),
  ('expresion_cadena -> expresion_cadena CONCAT expresion_cadena','expresion_cadena',3,'p_expresion_concatenacion','gramatica.py',283),
  ('expresion_cadena -> expresion_numerica','expresion_cadena',1,'p_expresion_cadena_numerico','gramatica.py',287),
  ('expresion_logica -> expresion_numerica MAYOR expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',291),
  ('expresion_logica -> expresion_numerica MENOR expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',292),
  ('expresion_logica -> expresion_numerica IGUALQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',293),
  ('expresion_logica -> expresion_numerica DISTINTO expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',294),
]
