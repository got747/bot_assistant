from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard_choice_payment_scheme = InlineKeyboardMarkup()

btn_daily_payment_plan = InlineKeyboardButton(text="Дневная смена", callback_data="daily_payment_plan")
btn_evening_payment_plan = InlineKeyboardButton(text="Вечерняя смена", callback_data="evening_payment_plan")

keyboard_choice_payment_scheme.add(btn_daily_payment_plan, btn_evening_payment_plan)

keyboard_payment_process_management = InlineKeyboardMarkup()

btn_finished = InlineKeyboardButton(text="Закончить", callback_data="finished")
btn_back = InlineKeyboardButton(text="Обратно", callback_data="back")
btn_undo = InlineKeyboardButton(text="Ошибся", callback_data="undo")

keyboard_payment_process_management.add(btn_finished, btn_back, btn_undo)
