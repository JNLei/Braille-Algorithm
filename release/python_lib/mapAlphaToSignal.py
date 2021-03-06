# Contains dict that map Eglish letters to signals
# Unicode table: https://www.rapidtables.com/code/text/unicode-characters.html
CAPITAL = '000001'

letters = { 'a': '100000',
			'b': '101000',
			'c': '110000',
			'd': '110100',
			'e': '100100',
			'f': '111000',
			'g': '111100',
			'h': '101100',
			'i': '011000',
			'j': '011100',
			'k': '100010',
			'l': '101010',
			'm': '110010',
			'n': '110110',
			'o': '100110',
			'p': '111010',
			'q': '111110',
			'r': '101110',
			's': '011010',
			't': '011110',
			'u': '100011',
			'v': '101011',
			'w': '011101',
			'x': '110011',
			'y': '110111',
			'z': '100111',
            'A': '100000',
			'B': '101000',
			'C': '110000',
			'D': '110100',
			'E': '100100',
			'F': '111000',
			'G': '111100',
			'H': '101100',
			'I': '011000',
			'J': '011100',
			'K': '100010',
			'L': '101010',
			'M': '110010',
			'N': '110110',
			'O': '100110',
			'P': '111010',
			'Q': '111110',
			'R': '101110',
			'S': '011010',
			'T': '011110',
			'U': '100011',
			'V': '101011',
			'W': '011101',
			'X': '110011',
			'Y': '110111',
			'Z': '100111'}
			
contractions = {'but': '101000', 'But': '101000', 'BUT': '101000', 
                'can': '110000', 'Can': '110000', 'CAN': '110000', 
                'do': '110100', 'Do': CAPITAL + '110100', 'DO': CAPITAL*2 + '110100',
                'every': '100100', 'Every': CAPITAL + '100100', 'EVERY': CAPITAL*2 + '100100',
                'from': '111000', 'From': CAPITAL + '111000', 'FROM': CAPITAL*2 + '111000',
                'go': '111100', 'Go': CAPITAL + '111100', 'GO': CAPITAL*2 + '111100',
                'have': '101100', 'Have': CAPITAL + '101100', 'HAVE': CAPITAL*2 + '101100',
                'just': '011100', 'Just': CAPITAL + '011100', 'JUST': CAPITAL*2 + '011100',
                'knowledge': '010001', 'Knowledge': CAPITAL + '010001', 'KNOWLEDGE': CAPITAL*2 + '010001',
                'like': '010101', 'Like': CAPITAL + '010101', 'LIKE': CAPITAL*2 + '010101',
                'more': '110010', 'More': CAPITAL + '110010', 'MORE': CAPITAL*2 + '110010',
                'not': '110110', 'Not': CAPITAL + '110110', 'NOT': CAPITAL*2 + '110110',
                'people': '111010', 'People': CAPITAL + '111010', 'PEOPLE': CAPITAL*2 + '111010',
                'quite': '111110', 'Quite': CAPITAL + '111110', 'QUITE': CAPITAL*2 + '111110',
                'rather': '101110', 'Rather': CAPITAL + '101110', 'RATHER': CAPITAL*2 + '101110',
                'so': '011010', 'So': CAPITAL + '011010', 'SO': CAPITAL*2 + '011010',
                'that': '011110', 'That': CAPITAL + '011110', 'THAT': CAPITAL*2 + '011110',
                'us': '100011', 'Us': CAPITAL + '100011', 'US': CAPITAL*2 + '100011',
                'very': '101011', 'Very': CAPITAL + '101011', 'VERY': CAPITAL*2 + '101011',
                'it': '110011', 'It': CAPITAL + '110011', 'IT': CAPITAL*2 + '110011',
                'you': '110111', 'You': CAPITAL + '110111', 'YOU': CAPITAL*2 + '110111',
                'as': '100111', 'As': CAPITAL + '100111', 'AS': CAPITAL*2 + '100111',
                'and': '111011', 'And': CAPITAL + '111011', 'AND': CAPITAL*2 + '111011',
                'for': '111111', 'For': CAPITAL + '111111', 'FOR': CAPITAL*2 + '111111',
                'of': '101111', 'Of': CAPITAL + '101111', 'OF': CAPITAL*2 + '101111',
                'the': '011011', 'The': CAPITAL + '011011', 'THE': CAPITAL*2 + '011011',
                'with': '011111', 'With': CAPITAL + '011111', 'WITH': CAPITAL*2 + '011111',
                'child': '100001', 'Child': CAPITAL + '100001', 'CHILD': CAPITAL*2 + '100001',
                'shall': '110001', 'Shall': CAPITAL + '110001', 'SHALL': CAPITAL*2 + '110001',
                'this': '110101', 'This': CAPITAL + '110101', 'THIS': CAPITAL*2 + '110101',
                'which': '100101', 'Which': CAPITAL + '100101', 'WHICH': CAPITAL*2 + '100101',
                'out': '101101', 'Out': CAPITAL + '101101', 'OUT': CAPITAL*2 + '101101',
                'will': '011101', 'Will': CAPITAL + '011101', 'WILL': CAPITAL*2 + '011101',
                'his': '001011', 'His': CAPITAL + '001011', 'HIS': CAPITAL*2 + '001011',
                'in': '000110', 'In': CAPITAL + '000110', 'IN': CAPITAL*2 + '000110',
                'was': '000111', 'Was': CAPITAL + '000111', 'WAS': CAPITAL*2 + '000111',
                'were': '001111', 'Were': CAPITAL + '001111', 'WERE': CAPITAL*2 + '001111'}
                #'to': '001110'}

