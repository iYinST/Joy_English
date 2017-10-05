#coding=utf-8
import csv
import random
import sys,getopt

class joy_eng():
    eng_to_chn = []

    def load(self,filename='dir/dir.csv'):
        with open(filename,'r') as f:
            csv_file = csv.reader(f)
            for row in csv_file:
                self.eng_to_chn.append({row[0]:row[1:]})
                try:
                  self.eng_to_chn[-1][row[0]].remove('')
                except:
                    pass


    def match_eng(self,seq,eng):
        return eng == list(self.eng_to_chn[seq].keys())[0]

    def match_chn(self,seq,chn):
        return chn in list(self.eng_to_chn[seq].values())[0]

    def pratice(self):
        while(True):
            print('\r\n')
            mode = random.randrange(0,2)
            seq = random.randrange(0,len(self.eng_to_chn))
            counter = 0
            if mode == 0:
                print(list(self.eng_to_chn[seq].keys())[0])
                chn = input()
                if self.match_chn(seq=seq,chn=chn):
                    print('正确',list(self.eng_to_chn[seq].values())[0])
                else:
                    print('错误',list(self.eng_to_chn[seq].values())[0])

            else:
                print(list(self.eng_to_chn[seq].values())[0])
                eng = input()
                if self.match_eng(seq=seq,eng=eng):
                    print('正确',list(self.eng_to_chn[seq].keys())[0])
                else:
                    print('错误',list(self.eng_to_chn[seq].keys())[0])

if __name__ == '__main__':
    lib = sys.argv[1]
    je = joy_eng()
    je.load(lib)
    je.pratice()