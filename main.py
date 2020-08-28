import singer
import requests
import json
import sys

# Fundamental data urls
URL_COMPANY_OVERVIEW = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=JEPP7M48FZLYH6C0'
URL_INCOME_STATEMENT = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=JEPP7M48FZLYH6C0'
URL_BALANCE_SHEET = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=JEPP7M48FZLYH6C0'
URL_CASH_FLOW = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=JEPP7M48FZLYH6C0'

# Reading CLI arg, key of
argument = sys.argv[1]


def read_schema(file_name):
    """
    Reading schema data from json file
    :param file_name: file name
    :return: data from json
    """
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data


def singer_data(url, singer_schema, stream):
    """
    Request data from url, ETL data
    :param url: URL to data
    :param singer_schema: JSON shema
    :param stream: name of stream
    :return: nothing
    """
    data = requests.get(url)
    singer.write_schema(schema=singer_schema, stream_name=stream, key_properties=[""])
    singer.write_record(stream_name=stream, record=data.json())


# choosing the type of data
if argument == 'company-overview':
    schema = read_schema('schemas/company_overview.json')
    singer_data(URL_COMPANY_OVERVIEW, schema, 'company_overview')
elif argument == 'income-statement':
    schema = read_schema('schemas/income_statement.json')
    singer_data(URL_INCOME_STATEMENT, schema, 'income_statement')
elif argument == 'balance-sheet':
    schema = read_schema('schemas/balance_sheet.json')
    singer_data(URL_BALANCE_SHEET, schema, 'balance_sheet')
elif argument == 'cash-flow':
    schema = read_schema('schemas/cash_flow.json')
    singer_data(URL_CASH_FLOW, schema, 'cash_flow')
