module TpPesta where 
import Data.Char 
import Test.HUnit                                                


-- EJ 1
esMinuscula :: Char -> Bool
esMinuscula c 
            | ord c >= ord 'a' && ord c <= ord 'z' = True
            | otherwise = False


-- EJ 2
letraANatural :: Char -> Int
letraANatural c = ord c - ord 'a'



-- EJERCICIO 3 


desplazar :: Char -> Int -> Char
desplazar c n 
             | not (esMinuscula c) || n == 0 = c 
             | n > 0 = desplazarMayores c n 
             | n < 0 = desplazarMenores c n


desplazarMayores :: Char -> Int -> Char
desplazarMayores c n 
                    |ord c + n > ord 'z' =  desplazarMayores c (n - 26)
                    | otherwise = chr (ord c + n) 

desplazarMenores :: Char -> Int -> Char
desplazarMenores c n 
                    | ord c + n < ord 'a' =  desplazarMenores c (n + 26)
                    | otherwise = chr (ord c + n) 




--EJERICICIO 4

cifrar :: String -> Int -> String
cifrar [] _ = []
cifrar (x:xs) n 
              | esMinuscula x = pasarString (desplazarMayores (pasarChar (x:xs)) n) ++ cifrar xs n 
              | otherwise = x : cifrar xs n
               where pasarChar (x:xs) = x
                     pasarString x = [x]


--Ejercicio 5

descifrar :: String ->  Int -> String                                          
descifrar [] _ = []
descifrar (x:xs) n 
                  | esMinuscula x = pasarString (desplazarMenores (pasarChar (x:xs)) (-n)) ++ descifrar xs n  
                  | otherwise = x : descifrar xs n
                  where pasarChar (x:xs) = x
                        pasarString x = [x]



--EJERCICIO 6

cifrarLista :: [String] -> [String]
cifrarLista (x:xs) = cifradoDeElementos (x:xs) 0

cifradoDeElementos :: [String] -> Int -> [String]
cifradoDeElementos [] _ = []
cifradoDeElementos (x:xs) i = cifrar x i : cifradoDeElementos xs (i + 1) 
                          
                                     
--EJERCICIO 7

frecuencia :: String -> [Float]
frecuencia (x:xs) = porcentajes (listaCantidades (x:xs) (ord 'a') ) (cantidadMinusculas (x:xs))


listaCantidades :: String ->  Int -> [Int]
listaCantidades  (x:xs)  a 
                               | a == ord 'z' + 1 = []
                               | otherwise = cantidadDeA (x:xs) (chr a): listaCantidades (x:xs) (a+1)

cantidadDeA :: String -> Char -> Int
cantidadDeA [] _ = 0
cantidadDeA [x] a
             | not (esMinuscula a) = 0 
cantidadDeA (x:xs) a 
             | x == a = 1 + cantidadDeA xs a
             | otherwise = cantidadDeA xs a

porcentajes :: [Int] -> Int -> [Float]
porcentajes [] _ = []
porcentajes (x:xs) tot 
                      | tot == 0 = porcentajes (x:xs) 1
                      | otherwise = (fromIntegral x  / fromIntegral tot) * 100 : porcentajes xs tot
                      

cantidadMinusculas :: String -> Int
cantidadMinusculas [] = 0
cantidadMinusculas (x:xs) 
                         | esMinuscula x =  1 + cantidadMinusculas xs
                         | otherwise = cantidadMinusculas xs 


--EJERCICIO 8

cifradoMasFrecuente :: String -> Int -> (Char, Float)
cifradoMasFrecuente (x:xs) n = (letraDelMax  (maximo (frecuencia (cifrar (x:xs) n ))) (ord 'a') (frecuencia (cifrar (x:xs) n ))  ,  maximo (frecuencia (cifrar (x:xs) n ) ))

letraDelMax :: Float -> Int -> [Float]-> Char
letraDelMax max a (x:xs)
                        | max == x = chr a
                        | otherwise = letraDelMax max (a+1) xs

maximo :: [Float] -> Float
maximo [x] = x
maximo (x:y:xs)
                | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)


