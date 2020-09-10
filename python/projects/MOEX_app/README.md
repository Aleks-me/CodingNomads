# Python Capstone Project 

This is my final work after completing "Python software developer" course with CodingNomads.
I've decided to use Moscow Exchange free API since I have interest in investing.

Main ideas:
- collect data for selected instrument or instruments;
- save data to MYSQL database;
- explore data to find an instrument which is not much volatile,
  has good liquidity, not that expensive to by and has a potential
  to earn some money.


## Getting Started

In order to get all work:
1. You'll need a local MYSQL server ready with several tables created.
2. Check methods description.
3. Run "main.py".

```
Structure of MYSQL DB: MOEX db -> "Shares" table
			     	-> "FederalBonds" table
			    	-> "CorporateEurobonds" table
			     	-> "CorporateBonds" table

"Shares" columns:
crecid**		int AI PK
* **board**		varchar(6)
* **trade_date**	date
* **short_name**	varchar(50)
* **secid**		varchar(6)
* **num_trades**	int
* **trade_value**	decimal(15,2)
* **open_price**	decimal(8,2)
* **low_price**	decimal(8,2)
* **high_price**	decimal(8,2)
* **close_price**	decimal(8,2)


"FederalBonds", "CorporateBonds" and "CorporateEurobonds" columns:
* **id**		int AI PK
* **board**		varchar(6)
* **trade_date**	date
* **short_name**	varchar(20)
* **secid**		varchar(20)
* **num_trades**	int
* **trade_value**	decimal(15,2)
* **open_price**	decimal(8,2)
* **low_price**	decimal(8,2)
* **high_price**	decimal(8,2)
* **close_price**	decimal(8,2)
* **expire_date**	date
* **nom_value**	decimal(8,2)
* **unit**		varchar(7)

```


### Prerequisites

See requirements.txt


## Authors

* **Alex Kuznetsov** - *Initial work* - [ Aleks-me ](https://github.com/Aleks-me)

See also the [CodingNomads](https://codingnomads.co/)
