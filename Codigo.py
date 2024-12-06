Volleyball_consejos = {
    "Volear":"puedes voleaar en casos de que la pelota venga muy alto y para colocar",
    "Rematar":"pudes rematar en casos de que tu equipo te pase el balon",
    "bloquear":"bloquea cuando el rival intente rematar",
    "hablar":"habla con tu equipo sobre quien va a por el balon"
}
volleyball = input("escribe sobre que movimiento quieres aprender")

if volleyball in Volleyball_consejos.keys():
    print(Volleyball_consejos[volleyball])
    
else:
    print("no tengo ese consejo en mis datos")
