# tap-alphavantage


  <p align="center">
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

Buliding TAP for Alpha Vantage API using Singer.io Python


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.8
* Singer.io


### Installation

1. Clone the repo
```sh
git clone https://github.com/mirpulatov/tap-alphavantage.git
```
2. Install Python packages
```sh
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

Geting json FUNDAMENTAL DATA and convert to csv

Company overview:
```sh
python main.py company-overview | target csv
```
Income statement:
```sh
python main.py income-statement | target csv
```
Balance Sheet:
```sh
python main.py balance-sheet | target csv
```
Cash Flow:
```sh
python main.py cash-flow | target csv
```

<!-- CONTACT -->
## Contact

Mirpulatov Islombek - [imirpulatov@icloud.com](imirpulatov@icloud.com) - email

Tap AlphaVantage: [https://github.com/mirpulatov/tap-alphavantage](https://github.com/mirpulatov/tap-alphavantage)

<!-- COMMENTS -->
## Comments

It's bad that singer.io has poor documentation. Also, I did not completely transfer all the data tabs, since this 
is more mechanical work.

I found a Cookicutter - a template for organizing a project, but the first time I decided to do it manually.

