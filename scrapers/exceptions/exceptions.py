#!/usr/bin/python

class ScrapingFailed(Exception):
	def __init__(self, message):
		Exception.__init__(self, "Non posso eseguire scrape %s :(" % message)