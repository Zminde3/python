!pip install ipython-sql
%load_ext sql
%sql sqlite:///gimnazija.db
%%sql
SELECT * FROM mokytojai;
