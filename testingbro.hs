import Data.Char


frecuencia :: String -> [Float]
frecuencia (x:xs) = porcentajes (listaCantidades (x:xs) (ord 'a') ) (cantidadMinusculas (x:xs))


listaCantidades :: String ->  Int -> [Int]
listaCantidades  (x:xs)  a 
                               | a == ord 'z' + 1 = []
                               | otherwise = cantidadDeA (x:xs) (chr a): listaCantidades (x:xs) (a+1)
cantidadDeA :: String -> Char -> Int
cantidadDeA [] _ = 0
cantidadDeA (x:xs) a 
             | x == a = 1 + cantidadDeA (xs) a
             | otherwise = cantidadDeA (xs) a

porcentajes :: [Int] -> Int -> [Float]
porcentajes [] _ = []
porcentajes (x:xs) tot = ((fromIntegral x)  / (fromIntegral tot)) * 100 : porcentajes xs tot 
                      


cantidadMinusculas :: String -> Int
cantidadMinusculas [] = 0
cantidadMinusculas (x:xs) 
                         | esMinuscula x == True =  1 + cantidadMinusculas xs
                         | otherwise = cantidadMinusculas xs 
                    
esMinuscula :: Char -> Bool
esMinuscula c 
            | ord c >= ord 'a' && ord c <= ord 'z' = True
            | otherwise = False

----            
cifrar :: String -> Int -> String
cifrar [] _ = []
cifrar (x:xs) n 
              | esMinuscula x = pasarString (desplazarMayores (pasarChar (x:xs)) n) ++ cifrar xs n 
              | otherwise = x : cifrar xs n
               where pasarChar (x:xs) = x
                     pasarString x = [x]
------

descifrar :: String ->  Int -> String                                          
descifrar [] _ = []
descifrar (x:xs) n 
                  | esMinuscula x = pasarString (desplazarMenores (pasarChar (x:xs)) (-n)) ++ descifrar xs n  -- para que la formula de dezplazarmenores funcione hago que la n sea negativa
                  | otherwise = x : descifrar xs n
                  where pasarChar (x:xs) = x
                        pasarString x = [x]



-----------
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



----

cifradoMasFrecuente :: String -> Int -> (Char, Float)
cifradoMasFrecuente (x:xs) n = (letraDelMax  (maximo (frecuencia (cifrar (x:xs) n ))) (ord 'a') (frecuencia (cifrar (x:xs) n ))  , ( maximo (frecuencia (cifrar (x:xs) n )) ))

letraDelMax :: Float -> Int -> [Float]-> Char
letraDelMax max a (x:xs)
                        | max == x = chr a
                        | otherwise = letraDelMax max (a+1) (xs)

maximo :: [Float] -> Float
maximo [x] = x
maximo (x:y:xs)
                | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)


--------------------

esDescifrado :: String -> String -> Bool

esDescifrado (x:xs) (a:bc) = cifrarAlInfinito (x:xs) (a:bc) 26

cifrarAlInfinito :: String ->  String -> Int -> Bool
cifrarAlInfinito _ _ 0 = False
cifrarAlInfinito (x:xs) (a:bc) n
                                | cifrar (x:xs) n == (a:bc) = True
                                | otherwise = cifrarAlInfinito (x:xs) (a:bc) (n-1)


-----------------------

expandirClave :: String -> Int -> String
expandirClave clave 0 = " "
expandirClave clave n = expandirClaveAux clave n 0
                     


expandirClaveAux :: String -> Int -> Int -> String 
expandirClaveAux clave n  c
                            | c >= n = [] 
                            | otherwise = obtenerLetra clave (mod c (length clave)) : expandirClaveAux clave n ( c + 1)

obtenerLetra :: String -> Int -> Char                                         -- queda aclarado que esto esta programado en base a los requiere
obtenerLetra (x:xs) 0 = x
obtenerLetra (x:xs) n = obtenerLetra xs (n - 1) 
                      
-------------------

cifrarVigenere :: String -> String -> String
cifrarVigenere s clave = aux s (expandirClave clave (length s)) 

aux :: String -> String -> String
aux [] [] = []
aux (x:xs) (a:bc) = desplazar x (ord a - ord 'a') : aux xs bc
                 

---------------------
descifrarVigenere :: String -> String -> String
descifrarVigenere s clave = aux2 s (expandirClave clave (length s)) 

aux2 :: String -> String -> String
aux2 [] [] = []
aux2 (x:xs) (a:bc) = desplazar x (ord 'a' - ord a) : aux2 xs bc
                 
