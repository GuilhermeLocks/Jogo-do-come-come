import emoji

# Converter texto para emoji
texto_com_emoji = emoji.emojize("Python is :thumbs_up:")
print(texto_com_emoji)  # Saída: Python is 👍

# Exibir emoji diretamente
print(emoji.emojize(":heart:"))  # Saída: ❤️
help(emoji)