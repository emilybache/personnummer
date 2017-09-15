#!/usr/bin/env python3

import datetime
import random
from dateutil import relativedelta
import luhn
import argparse

def generate_invalid_personnummer(min_age, max_age):
	return _generate_personnummer(min_age, max_age, valid=False)

def generate_valid_personnummer(min_age, max_age):
	return _generate_personnummer(min_age, max_age, valid=True)

def _generate_personnummer(min_age, max_age, valid=True):
	birthdate = random_date(convert_age_to_date(max_age), convert_age_to_date(min_age))
	formatted_birthdate = birthdate.strftime("%Y%m%d")
	three_random = "{n:03d}".format(n=random.randrange(0, 1000))
	first_eleven = "{formatted_birthdate}{three_random}".format(**locals())
	checksum = _generate_checksum(first_eleven[2:], valid=valid)
	return "{formatted_birthdate}-{three_random}{checksum}".format(**locals())

def _generate_checksum(nine_figures, valid=True):
	checksum = luhn.generate(nine_figures)
	if valid:
		return checksum
	else:
		# generate a random checksum candidate, excluding 9
		invalid_checksum = random.randrange(0,9)
		# if we happened to randomly choose the correct checksum, add one to make it invalid again
		if invalid_checksum == checksum:
			invalid_checksum += 1
		return invalid_checksum

def convert_age_to_date(age):
	latest_possible_birthdate = datetime.datetime.today() - relativedelta.relativedelta(years=age)
	oldest_possible_birthdate = latest_possible_birthdate + relativedelta.relativedelta(days=364)
	return oldest_possible_birthdate

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--count", type=int, default=1,
                    help="count of personal numbers to generate, defaults to 1")
	parser.add_argument("--min-age", type=int, default=18,
                    help="minimum age of personal numbers, defaults to 18")
	parser.add_argument("--max-age", type=int, default=125,
                    help="maximum age of personal numbers, defaults to 125")
	parser.add_argument("-i", "--invalid-checksums", help="Include this argument if the checksums should be invalid",
                    action="store_true")

	pargs = parser.parse_args()

	for i in range(pargs.count):
		print(_generate_personnummer(min_age=pargs.min_age,
			max_age=pargs.max_age,
		 	valid= not pargs.invalid_checksums))

if __name__ == "__main__":
    main()