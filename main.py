import singer
import requests
import json
import sys

# Fundamental data urls
URL_COMPANY_OVERVIEW = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=JEPP7M48FZLYH6C0'
URL_INCOME_STATEMENT = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=JEPP7M48FZLYH6C0'

argument = sys.argv[1]


def read_schema(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data


def singer_data(url, singer_schema):
    data = requests.get(url)
    singer.write_schema(schema=singer_schema, stream_name='my_stream', key_properties=[""])
    singer.write_record(stream_name='my_stream', record=data.json())


if argument == 'company-overview':
    schema = read_schema('schemas/company_overview.json')
    singer_data(URL_COMPANY_OVERVIEW, schema)
elif argument == 'income-statement':
    schema = read_schema('schemas/income_statement.json')
    singer_data(URL_INCOME_STATEMENT, schema)




