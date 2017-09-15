import datetime
from dateutil import relativedelta
import luhn
import sys

import personnummer

def test_valid_personnummer():
    pnr = personnummer.generate_valid_personnummer(min_age=18, max_age=110)
    assert len(pnr) == 13
    assert pnr[8] == '-'
    cleaned_pnr = pnr.replace("-", "")
    assert luhn.generate(cleaned_pnr[2:-1]) == int(pnr[-1])

def test_invalid_personnummer():
    pnr = personnummer.generate_invalid_personnummer(min_age=18, max_age=110)
    assert len(pnr) == 13
    assert pnr[8] == '-'
    cleaned_pnr = pnr.replace("-", "")
    assert luhn.generate(cleaned_pnr[2:-1]) != int(pnr[-1])

def test_convert_age_to_date():
    age = 18
    eighteen_years_ago = datetime.datetime.today() - relativedelta.relativedelta(years=18)
    nineteen_years_ago = eighteen_years_ago + relativedelta.relativedelta(years=1)
    birthdate = personnummer.convert_age_to_date(age=18)
    assert birthdate >= eighteen_years_ago
    assert birthdate < nineteen_years_ago

def test_random_date():
    today = datetime.datetime.today()
    eighteen_years_ago = today - relativedelta.relativedelta(years=18)
    thedate = personnummer.random_date(start=eighteen_years_ago, end=today)
    assert thedate < today
    assert thedate > eighteen_years_ago

def test_main(capfd):
    args = ["--count", "1", "--min-age", "0", "--max-age", "100", "--invalid-checksums"]
    sys.argv.extend(args)
    personnummer.main()
    out, err = capfd.readouterr()
    assert len(out.splitlines()) == 1
    cleaned_pnr = out.strip().replace("-", "")
    assert luhn.generate(cleaned_pnr[2:-1]) != int(cleaned_pnr[-1])


