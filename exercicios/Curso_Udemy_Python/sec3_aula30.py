class Horas:

	def __init__(self, hora=0, min=0, seg=0, *args, **kwargs):
		super(Horas, self).__init__(*args, **kwargs)
		self.hora = hora
		self.min = min
		self.seg = seg

	def ajustar_relogio(self, hora, min, seg=0):
		self.hora = hora
		self.min = min
		self.seg = seg

	def __str__(self):
		return '{0:02d}:{1:02d}:{2:02d}'.format(self.hora, self.min, self.seg)# + ', ' + super(Horas, self).__str__()
	
	def tick(self):
		if self.seg == 59:
			self.seg = 0
			if self.min == 59:
				self.min = 0
				if self.hora == 23:
					self.hora = 0
				else:
					self.hora += 1
			else:
				self.min += 1
		else:
			self.seg += 1

'''h = Horas(22, 59, 59)

print(h)
h.tick()
print(h)'''

class Calendario:

	meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

	def __init__(self, dia, mes, ano, *args, **kwargs):
		super(Calendario, self).__init__(*args, **kwargs)
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def ajustar_data(self):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def __str__(self):
		return '{0:02d}/{1:02d}/{2:04d}'.format(self.dia, self.mes, self.ano)

	def avancar(self):
		dia_max = Calendario.meses[self.mes - 1]

		if self.dia == dia_max:
			self.dia = 1
			if self.mes == 12:
				self.mes = 1
				self.ano += 1
			else:
				self.mes += 1
		else:
			self.dia += 1

''''c = Calendario(31, 12, 1996)

print(c)
c.avancar()
print(c)'''

class Relogio(Horas, Calendario):

	def __init__(self, hora, min, seg, dia, mes, ano):
		super(Relogio, self).__init__(hora=hora, min=min, seg=seg, dia=dia, mes=mes, ano=ano)
		#Horas.__init__(self, hora, min, seg)
		#Calendario.__init__(self, dia, mes, ano)

	def __str__(self):
		#return super(Relogio, self).__str__()
		return Horas.__str__(self) + ', ' + Calendario.__str__(self)

	def tick(self):
		hora_anterior = self.hora
		Horas.tick(self)
		if self.hora < hora_anterior:
			self.avancar()


r = Relogio(23, 59, 59, 31, 12, 2018)

print(r)
r.tick()
print(r)
print(Relogio.mro())