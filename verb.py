# -*- coding: utf-8 -*-
import time

def main():
    vowels = ['a','i','u','e','o']
    while True:
        time.sleep(1)
        present = input('動詞を入力してネ>')
        if(present == 'OK'):
            print('またね～')
            break
        prog = ''
    
        if present in ['visit','limit','play','enjoy','listen','see','dye','enter']:
            prog = present + 'ing'
    
        elif present[-2:] == 'ie':
            prog = present.replace(present[-2:], 'ying')
    
        elif present[-1] == 'e':
            prog = present.replace(present[-1], 'ing')
    
        elif present[-1] == 'c':
            prog = present + 'king'
    
    #長母音+子音 -> ing
        elif (present[-3] in vowels) and (present[-2] in vowels):
            prog = present + 'ing'
    
    #母音+子音
        elif present[-2] in vowels:
            prog = present + present[-1] + 'ing'
    
    #終了
        elif present == 'end':
            break
    
    #その他
        else:
            prog = present + 'ing'
    
        print('現在分詞はコレ->' + prog)
    
    #例外 (6つのみ)
        past = ''
        if present in ['visit', 'limit', 'play', 'enjoy', 'listen', 'enter']:
            past = present + 'ed'
        elif present == 'dye':
            past = present + 'd'
    
    #不規則動詞 (6つのみ)
        elif present == 'get':
            past = 'got-got'
        elif present == 'run':
            past = 'ran-run'
        elif present == 'swim':
            past = 'swam-swumt'
        elif present == 'begin':
            past = 'read-read'
    
        elif present[-1] == 'e':
            past = present + 'd'
    
    #末尾から２文字目が母音であるか判断
        elif present[-1:] == 'p':
            if present[-2] in vowels:
                past = present + 'ped'
            else:
                past = present + 'ed'
    
    #上記同様
        elif present[-1:] == 'y':
            if present[-2] in  vowels:
                past = present + 'ed'
            else:
                past = present.replace(present[-1], 'ied')
    
        elif present[-1] == 'c':
            past = present + 'ked'
    
        elif present[-2:] in  ['ir','er','ur']:
            past = present + present[-1] + 'ed'
    
        elif present[-2] in vowels:
            past = present + present[-1] + 'ed'
    
    #その他
        else:
            past = present + 'ed'
        print('過去形はコレ ->' + past)
        print('\n')

if __name__ == "__main__":
    main()       
