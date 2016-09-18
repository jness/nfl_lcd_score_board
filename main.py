#!/usr/bin/env python

import time

import Adafruit_CharLCD as LCD
import requests

# Raspberry Pi pin configuration:
lcd_rs        = 7
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(
		lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
		lcd_columns, lcd_rows
	)

# Start fetch / display loop
while True:

	# fetch current score from NFL api
	res = requests.get('http://www.nfl.com/liveupdate/scorestrip/ss.json')
	
	if res:

		for game in res.json().get('gms', []):

			# parse our teams and scores
			home_team = '%s %s' % (game['h'], game['hnn'])
			home_team = home_team[:13]
			home_team_score = game['hs']

			away_team = '%s %s' % (game['v'], game['vnn'])
			away_team = away_team[:13]
			away_team_score = game['vs']

			# clear lcd screen
			lcd.clear()

			# write results to lcd screen
			lcd.message('%s %s\n%s %s' % (
					home_team, home_team_score, away_team, away_team_score
				)
			)

			time.sleep(5)

