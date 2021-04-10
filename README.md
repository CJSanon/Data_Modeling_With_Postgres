# Data Modeling With Postgres

## Project
This project is meant to provide a data pipeline that allows for the Sparkify analytics team to query JSON logs in order to analyze user activity on their music streaming app.


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
- Drop all the tables and then create all the tables (SQL commands are in a sepearate file so we import the queries from that file).
- To end we close the connection.

### sql_queries.py
Create an idempotent script that contains all our SQL queries:
1. Drop all fact and dimension tables.
2. Create our fact table "songplays" and dimension tables "users", "songs", "artists", and "time".
3. Create insert queries that allow us to take in data from the log files and insert into our Postgres tables.
4. Construct a query to put song id and artist id in the same table.
5. Construct a query for finding artists location based on their latitude and longitude.
6. Create a list of create and drop table queries to make query running iteratable. 


