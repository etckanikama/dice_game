import dice

num = input('4面体,6面体,8面体,12面体,20面体のサイコロがあります。これらのどれを選びますか？：')
num = int(num)
my_dice = dice.Dice(num)
cpu_dice = dice.Dice(num)

my_pip = my_dice.shoot()
cpu_pip = cpu_dice.shoot()

print('CPU: {}/ あなた: {}'.format(cpu_pip, my_pip))
if my_pip > cpu_pip:
    print('おめでとう！あなたの勝ち。')
elif my_pip < cpu_pip:
    print('残念。あなたの負け。')
else:
    print('引き分け')