import discord
from discord.ext import commands
import random

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Listas de información
datos = [
    "🌳 Un árbol puede absorber hasta 22 kg de CO2 al año.",
    "🌊 Más de 8 millones de toneladas de plástico llegan al océano cada año.",
    "♻️ Reciclar una lata de aluminio ahorra hasta un 95% de la energía necesaria para fabricar una nueva.",
    "🔥 La temperatura global ha aumentado aproximadamente 1,1 °C desde la era preindustrial.",
    "🐝 Las abejas son responsables de la polinización de aproximadamente un tercio de los alimentos que consumimos."
]

consejos = [
    "💡 Apaga las luces cuando no las necesites.",
    "🚲 Utiliza bicicleta o camina para trayectos cortos.",
    "🚿 Reduce el tiempo de tus duchas para ahorrar agua.",
    "🥤 Utiliza botellas reutilizables en lugar de plásticas.",
    "🌱 Planta árboles o participa en actividades de reforestación."
]

retos = [
    "🏆 Reto del día: No utilices plásticos desechables.",
    "🏆 Reto del día: Ahorra agua cerrando el grifo mientras te cepillas.",
    "🏆 Reto del día: Recicla al menos 5 objetos hoy.",
    "🏆 Reto del día: Apaga todos los aparatos eléctricos que no estés usando.",
    "🏆 Reto del día: Recoge basura de tu comunidad durante 10 minutos."
]

preguntas = {
    "¿Cuál es el principal gas responsable del efecto invernadero?":
    "El dióxido de carbono (CO2).",

    "¿Qué acción ayuda más al medio ambiente?":
    "Reducir, reutilizar y reciclar.",

    "¿Qué recurso natural debemos ahorrar constantemente?":
    "El agua."
}


@bot.event
async def on_ready():
    print(f"✅ {bot.user} está conectado y listo.")


@bot.command()
async def ayudaeco(ctx):
    mensaje = """
🌍 **Comandos de EcoBot**

`!dato` - Muestra un dato ambiental.
`!consejo` - Da un consejo ecológico.
`!reto` - Propone un reto ecológico.
`!quiz` - Hace una pregunta sobre el medio ambiente.
`!causas` - Muestra causas del cambio climático.
`!consecuencias` - Muestra consecuencias del cambio climático.
`!reciclar` - Consejos para reciclar.
`!saludo` - Saluda al usuario.
"""
    await ctx.send(mensaje)


@bot.command()
async def saludo(ctx):
    await ctx.send(f"Hola {ctx.author.mention} 🌱 ¡Bienvenido a EcoBot!")


@bot.command()
async def dato(ctx):
    await ctx.send(random.choice(datos))


@bot.command()
async def consejo(ctx):
    await ctx.send(random.choice(consejos))


@bot.command()
async def reto(ctx):
    await ctx.send(random.choice(retos))


@bot.command()
async def quiz(ctx):
    pregunta = random.choice(list(preguntas.keys()))
    respuesta = preguntas[pregunta]

    await ctx.send(f"❓ {pregunta}")
    await ctx.send(f"✅ Respuesta: {respuesta}")


@bot.command()
async def causas(ctx):
    await ctx.send("""
🌡️ **Principales causas del cambio climático:**

• Quema de combustibles fósiles.
• Deforestación.
• Contaminación industrial.
• Uso excesivo de vehículos.
• Producción masiva de residuos.
""")


@bot.command()
async def consecuencias(ctx):
    await ctx.send("""
⚠️ **Consecuencias del cambio climático:**

• Aumento de la temperatura global.
• Derretimiento de glaciares.
• Aumento del nivel del mar.
• Sequías e inundaciones más frecuentes.
• Pérdida de biodiversidad.
""")


@bot.command()
async def reciclar(ctx):
    await ctx.send("""
♻️ **Consejos de reciclaje**

🟦 Papel y cartón → Contenedor azul.
🟨 Plásticos y envases → Contenedor amarillo.
🟩 Vidrio → Contenedor verde.

Antes de reciclar, limpia los envases.
""")

bot.run("TU_TOKEN")