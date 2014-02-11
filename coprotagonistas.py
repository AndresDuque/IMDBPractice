import utilidades
import shelve

def coprotagonistas(actor1,actor2):
	"""Devuelve la interseccion de peliculas en las que 
	han estado juntos"""
	d=shelve.open("movie_db.shelve")
	peliculas1=d[actor1]
	peliculas2=d[actor2]
	print peliculas1
	print peliculas2
	for i in peliculas1:
		for j in peliculas2:
			if i==j:
				print(i)
				
	d.close()


if __name__=='__main__':
	actor1='Pitt, Brad'
	actor2='Jolie, Angelina'
	
	coprotagonistas(actor1,actor2)
