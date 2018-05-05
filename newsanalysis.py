#!/user/bin/env python3
import psycopg2

dbname = "news"
# What are the most popular three articles of all time
query_1_title = ("What are the three most popular articles of all time")
query_1 = """select articles.title, count(*) as view
           from articles join log on log.path like
           concat('%',articles.slug,'%')
           group by articles.title order by view desc limit 3;"""

# Who are the most popular article authors of all time
query_2_title = ("Who are the most popular article authors of all time")
query_2 = """select authors.name, count(*) as view from authors join articles on
            authors.id = articles.author join log on log.path like concat
            ('%',articles.slug,'%') group by authors.name
            order by view desc limit 3;"""

# On which days did more than 1% of requests lead to errors
query_3_title = ("On which days did more than 1% of requests lead to errors")
query_3 = """select day, perc from (select day, round((sum(requests)/
           (select count(*) from log where substring(cast(log.time as text)
           , 0, 11) = day) * 100), 2) as perc from (select substring
           (cast(log.time as text), 0, 11) as day, count(*) as requests
           from log where status like '%404%' group by day) as log_percentage
           group by day order by perc desc) as final_query where perc >= 1;"""

# storing result for the above queries
result_1 = dict()
result_1['head'] = "THE MOST POPULAR THREE ARTICLES:\n"

result_2 = dict()
result_2['head'] = "TOP THREE AUTHORS BY VIEWS:\n"

result_3 = dict()
result_3['head'] = " DAYS WITH MORE THAN 1% ERROR:\n"


# Defining a function to run the query and return the result
def running_queries(query):
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


# defining a function to print the result
def print_result(title):
    print('\n' + title['head'] + '\n\n')
    for row in title['result_of_query']:
        print(str(row[0]) + ' ->->-> ' + str(row[1]) + '\n')
    print('\n')

# storing result of the queries in the variables
result_1['result_of_query'] = running_queries(query_1)
result_2['result_of_query'] = running_queries(query_2)
result_3['result_of_query'] = running_queries(query_3)


# Printing the result
print_result(result_1)
print_result(result_2)
print_result(result_3)
