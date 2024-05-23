import Test.HUnit
import Solucion
import Data.List

runTestsPropios = runTestTT allTests

allTests = test [
    "esMinuscula" ~: esMinuculaTest,
    "letraANatural" ~: letraANaturalTest,
    "desplazar" ~: desplazarTest,
    "cifrar" ~: cifrarTest,
    "descifrar" ~: descifrarTest,
    "cifrarLista" ~: cifrarListaTest,
    "frecuencia" ~: frecuenciaTest,
    "cifradoMasFrecuente" ~: cifradoMasFrecuenteTest,
    "esDescifrado" ~: esDescifradoTest,
    "todosLosDescifrados" ~: todosLosDescifradosTest,
    "expandirClave" ~: expandirClaveTest,
    "cifrarVigenere" ~: cifrarVigenereTest,
    "descifrarVigenere" ~: descifrarVigenereTest,
    "peorCifrado" ~: peorCifradoTest,
    "combinacionesVigenere" ~: combinacionesVigenereTest
    ]


-- esMinuscula
 
esMinuculaTest = test [
    " Casobase 1 : 'a' " ~: esMinuscula 'a' ~?= True, 
    " Casobase 2 : 'B' " ~: esMinuscula 'B' ~?= False,
    " Caso Absurdo : ',' " ~: esMinuscula ',' ~?= False
            ]

-- letraANatural

letraANaturalTest = test [                                         
    " Casobase 1 : 'a' " ~: letraANatural 'a' ~?= 0,
    " Casobase 2 : 'z' " ~: letraANatural 'z' ~?= 25,
    " Casobase 3 : 'd' " ~: letraANatural 'd' ~?= 3
    ]


-- desplazar 

desplazarTest = test [
    " Casobase 1 : 'a' 3" ~: desplazar 'a' 3 ~?= 'd',
    " Casobase 2 : 'z' 1" ~: desplazar 'z' 1 ~?= 'a',
    " Casobase 2 : 'a' (-1) " ~: desplazar 'a' (-1) ~?= 'z'
    ]

-- cifrar

cifrarTest = test  [
    " Casobase 1 : computacion 3 " ~: cifrar "computacion" 3 ~?= "frpsxwdflrq",
    " Casobase 2 : La Cabra 26 " ~: cifrar "La Cabra" 26 ~?= "La Cabra",
    " Casobase 3 : La Cabra 25 " ~: cifrar "La Cabra" 25 ~?= "Lz Czaqz",
    " Casobase 4 : La Cabra 1986 " ~: cifrar "La Cabra" 1986 ~?= "Lk Cklbk"
    ]

-- descifrar

descifrarTest = test [
    " CB 1 : frpsxwdflrq 3" ~: descifrar "frpsxwdflrq" 3 ~?= "computacion",
    " CB 2 : medilunas 146 " ~: descifrar "medilunas" 146 ~?= "wonsvexkc",
    " CB 3 : medilunas 68 " ~: descifrar "medilunas" 68 ~?= "wonsvexkc",
    " CB 4 : Medilunas de el torreon 365"  ~: descifrar "Medilunas de el torreon" 365 ~?= "Mdchktmzr cd dk snqqdnm"
    ]

-- cifrarLista

cifrarListaTest = test [
    " CB 1 : [compu, labo, intro] " ~: cifrarLista ["compu", "labo", "intro"] ~?= ["compu", "mbcp", "kpvtq"],
    " CB 2 : [hola, como, estas] " ~: cifrarLista ["hola", "como", "estas"] ~?= ["hola","dpnp","guvcu"],
    " CB 3 :  [el, tiempo, es, dinero] " ~: cifrarLista  ["el", "tiempo", "es", "dinero"] ~?= ["el","ujfnqp","gu","glqhur"]
    ]

-- frecuencia 

