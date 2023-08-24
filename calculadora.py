from time import sleep
print('========== BEM VINDO ==========')
sleep(1)
nome = str(input('Digite seu nome: '))
print('Muito prazer!, vamos calcular sua premiação,', nome, '?')
sleep(1)
target = float(input('Digite o seu TARGET: '))
print('Vamos começar pelo MERCANTIL: ')
sleep(1)
mer = float(input('Qual é a sua meta MERCANTIL? '))
pmer = 30 / 100 * target
mer1 = float(input('Quanto a sua loja fez de MERCANTIL? '))
print('Calculando...')
sleep(2)
if mer1 < mer:
    print('Sua loja não atingiu a meta MERCANTIL, que pena!')
elif mer1 == mer:
    print('Sua premiação será de R${}, PARABÉNS!'.format(pmer))
elif 101 / 100 * mer <= mer1 < 105 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNSa!'.format(pmer))
elif 105 / 100 * mer <= mer1 < 110 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(110 / 100 * pmer))
elif 110 / 100 * mer <= mer1 < 115 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(120 / 100 * pmer))
elif 115 / 100 * mer <= mer1 < 120 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(130 / 100 * pmer))
elif 120 / 100 * mer <= mer1 < 125 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(140 / 100 * pmer))
elif 125 / 100 * mer <= mer1 < 130 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(150 / 100 * pmer))
elif 130 / 100 * mer <= mer1 < 135 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(160 / 100 * pmer))
elif 135 / 100 * mer <= mer1 < 140 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(170 / 100 * pmer))
elif 140 / 100 * mer <= mer1 < 145 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(180 / 100 * pmer))
elif 145 / 100 * mer <= mer1 < 150 / 100 * mer:
    print('Sua premiação será de R${} PARABÉNS!'.format(100 / 100 * pmer))
elif mer1 == 150 / 100 * mer:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(200 / 100 * pmer))
print('Ótimo, agora vamos calcular seu prêmio de serviços de BALCÃO: ')
sleep(1)
bal = float(input('Qual a sua meta de BALCÃO? '))
pbal = 50 / 100 * target
bal1 = float(input('Quanto a sua loja fez de BALCÃO? '))
print('Calculando...')
sleep(2)
if bal1 < bal:
    print('Sua loja não atingiu a meta de BALCÃO, que pena!')
elif bal1 == bal < 105 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(pbal))
elif 101 / 100 * bal <= bal1 < 105 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(pbal))
elif 105 / 100 * bal <= bal1 < 110 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(110 / 100 * pbal))
elif 110 / 100 * bal <= bal1 < 115 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(120 / 100 * pbal))
elif 115 / 100 * bal <= bal1 < 120 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(130 / 100 * pbal))
elif 120 / 100 * bal <= bal1 < 125 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(140 / 100 * pbal))
elif 125 / 100 * bal <= bal1 < 130 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(150 / 100 * pbal))
elif 130 / 100 * bal <= bal1 < 135 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(160 / 100 * pbal))
elif 135 / 100 * bal <= bal1 < 140 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(170 / 100 * pbal))
elif 140 / 100 * bal <= bal1 < 145 / 100 * bal:
    print('Sua premiação será de R${} PARABÉNS!'.format(180 / 100 * pbal))
elif 145 / 100 * bal <= bal1 < 150 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(190 / 100 * pbal))
elif bal1 >= 150 / 100 * bal:
    print('Sua premiação será de R${} ,PARABÉNS!'.format(200 / 100 * pbal))
print('Por último vamos calcular o seu IQV: ')
sleep(1)
i40 = 4.0
i41 = 4.1
i42 = 4.2
i43 = 4.3
i44 = 4.4
i45 = 4.5
i46 = 4.6
i47 = 4.7
i48 = 4.8
i49 = 4.9
i50 = 5.0
iqv = float(input('Digite a nota que a sua loja atingiu no IQV: '))
print('Calculando...')
sleep(2)
piqv = 20 / 100 * target
if iqv < i40:
    print('Sua loja não atingiu a nota mínima para premiar no IQV, que pena!')
elif iqv == i40:
    print('Sua premiação será de R${} , PARABÉNS!'.format(piqv))
elif iqv == i41:
    print('Sua premiação será de R${} , PARABÉNS!'.format(110 / 100 * piqv))
elif iqv == i42:
    print('Sua premiação será de R${} , PARABÉNS!'.format(120 / 100 * piqv))
elif iqv == i43:
    print('Sua premiação será de R${} , PARABÉNS!'.format(130 / 100 * piqv))
elif iqv == i44:
    print('Sua premiação será de R${} , PARABÉNS!'.format(140 / 100 * piqv))
elif iqv == i45:
    print('Sua premiação será de R${} , PARABÉNS!'.format(150 / 100 * piqv))
elif iqv == i46:
    print('Sua premiação será de R${} , PARABÉNS!'.format(160 / 100 * piqv))
elif iqv == i47:
    print('Sua premiação será de R${} , PARABÉNS!'.format(170 / 100 * piqv))
elif iqv == i48:
    print('Sua premiação será de R${} , PARABÉNS!'.format(180 / 100 * piqv))
elif iqv == i49:
    print('Sua premiação será de R${} , PARABÉNS!'.format(190 / 100 * piqv))
elif iqv == i50:
    print('Sua premiação será de R${} , PARABÉNS!'.format(200 / 100 * piqv))
print('Obrigado por utilizar nosso sistema! =)')
print('==========FIM==========')
