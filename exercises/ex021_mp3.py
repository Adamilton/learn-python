# faça um programa  em Python que abra e reproduza áudio de um arquivo MP3.
import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('animals.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()