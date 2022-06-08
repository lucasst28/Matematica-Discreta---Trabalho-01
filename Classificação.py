from collections import defaultdict
import copy

class Relacao(defaultdict):

	def __init__(self, s, func=None):
		super(Relacao, self).__init__(set)
		self.s = s
		if func: 
			f = getattr(self, "_" + str(func))
			f()

	def _identidade(self):
		for x in self.s:
			self[x].add(x)

	def _all(self):
		for x in self.s:
			self[x] = self.s

	def Depares(pares):
		s = set()
		for p in pares:
			for x in p:
				s.add(x)
		rel = Relacao(s)
		for x, y in pares:
			rel.add(x, y)
		return rel

	def pares(self):
		return [(x, y) for x, ys in self.items() for y in ys]

	def add(self, k, v):
		self[k].add(v)

	def remove(self, k, v):
		self[k].remove(v)

	def inversa(self):
		inv = Relacao(self.s)
		for k, v in self.items():
			for x in v:
				inv[x].add(k)
		return inv

	def intersecao(self, other):
		isect = Relacao(self.s)
		s = set(self.keys()).intersection(set(other.keys()))
		for k in s:
			isect[k] = self[k].intersection(other[k])
		return isect

	def subpar(self, other):
		if not set(self.keys()).issubset(set(other.keys())): return False
		for k,v in self.items():
			if not v.issubset(other[k]): return False
		return True

	def contains(self, k, v):
		return k in self and v in self[k]

	def compose(self, other):
		comp = Relacao(self.s)
		copy_other = copy.copy(other)
		for k, v in copy_other.items():
			for x in v:
				for y in self[x]:
					comp[k].add(y)
		return comp

	def subset(self, other):
		if not set(self.keys()).issubset(set(other.keys())): return False
		for k,v in self.items():
			if not v.issubset(other[k]): return False
		return True

	def inversa(self):
		inv = Relacao(self.s)
		for k, v in self.items():
			for x in v:
				inv[x].add(k)
		return inv

	def intersect(self, other):
		isect = Relacao(self.s)
		s = set(self.keys()).intersection(set(other.keys()))
		for k in s:
			isect[k] = self[k].intersection(other[k])
		return isect

	def subset(self, other):
		if not set(self.keys()).issubset(set(other.keys())): 
			return False
		for k,v in self.items():
			if not v.issubset(other[k]): 
				return False
		return True

	def contains(self, k, v):
		return k in self and v in self[k]

	def compose(self, other):
		comp = Relacao(self.s)
		copy_other = other.copy()
		for k, v in copy_other.items():
			for x in v:
				for y in self[x]:
					comp[k].add(y)
		return comp

	def reflexiva(self):
		i = Relacao(self.s, "identidade")
		return i.subset(self)

	def simetrica(self):
		inv = self.inversa()
		return self.subset(inv)

	def transitiva(self):
		return self.compose(self).subset(self)


def powerset(s):
	if len(s) == 0: return [[]]
	x = s[0]
	ss = s[1:]
	ps = powerset(ss)
	ps2 = [y + [x] for y in ps]
	return ps + ps2

def lista():

    lista = []
    while True:
        elem = input("Adicione um novo elemento a lista (ENTER encerra):")
        if elem == "":
            break
        lista.append(int(elem))
    return lista
	
if __name__ == '__main__':
	
	s = lista()
	r = Relacao(s, "all")
	prs = r.pares()
	powerprs = powerset(prs)
	contents = ["%r\n" % (rel) for rel in powerprs]
	open("rels.txt", "w").writelines(contents)
	powerrels = [Relacao.Depares(rel) for rel in powerprs]
	contents2 = ["Reflexiva : %r, Simetrica: %r, Transitiva: %r\n" % (rel.reflexiva(), rel.simetrica(), rel.transitiva()) for rel in powerrels]
	open("flags.txt", "w").writelines(contents2)
	results = contents + contents2
	open("results.txt", "w").writelines(results)