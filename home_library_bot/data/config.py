from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
PGUSER = env.str("PGUSER") # DB's username
PGPASSWORD = env.str("PGPASSWORD") # DB's password
DATABASE = env.str("DATABASE") # DB's name
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

#link for connection to database
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}"
aiogram_redis = {
    'host': IP,
}

redis = {
    'addresss': (IP, 6379),
    'encoding': 'utf8'
}
