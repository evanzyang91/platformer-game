import pygame

map = [
'                            ', 
'                            ', 
'        E                   ', 
' 11    111    P   11  11    ', 
' 11                         ', 
' 1111         11         11 ', 
' 1111       1111        11  ', 
' 11    1  1111    11  111111', 
'       1  1111    11  111111',
'     111  111111  11  111111', 
'11111111  111111  11  111111']

tileSize = 64 
screenWidth = 1200
screenHeight = len(map) * tileSize