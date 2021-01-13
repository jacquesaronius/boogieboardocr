# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 03:47:32 2021

@author: Jacques Bourquin
"""
from abc import ABC, abstractmethod
import cv2 as cv
import pytesseract as t

class OcrInterface(ABC):
    @abstractmethod
    def scan(self, img_path: str) -> str:
        pass

class Ocr(OcrInterface):
    def scan(self, img_path: str) -> str:
        return ""