frecuenciaTest = test [
    " CB 1 : taller " ~: frecuencia "taller" ~?= [16.666668,0.0,0.0,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0,33.333336, 0.0,0.0,0.0,0.0,0.0,16.666668,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0],
    " CB 2 : computacion " ~: frecuencia "computacion" ~?= [9.090909,0.0,18.181818,0.0,0.0,0.0,0.0,0.0,9.090909,0.0,0.0,0.0,9.090909,9.090909,18.181818,9.090909,0.0,0.0,0.0,9.090909,9.090909,0.0,0.0,0.0,0.0,0.0],
    " CB 3 : pErrO " ~: frecuencia "pErrO" ~?= [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,33.333336,0.0,66.66667,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    " CB 4 : verNaY " ~: frecuencia "verNaY" ~?= [25.0,0.0,0.0,0.0,25.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,25.0,0.0,0.0,0.0,25.0,0.0,0.0,0.0,0.0],
    " CA : BUENAS " ~: frecuencia "BUENAS" ~?= [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    ]

-- cifradoMasFrecuente

cifradoMasFrecuenteTest = test [ 
    " CB 1 : taller  3 " ~: cifradoMasFrecuente "taller" 3 ~?= ('o', 33.333336),
    " CB 2 : Cubano  120 " ~: cifradoMasFrecuente "Cubano" 120 ~?= ('d', 20.0),
    " CA : ARGENTINo 33 " ~: cifradoMasFrecuente "ARGENTINo" 33 ~?= ('v', 100.0)
    ]

-- esDescifrado 

esDescifradoTest = test [
    " CB 1 : taller compu" ~: esDescifrado "taller" "compu" ~?= False,
    " CB 2 : hola hola" ~: esDescifrado "hola" "hola" ~?= True,
    " CB 3 mesa cuiq" ~: esDescifrado "mesa" "cuiq" ~?= True,
    " CA : HOLA HOLA" ~: esDescifrado "HOLA" "HOLA" ~?= True
    ]

-- todosLosDescifrados

todosLosDescifradosTest = test [
    " CB 1 : compu frpsx mywza" ~: todosLosDescifrados ["compu", "frpsx", "mywza"] ~?= [("compu", "frpsx"), ("frpsx", "compu")],
    " CB 2 : taller wjuygf vcnngt ywrbcq" ~: todosLosDescifrados ["taller", "wjuygf","vcnngt", "ywrbcq"] ~?= [("taller", "vcnngt") , ("vcnngt", "taller")], 
    " CB 3 : taller vcnngt szkkdq" ~: todosLosDescifrados ["taller", "szkkdq", "vcnngt" ] ~?= [("taller","szkkdq"), ("taller", "vcnngt"), ("szkkdq", "taller"), ("szkkdq","vcnngt"), ("vcnngt", "taller"), ("vcnngt", "szkkdq")],
    " CA : perro Perro quiero" ~: todosLosDescifrados ["perro", "Perro", "quiero"] ~?= []
    ]

-- expandirClave 

expandirClaveTest = test [
    " CB 1 : compu 8" ~: expandirClave "compu" 8 ~?= "compucom",
    " CB 2 : clave 27 " ~: expandirClave "clave" 27 ~?= "claveclaveclaveclaveclavecl",
    " CB 3 : hola 3" ~: expandirClave "hola" 3 ~?= "hol",
    " CB 4 : largo 100" ~: expandirClave "largo" 100 ~?= "largolargolargolargolargolargolargolargolargolargolargolargolargolargolargolargolargolargolargolargo",
    " CA : abc 0" ~: expandirClave "abc" 0 ~?= ""
    ]

-- cifrarVigenere 

cifrarVigenereTest = test [
    " CB 1 : computacion ip" ~: cifrarVigenere "computacion" "ip" ~?= "kdueciirqdv",
    " CB 2 : hola buenas" ~: cifrarVigenere "hola" "buenas" ~?= "iipn",
    " CB 3 : introduccion_a_la_programacion compu" ~: cifrarVigenere "introduccion a la programacion" "compu" ~?= "kbfgifiorcqb p no elqudpgcqudh",
    " CB 4 : iiii mira" ~: cifrarVigenere "iiii" "mira" ~?= "uqzi"
    ]

-- descifrarVigenere

descifrarVigenereTest = test [
    " CB 1 : kdueciirqdv ip" ~: descifrarVigenere "kdueciirqdv" "ip" ~?= "computacion",
    " CB 2 : Cplpqbzn mira" ~: descifrarVigenere "Cplpqbzn" "mira" ~?= "Chupetin",
    " CB 3 : Dioekirlck xgwls necesarios" ~: descifrarVigenere "Dioekirlck xgwls" "necesarios" ~?= "Demasiados tests" 
    ]


-- peorCifrado

peorCifradoTest = test [
    " CB 1 : lacabra [esto es boca]" ~: peorCifrado "lacabra" ["esto", "es" , "boca"] ~?= "boca",
    " CB 2 : calleri [y de rabona]" ~: peorCifrado "calleri" ["y", "de", "rabona"] ~?= "de",
    " CB 3 : trabajogrupal [intro a la programacion]" ~: peorCifrado "trabajogrupal" ["intro","a", "la", "programacion"] ~?= "a",
    " CB 4 : disfruto [aprender mucho matematicas complejas]" ~: peorCifrado "disfruto" ["aprender", "mucho", "matematicas", "complejas"] ~?= "matematicas"
    ]   

-- combinacionesVigenere

combinacionesVigenereTest = test [
    " CB 1" ~: combinacionesVigenere ["aaaa", "bbbb"] ["b", "c"] "cccc" ~?= [("aaaa", "c"), ("bbbb", "b")],
    " CB 2" ~: combinacionesVigenere ["slash", "tini"] ["guitarra", "album"] "yfilh" ~?= [("slash", "guitarra")],
    " CB 3" ~: combinacionesVigenere ["messi", "cristiano"] ["arabia", "mejorjugador"] "yibgz" ~?= [("messi", "mejorjugador")]