--EJERCICIO 9

esDescifrado :: String -> String -> Bool
esDescifrado (x:xs) (a:bc) = cifrarAlInfinito (x:xs) (a:bc) 26

cifrarAlInfinito :: String ->  String -> Int -> Bool
cifrarAlInfinito _ _ 0 = False
cifrarAlInfinito (x:xs) (a:bc) n
                                | cifrar (x:xs) n == (a:bc) = True
                                | otherwise = cifrarAlInfinito (x:xs) (a:bc) (n-1)

--EJERCICIO 10

todosLosDescifrados :: [String] -> [(String, String)]
todosLosDescifrados l1 = todosLosDescifradosAux l1 l1       
                      
todosLosDescifradosAux :: [String] -> [String] -> [(String, String)]
todosLosDescifradosAux [] _ = []                                               
todosLosDescifradosAux (x:xs) l1 = todosLosDescifradosAux2 x l1 ++ todosLosDescifradosAux xs l1                   

todosLosDescifradosAux2 :: String -> [String] -> [(String, String)]                 
todosLosDescifradosAux2 _ [] = []
todosLosDescifradosAux2 x (xl1:xs) 
                                  | (x /= xl1 ) && esDescifrado x xl1 = (x,xl1) : todosLosDescifradosAux2 x xs
                                  | otherwise = todosLosDescifradosAux2 x xs


--Ejercicio 11 

expandirClave :: String -> Int -> String
expandirClave clave 0 = ""
expandirClave clave n = expandirClaveAux clave n 0
                     


expandirClaveAux :: String -> Int -> Int -> String 
expandirClaveAux clave n  c
                            | c >= n = [] 
                            | otherwise = obtenerLetra clave (mod c (length clave)) : expandirClaveAux clave n (c + 1)

obtenerLetra :: String -> Int -> Char                                        
obtenerLetra (x:xs) 0 = x
obtenerLetra (x:xs) n = obtenerLetra xs (n - 1) 
                      

-- Ejercicio 12 

cifrarVigenere :: String -> String -> String
cifrarVigenere s clave = cifradoPorPosicion s (expandirClave clave (length s)) 

cifradoPorPosicion :: String -> String -> String
cifradoPorPosicion [] [] = []
cifradoPorPosicion (x:xs) (a:bc) = desplazar x (ord a - ord 'a') : cifradoPorPosicion xs bc
                 

--EJERCICIO 13

descifrarVigenere :: String -> String -> String
descifrarVigenere s clave = cifradoPorPosicionMenosN s (expandirClave clave (length s)) 

cifradoPorPosicionMenosN :: String -> String -> String
cifradoPorPosicionMenosN [] [] = []
cifradoPorPosicionMenosN (x:xs) (a:bc) = desplazar x (ord 'a' - ord a) : cifradoPorPosicionMenosN xs bc
                 
--EJERCICIO 14

peorCifrado :: String -> [String] -> String
peorCifrado s [x] = x 
peorCifrado s (x : y : xs) | distancia_del_vigenere s (cifrarVigenere s x)  < distancia_del_vigenere s (cifrarVigenere s y) = peorCifrado s (x : xs)
                           | otherwise = peorCifrado s (y : xs)


distancia_del_vigenere :: String -> String -> Int 
distancia_del_vigenere [] [] = 0 
distancia_del_vigenere (x:xs) (q:qs) = (abs ((letraANatural x) - (letraANatural q)) + distancia_del_vigenere xs qs)


-- Ejercicio 15

combinacionesVigenere :: [String] -> [String] -> String -> [(String, String)]
combinacionesVigenere [] _ _ = []
combinacionesVigenere (x:xs) claves cifrado = comparoCifrado x claves cifrado ++ combinacionesVigenere xs claves cifrado


comparoCifrado :: String -> [String] -> String -> [(String, String)]
comparoCifrado _ [] _ = []
comparoCifrado s (x:xs) cifrado     
                               | cifrarVigenere s x == cifrado = (s,x): comparoCifrado s xs cifrado
                               | otherwise = comparoCifrado s xs cifrado



