# Data Modeling With Postgres

## Project Purpose
This project is meant to provide a data pipeline that allows for the Sparkify analytics team to query JSON logs in order to understand the songs their users are lstening to.

![](app_interaction.gif)

## Libraries and Technology Used
- For ETL: Python - Pandas and psycopg2
- For visualization: Plotly and Dash
- Database: PostgreSQL

## Files Used
### create_tables.py
We create an idempotent script that:
- Drops the sparkify database if it already exists and then creates the sparkify database.
- Connects to the database and gets the cursor object so we can execute PostgreSQL commands in a database session.
- We then drop all the tables and then create all the tables (SQL commands are in a sepearate file so we import the queries from that file).
- To end we close the connection.

### sql_queries.py
We create an idempotent script that contains all our SQL queries:
1. We drop all fact and dimension tables.
2. We create our fact table "songplays" and 
