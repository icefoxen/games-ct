
import pygame
from pygame.locals import *

KEY_QUIT   = 0
KEY_LEFT   = 1
KEY_RIGHT  = 2
KEY_UP     = 3
KEY_DOWN   = 4
KEY_FWD   = 9
KEY_BACK  = 10


KEY_ROLLP  = 5
KEY_ROLLN  = 6
KEY_PITCHP = 7
KEY_PITCHN = 8
KEY_YAWP   = 11
KEY_YAWN   = 12


KEYSPRESSED = []
for x in range( 13 ):
    KEYSPRESSED.append( False )


# Key bindings
KB_QUIT   = K_q

KB_LEFT   = K_s
KB_RIGHT  = K_f
KB_UP     = K_e
KB_DOWN   = K_d
KB_FWD    = K_a
KB_BACK   = K_z


# P = positive direction, N = negative direction
KB_ROLLP   = K_j
KB_ROLLN  = K_l
KB_PITCHP = K_i
KB_PITCHN = K_k
KB_YAWP   = K_SEMICOLON
KB_YAWN   = K_SLASH


