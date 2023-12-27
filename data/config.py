from environs import Env

env = Env()
env.read_env()

# READ FILES FROM .env file
BOT_TOKEN = env.str("BOT_TOKEN") # BOT TOKENT
ADMINS = env.list("ADMINS")  # ADMINS
# IP = env.str("ip")  # IP HOSTING
