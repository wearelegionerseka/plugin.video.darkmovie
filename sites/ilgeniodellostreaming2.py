#!/usr/bin/python

from hosts import hosts
from sys import version_info
from bs4 import BeautifulSoup
from requests import post, get

from scrapers.utils import (
	m_identify, headers,
	recognize_mirror
)

host = "https://ilgeniodellostreaming.cam/"
excapes = ["Back", "back", ""]

if version_info.major < 3:
	input = raw_input

def search_film(film_to_search):
	search_data = {
		"story": film_to_search,
		"do": "search",
		"subaction": "search"
	}

	body = post(
		host,
		params = search_data,
		timeout = 8
	).text

	parsing = BeautifulSoup(body, "html.parser")

	json = {
		"results": []
	}

	how = json['results']

	for a in parsing.find_all("div", class_ = "result-item"):
		image = a.find("img").get("src")
		some = a.find_all("a")[1]
		link = some.get("href")
		title = some.get_text()

		data = {
			"title": title,
			"link": link,
			"image": host + image
		}

		how.append(data)

	return json
	
def search_mirrors(film_to_see):
	body = get(film_to_see).text
	parsing = BeautifulSoup(body, "html.parser")

	json = {
		"results": []
	}

	datas = json['results']
	options = parsing.find("ul", class_ = "options-list")

	for a in options.find_all("li"):
		option = a.find("a")
		link_mirror = option.get("data-link")

		mirror = (
			link_mirror
			.split(".")[0]
			.split("/")[-1]
		)

		quality = (
			option
			.get_text()
			.split(" ")[-1]
		)

		try:
			hosts[mirror]

			if not link_mirror.startswith("http"):
				link_mirror = "http:%s" % link_mirror 

			data = {
				"mirror": mirror,
				"quality": quality,
				"link": link_mirror
			}

			datas.append(data)
		except KeyError:
			pass

	return json

def identify(info):
	link = info['link']
	mirror = info['mirror']
	link = m_identify(link)
	return hosts[mirror].get_video(link)

def menu():
	while True:
		try:
			ans = input("Type the film title which you would search: ")
			result = search_film(ans)['results']

			while True:
				for a in range(
					len(result)
				):
					print(
						"%d): %s" % 
						(
							a + 1,
							result[a]['title']
						)
					)

				ans = input("What film do you want to see?: ")

				if ans in excapes:
					break
					
				index = int(ans) - 1
				film_to_see = result[index]['link']
				datas = search_mirrors(film_to_see)['results']

				while True:
					for a in range(
						len(datas)
					):
						print(
							"%s): %s (%s)"
							% (
								a + 1,
								datas[a]['mirror'],
								datas[a]['quality']
							)
						)

					ans = input("What film do you want to see?: ")

					if ans in excapes:
						break

					index = int(ans) - 1
					video = identify(datas[index])
					print(video)
		except KeyboardInterrupt:
			break

if __name__ == "__main__":
	menu()