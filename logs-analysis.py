#!/usr/bin/env python2


import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def mostPopulatArticles():
    conn = connect()
    cursor = conn.cursor()
    queryStr = """select title,count(*) as views
        from articles join log on log.path like concat('%',articles.slug)
        group by(title) order by(views) desc limit 3;"""
    cursor.execute(queryStr)
    res = cursor.fetchall()
    print "Those are the most three popular articles:"
    for row in res:
        print "title: ", row[0], "__", row[1], " views"

    cursor.close()
    conn.close()


def mostPopularAuthors():
    conn = connect()
    cursor = conn.cursor()
    queryStr = """select name,res.views from authors,
        (select author,count(*) as views from
        articles join log on log.path like concat('%',articles.slug)
        group by(author) order by(views) desc) as res
        where authors.id=res.author;"""
    cursor.execute(queryStr)
    res = cursor.fetchall()
    print "Those are the most three popular authors:"
    for row in res:
        print "author: ", row[0], "__", row[1], " views"

    cursor.close()
    conn.close()


def precentageGRTone():
    conn = connect()
    cursor = conn.cursor()
    queryStr = "select * from precentage where precentage.precentage > 1;"
    cursor.execute(queryStr)
    res = cursor.fetchall()
    print "Those are the days that errors precentages > 1 :"
    for row in res:
        print "day: ", row[0], "__", row[1], "% errors"

    cursor.close()
    conn.close()


if __name__ == "__main__":

    mostPopulatArticles()
    print '*' * 50, '\n'

    mostPopularAuthors()
    print '*' * 50, '\n'
    precentageGRTone()
    print '*' * 50, '\n'
