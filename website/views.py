import numpy
from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required,current_user
from .models import User,appointments
from . import db
import csv
from mail import mail

views = Blueprint('views', __name__)



@views.route('/')
@login_required
def home():
    if current_user.type == "client":
        return render_template("home1.html")
    if current_user.type == "psychiatrist":

        appoint = appointments.query.all()

        return render_template("home2.html",data = appoint,user = current_user)

    else:
        flash("something went wrong")
        return redirect(url_for("auth.logout"))


@views.route('/videocall')
def videocall():
    return render_template("videocall.html",user=current_user)


@views.route('/booking/<userid>',methods=["GET","POST"])
@login_required
def booking(userid):
    time = "XX:XX am"
    date = "XX/XX/XXXX"

    ff = appointments(name=current_user.name,time = time,patid = current_user.id,date = date, number=current_user.phone,user_id = userid)
    mail(current_user.email)
    db.session.add(ff)
    db.session.commit()

    return redirect(url_for("views.home",user=current_user))

@views.route('/detailsss')
def detailsss():
    detail = ["emotion",]
    return render_template("details.html",data = detail)