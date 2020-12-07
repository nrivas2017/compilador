
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNACIONleftDISTINTOleftMENORMAYORleftMASMENOSleftPORDIVIDIDOleftPOTENCIAleftPAREIZQPAREDERAFN ASIGNACION CADENA CHILLKA COMENTARIO COMENTARIO_MULTILINEA CONCAT DECIMAL DISTINTO DIVIDIDO ENTERO ID IGUALQUE LI LLITULUN MAS MAYOR MENOR MENOS NV NVLI PAREDER PAREIZQ PEKENUN PONWI POR POTENCIA PVLE RAKIN TUNTEPUinit            : instruccionesinstrucciones    : instrucciones instrucciondefinicion_instr   : RAKIN ID\n                          | CHILLKA IDinstrucciones    : instruccion instruccion      : pekenun_instr\n                        | definicion_instr\n                        | asignacion_instr\n                        | tuntepu_instr\n                        | li_instr\n                        | nvli_instrpekenun_instr     : PEKENUN PAREIZQ expresion_cadena PAREDERasignacion_instr   : ID ASIGNACION expresion_numerica\n                          | ID ASIGNACION expresion_cadena tuntepu_instr     : TUNTEPU PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFNli_instr           : LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFNnvli_instr      : LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN NVLI LLITULUN instrucciones AFNexpresion_numerica : expresion_numerica MAS expresion_numerica\n                        | expresion_numerica MENOS expresion_numerica\n                        | expresion_numerica POR expresion_numerica\n                        | expresion_numerica DIVIDIDO expresion_numerica\n                        | expresion_numerica POTENCIA expresion_numericaexpresion_numerica : PAREIZQ expresion_numerica PAREDERexpresion_numerica : ENTERO\n                        | DECIMALexpresion_numerica   : IDexpresion_cadena     : CADENAexpresion_cadena     : expresion_cadena CONCAT expresion_cadenaexpresion_cadena     : expresion_numericaexpresion_logica : expresion_numerica MAYOR expresion_numerica\n                        | expresion_numerica MENOR expresion_numerica\n                        | expresion_numerica IGUALQUE expresion_numerica\n                        | expresion_numerica DISTINTO expresion_numerica'
    
