#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    #salários até R$ 280,00 (incluindo) : aumento de 20%
    #salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    #salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    #salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    #o salário antes do reajuste;
    #o percentual de aumento aplicado;
    #o valor do aumento;
    #o novo salário, após o aumento.

wage_receiver = float(input('Type your wage: '))
new_wage = float(0)
wage_rise = 0
percentage = 0
i = 1

while i == 1:
    if wage_receiver > 0 and wage_receiver <= 280:
        wage_rise = wage_receiver * 0.20
        new_wage = wage_receiver + wage_rise
        percentage = 20
        i = 0
        
    elif wage_receiver > 280 and wage_receiver <= 700:
        wage_rise = wage_receiver * 0.15
        new_wage = wage_receiver + wage_rise
        percentage = 15
        i = 0
    
    elif wage_receiver > 700 and wage_receiver <= 1500:
        wage_rise = wage_receiver * 0.10
        new_wage = wage_receiver + wage_rise
        percentage = 10
        i = 0
        
    elif wage_receiver > 1500:
        wage_rise = wage_receiver * 0.05
        new_wage = wage_receiver + wage_rise
        percentage = 5
        i = 0
    
    else:
        print('Type a valid number.\n')
        
        
    if i == 0:
        print(f'''Old wage: {wage_receiver}
Rise value: {wage_rise}
Percentage = {percentage}%
New wage = {new_wage}''')
        
