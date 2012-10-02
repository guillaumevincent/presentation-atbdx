class FizzBuzz(object):
    
    def __init__(self):
        self.generateurs = []
        
    def main(self):
        for num in xrange(1,106):
            print self.dit(num)
    
    def dit(self,nombre):
        resultat = ''
        for gen in self.generateurs:
            resultat = gen.dit(resultat, nombre)
            
        if not resultat:
            return nombre
        else:
            return resultat + '!'


class GenerateurFizz(object):
    def dit(self, resultat_precedent, nombre):
        if nombre % 3 == 0:
            return resultat_precedent + 'Fizz'
        else:
            return resultat_precedent
    
class GenerateurBuzz(object):
    def dit(self, resultat_precedent, nombre):
        if nombre % 5 == 0:
            return resultat_precedent + 'Buzz'
        else:
            return resultat_precedent
            
class GenerateurBang(object):
    def dit(self, resultat_precedent, nombre):
        if nombre % 7 == 0:
            return resultat_precedent + 'Bang'
        else:
            return resultat_precedent

class GenerateurWoopee(object):
    def dit(self, resultat_precedent, nombre):
        if nombre == 69:
            return 'Woopee'
        else:
            return resultat_precedent
            
            
if __name__ == '__main__':
    fb = FizzBuzz()
    fb.generateurs.append(GenerateurFizz())
    fb.generateurs.append(GenerateurBuzz())
    fb.generateurs.append(GenerateurBang())
    fb.main()
