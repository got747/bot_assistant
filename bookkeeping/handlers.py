from aiogram import types 

from aiogram.dispatcher import FSMContext

from . import keyboard as kb
from loader import bot
from bookkeeping.states import StepsToCalculatePayment 

async def process_callback_daily_payment_plan(callback_query: types.CallbackQuery):
    print("process_callback_daily_payment_plan message:")

    test_message = "<strong>Окей</strong>, \n Считаем <strong>день</strong>. \n Сколько было зазывал?"

    await StepsToCalculatePayment.waiting_for_the_number_of_touts.set()
     
    await bot.send_message(callback_query.from_user.id, test_message, reply_markup=kb.keyboard_payment_process_management, parse_mode=types.ParseMode.HTML)
    await bot.answer_callback_query(callback_query.id)

async def finished_payment_process(callback_query: types.CallbackQuery, state: FSMContext):
    print("finished_payment_process message:")

    test_message = "Чтобы это не было, я это постарался закончить "
    await state.finish() 

    await bot.send_message(callback_query.from_user.id, test_message, parse_mode=types.ParseMode.HTML)
    await bot.answer_callback_query(callback_query.id)
  
async def get_inf_about_touts(message: types.Message, state: FSMContext):
    print("get_inf_about_touts message:", message.text)
    if message.text.isdigit():
        
        current_state_date = await state.get_data()
        int_from_message = int(message.text)
        print("get_inf_about_touts message:",current_state_date)

        if 'number_touts' not in current_state_date and 'counter_touts' not in current_state_date and 'list_money_brought_by_touts' not in current_state_date:
            number_touts = counter_touts = int_from_message
            if number_touts < 1:
                await message.answer("Зазывал не может быть меньше 1")
            else:
                await state.update_data(number_touts = number_touts, counter_touts = counter_touts - 1, list_money_brought_by_touts = [])
                await message.answer(f"Хорошо, кол-во зазывал: {number_touts} \nВведи на сколько собрал зазывала №{number_touts - (counter_touts - 1)}")                
        else:  
            current_state_date['list_money_brought_by_touts'].append(int_from_message)
            await state.update_data(list_money_brought_by_touts = current_state_date['list_money_brought_by_touts'])  

            if  current_state_date['counter_touts'] > 0:
                await state.update_data(counter_touts = current_state_date['counter_touts'] - 1)
                await message.answer(f"Введи на сколько собрал зазывала №{current_state_date['number_touts'] - (current_state_date['counter_touts'] - 1)}")

            else:
                 await message.answer("Супер, ты ввел всю информацию по зазывалам.\nВведи солько работало катеров")
                 await StepsToCalculatePayment.next()

    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_inf_about_boats(message: types.Message, state: FSMContext):
    print("get_inf_about_boats message:", message.text)
    if message.text.isdigit():
        current_state_date = await state.get_data()
        int_from_message = int(message.text)
        print("get_inf_about_boats message:",current_state_date)

        if ( 'number_boats' not in current_state_date 
                and 'counter_boats' not in current_state_date 
                and 'list_number_cruise_boats' not in current_state_date):          

            number_boats = counter_boats = int_from_message

            if number_boats < 1:
                await message.answer("Катеров не может быть меньше 1")
            else:
                await state.update_data(number_boats = number_boats, counter_boats = counter_boats - 1 , list_number_cruise_boats = [], list_with_general_overloads_for_boats = [])
                await message.answer(f"Хорошо, кол-во катеров: {number_boats} \nВведи на сколько рейсов сделал катер №{number_boats - (counter_boats - 1)}")
        else: 

            current_state_date['list_number_cruise_boats'].append(int_from_message)
            await state.update_data(list_number_cruise_boats = current_state_date['list_number_cruise_boats'])

            if  current_state_date['counter_boats'] > 0:
                await state.update_data(counter_boats = current_state_date['counter_boats'] - 1)
                await message.answer(f"Введи на сколько рейсов сделал рейсов катер №{current_state_date['number_boats'] - (current_state_date['counter_boats'] - 1)}")

            else:
                 await message.answer(f"Супер, ты ввел сколько рейсов сделали катера.\n"
                                    f"Введи сколько катер №{current_state_date['number_boats'] - (current_state_date['number_boats'] - 1 )} взял зайцев")
                 await state.update_data(counter_boats = current_state_date['number_boats'] - 1)
                 await StepsToCalculatePayment.next()                
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_inf_about_overloads_cruises(message: types.Message, state: FSMContext):
    print("get_inf_about_overloads_cruises message:", message.text)
    if message.text.isdigit():
        
        int_from_message = int(message.text)
        current_state_date = await state.get_data()

        if 'list_with_general_overloads_for_boats' not in current_state_date:
            await state.update_data(list_with_general_overloads_for_boats = [int_from_message])
        else:
            current_state_date['list_with_general_overloads_for_boats'].append(int_from_message) 
            await state.update_data(list_with_general_overloads_for_boats = current_state_date['list_with_general_overloads_for_boats'])
      
        if  current_state_date['counter_boats'] > 0:
            await state.update_data(counter_boats = current_state_date['counter_boats'] - 1)
            await message.answer(f"Введи сколько зайцев взял катер №{current_state_date['number_boats'] - (current_state_date['counter_boats'] - 1)}")
        else:
            await message.answer(f"Информация по всем катерам введена.\n"
                                    "Дело за малым\n"
                                    "Введи сколко было получено наличных за рейсы")
            await StepsToCalculatePayment.next()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_how_amount_of_cash_for_cruises(message: types.Message, state: FSMContext):
    print("get_how_amount_of_cash_for_cruises message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_cash_for_cruises.__name__, state)
        int_from_message = int(message.text)
        await state.update_data(cash_for_cruises = int_from_message)
        await message.answer(f"Ого! А сколько вышло по Б/Н")
        await StepsToCalculatePayment.next()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_how_amount_of_non_cash_for_cruises(message: types.Message, state: FSMContext):
    print("get_how_amount_of_non_cash_for_cruises message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_non_cash_for_cruises.__name__, state)
        int_from_message = int(message.text)
        await state.update_data(non_cash_for_cruises = int_from_message)
        await message.answer(f"Не плохо! За бар наличными сколько получилось?")
        await StepsToCalculatePayment.next()
    else: 
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_how_amount_of_cash_for_bar(message: types.Message, state: FSMContext):
    print("get_how_amount_of_cash_for_bar message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_cash_for_bar.__name__, state)
        int_from_message = int(message.text)
        await state.update_data(cash_for_bar = int_from_message)
        await message.answer(f"Тут будет текст! За бар Б/Н сколько получилось?")
        await StepsToCalculatePayment.next()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")
        
async def get_how_amount_of_cash_for_bar(message: types.Message, state: FSMContext):
    print("get_how_amount_of_cash_for_bar message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_cash_for_bar.__name__, state)
        int_from_message = int(message.text)
        await state.update_data(cash_for_bar = int_from_message)
        await message.answer(f"Тут будет текст! За бар Б/Н сколько получилось?")
        await StepsToCalculatePayment.next()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_how_amount_of_non_cash_for_bar(message: types.Message, state: FSMContext):
    print("get_how_amount_of_non_cash_for_bar message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_non_cash_for_bar.__name__, state)
        int_from_message = int(message.text)
        await state.update_data(non_cash_for_bar = int_from_message)
        await message.answer(f"Тут будет текст! Сумма Б/Н за сувенирку?")
        
        await StepsToCalculatePayment.next()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_how_much_was_paid_in_cash(message: types.Message, state: FSMContext):
    print("get_how_much_was_paid_in_cash message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_non_cash_for_souvenirs.__name__, state)

        int_from_message = int(message.text)
        await state.update_data(salaries_given_out_cash = int_from_message)

        await message.answer(f"Теперь введи сколько выплатили Б/Н", reply_markup=kb.keyboard_payment_process_management)        
        await StepsToCalculatePayment.waiting_for_how_much_was_paid_in_non_cash.set()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_how_much_was_paid_in_non_cash(message: types.Message, state: FSMContext):
    print("get_how_much_was_paid_in_non_cash message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_non_cash_for_souvenirs.__name__, state)

        int_from_message = int(message.text)
        await state.update_data(salaries_given_out_non_cash = int_from_message)
        await report_processing(message.from_user.id ,state)
        await message.answer(f"На этом всё. Нажми \" Закончить\" ", reply_markup=kb.keyboard_payment_process_management)        
        await StepsToCalculatePayment.next()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def get_how_amount_of_non_cash_for_souvenirs(message: types.Message, state: FSMContext):
    print("get_how_amount_of_non_cash_for_souvenirs message:", message.text)
    if message.text.isdigit():
        await my_debug(get_how_amount_of_non_cash_for_souvenirs.__name__, state)
        int_from_message = int(message.text)
        await state.update_data(non_cash_for_souvenirs = int_from_message)
        
        #await state.reset_data()
        #await state.set_data({'number_touts': 2, 'counter_touts': 0, 'list_money_brought_by_touts': [40000, 20000], 'number_boats': 2, 'counter_boats': 0, 'list_number_cruise_boats': [6, 7], 'list_with_general_overloads_for_boats': [1, 6], 'cash_for_cruises': 40000, 'non_cash_for_cruises': 20000, 'cash_for_bar': 2000, 'non_cash_for_bar': 700, 'non_cash_for_souvenirs': 1300})
        
        await report_processing(message.from_user.id ,state)
        await message.answer(f"Чтобы закончить нажми кнопку. Либо введи сумму ЗП налом", reply_markup=kb.keyboard_payment_process_management)
        
        await StepsToCalculatePayment.waiting_for_how_much_was_paid_in_cash.set()
    else:
        await message.answer("Извини, но сейчас я жду от тебя только целые числа")

async def report_processing(id, state: FSMContext):
    dict_data_by_report = await preparation_report(state)
    report =  [f"Общая сумма за рейсы: {dict_data_by_report.get('total_amount_for_cruises','значений нет')}",
                f"Общая сумма за бар:   {dict_data_by_report.get('total_amount_for_bar','значений нет')}" ,
                f"Общая сумма за сувениры: {dict_data_by_report.get('non_cash_for_souvenirs','значений нет')}" ,
                f"Наличными по факту: {dict_data_by_report.get('total_cash','значений нет')}" ,
                f"Б/Н по факту:  {dict_data_by_report.get('total_non_cash','значений нет')}\n", 
            ]
    

    for i in range(len(dict_data_by_report['list_with_salaries_touts'])):
        report.append(f"Оплата зазывале №{i+1}: {dict_data_by_report['list_with_salaries_touts'][i]}")

    
    for i in range(len(dict_data_by_report['list_with_salaries_captains'])):
        report.append(f"Оплата капитана {i+1} катера составляет: {dict_data_by_report['list_with_salaries_captains'][i]}")
            
  
    report.append(f"Оплата администратору: {dict_data_by_report['salaries_admin']}\n")

    if 'salaries_given_out_cash' in dict_data_by_report and 'salaries_given_out_non_cash' in dict_data_by_report and 'cash_balance' in dict_data_by_report:
        report.append(f"Наличными было выдано: {dict_data_by_report['salaries_given_out_cash']}")
        report.append(f"Б/н было выдано: {dict_data_by_report['salaries_given_out_non_cash']}\n")
        report.append(f"В кассе должно остаться наличными: {dict_data_by_report['cash_balance']}\n")
     

    await bot.send_message(id, "\n".join(report),parse_mode=types.ParseMode.HTML)

async def preparation_report(state: FSMContext):
    current_state_date = await state.get_data()

    dict_data_by_report={}

    dict_data_by_report['total_amount_for_cruises'] = current_state_date['cash_for_cruises'] + current_state_date['non_cash_for_cruises']
    dict_data_by_report['total_amount_for_bar'] = current_state_date['cash_for_bar'] + current_state_date['non_cash_for_bar']
    
    dict_data_by_report['total_cash'] = current_state_date['cash_for_cruises'] + current_state_date['cash_for_bar']
    dict_data_by_report['non_cash_for_souvenirs'] = current_state_date['non_cash_for_souvenirs']
    dict_data_by_report['total_non_cash'] = current_state_date['non_cash_for_cruises'] + current_state_date['non_cash_for_bar'] + current_state_date['non_cash_for_souvenirs']

    dict_data_by_report['list_with_salaries_touts'] = [i * 0.1 for i in current_state_date['list_money_brought_by_touts']]
    
    dict_data_by_report['list_with_salaries_captains'] = []
    for i in range(current_state_date['number_boats']):
        dict_data_by_report['list_with_salaries_captains'].append(
            current_state_date['list_number_cruise_boats'][i] * 1200 + 100 * current_state_date['list_with_general_overloads_for_boats'][i]
        )

    dict_data_by_report['salaries_admin'] = (dict_data_by_report['total_amount_for_cruises'] - sum(dict_data_by_report['list_with_salaries_captains'])) \
                                                * 0.1 + dict_data_by_report['total_amount_for_bar'] * 0.1 + current_state_date['non_cash_for_souvenirs'] * 0.1

    if 'salaries_given_out_cash' in current_state_date and 'salaries_given_out_non_cash' in current_state_date:
        dict_data_by_report['salaries_given_out_cash'] = current_state_date['salaries_given_out_cash']
        dict_data_by_report['salaries_given_out_non_cash'] = current_state_date['salaries_given_out_non_cash']
        dict_data_by_report['cash_balance'] = dict_data_by_report['total_cash'] - dict_data_by_report['salaries_given_out_cash'] 

    return dict_data_by_report

async def choice_payment_scheme(message: types.Message):
    await message.reply("Выбири какую смену считаем", reply_markup=kb.keyboard_choice_payment_scheme)

async def simple_message(message: types.Message):
    test_message = "<strong>Ой-ёй</strong>, \n Я не знаю этих слов. \n Вот, что я умею: \n /shift"
    await message.answer(test_message, parse_mode=types.ParseMode.HTML)

async def my_debug( name_def, state = None):
    print(name_def)
    if state is not None:
        current_state_date = await state.get_data()
        print(name_def, current_state_date)