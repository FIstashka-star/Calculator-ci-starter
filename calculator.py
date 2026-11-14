class Calculator:
	def add(self, a:float, b:float) -> float:
		return a + b

	def subtract(self, a:float, b:float) -> float:
		return a - b

	def multiply(self, a:float, b:float) -> float:
		retun a * b

	def divide(self, a:float, b:float) -> float:
		if b == 0:
			return 0.0
        return a / b
