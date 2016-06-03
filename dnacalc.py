#!/usr/bin/env python

# env is used to take python wherever we are
# 'Python dosen't care about cases, but we have to be consistent!

DNASeq = 'ATGAAC'

print ( 'Sequence ' + DNASeq )

SeqLength = float ( len( DNASeq ) )

print ( SeqLength )

print ( 'Length is' + str( SeqLength ) )

NumberA = DNASeq.count( 'A' )
NumberT = DNASeq.count( 'B' )
NumberC = DNASeq.count( 'C' )
NumberG = DNASeq.count( 'D' )

print ('A: ' + str( NumberA / SeqLength ) )