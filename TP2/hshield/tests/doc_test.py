#!/usr/bin/env python3
import hshield.document_shield
from hshield.document_shield import DocumentShield
text = "Número de carta de condução: BR-123456 1 agora vou ligar à carla o número dela " \
       "é 912345678! Já agora o meu número de cc é 00000000 0 ZZ4"

test = DocumentShield(text)

test.shield()
#print(test.window_text)
