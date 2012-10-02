class FizzBuzz(object):
	
	def __init__(self):
		self.generateurs = []
		
	def main(self):
		for num in xrange(1,106):
			print self.dit(num)
	
	def dit(self,nombre):
		resultat = None
		resultat_precedent = ''
		for gen in self.generateurs:
			resultat = gen.dit(nombre)
			if resultat:
				resultat_precedent += resultat
			
		if not resultat_precedent:
			return nombre
		else:
			return resultat_precedent + '!'


class GenerateurFizz(object):
	def dit(self, nombre):
		if nombre % 3 == 0:
			return 'Fizz'
	
class GenerateurBuzz(object):
	def dit(self, nombre):
		if nombre % 5 == 0:
			return 'Buzz'
			
class GenerateurBang(object):
	def dit(self, nombre):
		if nombre % 7 == 0:
			return 'Bang'
			
			
if __name__ == '__main__':
	fb = FizzBuzz()
	fb.generateurs.append(GenerateurFizz())
	fb.generateurs.append(GenerateurBuzz())
	fb.generateurs.append(GenerateurBang())
	fb.main()
