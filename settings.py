# -*- coding: utf-8 -*-

movie_genres_image = "images/genres.png"
tvshow_genres_image = "images/genres_tvshow.png"
movie_highly_rated_image = "images/highly-rated.png"
tvshow_highly_rated_image = "images/highly-rated_tvshow.png"
movie_most_popular_image = "images/most-popular.png"
tvshow_most_popular_image = "images/most-popular_tvshow.png"
movie_most_voted_image = "images/most-voted.png"
tvshow_most_voted_image = "images/most-voted_tvshow.png"
movie_image = "images/movies.png"
search_movie_image = "images/search_movie.png"
movie_search_people_image = "images/search_people.png"
tvshow_search_people_image = "images/search_people_tvshow.png"
search_tvshow_image = "images/search_tvshow.png"
tvshow_image = "images/tvshows.png"
movie_years_image = "images/years.png"
tvshow_years_image = "images/years_tvshow.png"
next_image = "images/next.png"
movieDB_api_key = "8804be4f30f706e9e0ec40c32d961635"

menu_items = [
	("[B][COLOR yellow]>>>>>[COLOR lime]Film[COLOR yellow]<<<<<[/COLOR][/B]", movie_image),
    
    ("[B][COLOR yellow]>>>>>[COLOR lime]Serie TV[COLOR yellow]<<<<<[/COLOR][/B]", tvshow_image),
    
    ]

film_menu_items = [
	("[B][COLOR lime]Ricerca per titolo film[/COLOR][/B]", search_movie_image),
	("[B][COLOR lime]Ricerca per attore[/COLOR][/B]", movie_search_people_image),
	("[B][COLOR lime]Film più popolari[/COLOR][/B]", movie_most_popular_image),
	("[B][COLOR lime]Film più votati[/COLOR][/B]", movie_most_voted_image),
	("[B][COLOR lime]Film più valutati[/COLOR][/B]", movie_highly_rated_image),
	("[B][COLOR lime]Film divisi per anno[/COLOR][/B]", movie_years_image),
	("[B][COLOR lime]Film per genere[/COLOR][/B]", movie_genres_image)
]

tvshow_menu_items = [
	("[B][COLOR lime]Ricerca serie TV[/COLOR][/B]", search_tvshow_image),
	("[B][COLOR lime]Ricerca per attore[/COLOR][/B]", tvshow_search_people_image),
	("[B][COLOR lime]Serie TV più popolari[/COLOR][/B]", tvshow_most_popular_image),
	("[B][COLOR lime]Serie TV piu votate[/COLOR][/B]", tvshow_most_voted_image),
	("[B][COLOR lime]Serie TV altamente valutate[/COLOR][/B]", tvshow_highly_rated_image),
	("[B][COLOR lime]Serie TV divise per anno[/COLOR][/B]", tvshow_years_image),
	("[B][COLOR lime]Serie TV per genere[/COLOR][/B]", tvshow_genres_image)
]

messages = {
	"start_search": {
		"title": "[B][COLOR cyan]Attendere prego         * BETA mod by Area69 *[/COLOR][/B]",
		"text": "[B][COLOR lime]Inizio ricerca...[/COLOR][/B]"
	},

	"movie": {
		"popular": "[B][COLOR lime]Ricerca film più popolari in corso...[/COLOR][/B]",
		"top_rated": "[B][COLOR lime]Ricerca film più votati in corso...[/COLOR][/B]",
		"discover": "[B][COLOR lime]Ricerco i film più valutati in corso...[/COLOR][/B]",
		"genre": "[B][COLOR lime]Ricerca film per genere scelto in corso...[/COLOR][/B]",
		"year": "[B][COLOR lime]Ricerca film per anno scelto in corso...[/COLOR][/B]",
		"default": "[B][COLOR lime]Ricerco film con il titolo scelto in corso...[/COLOR][/B]"
		
	},

	"tvshow": {
		"popular": "[B][COLOR lime]Ricerca serie tv più popolari in corso...[/COLOR][/B]",
		"top_rated": "[B][COLOR lime]Ricerca serie tv più votata in corso...[/COLOR][/B]",
		"discover": "[B][COLOR lime]Ricerco le serie tv scelta in corso...[/COLOR][/B]",
		"genre": "[B][COLOR lime]Ricerca serie tv per genere scelto in corso...[/COLOR][/B]",
		"year": "[B][COLOR lime]Ricerca serie tv per anno scelto in corso...[/COLOR][/B]",
		"default": "[B][COLOR lime]Riceco la serie tv con il titolo scelto in corso...[/COLOR][/B]"
	},

	"stream": {
		"error_stream_title": "[B][COLOR cyan]A T T E N Z I O N E[/COLOR][/B]",
		"error_stream_text": "[B][COLOR lime]Riproduzione fallita di uno o piu elementi, prova altra sorgente.[/COLOR][/B]"
	},

	"person": "[B][COLOR lime]Ricerco Attore scelto in corso...[/COLOR][/B]",
	"movie_list": "[B][COLOR lime]Lista Film[/COLOR][/B]",
	"tvshow_list": "[B][COLOR lime]Lista Serie Tv[/COLOR][/B]",
	"episode": "[B][COLOR lime]Episodio[/COLOR][/B]",
	"playing": "[B][COLOR lime]Buona Visione[/COLOR][/B]"
}