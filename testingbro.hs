import Data.Char

esMinuscula :: Char -> Bool
esMinuscula c = ord c >= ord 'a' && ord c <= ord 'z'


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
