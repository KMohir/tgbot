from aiogram import types


async def set_default_commands(dp):

    await dp.bot.set_my_commands([
        types.BotCommand("start", "Botni ishga tushurish"),
        types.BotCommand("ask", "Texnik yordamga habar yozish"),
        types.BotCommand("change_language", "Tilni ozgartirish"),
        types.BotCommand("about",'ProTestim haqida bilish')
    ])
