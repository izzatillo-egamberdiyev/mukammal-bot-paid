from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
BOT_ID = BOT_TOKEN.split(:)[1]
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
MYBOT = env.str("MY_BOT")
IP = env.str("ip")  # Xosting ip manzili
