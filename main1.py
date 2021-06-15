import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token="31e97c2cf580bac6ccb0ba0fe930f3373346e6560a0fe087fc3b165eea548b4444d58e4aeb586ecab0348")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def write_msg(id, some_text):
    vk_session.method("messages.send",{"user_id":id, "message":some_text,"random_id":0})
for event in longpool. listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            proceed = "привет"
            proceed1 = "привет!"
            proceed2 = "здравствуйте"
            proceed3 = "здравствуйте!"
            if msg ==proceed:
                write_msg(event.user_id, "Здравствуйте. Добро пожаловать в группу Перезагрузка - педагог будущего!")
                write_msg(event.user_id,"Список часто задаваемых вопросов: ")
                write_msg(event.user_id, "1. Какие цифровые ресурсы можно использовать в работе педагога?")
                write_msg(event.user_id, "2. Какие есть онлайн-конструкторы для создания персонального сайта, блога?")
                write_msg(event.user_id, "3. Что такое цифровая лаборатория?")
                write_msg(event.user_id, "4. Что такое облачные технологии?")
                write_msg(event.user_id, "5. Гугл сервисы в образовании.")
                write_msg(event.user_id, "5. Что такое Цифровая школа?")
            elif msg == proceed1:
                write_msg(event.user_id, "Здравствуйте. Добро пожаловать в группу Перезагрузка - педагог будущего!")
                write_msg(event.user_id,"Список часто задаваемых вопросов: ")
                write_msg(event.user_id, "1. Какие цифровые ресурсы можно использовать в работе педагога?")
                write_msg(event.user_id, "2. Какие есть онлайн-конструкторы для создания персонального сайта, блога?")
                write_msg(event.user_id, "3. Что такое цифровая лаборатория?")
                write_msg(event.user_id, "4. Что такое облачные технологии?")
                write_msg(event.user_id, "5. Гугл сервисы в образовании.")
                write_msg(event.user_id, "5. Что такое Цифровая школа?")
            elif msg == proceed2:
                write_msg(event.user_id, "Здравствуйте. Добро пожаловать в группу Перезагрузка - педагог будущего!")
                write_msg(event.user_id,"Список часто задаваемых вопросов: ")
                write_msg(event.user_id, "1. Какие цифровые ресурсы можно использовать в работе педагога?")
                write_msg(event.user_id, "2. Какие есть онлайн-конструкторы для создания персонального сайта, блога?")
                write_msg(event.user_id, "3. Что такое цифровая лаборатория?")
                write_msg(event.user_id, "4. Что такое облачные технологии?")
                write_msg(event.user_id, "5. Гугл сервисы в образовании.")
                write_msg(event.user_id, "5. Что такое Цифровая школа?")
            elif msg == proceed3:
                write_msg(event.user_id, "Здравствуйте. Добро пожаловать в группу Перезагрузка - педагог будущего!")
                write_msg(event.user_id,"Список часто задаваемых вопросов: ")
                write_msg(event.user_id, "1. Какие цифровые ресурсы можно использовать в работе педагога?")
                write_msg(event.user_id, "2. Какие есть онлайн-конструкторы для создания персонального сайта, блога?")
                write_msg(event.user_id, "3. Что такое цифровая лаборатория?")
                write_msg(event.user_id, "4. Что такое облачные технологии?")
                write_msg(event.user_id, "5. Гугл сервисы в образовании.")
                write_msg(event.user_id, "5. Что такое Цифровая школа?")
            elif msg == "что такое цифровая школа?":
                write_msg(event.user_id, "Цифровая школа – это комплекс аппаратно-программных средств, smart-технологий и методологии, которые позволяют создать единую информационную образовательную среду, способную кардинально повысить качество и доступность общего образования")
            elif msg =="что такое облачные технологии?":
                write_msg(event.user_id,"Облако — это набор технологий, позволяющий использовать ресурсы удаленных систем, как будто бы они находятся совсем рядом — у вас дома или в офисе https://www.google.ru/drive/ https://e.mail.ru/login?fail=1&sdc=1&page=https%3A%2F%2Fcloud.mail.ru%2F")
            elif msg == "гугл сервисы в образовании.":
                write_msg(event.user_id, "Это:Гугл класс https://edu.google.com/products/classroom/ гугл документы https://www.google.ru/intl/ru/docs/about/ гугл формы https://www.google.ru/forms/about/")
            elif msg =="что такое цифровая лаборатория?":
                write_msg(event.user_id,"Цифровая (компьютерная) лаборатория (ЦЛ) — комплект учебного оборудования, включающий измерительный блок, интерфейс которого позволяет обеспечивать связь с компьютером, и датчики, регистрирующие значения различных физических величин: температуры, pH водного раствора, электропроводности, давления, влажности и др. Самые популярные компании: PASCO, PROLOG, KOBRA-4, NAU-RA")
            elif msg =="какие есть онлайн-конструкторы для создания персонального сайта, блога?":
                write_msg(event.user_id,"Tilda https://tilda.cc/ru/, Wix https://ru.wix.com/russianhtml/911-b-r-r?utm_source=yandex&utm_medium=cpc&utm_campaign=yx_lang_russian_2_yx_broad%5Ebuilder-tbad&experiment_id=Конструктор%20для%20создания%20сайта%5E3506853076%5E648223972%5E2%5Epremium&yclid=3254363241467652394, Tinkoff https://www.tinkoff.ru/business/website-builder/?utm_source=yandex&utm_medium=ctx.cpc&utm_campaign=business.site_builder__sme.site_search_general_rus&utm_term=создание%20сайтов%20онлайн%20конструктор&utm_content=k50id%7C0100000025814856951_%7Ccid%7C58881351%7Cgid%7C4445339741%7Caid%7C10208688689%7Cadp%7Cno%7Cpostype%7Cpremium%7Cpos%7C1%7Csrctype%7Csearch%7Csrc%7Cnone%7Cdvc%7Cdesktop%7Cregionid%7C18%7Cregioname%7CПетрозаводск%7C&yclid=3254356968297494904")
            elif msg =="какие цифровые ресурсы можно использовать в работе педагога?":
                write_msg(event.user_id,"«Kahoot!» представляет собой игровую обучающую платформу, используемую в качестве образовательной технологии в школах и других учебных заведениях.(https://kahoot.com/); Онлайн школа Фоксфорд предлагает не только подготовку детей к ОГЭ/ЕГЭ, но и также онлайн курсы повышения квалификации для учителей. Школа также предлагает использовать готовые онлайн тесты для учеников, и участие в конкурсах и олимпиадах по всем предметам. (https://foxford.ru/); Сайты Решу ОГЭ/ЕГЭ - данный ресурс отлично подходит для подготовки к ГИА, платформа позволяет составлять тесты для учителей, а также разбивать их по темам. (https://ege.sdamgia.ru/)")
                write_msg(event.user_id,"Интерактивные уроки по всему школьному курсу с 1-го по 11-й класс лучших учителей страны предоставляет «Российская электронная школа». (https://resh.edu.ru/); «Московская электронная школа» – это широкий набор электронных учебников и тестов, интерактивные сценарии уроков. (https://www.mos.ru/city/projects/mesh/); Младшие школьники смогут продолжить занятия по русскому языку и математике с помощью сервиса «Яндекс.Учебник». (https://education.yandex.ru/main/); Проверить, как дети усвоили материал, учителям поможет «ЯКласс». (https://www.yaklass.ru/); Всероссийский образовательный проект «Урок цифры» позволяет школьникам, не выходя из дома, знакомиться с основами цифровой экономики, цифровых технологий и программирования. (https://xn--h1adlhdnlo2c.xn--p1ai/)")
