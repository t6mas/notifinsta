import instaloader, time, requests, os

# Configuración
USUARIO = "typemkeell"  # 👈 usuario a monitorear
WEBHOOK_URL = "https://discord.com/api/webhooks/1434371712673124443/_l7xzlrLHxe3zx5Lg6BvcQgY57mCQbW-LPBpuy_n3WHx_6HnkpXDApZ88rFJcS_qX-PT"  # 👈 tu webhook de Discord
SESSION_FILE = "session-solomuero.jpg"  # 👈 reemplazá con el nombre exacto de tu archivo de sesión

# Inicializar Instaloader
L = instaloader.Instaloader()
L.load_session_from_file("solomuero.jpg", SESSION_FILE)  # ⚠️ poné tu usuario real aquí

def get_story_ids():
    ids = []
    for story in L.get_stories(userids=[L.check_profile_id(USUARIO)]):
        for item in story.get_items():
            ids.append(item.mediaid)
    return ids

print(f"👀 Monitoreando historias de @{USUARIO}...")
historias_previas = set(get_story_ids())

while True:
    time.sleep(300)  # cada 5 minutos
    actuales = set(get_story_ids())
    nuevas = actuales - historias_previas
    if nuevas:
        msg = f"📸 Nueva historia subida por @{USUARIO}!\nhttps://www.instagram.com/stories/{USUARIO}/"
        requests.post(WEBHOOK_URL, json={"content": msg})
        historias_previas = actuales
        print(msg)

