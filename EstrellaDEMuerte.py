class naveP():
    def __init__(self,destruir, vida):
        self.vida=vida
        self.destruir=destruir
    def des(destruir, vida, volumen):
        while volumen<=vida:
            if volumen==500:
                return 'se ha destruido el planeta Concordia:','tienes ahora',vida-volumen,'de vida'
            elif volumen==800:
                return 'se ha destruido el planeta Concordia:','tienes ahora',vida-volumen,'de vida'
        if volumen>vida:
            return 'no se ha podido destruir la nave'

