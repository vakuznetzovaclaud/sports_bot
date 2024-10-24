import asyncio
import aiogram
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, InputFile
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
bot = Bot(token = '7208151572:AAGVjQ3YHDGTqduBJBCg8yz5twYr_x2vAvU')
dp = Dispatcher()
router = Router()
@router.message(Command('start'))
async def send_welcome(message: Message):
    username = message.from_user.first_name
    await message.answer(username + ", привет! Это бот для спортсменов.")
    kb = [
        [
            types.KeyboardButton(text='Что умеет бот?'),
            types.KeyboardButton(text='Программы тренировок'),
        ],
        [
            types.KeyboardButton(text='Мотивирующие цитаты'),
            types.KeyboardButton(text='Мотивирующие картинки'),
        ],
        [
            types.KeyboardButton(text='Полезные рецепты'),
            types.KeyboardButton(text='Советы по питанию'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard = kb
    )
    await message.answer("Выбери раздел", reply_markup=keyboard)

@router.message(F.text == 'Что умеет бот?')
async def what_do_you_can(message: Message):
    await message.answer('Давай расскажу, зачем тебе может понадобиться этот бот:\n\n • Тренировки: здесь ты можешь найти видеоуроки о том, как составить индивидуальную программу тренировок или улучшить уже имеющуюся.\n\n • Мотивавация: здесь ты сможешь найти фразы и картинки, которые в трудную минуту помогут тебе вернуться на путь истинный.\n\n • Питание: здесь ты сможешь найти общие рекмендации по питанию для спортсменов и много полезных рецептов.')

@router.message(F.text == 'Советы по питанию')
async def buttons1(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text = 'белки',
        callback_data='белки'
    ))
    builder.add(types.InlineKeyboardButton(
        text = 'жиры',
        callback_data='жиры'
    ))
    builder.add(types.InlineKeyboardButton(
        text='углеводы',
        callback_data='углеводы'
    ))
    await message.answer("О чем ты хочешь узнать?", reply_markup=builder.as_markup())


@dp.callback_query(F.data == 'белки')
async def send_proteins(callback: types.CallbackQuery):
    await callback.message.answer('Белки играют важную роль в спортивной диете, способствуя восстановлению и росту мышц.\nСпортсменам стоит уделять внимание качеству и количеству потребляемого белка.\n\n • Спортсменам рекомендуется потреблять больше белков, чем обычным людям. Рекомендуемая норма составляет от 1.2 до 2.0 граммов белка на килограмм массы тела в зависимости от типа и интенсивности тренировок.\n\n • Животные источники: Мясо, рыба, яйца, молочные продукты (молоко, йогурт, сыр) содержат все необходимые аминокислоты.\n\n • Растительные источники: Бобовые (чечевица, фасоль), орехи, семена, соевые продукты (тофу, темпе) также являются хорошими источниками белка, но могут не содержать всех незаменимых аминокислот.\n\n • Для максимального эффекта рекомендуется потреблять белок в течение 30-60 минут после тренировки. Это помогает восстановить мышцы и улучшить их рост.')
@dp.callback_query(F.data == 'жиры')
async def send_fats(callback: types.CallbackQuery):
    await callback.message.answer("Жиры играют жизненно важную роль в рационе спортсменов. Правильный выбор и количество жиров могут значительно улучшить производительность, восстановление и общее здоровье.\n\n • Насыщенные жиры: Обычно содержатся в животных продуктах и некоторых растительных маслах. Их потребление должно быть ограничено, так как они могут повышать уровень холестерина. \n\n • Мононенасыщенные жиры: Полезные жиры, которые могут способствовать снижению уровня плохого холестерина. Источники: оливковое масло, авокадо, орехи.\n\n • Полиненасыщенные жиры: Включают омега-3 и омега-6 жирные кислоты, которые важны для здоровья сердца и снижения воспалений. Источники: рыба (лосось, скумбрия), семена льна, грецкие орехи.\n\n • Трансжиры: Искусственно созданные жиры, которые следует избегать, так как они повышают риск сердечно-сосудистых заболеваний.\n\n • Жиры должны составлять 20-35% от общего калорийного рациона спортсмена. Предпочитайте полезные жиры (моно- и полиненасыщенные) и ограничьте потребление насыщенных и трансжиров. Включайте источники жиров в свой рацион до и после тренировок для поддержания энергии и восстановления.")
@dp.callback_query(F.data == 'углеводы')
async def send_carbs(callback: types.CallbackQuery):
    await callback.message.answer("Углеводы являются основным источником энергии для организма, особенно во время интенсивных физических нагрузок. Они быстро перевариваются и усваиваются, что позволяет быстро восполнить запасы энергии.\n\n • Сложные углеводы (например, цельнозерновые продукты, овощи, бобовые) обеспечивают длительное поступление энергии.\n\n • Простые углеводы (например, фрукты, мед, сладости) быстро усваиваются и могут быть полезны для быстрого восстановления энергии после интенсивной тренировки.\n\n • Для спортсменов рекомендуется потреблять углеводы в количестве 6-10 граммов на килограмм массы тела в день, в зависимости от уровня активности и типа спорта. Употребление углеводов за 1-3 часа до тренировки помогает повысить уровень глюкозы в крови и улучшить производительность.")
import random
used_lines = []
@router.message(F.text == 'Мотивирующие цитаты')
async def random_quote(message: Message):
    with open('C:/Users/User/PycharmProjects/pythonProject1/motivational_quotes2', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(used_lines) == len(lines):
            used_lines.clear()
        random_line = random.choice(lines)
        while random_line in used_lines:
            random_line = random.choice(lines)
        used_lines.append(random_line)
        await bot.send_message(message.chat.id, random_line)
import os
@router.message(F.text == 'Мотивирующие картинки')
async def random_picture(message: Message):
        images = [f for f in os.listdir('C:/Users/User/PycharmProjects/pythonProject1/motivational_pictures')]
        random_image = random.choice(images)
        await bot.send_photo(message.chat.id, types.FSInputFile(path=(os.path.join('C:/Users/User/PycharmProjects/pythonProject1/motivational_pictures/', random_image))))


@router.message(F.text == 'Полезные рецепты')
async def recipes(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Полезные рецепты здесь',
        url='https://fitstars.ru/recipes'
    ))
    await message.answer("Думаешь, что приготовить, чтобы сохранить форму? Отлично, лови классные варианты!",
                         reply_markup=builder.as_markup())

@router.message(F.text == 'Программы тренировок')
async def recipes2(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Видео с готовой программой тренировок и тем, как изменить ее под себя',
        url='https://www.youtube.com/watch?v=eMjyvIQbn9M'
    ))
    builder.add(types.InlineKeyboardButton(
        text='Теория о том, как составлять тренировки',
        url='https://www.youtube.com/watch?v=5iHQDUvR_vc'
    ))
    builder.add(types.InlineKeyboardButton(
        text='Как увеличить эффективность своих тренировок',
        url='https://www.youtube.com/watch?v=geK9GNKGRpo'
    ))
    await message.answer("Вот несколько информативных ресурсов, которые помогут тебе тренироваться:",
                         reply_markup=builder.as_markup())

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())