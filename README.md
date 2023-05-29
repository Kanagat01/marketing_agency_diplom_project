# Заказ по дипломному проекту по теме Маркетинговое Агентство
На сайте есть 5 страниц Главная, О компании, Услуги, Наши проекты и Политика обработки личных данных. <br>
Последняя страница была очень простой, содержала лишь h3, p и br и была создана лишь для того чтобы ссылка в форме была рабочей. <br>
Frontend сайта был создан с использованием bootstrap5, в некоторых местах добавлял собственные стили. <br>
Сделал для каждой страницы собственный шаблон и базовый шаблон от которого наследуются все остальные. <br>
Базовый шаблон содержал в себе навигационную панель с логотипом, который пересылал на главную страницу и ссылки на другие страницы сайта, <br>
и футер со ссылками в соц.сети <br>
В главной странице были описаны преимущества, некоторые услуги, цифры компании(заработок, количество проектов и т.д.), отзывы и 2 формы. <br>
Первая форма - форма консультации, содержала поля имени и номера телефона, маска для номера была взята из библиотеки jquery, данные <br>
сохранялись в бд и их можно было увидеть в панели админа. Вторая форма - форма заказа услуги, данные также сохранялись в бд, с <br>
возможностью посмотреть из админ панели, содержала поля имени, номера телефона, email, описание услуги и бюджета. <br>
Страница о компании была достаточно простой, только список услуг динамически подгружался с бд. <br>
Страница услуги состояла из списка услуг, с фото, описанием и диапазоном цен. Описания услуг могли быть разной длины поэтому они <br> 
были оформлены ввиде карточек и с кнопкой подробнее и с всплывающим модальным окном, чтобы придать всем карточкам одинаковый вид и размер. <br>
Страница наши проекты, была также как страница услуг, т.е. содержала название, фото, описание и цену. Для разнообразия была оформлена ввиде секций. <br> 
Каждый четный проект имел черный фон, где фото была выравнена в правую сторону, а название, описание и цена была в левой части, а каждый нечетный <br>
проект имел серый фон, где фото была выравнена в левую сторону, а название, описание и цена были указаны в правой части. <br>
<br>
В последнем коммите было добавлено регистрация и авторизация, личный кабинет и страница мои заказы, где можно увидеть статус своих заявок
