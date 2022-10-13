import model
import logger

def get_exp():#метод получения информации
    return input()

def sow_result(a):#метод  вывода информации
    print(a)

exp = get_exp()
answer = model.eval_exp(exp)#получение корне
logger.log_exp(exp)
logger.log_answ(answer)
sow_result(answer)#вывод корней