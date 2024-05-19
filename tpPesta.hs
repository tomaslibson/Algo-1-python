import Data.Char

-- EJ 1
esMinuscula :: Char -> Bool
esMinuscula c = ord c >= ord 'a' && ord c <= ord 'z'

-- EJ 2
letraANatural :: Char -> Int
letraANatural c = (ord c) - (ord 'a')


--esto es una funcion que creo que puede ser util para lo que necesitamos en el Tp
{- naturalALetra :: Int -> Char
naturalALetra n
    | 0 <= n && n <= 25 = chr ((ord 'a') + n ) -}


-- Ej 3 

{- desplazar :: Char -> Int -> Char
desplazar minus 0 = minus 
desplazar minus n
    | not (esMinuscula minus) = minus 
    | (-25) <= n && n <= 25 && esMinuscula minus = desplazarAux minus n 

desplazarAux :: Char -> Int -> Char
desplazarAux l n                                                                        --lo dejo encaminado 
    | n < 0 = anterior l n 
    | n > 0 = proximo l n 

proximo :: Char -> Int -> Char 
proximo l 0 = l
proximo 'z' n = proximo (ord 'a') (n - 1)
proximo l n = proximo 

anteriror :: Char -> Int -> Char
anterior l 0 = l
anterior 'a' l = anterior -} 

desplazar :: Char -> Int -> Char
desplazar c n 
             | not (esMinuscula c) || n == 0 = c 
             | n > 0 = desplazarMayores c n 
             | n < 0 = desplazarmenores c n


desplazarMayores :: Char -> Int -> Char
desplazarMayores c n 
                    |ord c + n > ord 'z' =  desplazarMayores c (n - 26)
                    | otherwise = chr (ord c + n) 

desplazarmenores :: Char -> Int -> Char
desplazarmenores c n 
                    | ord c + n < ord 'a' =  desplazarmenores c (n + 26)
                    | otherwise = chr (ord c + n) 





{- centrar pedro :: Int -> Int 
centrar n | n >= -25 && n <= 25 = n
          | n > 25 = centrar (n - 26)
          | otherwise = centrar (n + 26) 
          -} 

{- centrar :: Int -> Int
centrar n  
    | n > 25 = n - 26
    | n < 0 = n + 26
    | otherwise = n

naturalALetra :: Int -> Char
naturalALetra n
    | 0 <= n && n <= 25 = chr ((ord 'a') + n )
 -}
 
{- 
 desplazar :: int -> Int
 desplazar n
            | n > 26 = desplazar n - 26
            | otherwise = chequear c n 


desplazar :: Char -> Int -> Char
desplazar c n 
            | ord c + n > ord 'z' = desplzar (ord c + n - ord a)  
            | otherwise = ord c + n 

-}

--EJERICICIO 4


cifrar :: String -> Int -> String
cifrar [] _ = []
cifrar (x:xs) n 
              | esMinuscula (x) == True = pasarString (desplazarString (pasarChar (x:xs)) n) ++ cifrar xs n 
              | otherwise = x:cifrar xs n


pasarChar :: String -> Char 
pasarChar (x:xs) = x  

pasarString :: Char -> String 
pasarString x = [x] 

desplazarString :: Char -> Int -> Char
desplazarString x n 
                    |ord x + n > ord 'z' =  desplazarString x (n - 26)
                    | otherwise = (chr (ord x + n)) 
