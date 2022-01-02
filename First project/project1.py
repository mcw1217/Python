import random
import time
import os
import sys
from utils.display import delay_print


def inital_display():
    print("===================================")
    print("몬스터 리그에 오신것을 환영합니다.")
    monsters=["화끈몬","축축몬","수풀몬"]
    for index,monster in enumerate(monsters):
        print(f"[{index+1}] {monster}\t", end="")
        
    while True:
        try:
            #사용자의 숫자를 입력받습니다.
            selected_num=input('\n플레이할 "몬스터"의 번호를 선택해주세요:')
            
            #사용자가 선택한 몬스터
            user_monster=monsters[int(selected_num)-1]
        except ValueError:
            print("올바르지 않은 값입니다.")
        except IndexError:
            print("올바르지 않은 번호입니다.")
        except Exception as e:
            print(e)
        else:
            #게임 플레이어의 이름을 입력
            user_name=input("플레이어의 이름을 입력해주세요.")
            break
    print(f"[{selected_num}] {user_monster}를 선택하셨습니다.")
    print(f"{user_name} 님 환영합니다.")
    return user_monster

class Monster:
    def __init__(self,name,types,moves,EVs,health="==================="):
        self.name=name
        self.types=types
        self.moves=moves
        self.attack=EVs["공격력"]
        self.defense=EVs["방어력"]
        self.evasion=round(random.uniform(0.1, 0.3), 4) #회피율 능력치
        self.health=health
        self.bars=20
        
        
def create_monster(monster):
    if monster=="화끈몬":
        return Monster("화끈몬","불",["불꽃뿜기","머리박치기","불꽃펀치"],{"공격력":3,"방어력":2})
    elif monster =="축축몬":
        return Monster("축축몬","물",["불꽃뿜기","머리박치기","불꽃펀치"],{"공격력":3,"방어력":2})
    elif monster =="수풀몬":
        return Monster("수풀몬","풀",["불꽃뿜기","머리박치기","불꽃펀치"],{"공격력":3,"방어력":2})
    
    
def inital_fight(home_monster, away_monster):
    print("===================전투가 시작되었습니다!!====================")
    print(f"\n[{home_monster.name}]")
    print("타입/", home_monster.types)
    print("공격력/", home_monster.attack)
    print("방어력/", home_monster.defense)
    print("회피율/", home_monster.evasion)
    print("\nVS\n")
    print(f"\n[{away_monster.name}]")
    print("타입/", away_monster.types)
    print("공격력/", away_monster.attack)
    print("방어력/", away_monster.defense)
    print("회피율/", away_monster.evasion)
        
    attrs=["불","물","풀"]
    string_1_attack=""
    string_2_attack=""
    for index, value in enumerate(attrs):
        if home_monster.types==value:
            if away_monster.types==value:
                string_1_attack="\n효과는 평범했다."
                string_2_attack="\n효과는 평범했다."
                    
            #away_monster 속성이 더 강력할때
            if away_monster.types==attrs[(index+1) %3]:
                away_monster.attack*=2
                away_monster.defense*=2
                string_1_attack="\n효과가 별로인 듯하다...."
                string_2_attack="\n효과는 매우 뛰어났다!!"
                    
            #home_monster 속성이 더 강력할 때
            if away_monster.types==attrs[(index+2) %3]:
                home_monster.attack*=2
                home_monster.defense*=2
                string_1_attack="\n효과가 별로인 듯하다...."
                string_2_attack="\n효과는 매우 뛰어났다!!"
                    
    fight(home_monster, away_monster, string_1_attack, string_2_attack)
            
            
def fight(home_monster, away_monster, string_1_attack, string_2_attack):
    while (home_monster.bars>0) and (away_monster.bars>0):
        print(f"\n[유저]{home_monster.name}\t{home_monster.health}")
        print(f"[상대]{away_monster.name}\t{away_monster.health}\n")
        turn(home_monster, away_monster, string_1_attack, True)
        turn(away_monster, home_monster, string_2_attack, False)
            
def turn(home_monster, away_monster, effective, is_user):
    if is_user:
        print(f"가랏{home_monster.name}!")
    else:
        print(f"{home_monster.name}이 공격해 왔다!")
            
    for index, value in enumerate(home_monster.moves):
        print(f"{index+1}", value)
            
    if is_user:
        while True:
            try:
                move_index=int(input("공격을 선택하세요:"))
                if move_index-1 in range(len(home_monster.moves)):
                    break
                else:
                    print("숫자만 입력 가능합니다.")
            except:
                print("숫자만 입력 가능합니다.")
    else:
        move_index=random.randint(0,2) #상대가 무작위로 경격 선택
    delay_print(f"\n{home_monster.name}! {home_monster.moves[move_index-1]} 공격!")
    time.sleep(1)
        
    #회피율 기준을 공격이 빗나가면 체력을 소모하지 않음
    if random.uniform(0,1)<away_monster.evasion:
        delay_print(f"\n공격이 빗나갔습니다!!!")
    else:
        #체력을 깎음, 방어력이 높을 때 away_monster.bars가 증가하지 않도록 주의
        delay_print(effective)
        away_monster.bars-=home_monster.attack - (0.3*away_monster.defense)
            
    away_monster.health="" #초기화 이후 다시 할당
        
    #체력 업데이트 후 출력
    for _ in range(int(away_monster.bars)):
        away_monster.health+="="
        
    time.sleep(1)
    os.system("cls")
        
        
        #체력 게이지 소모 후 경기 종료
    if away_monster.bars<=0:
        delay_print(f"\n[{home_monster.name}] 승리하였습니다...")
        delay_print(f"\n[{away_monster.name}] 패배하였습니다...")
        sys.exit(0)
        
if __name__ =="__main__":
    #인사 출력 및 유저 몬스터 선택
    user_monster=create_monster(inital_display())
    #상대 몬스터 생성, 기본 "축축몬"
    other_monster=create_monster("축축몬")
            
            #생성된 몬스터 객체 확인
            #print(vars(user_monster))
            #print(vars(other_monster))
            
            #경기 시작
    inital_fight(user_monster, other_monster)
            
            
        
        
        
        
            
                
        
    
        
