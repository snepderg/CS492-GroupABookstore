import uuid

from flask import flash, redirect, render_template, request, session, url_for

from flask_app import app
from flask_app.models.book_model import Book
from flask_app.models.books_in_order import Books_in_Order
from flask_app.models.order_model import Order
from flask_app.models.user_model import User


@app.route('/order/add_book/<int:book_id>', methods = ['POST'])
def create_order(book_id):
  book = Book.get_by_id({'id':book_id})
  if 'order_id' not in session:
    data = {
      'customer_id' : session['user_id'],
      'total' : 0 + book.price,
      'order_number': str(uuid.uuid4())[:9]
    }
    print('new order data', data)
    new_order = Order.create_order(data)
    session['order_id'] = new_order
    order_data = {'order_id':new_order, 'book_id':book_id}
    Order.add_book_to_order(order_data)
    Book.update_book_quantity({'id':book_id,'quantity_in_stock':book.quantity_in_stock -1})
    return redirect(f'/book/{book.id}/view')
  else:
    order = Order.get_by_id({'id':session['order_id']})
    update_order_total = {
      'id' : session['order_id'],
      'total' : order.total + book.price
    }
    print('update order total', update_order_total)
    Order.add_book_to_order({'order_id':order.id, 'book_id':book_id})
    Order.update_order(update_order_total)
    Book.update_book_quantity({'id':book_id,'quantity_in_stock':book.quantity_in_stock -1})
    flash(f'Added {book.title} to cart.', 'info')
    return redirect(f'/book/{book.id}/view')

@app.route('/order/<int:user_id>/view')
def view_order(user_id):
  customer_order = Order.get_order_by_customer({'customer_id':user_id})
  order = Order.get_one_with_books({'id':customer_order.id})
  one_user = User.get_by_id({'id':session['user_id']})
  return render_template('view_order.html', order = order, one_user = one_user)

@app.route('/order/<int:book_order_id>/delete_book')
def delete_book_from_order(book_order_id):
  order = Order.get_one_with_books({'id':session['order_id']})
  book_in_order = Books_in_Order.find_one_entry({'id':book_order_id})
  book = Book.get_by_id({'id': book_in_order.book_id})
  Order.update_order({'id':session['order_id'],'total':(order.total - book.price)})
  Book.update_book_quantity({'id':book.id,'quantity_in_stock':book.quantity_in_stock + 1})
  Books_in_Order.delete_one_book({'id':book_order_id})
  print("what is the total", order.total)
  print("length of books before if", len(order.books))

  if len(order.books) == 0:
    print("length of books", len(order.books))
    Order.delete_order({'id':session['order_id']})
    print('***ORDER DELETED****')
    del session['order_id']
    flash('Cart is empty')
    return redirect('/dashboard')
  else:
    flash(f'{book.title} removed from cart.')
  return redirect(f'/order/{session["user_id"]}/view')



