import flet

# Creamos un nuevo proyecto Flet
app = flet.App()

# Creamos las rutas de la aplicación
@app.route("/")
def index():
    # Si el usuario está autenticado, le redirigimos a la página principal
    if app.user:
        return flet.redirect("/home")

    # Si no está autenticado, le mostramos el formulario de login
    return flet.render("login.html")

@app.route("/login")
def login():
    # Obtenemos los datos del formulario de login
    email = request.form["email"]
    password = request.form["password"]

    # Validamos los datos
    if not email or not password:
        return flet.render("login.html", error="Los campos email y contraseña son obligatorios.")

    # Comprobamos si el usuario existe
    users = app.database.query("SELECT * FROM users WHERE email = ?", email)

    # Si no existe, mostramos un error
    if not users:
        return flet.render("login.html", error="El usuario no existe.")

    # Si existe, comprobamos si la contraseña es correcta
    user = users[0]
    if password != user["password"]:
        return flet.render("login.html", error="La contraseña es incorrecta.")

    # Si la contraseña es correcta, autenticamos al usuario
    app.user = user
    return flet.redirect("/home")

@app.route("/logout")
def logout():
    # Eliminamos al usuario de la sesión
    app.user = None
    return flet.redirect("/")

# Cargamos la plantilla de login
@app.template("login.html")
def login_template():
    # Si el usuario está autenticado, lo redirigimos a la página principal
    if app.user:
        return flet.redirect("/home")

    # Si no está autenticado, mostramos el formulario de login
    return flet.render("login.html", error=None)

# Cargamos la plantilla de la página principal
@app.template("home.html")
def home_template():
    # Si el usuario no está autenticado, lo redirigimos al formulario de login
    if not app.user:
        return flet.redirect("/")

    # Si está autenticado, mostramos la página principal
    return flet.render("home.html", user=app.user)

# Iniciamos la aplicación
app.run()
