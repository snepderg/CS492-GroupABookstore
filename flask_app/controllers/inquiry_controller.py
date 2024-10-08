from flask import flash, redirect, render_template, request, session, url_for

from flask_app import app
from flask_app.models.inquiry_model import Inquiry
from flask_app.models.user_model import User


def is_admin():
  user = User.get_by_id({'id': session['user_id']})
  return user.admin == 1

@app.route('/contact_us')
def contact_us():
  user = User.get_by_id({'id':session['user_id']})
  return render_template('new_inquiry.html', user = user)

@app.route('/inquiry/new/process', methods=['POST'])
def create_inquiry():
  if not Inquiry.validate(request.form):
    return redirect('/contact_us')
  Inquiry.create_inquiry(request.form)
  flash('Inquiry submitted successfully!\nOur team will reach out to you soon.', 'info')
  return redirect('/dashboard')

@app.route('/inquiries')
def view_all_inquiries():
  if session.get('admin') == 1:
    concerns = Inquiry.view_all_inquiries()
    return render_template('view_inquiries.html', concerns = concerns)
  else:
    return redirect ('/dashboard')

@app.route ('/inquiry/<int:id>/view')
def view_inquiry(id):
  if session.get('admin') == 1:
    concern = Inquiry.view_one_with_user({'id':id})
    return render_template('inquiry.html', concern = concern)
  else:
    return redirect ('/dashboard')

@app.route('/inquiry/<int:id>/delete')
def delete_inquiry(id):
  if session.get('admin') == 1:
    Inquiry.delete_inquiry({'id':id})
    return redirect('/inquiries')