from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from . import handlers
from . import states 


async def setup(dp: Dispatcher):
    
    dp.register_callback_query_handler(handlers.process_callback_daily_payment_plan, text='daily_payment_plan')
    dp.register_callback_query_handler(handlers.finished_payment_process,text='finished', state='*')
   
    dp.register_message_handler(handlers.get_inf_about_touts,state=states.StepsToCalculatePayment.waiting_for_the_number_of_touts)
    dp.register_message_handler(handlers.get_inf_about_boats, state=states.StepsToCalculatePayment.waiting_for_inf_on_boats_cruises)
    dp.register_message_handler(handlers.get_inf_about_overloads_cruises,state=states.StepsToCalculatePayment.waiting_for_inf_on_overloads_cruises)
    dp.register_message_handler(handlers.get_how_amount_of_cash_for_cruises, state=states.StepsToCalculatePayment.waiting_for_the_amount_of_cash_for_cruises)
    dp.register_message_handler(handlers.get_how_amount_of_non_cash_for_cruises, state=states.StepsToCalculatePayment.waiting_for_the_amount_of_non_cash_for_cruises)
    dp.register_message_handler(handlers.get_how_amount_of_cash_for_bar, state=states.StepsToCalculatePayment.waiting_for_the_amount_of_cash_for_bar)
    dp.register_message_handler(handlers.get_how_amount_of_cash_for_bar, state=states.StepsToCalculatePayment.waiting_for_the_amount_of_cash_for_bar)
    dp.register_message_handler(handlers.get_how_amount_of_non_cash_for_bar, state=states.StepsToCalculatePayment.waiting_for_the_amount_of_non_cash_for_bar)
    dp.register_message_handler(handlers.get_how_much_was_paid_in_cash, state=states.StepsToCalculatePayment.waiting_for_how_much_was_paid_in_cash)
    dp.register_message_handler(handlers.get_how_much_was_paid_in_non_cash, state=states.StepsToCalculatePayment.waiting_for_how_much_was_paid_in_non_cash)
    dp.register_message_handler(handlers.get_how_amount_of_non_cash_for_souvenirs, state=states.StepsToCalculatePayment.waiting_for_the_amount_of_non_cash_for_souvenirs)

    dp.register_message_handler(handlers.choice_payment_scheme, commands=['shift'])
    dp.register_message_handler(handlers.simple_message)
    # Commands
    #dp.register_message_handler(cmd_start, CommandStart(''), state='*')
