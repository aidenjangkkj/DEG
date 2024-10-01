import pygame
import sys
import random
import time
import sys
from pygame.locals import *

# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLINK = [(224, 255, 255), (192, 240, 255), (128, 224, 255), (64, 192, 255), (128, 224, 255), (192, 240, 255)]



# 이미지 로딩
imgForestFloor=[
    pygame.image.load("image/tile/forest/floor.png"),
    pygame.image.load("image/tile/forest/tbox.png"),
    pygame.image.load("image/tile/forest/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgForestWall=pygame.image.load("image/tile/forest/wall.png")
imgForestWall2=pygame.image.load("image/tile/forest/wall2.png")


imgTownFloor=[
    pygame.image.load("image/tile/town/floor.png"),
    pygame.image.load("image/tile/town/tbox.png"),
    pygame.image.load("image/tile/town/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgTownWall=pygame.image.load("image/tile/town/wall.png")
imgTownWall2=pygame.image.load("image/tile/town/wall2.png")


imgShaftFloor=[
    pygame.image.load("image/tile/shaft/floor.png"),
    pygame.image.load("image/tile/shaft/tbox.png"),
    pygame.image.load("image/tile/shaft/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgShaftWall=pygame.image.load("image/tile/shaft/wall.png")
imgShaftWall2=pygame.image.load("image/tile/shaft/wall2.png")


imgLibFloor=[
    pygame.image.load("image/tile/lib/floor.png"),
    pygame.image.load("image/tile/lib/tbox.png"),
    pygame.image.load("image/tile/lib/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgLibWall=pygame.image.load("image/tile/lib/wall.png")
imgLibWall2=pygame.image.load("image/tile/lib/wall2.png")


imgLabFloor=[
    pygame.image.load("image/tile/lab/floor.png"),
    pygame.image.load("image/tile/lab/tbox.png"),
    pygame.image.load("image/tile/lab/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgLabWall=pygame.image.load("image/tile/lab/wall.png")
imgLabWall2=pygame.image.load("image/tile/lab/wall2.png")


imgFrostFloor=[
    pygame.image.load("image/tile/frost/floor.png"),
    pygame.image.load("image/tile/frost/tbox.png"),
    pygame.image.load("image/tile/frost/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgFrostWall=pygame.image.load("image/tile/frost/wall.png")
imgFrostWall2=pygame.image.load("image/tile/frost/wall2.png")


imgFlameFloor=[
    pygame.image.load("image/tile/flame/floor.png"),
    pygame.image.load("image/tile/flame/tbox.png"),
    pygame.image.load("image/tile/flame/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgFlameWall=pygame.image.load("image/tile/flame/wall.png")
imgFlameWall2=pygame.image.load("image/tile/flame/wall2.png")

imgDarkFloor=[
    pygame.image.load("image/tile/dark/floor.png"),
    pygame.image.load("image/tile/dark/tbox.png"),
    pygame.image.load("image/tile/dark/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgDarkWall=pygame.image.load("image/tile/dark/wall.png")
imgDarkWall2=pygame.image.load("image/tile/dark/wall2.png")

imgTimeFloor=[
    pygame.image.load("image/tile/time/floor.png"),
    pygame.image.load("image/tile/time/tbox.png"),
    pygame.image.load("image/tile/time/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgTimeWall=pygame.image.load("image/tile/time/wall.png")
imgTimeWall2=pygame.image.load("image/tile/time/wall2.png")

imgChaosFloor=[
    pygame.image.load("image/tile/chaos/floor.png"),
    pygame.image.load("image/tile/chaos/tbox.png"),
    pygame.image.load("image/tile/chaos/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgChaosWall=pygame.image.load("image/tile/chaos/wall.png")
imgChaosWall2=pygame.image.load("image/tile/chaos/wall2.png")

imgInfiFloor=[
    pygame.image.load("image/tile/infi/floor.png"),
    pygame.image.load("image/tile/infi/tbox.png"),
    pygame.image.load("image/tile/infi/cocoon.png"),
    pygame.image.load("image/stairs.png")
    ]
imgInfiWall=pygame.image.load("image/tile/infi/wall.png")
imgInfiWall2=pygame.image.load("image/tile/infi/wall2.png")

imgTitle = pygame.image.load("image/title.png")
imgDark = pygame.image.load("image/dark.png")
imgPara = pygame.image.load("image/parameter.png")


imgForestEnemy = [
    pygame.image.load("image/monster/forest/monster1.png"),
    pygame.image.load("image/monster/forest/monster2.png"),
    pygame.image.load("image/monster/forest/monster3.png"),
    pygame.image.load("image/monster/forest/monster4.png"),
    pygame.image.load("image/monster/forest/monster5.png")
    ]
imgShaftEnemy = [
    pygame.image.load("image/monster/shaft/monster1.png"),
    pygame.image.load("image/monster/shaft/monster2.png"),
    pygame.image.load("image/monster/shaft/monster3.png"),
    pygame.image.load("image/monster/shaft/monster4.png"),
    pygame.image.load("image/monster/shaft/monster5.png")
    ]
imgTownEnemy = [
    pygame.image.load("image/monster/town/monster1.png"),
    pygame.image.load("image/monster/town/monster2.png"),
    pygame.image.load("image/monster/town/monster3.png"),
    pygame.image.load("image/monster/town/monster4.png"),
    pygame.image.load("image/monster/town/monster5.png")
    ]
imgLibEnemy = [
    pygame.image.load("image/monster/lib/monster1.png"),
    pygame.image.load("image/monster/lib/monster2.png"),
    pygame.image.load("image/monster/lib/monster3.png"),
    pygame.image.load("image/monster/lib/monster4.png"),
    pygame.image.load("image/monster/lib/monster5.png")
    ]
imgLabEnemy = [
    pygame.image.load("image/monster/lab/monster1.png"),
    pygame.image.load("image/monster/lab/monster2.png"),
    pygame.image.load("image/monster/lab/monster3.png"),
    pygame.image.load("image/monster/lab/monster4.png"),
    pygame.image.load("image/monster/lab/monster5.png")
    ]
imgFrostEnemy = [
    pygame.image.load("image/monster/frost/monster1.png"),
    pygame.image.load("image/monster/frost/monster2.png"),
    pygame.image.load("image/monster/frost/monster3.png"),
    pygame.image.load("image/monster/frost/monster4.png"),
    pygame.image.load("image/monster/frost/monster5.png")
    ]
imgFlameEnemy = [
    pygame.image.load("image/monster/flame/monster1.png"),
    pygame.image.load("image/monster/flame/monster2.png"),
    pygame.image.load("image/monster/flame/monster3.png"),
    pygame.image.load("image/monster/flame/monster4.png"),
    pygame.image.load("image/monster/flame/monster5.png")
    ]
imgDarkEnemy = [
    pygame.image.load("image/monster/dark/monster1.png"),
    pygame.image.load("image/monster/dark/monster2.png"),
    pygame.image.load("image/monster/dark/monster3.png"),
    pygame.image.load("image/monster/dark/monster4.png"),
    pygame.image.load("image/monster/dark/monster5.png")
    ]
imgTimeEnemy = [
    pygame.image.load("image/monster/time/monster1.png"),
    pygame.image.load("image/monster/time/monster2.png"),
    pygame.image.load("image/monster/time/monster3.png"),
    pygame.image.load("image/monster/time/monster4.png"),
    pygame.image.load("image/monster/time/monster5.png")
    ]
imgChaosEnemy = [
    pygame.image.load("image/monster/chaos/monster1.png"),
    pygame.image.load("image/monster/chaos/monster2.png"),
    pygame.image.load("image/monster/chaos/monster3.png"),
    pygame.image.load("image/monster/chaos/monster4.png"),
    pygame.image.load("image/monster/chaos/monster5.png")
    ]

imgInfiEnemy = [imgForestEnemy,imgShaftEnemy,imgTownEnemy,
                imgLibEnemy,imgLabEnemy,imgFrostEnemy,
                imgFlameEnemy,imgDarkEnemy,imgTimeEnemy,imgChaosEnemy]

pygame.mixer.init()
bgmForest= pygame.mixer.Sound("music/bgm/forest.wav")
bgmShaft= pygame.mixer.Sound("music/bgm/shaft.wav")
bgmTown= pygame.mixer.Sound("music/bgm/town.wav")
bgmLib= pygame.mixer.Sound("music/bgm/lib.wav")
bgmLab= pygame.mixer.Sound("music/bgm/lab.wav")
bgmFrost= pygame.mixer.Sound("music/bgm/frost.wav")
bgmFlame= pygame.mixer.Sound("music/bgm/flame.wav")
bgmDark= pygame.mixer.Sound("music/bgm/dark.wav")
bgmTime= pygame.mixer.Sound("music/bgm/time.wav")
bgmChaos= pygame.mixer.Sound("music/bgm/chaos.wav")



sfxForestEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/forest/wolf.wav"),
    pygame.mixer.Sound( "music/monster_sfx/forest/ghost.wav"),
    pygame.mixer.Sound( "music/monster_sfx/forest/fairy.wav"),
    pygame.mixer.Sound( "music/monster_sfx/forest/spider.wav"),
    pygame.mixer.Sound( "music/monster_sfx/forest/forest_golem.wav")
]
sfxShaftEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/shaft/miner.wav"),
    pygame.mixer.Sound( "music/monster_sfx/shaft/stone_golem.wav"),
    pygame.mixer.Sound( "music/monster_sfx/shaft/ghost_miner.wav"),
    pygame.mixer.Sound( "music/monster_sfx/shaft/cave_bat.wav"),
    pygame.mixer.Sound( "music/monster_sfx/shaft/pain_beast.wav")
]
sfxTownEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/town/corrupted_human.wav"),
    pygame.mixer.Sound( "music/monster_sfx/town/death_witch.wav"),
    pygame.mixer.Sound( "music/monster_sfx/town/farmer.wav"),
    pygame.mixer.Sound( "music/monster_sfx/town/death_knight.wav"),
    pygame.mixer.Sound( "music/monster_sfx/town/dark_hound.wav")
]
sfxLibEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/lib/flying_book.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lib/guardian.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lib/ghost_of_magician.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lib/book_of_darkness.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lib/guardian.wav")
]
sfxLabEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/lab/creature.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lab/magic_creature.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lab/guardian.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lab/bat_of_darkness.wav"),
    pygame.mixer.Sound( "music/monster_sfx/lab/arcane_golem.wav")
]
sfxFrostEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/frost/wolf.wav"),
    pygame.mixer.Sound( "music/monster_sfx/frost/sprit.wav"),
    pygame.mixer.Sound( "music/monster_sfx/frost/spider.wav"),
    pygame.mixer.Sound( "music/monster_sfx/frost/golem.wav"),
    pygame.mixer.Sound( "music/monster_sfx/frost/drake.wav")
]
sfxFlameEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/flame/lion.wav"),
    pygame.mixer.Sound( "music/monster_sfx/flame/sprit.wav"),
    pygame.mixer.Sound( "music/monster_sfx/flame/spider.wav"),
    pygame.mixer.Sound( "music/monster_sfx/flame/golem.wav"),
    pygame.mixer.Sound( "music/monster_sfx/flame/knight.wav")
]
sfxDarkEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/dark/cultist.wav"),
    pygame.mixer.Sound( "music/monster_sfx/dark/demon.wav"),
    pygame.mixer.Sound( "music/monster_sfx/dark/sprit.wav"),
    pygame.mixer.Sound( "music/monster_sfx/dark/guardian.wav"),
    pygame.mixer.Sound( "music/monster_sfx/dark/lord.wav")
]
sfxTimeEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/time/watcher.wav"),
    pygame.mixer.Sound( "music/monster_sfx/time/wraith.wav"),
    pygame.mixer.Sound( "music/monster_sfx/time/sprit.wav"),
    pygame.mixer.Sound( "music/monster_sfx/time/Soldier.wav"),
    pygame.mixer.Sound( "music/monster_sfx/time/lord.wav")
]
sfxChaosEnemy = [
    pygame.mixer.Sound( "music/monster_sfx/chaos/Disciple.wav"),
    pygame.mixer.Sound( "music/monster_sfx/chaos/beast.wav"),
    pygame.mixer.Sound( "music/monster_sfx/chaos/sprit.wav"),
    pygame.mixer.Sound( "music/monster_sfx/chaos/knight.wav"),
    pygame.mixer.Sound( "music/monster_sfx/chaos/lord.wav")
]
sfxInfiEnemy = [sfxForestEnemy,
                sfxShaftEnemy,
                sfxTownEnemy,
                sfxLibEnemy,
                sfxLabEnemy,
                sfxFrostEnemy,
                sfxFlameEnemy,
                sfxDarkEnemy,
                sfxTimeEnemy,
                sfxChaosEnemy]



imgBase = pygame.image.load("image/background/base.png")
imgForest = pygame.image.load("image/background/forest.png")
imgShaft = pygame.image.load("image/background/shaft.png")
imgTown = pygame.image.load("image/background/town.png")
imgLib = pygame.image.load("image/background/lib.png")
imgLab = pygame.image.load("image/background/lab.png")
imgFrost = pygame.image.load("image/background/frost.png")
imgFlame = pygame.image.load("image/background/flame.png")
imgDark = pygame.image.load("image/background/dark.png")
imgTime = pygame.image.load("image/background/time.png")
imgChaos = pygame.image.load("image/background/chaos.png")
imgInfi = pygame.image.load("image/background/infi.png")

imgItem = [
    pygame.image.load("image/potion.png"),
    pygame.image.load("image/blaze_gem.png"),
    pygame.image.load("image/spoiled.png"),
    pygame.image.load("image/apple.png"),
    pygame.image.load("image/meat.png")
]
imgPlayer = [
    pygame.image.load("image/char/char0.png"),
    pygame.image.load("image/char/char1.png"),
    pygame.image.load("image/char/char2.png"),
    pygame.image.load("image/char/char3.png"),
    pygame.image.load("image/char/char4.png"),
    pygame.image.load("image/char/char5.png"),
    pygame.image.load("image/char/char6.png"),
    pygame.image.load("image/char/char7.png"),
    pygame.image.load("image/char/char8.png")
]
imgEffect = [
    pygame.image.load("image/effect_a.png"),
    pygame.image.load("image/effect_b.png")
]
font_path = "font/kodia.ttf"


# 변수 선언
speed = 1
idx = 0
tmr = 0
floor = 0
fl_max = 1
welcome = 0

pl_x = 0
pl_y = 0
pl_d = 0
pl_a = 0
pl_lifemax = 0
pl_life = 0
pl_str = 0
food = 0
potion = 0
blazegem = 0
treasure = 0

emy_name = ""
emy_lifemax = 0
emy_life = 0
emy_str = 0
emy_x = 0
emy_y = 0
emy_step = 0
emy_blink = 0

dmg_eff = 0
btl_cmd = 0
text_lines = [
    "한때 번영을 누리던 이 세계는 이제 고통과 절망에 빠져 있습니다.",
    "그 중심에는 끝없이 높이 솟은 '어둠의 탑' 이 자리 잡고 있습니다",
    "전설에 따르면, 탑의 꼭대기에는 세상을 구원하거나,",
    "완전히 멸망시킬 수 있는 강력한 유물이 숨겨져 있다고 합니다",
    "당신은 이 탑을 정복하려는 고독한 모험가입니다.",
    "과거의 상처와 개인적인 복수를 위해 이 위험천만한 여정을 떠납니다.",
    "목표는 단 하나, 탑의 정상에 도달하여 유물을 손에 넣는 것입니다."
]

COMMAND = ["[A] Attack", "[P]otion", "[B]laze gem", "[R]un"]
TRE_NAME = ["Potion", "Blaze gem", "Food spoiled.", "Food +20", "Food +100"]
FOREST_EMY_NAME = [
    "어둠의 늑대", "숲의 정령", "타락한 요정", "거미 군주", "숲의 골렘"
]
SHAFT_EMY_NAME = [
    "광기의 광부", "암석 괴물", "유령 광부", "동굴 박쥐", "고통의 괴수"
]
TOWN_EMY_NAME = [
    "타락한 주민", "죽음의 마녀", "부패한 농부", "어둠의 기사", "어둠의 개"
]
LIB_EMY_NAME = [
    "살아있는 책", "골렘", "마법사 유령", "어둠의 서적", "지식의 수호자"
]
LAB_EMY_NAME = [
    "변이 생물", "마법 실험체", "실험실 수호자", "변형된 박쥐", "마력의 골렘"
]
FROST_EMY_NAME = ["얼음 늑대","서리 정령","얼어붙은 거미","빙하 골렘","서리 드레이크"]

FLAME_EMY_NAME = ["화염의 사자","불길의 정령","용암 거미","화염 골렘","불의 기사"]

DARK_EMY_NAME = ["어둠의 신도","어둠의 악마","어둠의 정령","어둠의 수호자","어둠의 군주"]

TIME_EMY_NAME = ["시간의 감시자","시간의 망령","시공의 정령","시간의 병사","시간의 군주"]

CHAOS_EMY_NAME =["혼돈의 추종자", "혼돈의 사자","혼돈의 정령","혼돈의 기사","혼돈의 군주"]

INFI_EMY_NAME = [FOREST_EMY_NAME,SHAFT_EMY_NAME,TOWN_EMY_NAME,
                 LIB_EMY_NAME,LAB_EMY_NAME,FROST_EMY_NAME,
                 FLAME_EMY_NAME,DARK_EMY_NAME,TIME_EMY_NAME,CHAOS_EMY_NAME]


MAZE_W = 11
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0] * MAZE_W)

DUNGEON_W = MAZE_W * 3
DUNGEON_H = MAZE_H * 3
dungeon = []
for y in range(DUNGEON_H):
    dungeon.append([0] * DUNGEON_W)

def make_dungeon():  # 던전 자동 생성
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1, 0]
    # 테두리 벽
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W - 1] = 1
    # 가운데를 아무것도 없는 상태로 만듬
    for y in range(1, MAZE_H - 1):
        for x in range(1, MAZE_W - 1):
            maze[y][x] = 0
    # 기둥
    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            maze[y][x] = 1
    # 기둥에서 상하좌우로 벽 생성
    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            d = random.randint(0, 3)
            if x > 5:  # 2열부터 왼쪽에는 벽을 생성하지 않음
                d = random.randint(0, 2)
            maze[y + YP[d]][x + XP[d]] = 1

    # 미로에서 던전 생성
    # 전체를 벽으로
    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            dungeon[y][x] = 9
    # 방과 통로 배치
    for y in range(1, MAZE_H - 1):
        for x in range(1, MAZE_W - 1):
            dx = x * 3 + 1
            dy = y * 3 + 1
            if maze[y][x] == 0:
                if random.randint(0, 99) < 20:  # 방 생성
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            dungeon[dy + ry][dx + rx] = 0
                else:  # 통로 생성
                    dungeon[dy][dx] = 0
                    if maze[y - 1][x] == 0: dungeon[dy - 1][dx] = 0
                    if maze[y + 1][x] == 0: dungeon[dy + 1][dx] = 0
                    if maze[y][x - 1] == 0: dungeon[dy][dx - 1] = 0
                    if maze[y][x + 1] == 0: dungeon[dy][dx + 1] = 0

def draw_dungeon(bg, fnt):  # 던전 표시
    global floor, pl_x, pl_y, pl_a, dungeon
    if 0 < floor < 10:
        draw_floor(bg, fnt, imgForestFloor, imgForestWall, imgForestWall2)
    elif 10 <= floor < 20:
        draw_floor(bg, fnt, imgShaftFloor, imgShaftWall, imgShaftWall2)
    elif 20 <= floor < 30:
        draw_floor(bg, fnt, imgTownFloor, imgTownWall, imgTownWall2)
    elif 30 <= floor < 40:
        draw_floor(bg, fnt, imgLibFloor, imgLibWall, imgLibWall2)
    elif 40 <= floor < 50:
        draw_floor(bg, fnt, imgLabFloor, imgLabWall, imgLabWall2)
    elif 50 <= floor < 60:
        draw_floor(bg, fnt, imgFrostFloor, imgFrostWall, imgFrostWall2)
    elif 60 <= floor < 70:
        draw_floor(bg, fnt, imgFlameFloor, imgFlameWall, imgFlameWall2)
    elif 70 <= floor < 80:
        draw_floor(bg, fnt, imgDarkFloor, imgDarkWall, imgDarkWall2)
    elif 80 <= floor < 90:
        draw_floor(bg, fnt, imgTimeFloor, imgTimeWall, imgTimeWall2)    
    elif 90 <= floor < 100:
        draw_floor(bg, fnt, imgChaosFloor, imgChaosWall, imgChaosWall2)
    elif 100 <= floor:
        draw_floor(bg, fnt, imgInfiFloor, imgInfiWall, imgInfiWall2)

def draw_floor(bg, fnt, floor_img, wall_img, wall_img2):
    bg.fill(BLACK)
    for y in range(-4, 6):
        for x in range(-5, 6):
            X = (x + 5) * 80
            Y = (y + 4) * 80
            dx = pl_x + x
            dy = pl_y + y
            if 0 <= dx < DUNGEON_W and 0 <= dy < DUNGEON_H:
                if dungeon[dy][dx] <= 3:
                    bg.blit(floor_img[dungeon[dy][dx]], [X, Y])
                if dungeon[dy][dx] == 9:
                    bg.blit(wall_img, [X, Y - 40])
                    if dy >= 1 and dungeon[dy - 1][dx] == 9:
                        bg.blit(wall_img2, [X, Y - 80])
            if x == 0 and y == 0:  # 주인공 캐릭터 표시
                bg.blit(imgPlayer[pl_a], [X, Y - 40])
    bg.blit(imgDark, [0, 0])  # 네 모서리가 어두운 이미지 겹침
    draw_para(bg, fnt)  # 주인공 능력치 표시 

def put_event():  # 길에 이벤트 배치
    global pl_x, pl_y, pl_d, pl_a
    # 계단 배치
    while True:
        x = random.randint(3, DUNGEON_W - 4)
        y = random.randint(3, DUNGEON_H - 4)
        if (dungeon[y][x] == 0):
            for ry in range(-1, 2):  # 계단 주변을 길로 만듬
                for rx in range(-1, 2):
                    dungeon[y + ry][x + rx] = 0
            dungeon[y][x] = 3
            break
    # 보물 상자와 누에고치 배치
    for i in range(30):
        x = random.randint(3, DUNGEON_W - 4)
        y = random.randint(3, DUNGEON_H - 4)
        if (dungeon[y][x] == 0):
            dungeon[y][x] = random.choice([1, 2, 2, 2, 2]) #2는 싸움 1은 미정 리스투중 한개를 랜덤으로 대입
    # 플레이어 초기 위치
    while True:
        pl_x = random.randint(3, DUNGEON_W - 4)
        pl_y = random.randint(3, DUNGEON_H - 4)
        if (dungeon[pl_y][pl_x] == 0):
            break
    pl_d = 1
    pl_a = 2

def move_player(key):  # 주인공 이동
    global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life, food, potion, blazegem, treasure

    if dungeon[pl_y][pl_x] == 1:  # 보물상자에 닿음
        dungeon[pl_y][pl_x] = 0
        treasure = random.choice([0, 0, 0, 1, 1, 1, 1, 1, 1, 2])
        if treasure == 0:
            potion = potion + 1
        if treasure == 1:
            blazegem = blazegem + 1
        if treasure == 2:
            food = int(food + 50)
        idx = 3
        tmr = 0
        return
    if dungeon[pl_y][pl_x] == 2:  # 누에고치에 닿음
        dungeon[pl_y][pl_x] = 0
        r = random.randint(0, 99)
        if r < 40:  # 식량
            treasure = random.choice([3, 3, 3, 4])
            if treasure == 3: food = food + 20
            if treasure == 4: food = food + 100
            idx = 3
            tmr = 0
        else:  # 적 출현
            idx = 10
            tmr = 0
        return
    if dungeon[pl_y][pl_x] == 3:  # 계단에 닿음
        idx = 2
        tmr = 0
        return

    # 방향 키로 상하좌우 이동
    x = pl_x
    y = pl_y
    if key[K_UP] == 1:
        pl_d = 0
        if dungeon[pl_y - 1][pl_x] != 9:
            pl_y = pl_y - 1
    if key[K_DOWN] == 1:
        pl_d = 1
        if dungeon[pl_y + 1][pl_x] != 9:
            pl_y = pl_y + 1
    if key[K_LEFT] == 1:
        pl_d = 2
        if dungeon[pl_y][pl_x - 1] != 9:
            pl_x = pl_x - 1
    if key[K_RIGHT] == 1:
        pl_d = 3
        if dungeon[pl_y][pl_x + 1] != 9:
            pl_x = pl_x + 1
    pl_a = pl_d * 2
    if pl_x != x or pl_y != y:  # 이동 시 식량 및 체력 계산
        pl_a = pl_a + tmr % 2  # 이동 시 걷기 애니메이션
        if food > 0:
            food = food - 1
            if pl_life < pl_lifemax:
                pl_life = pl_life + 1
        else:
            pl_life = pl_life - 5
            if pl_life <= 0:
                pl_life = 0
                idx = 9
                tmr = 0

def draw_text(bg, txt, x, y, fnt, col):  # 그림자 포함한 문자 표시
    sur = fnt.render(txt, True, BLACK)
    bg.blit(sur, [x + 1, y + 2])
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])

def draw_para(bg, fnt):  # 주인공 능력 표시
    X = 30
    Y = 600
    bg.blit(imgPara, [X, Y])
    col = WHITE
    if pl_life < 10 and tmr % 2 == 0: col = RED
    draw_text(bg, "{}/{}".format(pl_life, pl_lifemax), X + 128, Y + 6, fnt, col)
    draw_text(bg, str(pl_str), X + 128, Y + 33, fnt, WHITE)
    col = WHITE
    if food == 0 and tmr % 2 == 0: col = RED
    draw_text(bg, str(food), X + 128, Y + 60, fnt, col)
    draw_text(bg, str(potion), X + 266, Y + 6, fnt, WHITE)
    draw_text(bg, str(blazegem), X + 266, Y + 33, fnt, WHITE)

def init_battle():  # 전투 시작 준비
    global imgEnemy, emy_name, emy_lifemax, emy_life, emy_str, emy_x, emy_y, sfxEnemy
    typ = random.randint(1, 5)
    if 1 <= floor <= 9:
        lev = random.randint(1, floor)
        sfxEnemy = sfxForestEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/forest/monster" + str(typ) + ".png"), (175, 230))
        emy_name = FOREST_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 10 <= floor <= 19:
        lev = random.randint(10, floor)
        sfxEnemy = sfxShaftEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/shaft/monster" + str(typ) + ".png"), (175, 230))
        emy_name = SHAFT_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 20 <= floor <= 29:
        lev = random.randint(20, floor)
        sfxEnemy = sfxTownEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/town/monster" + str(typ) + ".png"), (175, 230))
        emy_name = TOWN_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 30 <= floor <= 39:
        lev = random.randint(30, floor)
        sfxEnemy = sfxLibEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/lib/monster" + str(typ) + ".png"), (175, 230))
        emy_name = LIB_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 40 <= floor <= 49:
        lev = random.randint(40, floor)
        sfxEnemy = sfxLabEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/lab/monster" + str(typ) + ".png"), (175, 230))
        emy_name = LAB_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 50 <= floor <= 59:
        lev = random.randint(50, floor)
        sfxEnemy = sfxFrostEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/frost/monster" + str(typ) + ".png"), (175, 230))
        emy_name = FROST_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 60 <= floor <= 69:
        lev = random.randint(60, floor)
        sfxEnemy = sfxFlameEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/flame/monster" + str(typ) + ".png"), (175, 230))
        emy_name = FLAME_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 70 <= floor <= 79:
        lev = random.randint(70, floor)
        sfxEnemy = sfxDarkEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/dark/monster" + str(typ) + ".png"), (175, 230))
        emy_name = DARK_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 80 <= floor <= 89:
        lev = random.randint(80, floor)
        sfxEnemy = sfxTimeEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/time/monster" + str(typ) + ".png"), (175, 230))
        emy_name = TIME_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 90 <= floor <= 99:
        lev = random.randint(90, floor)
        sfxEnemy = sfxChaosEnemy[typ-1].play()
        imgEnemy = pygame.transform.scale(pygame.image.load("image/monster/chaos/monster" + str(typ) + ".png"), (175, 230))
        emy_name = CHAOS_EMY_NAME[typ-1] + " LV" + str(lev)
    elif 100<= floor :
        lev = random.randint(100, floor)
        sfxEnemy = sfxInfiEnemy[typ-1][typ-1].play()
        imgEnemy = pygame.transform.scale(imgInfiEnemy[typ-1][typ-1], (175, 230))
        emy_name = INFI_EMY_NAME[typ-1][typ-1] + " LV" + str(lev)
    
    emy_lifemax = 60 * (typ + 1) + (lev - 1) * 10
    emy_life = emy_lifemax
    emy_str = int(emy_lifemax / 8)
    emy_x = 440 - imgEnemy.get_width() / 2
    emy_y = 560 - imgEnemy.get_height()

def draw_bar(bg, x, y, w, h, val, ma):  # 적 체력 표시 게이지
    pygame.draw.rect(bg, WHITE, [x - 2, y - 2, w + 4, h + 4])
    pygame.draw.rect(bg, BLACK, [x, y, w, h])
    if val > 0:
        pygame.draw.rect(bg, (0, 128, 255), [x, y, w * val / ma, h])

def draw_battle(bg, fnt):  # 전투 화면 표시
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    if 1 <= floor <= 9:
        imgBtlBG = pygame.transform.scale(imgForest, (880, 720))
    elif 10 <= floor <= 19:
        imgBtlBG = pygame.transform.scale(imgShaft, (880, 720))
    elif 20 <= floor <= 29:
        imgBtlBG = pygame.transform.scale(imgTown, (880, 720))
    elif 30 <= floor <= 39:
        imgBtlBG = pygame.transform.scale(imgLib, (880, 720))
    elif 40 <= floor <= 49:
        imgBtlBG = pygame.transform.scale(imgLab, (880, 720))
    elif 50 <= floor <= 59:
        imgBtlBG = pygame.transform.scale(imgFrost, (880, 720))
    elif 60 <= floor <= 69:
        imgBtlBG = pygame.transform.scale(imgFlame, (880, 720))
    elif 70 <= floor <= 79:
        imgBtlBG = pygame.transform.scale(imgDark, (880, 720))
    elif 80 <= floor <= 89:
        imgBtlBG = pygame.transform.scale(imgTime, (880, 720))
    elif 90 <= floor <= 99:
        imgBtlBG = pygame.transform.scale(imgChaos, (880, 720))
    elif 90 <= floor <= 99:
        imgBtlBG = pygame.transform.scale(imgInfi, (880, 720))        
    
    bg.blit(imgBtlBG, [bx, by])
    if emy_life > 0 and emy_blink % 2 == 0:
        bg.blit(imgEnemy, [emy_x, emy_y + emy_step])
    draw_bar(bg, 340, 580, 200, 10, emy_life, emy_lifemax)
    if emy_blink > 0:
        emy_blink = emy_blink - 1
    for i in range(10):  # 전투 메시지 표시
        draw_text(bg, message[i], 600, 100 + i * 50, fnt, WHITE)
    draw_para(bg, fnt)  # 주인공 능력 표시

def battle_command(bg, fnt, key):  # 커맨드 입력 및 표시
    global btl_cmd
    ent = False
    if key[K_a]:  # A 키
        btl_cmd = 0
        ent = True
    if key[K_p]:  # P 키
        btl_cmd = 1
        ent = True
    if key[K_b]:  # B 키
        btl_cmd = 2
        ent = True
    if key[K_r]:  # R 키
        btl_cmd = 3
        ent = True
    if key[K_UP] and btl_cmd > 0:  # ↑ 키
        btl_cmd -= 1
    if key[K_DOWN] and btl_cmd < 3:  # ↓ 키
        btl_cmd += 1
    if key[K_SPACE] or key[K_RETURN]:
        ent = True
    for i in range(4):
        c = WHITE
        if btl_cmd == i: c = BLINK[tmr % 6]
        draw_text(bg, COMMAND[i], 20, 360 + i * 60, fnt, c)
    return ent

# 전투 메시지 표시 처리
message = [""] * 10
def init_message():
    for i in range(10):
        message[i] = ""

def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i + 1]
    message[9] = msg

def middleimage(): #계층 구분
    image_displayed = True
    screen = pygame.display.set_mode((880, 720))
    font = pygame.font.Font(font_path, 40)
    if floor == 0:
        if  image_displayed:
            screen.blit(pygame.transform.scale(imgForest, (880, 720)), (0, 0))
            draw_text(screen, "절망의 숲", 250, 560, font,WHITE)
            pygame.display.update()
            bgmForest.play(-1)
            pygame.time.wait(2000)
            image_displayed = False
    if floor == 10:
        if  image_displayed:
            bgmForest.stop()
            screen.blit(pygame.transform.scale(imgShaft, (880, 720)), (0, 0))
            draw_text(screen, "고통의 갱도", 250, 560, font,WHITE)
            pygame.display.update()
            bgmShaft.play(-1)
            pygame.time.wait(2000)
            image_displayed = False
    if floor == 20:
        if  image_displayed:
            bgmShaft.stop()
            screen.blit(pygame.transform.scale(imgTown, (880, 720)), (0, 0))
            draw_text(screen, "부패의 마을", 250, 560, font,WHITE)
            pygame.display.update()
            bgmTown.play(-1)
            pygame.time.wait(2000)
            image_displayed = False            
    if floor == 30:
        if  image_displayed:
            bgmTown.stop()
            screen.blit(pygame.transform.scale(imgLib, (880, 720)), (0, 0))
            draw_text(screen, "망각의 도서관", 250, 560, font,WHITE)
            pygame.display.update()
            bgmLib.play(-1)
            pygame.time.wait(2000)
            image_displayed = False            
    if floor == 40:
        if  image_displayed:
            bgmLib.stop()
            screen.blit(pygame.transform.scale(imgLab, (880, 720)), (0, 0))
            draw_text(screen, "마력의 실험실", 250, 560, font,WHITE)
            pygame.display.update()
            bgmLab.play(-1)
            pygame.time.wait(2000)
            image_displayed = False            
    if floor == 50:
        if  image_displayed:
            bgmLab.stop()
            screen.blit(pygame.transform.scale(imgFrost, (880, 720)), (0, 0))
            draw_text(screen, "서리 동굴", 250, 560, font,WHITE)
            pygame.display.update()
            bgmFrost.play(-1)
            pygame.time.wait(2000)
            image_displayed = False   
    if floor == 60:
        if  image_displayed:
            bgmFrost.stop()
            screen.blit(pygame.transform.scale(imgFlame, (880, 720)), (0, 0))
            draw_text(screen, "화염의 제단", 250, 560, font,WHITE)
            pygame.display.update()
            bgmFlame.play(-1)
            pygame.time.wait(2000)
            image_displayed = False   
    if floor == 70:
        if  image_displayed:
            bgmFlame.stop()
            screen.blit(pygame.transform.scale(imgDark, (880, 720)), (0, 0))
            draw_text(screen, "어둠의 성소", 250, 560, font,WHITE)
            pygame.display.update()
            bgmDark.play(-1)
            pygame.time.wait(2000)
            image_displayed = False   
    if floor == 80:
        if  image_displayed:
            bgmDark.stop()
            screen.blit(pygame.transform.scale(imgTime, (880, 720)), (0, 0))
            draw_text(screen, "초월한 시간", 250, 560, font,WHITE)
            pygame.display.update()
            bgmTime.play(-1)
            pygame.time.wait(2000)
            image_displayed = False   
    if floor == 90:
        if  image_displayed:
            bgmTime.stop()
            screen.blit(pygame.transform.scale(imgChaos, (880, 720)), (0, 0))
            draw_text(screen, "혼돈의 차원", 250, 560, font,WHITE)
            pygame.display.update()
            bgmChaos.play(-1)
            pygame.time.wait(2000)
            image_displayed = False
    if floor == 100:
        if  image_displayed:
            screen.blit(pygame.transform.scale(imgInfi, (880, 720)), (0, 0))
            draw_text(screen, "무한한 공간", 250, 560, font,WHITE)
            pygame.display.update()
            pygame.time.wait(2000)
            image_displayed = False            

def display_text():
    once = True
    screen_width = 880
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(font_path, 20)
    screen.blit(pygame.transform.scale(imgBase, (880, 720)), (0, 0))
    if once:
    # 각 줄의 텍스트를 화면에 렌더링
        total_text_height = len(text_lines) * font.get_linesize() + (len(text_lines) - 1) * 10
        y_offset = (screen_height - total_text_height) // 2  # 텍스트 블록의 시작 y 위치
        for line in text_lines:
            text_surface = font.render(line, True, WHITE)
            text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset + font.get_linesize() // 2))
            screen.blit(text_surface, text_rect)
            y_offset += font.get_linesize() + 10
        pygame.display.update()
        pygame.time.wait(8000)
        once = False
def emy_pattern(emy_dmg, stunState, emy_life):
    random_number = random.randint(1, 4)
    if random_number == 1:
        set_message("일반 공격!")
        set_message(str(emy_dmg) + "pts of damage!")
        return emy_dmg, stunState, emy_life
    
    elif random_number == 2:
        emy_dmg = emy_dmg * 2
        set_message("강타!")
        set_message(str(emy_dmg) + "pts of damage!")
        return emy_dmg, stunState, emy_life
    
    elif random_number == 3:
        set_message("회복!")
        set_message(str(emy_dmg) + "pts of heal!")
        emy_life = emy_life + emy_dmg
        return emy_dmg, stunState, emy_life
    
    elif random_number == 4:  
        set_message("기절!")
        emy_dmg = emy_dmg / 2
        stunState = True
        return emy_dmg, stunState, emy_life


def main():  # 메인 처리
    global speed, idx, tmr, floor, fl_max, welcome
    global pl_a, pl_lifemax, pl_life, pl_str,pl_dmg, food, potion, blazegem
    global emy_life, emy_step, emy_blink, dmg_eff, emy_dmg
    global stunState
    stunState=False
    lif_p = 0
    str_p = 0

    pygame.init()
    pygame.display.set_caption("One hour Dungeon")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(font_path, 30)
    fontS = pygame.font.Font(font_path, 20)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_j:  # 'j' 키를 눌렀을 때 floor 변수를 증가
                    floor += 1
            if event.type == KEYDOWN:
                if event.key == K_k:  # 'h' 키를 눌렀을 때 계단판정
                    idx = 2
                    tmr = 0
            if event.type == KEYDOWN:
                if event.key == K_h:  # 'h' 키를 눌렀을 때 floor 변수를 감소
                    floor -= 1
            if event.type == KEYDOWN:
                if event.key == K_o:  # 'O' 키를 눌렀을 때 전투 블록 판정
                    idx = 10
                    tmr = 0
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_s: # 's' 키를 눌렀을 때 speed 변수를 증가 즉 게임 속도 업
                    speed = speed + 1
                    if speed == 4: 
                        speed = 1
        

        tmr = tmr + 1
        key = pygame.key.get_pressed()

        if idx == 0:  # 타이틀 화면
            screen.fill(BLACK)
            screen.blit(imgTitle, [40, 60])
            if fl_max >= 2:
                draw_text(screen, "You reached floor {}.".format(fl_max), 300, 460, font, CYAN)
            draw_text(screen, "Press Space Key", 320, 560, font, BLINK[tmr % 6])
            if key[K_SPACE] == 1:
                idx = 4
        
        elif idx == 4:
            display_text()
            middleimage()
            make_dungeon()
            put_event()
            floor = 1
            welcome = 15
            pl_lifemax = 300
            pl_life = pl_lifemax
            pl_str = 100
            food = 300
            potion = 0
            blazegem = 0
            idx=1

        elif idx == 1:  # 플레이어 이동
            move_player(key)
            draw_dungeon(screen, fontS)
            draw_text(screen, "floor {} ({},{})".format(floor, pl_x, pl_y), 60, 40, fontS, WHITE)
            if welcome > 0:
                welcome = welcome - 1
                draw_text(screen, "Welcome to floor {}.".format(floor), 300, 180, font, CYAN)

        elif idx == 2:  # 화면 전환
            draw_dungeon(screen, fontS)
            if 1 <= tmr and tmr <= 5:
                h = 80 * tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720 - h, 880, h])
            if tmr == 5:
                floor = floor + 1
                middleimage()
                if floor > fl_max:
                    fl_max = floor
                welcome = 15
                make_dungeon()
                put_event()
            if 6 <= tmr and tmr <= 9:
                h = 80 * (10 - tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720 - h, 880, h])
            if tmr == 10:
                idx = 1

        elif idx == 3:  # 아이템 입수 혹은 함정
            draw_dungeon(screen, fontS)
            screen.blit(imgItem[treasure], [320, 220])
            draw_text(screen, TRE_NAME[treasure], 380, 240, font, WHITE)
            if tmr == 10:
                idx = 1

        elif idx == 9:  # 게임 오버
            if tmr <= 30:
                PL_TURN = [2, 4, 0, 6]
                pl_a = PL_TURN[tmr % 4]
                if tmr == 30: pl_a = 8  # 쓰러진 그림
                draw_dungeon(screen, fontS)
            elif tmr == 31:
                draw_text(screen, "You died.", 360, 240, font, RED)
                draw_text(screen, "Game over.", 360, 380, font, RED)
            elif tmr == 100:
                idx = 0
                tmr = 0

        elif idx == 10:  # 전투 시작
            if tmr == 1:
                init_battle()
                init_message()
            elif tmr <= 4:
                bx = (4 - tmr) * 220
                by = 0
                if 1 <= floor <= 9:
                    imgBtlBG = pygame.transform.scale(imgForest, (880, 720))
                elif 10 <= floor <= 19:
                    imgBtlBG = pygame.transform.scale(imgShaft, (880, 720))
                elif 20 <= floor <= 29:
                    imgBtlBG = pygame.transform.scale(imgTown, (880, 720))
                elif 30 <= floor <= 39:
                    imgBtlBG = pygame.transform.scale(imgLib, (880, 720))
                elif 40 <= floor <= 49:
                    imgBtlBG = pygame.transform.scale(imgLab, (880, 720))
                elif 50 <= floor <= 59:
                    imgBtlBG = pygame.transform.scale(imgFrost, (880, 720))
                elif 60 <= floor <= 69:
                    imgBtlBG = pygame.transform.scale(imgFlame, (880, 720))
                elif 70 <= floor <= 79:
                    imgBtlBG = pygame.transform.scale(imgDark, (880, 720))
                elif 80 <= floor <= 89:
                    imgBtlBG = pygame.transform.scale(imgTime, (880, 720))
                elif 90 <= floor <= 99:
                    imgBtlBG = pygame.transform.scale(imgChaos, (880, 720))
                elif 99 <= floor:
                    imgBtlBG = pygame.transform.scale(imgInfi, (880, 720))     
                
                screen.blit(imgBtlBG, [bx, by])
                draw_text(screen, "Encounter!", 350, 200, font, WHITE)
            elif tmr <= 16:
                draw_battle(screen, fontS)
                draw_text(screen, emy_name + " appear!", 300, 200, font, WHITE)
            else:
                idx = 11
                tmr = 0

        elif idx == 11:  # 플레이어 턴(입력 대기)
            draw_battle(screen, fontS)
            if tmr == 1: set_message("Your turn.")
            if battle_command(screen, font, key) == True:
                if btl_cmd == 0:
                    idx = 12
                    tmr = 0
                if btl_cmd == 1 and potion > 0:
                    idx = 20
                    tmr = 0
                if btl_cmd == 2 and blazegem > 0:
                    idx = 21
                    tmr = 0
                if btl_cmd == 3:
                    idx = 14
                    tmr = 0

        elif idx == 12:  # 플레이어 공격
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("You attack!")
                pl_dmg = pl_str + random.randint(0, 9)
            if 2 <= tmr and tmr <= 4:
                screen.blit(imgEffect[0], [700 - tmr * 120, -100 + tmr * 120])
            if tmr == 5:
                emy_blink = 5
                set_message(str(pl_dmg) + "pts of damage!")
            if tmr == 11:
                emy_life = emy_life - pl_dmg
                if emy_life <= 0:
                    emy_life = 0
                    idx = 16
                    tmr = 0
            if tmr == 16:
                idx = 13
                tmr = 0

        elif idx == 13:  # 적 턴, 적 공격
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Enemy turn.")
            if tmr == 5:
                set_message(emy_name + " attack!")
                emy_step = 30
            if tmr == 9:
                emy_dmg = emy_str + random.randint(0, 9)
                emy_dmg, stunState, emy_life=emy_pattern(emy_dmg,stunState,emy_life)
                dmg_eff = 5
                emy_step = 0

            if tmr == 15:
                pl_life = pl_life - emy_dmg
                if pl_life < 0:
                    pl_life = 0
                    idx = 15
                    tmr = 0
            if (tmr == 20 and stunState):
                idx = 13
                tmr = 0
                stunState = False
            if (tmr == 20 and not stunState):
                idx = 11
                tmr = 0



        elif idx == 14:  # 도망 가능한가?
            draw_battle(screen, fontS)
            if tmr == 1: set_message("...")
            if tmr == 2: set_message("......")
            if tmr == 3: set_message(".........")
            if tmr == 4: set_message("............")
            if tmr == 5:
                if random.randint(0, 99) < 60:
                    idx = 22
                else:
                    set_message("You failed to flee.")
            if tmr == 10:
                idx = 13
                tmr = 0

        elif idx == 15:  # 패배
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("You lose.")
            if tmr == 11:
                idx = 9
                tmr = 29

        elif idx == 16:  # 승리
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("You win!")
            if tmr == 28:
                idx = 22
                if random.randint(0, emy_lifemax) > random.randint(0, pl_lifemax):
                    idx = 17
                    tmr = 0

        elif idx == 17:  # 레벨업
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Level up!")
                lif_p = random.randint(10, 20)
                str_p = random.randint(5, 10)
            if tmr == 21:
                set_message("Max life + " + str(lif_p))
                pl_lifemax = pl_lifemax + lif_p
            if tmr == 26:
                set_message("Str + " + str(str_p))
                pl_str = pl_str + str_p
            if tmr == 50:
                idx = 22

        elif idx == 20:  # Potion
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Potion!")
            if tmr == 6:
                pl_life = pl_lifemax
                potion = potion - 1
            if tmr == 11:
                idx = 13
                tmr = 0

        elif idx == 21:  # Blaze gem
            draw_battle(screen, fontS)
            img_rz = pygame.transform.rotozoom(imgEffect[1], 30 * tmr, (12 - tmr) / 8)
            X = 440 - img_rz.get_width() / 2
            Y = 360 - img_rz.get_height() / 2
            screen.blit(img_rz, [X, Y])
            if tmr == 1:
                set_message("Blaze gem!")
            if tmr == 6:
                blazegem = blazegem - 1
            if tmr == 11:
                dmg = 1000
                idx = 12
                tmr = 4

        elif idx == 22:  # 전투 종료
            idx = 1

        draw_text(screen, "[S]peed " + str(speed), 740, 40, fontS, WHITE)

        pygame.display.update()
        clock.tick(4 + 2 * speed)

if __name__ == '__main__':
    main()
