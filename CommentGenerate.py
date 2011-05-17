#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

#Import all the moudles that should be in the README file.
import Main

#TODO: Write to file (only delete the last part of the file)
#TODO: Better markup
#TODO: Do not include modules/classes that is imported from standard library
class CommentGenerate:
	def __init__(self):
		newfile = self.openFile()
		for row in self.generateComments(): 
			print row
			newfile.append(row)
		self.writeToFile(newfile)
		
	
	def generateComments(self):
		array = []
		for name in dir(Main):
			info = getattr(Main, name).__doc__
			if info != None:
				array.append(name + ": \n" + info + "\n")
		return array
		

	def openFile(self):
		file = open("README.md", "r")
		newfile = []
		i = 0
		for row in file: 
			
			newfile.append(row[:-1])
			i= i+1
			if row == "Main functions\n":
				newfile.append("--------------\n")
				break
		file.close()
		return newfile

		
	def writeToFile(self, newfile):
		file = open("README.md", "w")
		for row in newfile:
			print >> file , row
		file.close()

			