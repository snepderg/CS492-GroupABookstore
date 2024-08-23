// The purpose of this file is to allow users to filter the DOM by book title or author name.

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('bookSearch');
    const booksContainer = document.querySelector('.books-container');
    const books = booksContainer.getElementsByClassName('card');
    const flashMessage = document.getElementById('flashMessage');

    searchInput.addEventListener('input', function() {
        const filter = searchInput.value.toLowerCase();
        let foundBooks = false;

        Array.from(books).forEach(function(book) {
            const title = book.querySelector('.card-title').textContent.toLowerCase();
            const author = book.querySelector('.card-text').textContent.toLowerCase();

            if (title.includes(filter) || author.includes(filter)) {
                book.style.display = '';
                foundBooks = true;
            } else {
                book.style.display = 'none';
            }
        });

        if (!foundBooks) {
            flashMessage.textContent = 'No books found for the search.';
            flashMessage.style.display = 'block';
        } else {
            flashMessage.style.display = 'none';
        }
    });
});