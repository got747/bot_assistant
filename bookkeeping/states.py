from aiogram.dispatcher.filters.state import State, StatesGroup


class StepsToCalculatePayment(StatesGroup):
    waiting_for_the_number_of_touts = State()
    waiting_for_inf_on_boats_cruises = State()
    waiting_for_inf_on_overloads_cruises = State()
    waiting_for_the_amount_of_cash_for_cruises = State()
    waiting_for_the_amount_of_non_cash_for_cruises = State()
    waiting_for_the_amount_of_cash_for_bar = State()
    waiting_for_the_amount_of_non_cash_for_bar = State()
    waiting_for_the_amount_of_non_cash_for_souvenirs = State()
    waiting_for_salaries_were_given_out_in_cash = State()
    waiting_for_salaries_were_given_out_in_non_cash = State()
    waiting_for_how_much_was_paid_in_cash = State()
    waiting_for_how_much_was_paid_in_non_cash = State()