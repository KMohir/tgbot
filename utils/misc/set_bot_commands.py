from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Botni ishga tushiring"),
        types.BotCommand("/ask", "Texnik yordamga xabar yozish"),
        types.BotCommand("/change_language", "Tilni ozgartirish"),
        types.BotCommand("help", "Yordam"),
    ])
