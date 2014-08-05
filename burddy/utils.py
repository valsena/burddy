from random import randint

def get_random(model):
	" gets a random entry of this model in the db "
	r = randint(0, model.query.count())
	return model.query.all()[r]
