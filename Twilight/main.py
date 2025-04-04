import telebot
from keras.models import load_model  # Для работы Keras требуется TensorFlow
from PIL import Image, ImageOps  # Установите pillow вместо PIL
import numpy as np
import h5py

f = h5py.File("keras_model.h5", mode="r+")
model_config_string = f.attrs.get("model_config")

if model_config_string.find('"groups": 1,') != -1:
    model_config_string = model_config_string.replace('"groups": 1,', '')
f.attrs.modify('model_config', model_config_string)
f.flush()

model_config_string = f.attrs.get("model_config")

assert model_config_string.find('"groups": 1,') == -1

def get_class(img):
    np.set_printoptions(suppress=True)
    model = load_model("keras_model.h5", compile=False)
    class_names = open("labels.txt", "r", encoding="utf-8").read().splitlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(img).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name[2:], confidence_score

bot = telebot.TeleBot("ВАШ ТОКЕН")

@bot.message_handler(content_types=['photo'])
def img(message):
    # Извлекаем информацию о файле
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    # Скачиваем файл
    downloaded_file = bot.download_file(file_info.file_path)
    # Сохраняем файл
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    a, b = get_class(file_name)
    if a == 'Аро Вольтури\n':
        bot.send_photo(message.chat.id, open('1.jpg', 'wb'))
        bot.send_message(message.chat.id, "Хитрый и манипулятивный лидер Вольтури, обладающий способностью читать мысли.\n")
    elif a == 'Белла\n':
        bot.send_photo(message.chat.id, open('2.jpg', 'wb'))
        bot.send_message(message.chat.id, "Непредсказуемая и смелая девушка, которая выбирает любовь вампира, несмотря на опасности.\n")
    elif a == 'Джаспер Хейл\n':
        bot.send_photo(message.chat.id, open('3.jpg', 'wb'))
        bot.send_message(message.chat.id, "Вампир с даром управления эмоциями, страдающий от своего прошлого.\n")
    elif a == 'Джейкоб\n':
        bot.send_photo(message.chat.id, open('4.jpg', 'wb'))
        bot.send_message(message.chat.id, "Превращающийся в волка, преданный друг Беллы, испытывающий к ней глубокие чувства.\n")
    elif a == 'Карлайл Каллен\n':
        bot.send_photo(message.chat.id, open('5.jpg', 'wb'))
        bot.send_message(message.chat.id, "Сострадательный и благородный вампир, посвятивший свою жизнь спасению людей.\n")
    elif a == 'Розали Хейл\n':
        bot.send_photo(message.chat.id, open('6.jpg', 'wb'))
        bot.send_message(message.chat.id, "Красивый и гордый вампир, мечтающий о человеческой жизни и семье.\n")
    elif a == 'Эдвард\n':
        bot.send_photo(message.chat.id, open('7.jpg', 'wb'))
        bot.send_message(message.chat.id, "Загадочный и романтичный вампир, влюбленный в Беллу, с даром читать мысли.\n")
    elif a == 'Элис Каллен\n':
        bot.send_photo(message.chat.id, open('8.jpg', 'wb'))
        bot.send_message(message.chat.id, "Оптимистичная и энергичная вампирша с даром предсказания будущего.\n")
    else:
        bot.send_photo(message.chat.id, open('9.jpg', 'wb'))
        bot.send_message(message.chat.id, "Сильный и добродушный вампир, обладающий чувством юмора и любовью к приключениям.\n")
# Запускаем бота
bot.polling()
