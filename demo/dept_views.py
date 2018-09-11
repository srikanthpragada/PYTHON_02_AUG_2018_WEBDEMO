from django.shortcuts import render
import sqlite3


def add_dept(request):
    return render(request, 'add_dept.html')


def list_depts(request):
    try:
        con = sqlite3.connect(r"e:\classroom\python\aug2\hr.db")
        cur = con.cursor()
        cur.execute("select * from departments")
        return render(request, 'list_depts.html', {"departments": cur.fetchall()})

    except Exception as ex:
        print("Database error ->", ex)
        return render(request, 'list_depts.html',
                      {'error': "Sorry! Could not retrieve details of departments"})
    finally:
        con.close()
