# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:46:04 2022

@author: Arshad Mehtiyev
"""


def song(an='cow', v='moo'):
    ending=', Ee-igh, Ee-eigh, Oh!'
    
    print('Old MacDonald had a farm'+ ending)
    print('And on that farm he had a '+an+ending)
    print('With a '+v+', '+v+' here and a '+v+', '+v+' there.')
    print('Here a '+v+', there a '+v+', everywhere a '+v+', '+v+'.')
    print('Old MacDonald had a farm'+ ending)
    print()
def main():
    animals={'pig':'oink',
             'duck':'quack',
             'horse':'neigh',
             'sheep':'baaa',
             'turkey':'gobble-gobble'}
    for k,v in animals.items():
        song(k,v)
    
    
    
if __name__=='__main__':
    main()