_lr_action_items = {'PEKENUN':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,49,50,51,52,53,54,55,56,61,62,63,64,65,67,68,69,],[10,10,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-27,-29,-24,-25,-26,-13,-14,-12,-23,-28,-18,-19,-20,-21,-22,10,10,10,10,-15,-16,10,10,-17,]),'RAKIN':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,49,50,51,52,53,54,55,56,61,62,63,64,65,67,68,69,],[11,11,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-27,-29,-24,-25,-26,-13,-14,-12,-23,-28,-18,-19,-20,-21,-22,11,11,11,11,-15,-16,11,11,-17,]),'CHILLKA':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,49,50,51,52,53,54,55,56,61,62,63,64,65,67,68,69,],[13,13,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-27,-29,-24,-25,-26,-13,-14,-12,-23,-28,-18,-19,-20,-21,-22,13,13,13,13,-15,-16,13,13,-17,]),'ID':([0,2,3,4,5,6,7,8,9,11,13,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,36,37,38,39,40,41,42,44,45,46,47,49,50,51,52,53,54,55,56,61,62,63,64,65,67,68,69,],[12,12,-5,-6,-7,-8,-9,-10,-11,18,20,-2,29,-3,29,-4,29,29,29,-27,-29,-24,-25,-26,-13,-14,-12,29,29,29,29,29,29,29,29,29,29,-23,-28,-18,-19,-20,-21,-22,12,12,12,12,-15,-16,12,12,-17,]),'TUNTEPU':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,49,50,51,52,53,54,55,56,61,62,63,64,65,67,68,69,],[14,14,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-27,-29,-24,-25,-26,-13,-14,-12,-23,-28,-18,-19,-20,-21,-22,14,14,14,14,-15,-16,14,14,-17,]),'LI':([0,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,49,50,51,52,53,54,55,56,61,62,63,64,65,67,68,69,],[15,15,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-27,-29,-24,-25,-26,-13,-14,-12,-23,-28,-18,-19,-20,-21,-22,15,15,15,15,-15,-16,15,15,-17,]),'$end':([1,2,3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,49,50,51,52,53,54,55,64,65,69,],[0,-1,-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-27,-29,-24,-25,-26,-13,-14,-12,-23,-28,-18,-19,-20,-21,-22,-15,-16,-17,]),'AFN':([3,4,5,6,7,8,9,16,18,20,25,26,27,28,29,30,31,36,49,50,51,52,53,54,55,62,63,64,65,68,69,],[-5,-6,-7,-8,-9,-10,-11,-2,-3,-4,-27,-29,-24,-25,-26,-13,-14,-12,-23,-28,-18,-19,-20,-21,-22,64,65,-15,-16,69,-17,]),'PAREIZQ':([10,14,15,17,19,21,22,23,37,38,39,40,41,42,44,45,46,47,],[17,21,22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'ASIGNACION':([12,],[19,]),'CADENA':([17,19,37,],[25,25,25,]),'ENTERO':([17,19,21,22,23,37,38,39,40,41,42,44,45,46,47,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'DECIMAL':([17,19,21,22,23,37,38,39,40,41,42,44,45,46,47,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'PAREDER':([24,25,26,27,28,29,32,34,35,49,50,51,52,53,54,55,57,58,59,60,],[36,-27,-29,-24,-25,-26,43,48,49,-23,-28,-18,-19,-20,-21,-22,-30,-31,-32,-33,]),'CONCAT':([24,25,26,27,28,29,30,31,49,50,51,52,53,54,55,],[37,-27,-29,-24,-25,-26,-29,37,-23,37,-18,-19,-20,-21,-22,]),'MAS':([26,27,28,29,30,33,35,49,51,52,53,54,55,57,58,59,60,],[38,-24,-25,-26,38,38,38,-23,-18,-19,-20,-21,-22,38,38,38,38,]),'MENOS':([26,27,28,29,30,33,35,49,51,52,53,54,55,57,58,59,60,],[39,-24,-25,-26,39,39,39,-23,-18,-19,-20,-21,-22,39,39,39,39,]),'POR':([26,27,28,29,30,33,35,49,51,52,53,54,55,57,58,59,60,],[40,-24,-25,-26,40,40,40,-23,40,40,-20,-21,-22,40,40,40,40,]),'DIVIDIDO':([26,27,28,29,30,33,35,49,51,52,53,54,55,57,58,59,60,],[41,-24,-25,-26,41,41,41,-23,41,41,-20,-21,-22,41,41,41,41,]),'POTENCIA':([26,27,28,29,30,33,35,49,51,52,53,54,55,57,58,59,60,],[42,-24,-25,-26,42,42,42,-23,42,42,42,42,-22,42,42,42,42,]),'MAYOR':([27,28,29,33,49,51,52,53,54,55,],[-24,-25,-26,44,-23,-18,-19,-20,-21,-22,]),'MENOR':([27,28,29,33,49,51,52,53,54,55,],[-24,-25,-26,45,-23,-18,-19,-20,-21,-22,]),'IGUALQUE':([27,28,29,33,49,51,52,53,54,55,],[-24,-25,-26,46,-23,-18,-19,-20,-21,-22,]),'DISTINTO':([27,28,29,33,49,51,52,53,54,55,],[-24,-25,-26,47,-23,-18,-19,-20,-21,-22,]),'LLITULUN':([43,48,66,],[56,61,67,]),'NVLI':([65,],[66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,56,61,67,],[2,62,63,68,]),'instruccion':([0,2,56,61,62,63,67,68,],[3,16,3,3,16,16,3,16,]),'pekenun_instr':([0,2,56,61,62,63,67,68,],[4,4,4,4,4,4,4,4,]),'definicion_instr':([0,2,56,61,62,63,67,68,],[5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,56,61,62,63,67,68,],[6,6,6,6,6,6,6,6,]),'tuntepu_instr':([0,2,56,61,62,63,67,68,],[7,7,7,7,7,7,7,7,]),'li_instr':([0,2,56,61,62,63,67,68,],[8,8,8,8,8,8,8,8,]),'nvli_instr':([0,2,56,61,62,63,67,68,],[9,9,9,9,9,9,9,9,]),'expresion_cadena':([17,19,37,],[24,31,50,]),'expresion_numerica':([17,19,21,22,23,37,38,39,40,41,42,44,45,46,47,],[26,30,33,33,35,26,51,52,53,54,55,57,58,59,60,]),'expresion_logica':([21,22,],[32,34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',168),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',172),
  ('definicion_instr -> RAKIN ID','definicion_instr',2,'p_instruccion_definicion','gramatica.py',177),
  ('definicion_instr -> CHILLKA ID','definicion_instr',2,'p_instruccion_definicion','gramatica.py',178),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',186),
  ('instruccion -> pekenun_instr','instruccion',1,'p_instruccion','gramatica.py',190),
  ('instruccion -> definicion_instr','instruccion',1,'p_instruccion','gramatica.py',191),
  ('instruccion -> asignacion_instr','instruccion',1,'p_instruccion','gramatica.py',192),
  ('instruccion -> tuntepu_instr','instruccion',1,'p_instruccion','gramatica.py',193),
  ('instruccion -> li_instr','instruccion',1,'p_instruccion','gramatica.py',194),
  ('instruccion -> nvli_instr','instruccion',1,'p_instruccion','gramatica.py',195),
  ('pekenun_instr -> PEKENUN PAREIZQ expresion_cadena PAREDER','pekenun_instr',4,'p_instruccion_pekenun','gramatica.py',199),
  ('asignacion_instr -> ID ASIGNACION expresion_numerica','asignacion_instr',3,'p_asignacion_instr','gramatica.py',203),
  ('asignacion_instr -> ID ASIGNACION expresion_cadena','asignacion_instr',3,'p_asignacion_instr','gramatica.py',204),
  ('tuntepu_instr -> TUNTEPU PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN','tuntepu_instr',7,'p_tuntepu_instr','gramatica.py',210),
  ('li_instr -> LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN','li_instr',7,'p_li_instr','gramatica.py',214),
  ('nvli_instr -> LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN NVLI LLITULUN instrucciones AFN','nvli_instr',11,'p_nvli_instr','gramatica.py',218),
  ('expresion_numerica -> expresion_numerica MAS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',222),
  ('expresion_numerica -> expresion_numerica MENOS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',223),
  ('expresion_numerica -> expresion_numerica POR expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',224),
  ('expresion_numerica -> expresion_numerica DIVIDIDO expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',225),
  ('expresion_numerica -> expresion_numerica POTENCIA expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',226),
  ('expresion_numerica -> PAREIZQ expresion_numerica PAREDER','expresion_numerica',3,'p_expresion_agrupacion','gramatica.py',234),
  ('expresion_numerica -> ENTERO','expresion_numerica',1,'p_expresion_number','gramatica.py',238),
  ('expresion_numerica -> DECIMAL','expresion_numerica',1,'p_expresion_number','gramatica.py',239),
  ('expresion_numerica -> ID','expresion_numerica',1,'p_expresion_id','gramatica.py',243),
  ('expresion_cadena -> CADENA','expresion_cadena',1,'p_expresion_cadena','gramatica.py',247),
  ('expresion_cadena -> expresion_cadena CONCAT expresion_cadena','expresion_cadena',3,'p_expresion_concatenacion','gramatica.py',251),
  ('expresion_cadena -> expresion_numerica','expresion_cadena',1,'p_expresion_cadena_numerico','gramatica.py',255),
  ('expresion_logica -> expresion_numerica MAYOR expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',259),
  ('expresion_logica -> expresion_numerica MENOR expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',260),
  ('expresion_logica -> expresion_numerica IGUALQUE expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',261),
  ('expresion_logica -> expresion_numerica DISTINTO expresion_numerica','expresion_logica',3,'p_expresion_logica','gramatica.py',262),
]
