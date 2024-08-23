// The purpose of this file is to add genre options and handle a dropdown menu for selecting a genre.

document.addEventListener('DOMContentLoaded', function () {
    const genreDropdown = document.getElementById('genreDropdownMenuButton');
    const genreList = document.getElementById('genreList');
    const hiddenInput = document.getElementById('selectedGenre');

    // Check if elements exist
    if (!genreDropdown || !genreList || !hiddenInput) {
        console.error('One or more elements not found');
        return;
    }

    // Array of genres
    const genres = [
        "Children's",
        "Fantasy",
        "Historical Fiction",
        "Horror",
        "Mystery",
        "Non-Fiction",
        "Romance",
        "Science Fiction",
        "Thriller"
    ];

    // Populate the dropdown list with genres
    genres.forEach(genre => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.className = 'dropdown-item fs-5';
        a.href = '#';
        a.textContent = genre;
        li.appendChild(a);
        genreList.appendChild(li);

        // Add event listener to each item
        a.addEventListener('click', function (e) {
            e.preventDefault(); // Prevent the default anchor behavior
            genreDropdown.querySelector('span').textContent = genre;
            hiddenInput.value = genre;
        });
    });
});
