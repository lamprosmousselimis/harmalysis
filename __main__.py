'''
The harmalysis language for harmonic analysis and roman numerals

Copyright (c) 2019, Nestor Napoles
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import harmalysis.parsers.roman
import harmalysis.parsers.chordlabel
import harmalysis.classes.pitch_class
import sys

test_strings = [
     'C:viio65',
     'f#_nat:#viiom7b|f#_nat:vii065|?e#m3D5m7',
     'f#_nat:#viiom7bx5[f#_nat=>:vii065]',
]

def parse(query, syntax='roman'):
    if syntax == 'roman':
        roman = harmalysis.parsers.roman.parse(query, create_png=True)
        return roman

if __name__ == '__main__':
     while True:
          try:
               query = input('> ')
          except EOFError:
               break
          roman = harmalysis.parsers.roman.parse(query, create_png=True)
          chordlabel = harmalysis.parsers.chordlabel.parse(str(roman.chord))
          print('\tApplied key: ' + str(roman.applied_key))
          print('\tIntervallic construction: ' + str(roman.chord))
          print('\tInversion: ' + str(roman.chord.inversion))
          print('\tChord label: ' + chordlabel)

