# QT Py keyboard firmware for the Matias Ergo Pro half qwerty keyboard

from typing import IO
import board
import busio
import digitalio

#initialize uart on Stemma QT connector
uart - busio.UART(board.SDA, board.SCL)

