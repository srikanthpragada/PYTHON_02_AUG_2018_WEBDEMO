from django.shortcuts import render, redirect
from .forms import AddDeptForm
import sqlite3


def add_dept(request):
    message = ""
    if request.method == "POST":
        f = AddDeptForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data["name"]
            location = f.cleaned_data["location"]

            # insert into DEPARTMENTS table
            try:
                con = sqlite3.connect(r"e:\classroom\python\aug2\hr.db")
                cur = con.cursor()
                cur.execute("insert into departments(deptname,location) values (?,?)",
                            (name, location))
                con.commit()
                return redirect("/demo/list_depts")
            except Exception as ex:
                print("Database error ->", ex)
                message = "Could not add department!"
            finally:
                con.close()
    else:
        f = AddDeptForm()

    return render(request, 'add_dept.html', {"form": f, "message": message})


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
