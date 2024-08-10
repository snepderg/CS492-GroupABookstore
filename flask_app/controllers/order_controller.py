from flask import flash, redirect, render_template, request, session, url_for

from flask_app import app
from flask_app.models.book_model import Book
from flask_app.models.order_model import Order


@app.route('/order/add_book/<int:book_id>', methods = ['POST'])
def create_order(book_id):
  book_order = {'book_id':book_id}
  book = Book.get_by_id({'id':book_id})
  if 'order_id' not in session:
    data = {
      'customer_id' : session['user_id'],
      'total' : 0 + book.price
    }
    print('new order data', data)
    new_order = Order.create_order(data)
    session['order_id'] = new_order
    order_data = {'order_id':new_order, 'book_id':book_id}
    Order.add_book_to_order(order_data)
    return redirect(f'/book/{book.id}/view')
  else: 
    order = Order.get_by_id({'id':session['order_id']})
    update_order = {
      'customer_id' : session['user_id'],
      'total' : order.total + book.price
    }
    print('update order total', update_order)
    Order.add_book_to_order(update_order)
    return redirect(f'/book/{book.id}/view')

@app.route('/order/<int:id>/view')
def view_order():
  order = Order.get_one_with_books({'id':session['order_id']})
  return render_template('view_order.html', order = order)

