# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 03:47:32 2021

@author: Jacques Bourquin
"""
from abc import ABC, abstractmethod
import cv2
import pytesseract as t
import imutils as im

class OcrInterface(ABC):
    @abstractmethod
    def scan(self, img_path: str) -> str:
        pass

class Ocr(OcrInterface):
    def __init__(self):
        pass

    @classmethod
    def scan(self, img_path: str) -> str:
        return ""