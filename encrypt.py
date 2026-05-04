
import bcrypt

password = "student2".encode('utf-8')

# Génère un sel + hash automatiquement
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)
