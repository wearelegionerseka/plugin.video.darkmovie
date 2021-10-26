#!/usr/bin/python

class VideoNotAvalaible(Exception):
	def __init__(self, message):
		Exception.__init__(self, "Il video %s non è dispobibile :(" % message)