abbreviation = {'ch': '100001', 'Ch': '100001', 'CH': '100001',
               'ing': '010011', 'Ing': '010011', 'ING': '010011',
                'ar': '010110', 'Ar': '010110', 'AR': '010110',
                'gh': '101001','Gh': CAPITAL + '101001', 'GH': CAPITAL*2 + '101001',
                'sh': '110001', 'Sh': CAPITAL + '110001', 'SH': CAPITAL*2 + '110001',
                'th': '110101', 'Th': CAPITAL + '110101', 'TH': CAPITAL*2 + '110101',
                'wh': '100101', 'Wh': CAPITAL + '100101', 'WH': CAPITAL*2 + '100101',
                'ed': '111001', 'Ed': CAPITAL + '111001', 'ED': CAPITAL*2 + '111001',
                'er': '111101', 'Er': CAPITAL + '111101', 'ER': CAPITAL*2 + '111101',
                'ou': '101101', 'Ou': CAPITAL + '101101', 'OU': CAPITAL*2 + '101101',
                'ow': '011001', 'Ow': CAPITAL + '011001', 'OW': CAPITAL*2 + '011001',
                'bb': '001010', 'Bb': CAPITAL + '001010', 'BB': CAPITAL*2 + '001010',
                'cc': '001100', 'Cc': CAPITAL + '001100', 'CC': CAPITAL*2 + '001100',
                'dd': '001101', 'Dd': CAPITAL + '001101', 'DD': CAPITAL*2 + '001101',
                'en': '001001', 'En': CAPITAL + '001001', 'EN': CAPITAL*2 + '001001',
                'gg': '001111', 'Gg': CAPITAL + '001111', 'GG': CAPITAL*2 + '001111',
                'in': '000110', 'In': CAPITAL + '000110', 'IN': CAPITAL*2 + '000110',
                'st': '010010', 'St': CAPITAL + '010010', 'ST': CAPITAL*2 + '010010'}

punctuation = {',': '001000',
               ';': '001010',
               ':': '001100',
               '.': '001101',
               '!': '001110',
               '(': '001111',
               ')': '001111',
               '“': '001011',
               '”': '000111',
               '?': '001011',
               '/': '010010',
               '#': '010111',
               '\'': '000010',
               '…': '001101'*3,
               '’': '000010',
               '­': '000011',
               '-': '000011',
               '‐': '000011',
               '‑': '000011',
               '‒': '000011',
               '–': '000011',
               '—': '000011',
               '―': '000011'}

numbers = {'1': '100000',
           '2': '101000',
           '3': '110000',
           '4': '110100',
           '5': '100100',
           '6': '111000',
           '7': '111100',
           '8': '101100',
           '9': '011000',
           '0': '011100'}
