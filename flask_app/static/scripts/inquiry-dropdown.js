// The purpose of this file is to add genre options and handle a dropdown menu for selecting a genre.

document.addEventListener('DOMContentLoaded', function () {
    const genreDropdown = document.getElementById('inquiryDropdownMenuButton');
    const genreList = document.getElementById('inquiryList');
    const hiddenInput = document.getElementById('selectedInquiry');

    // Check if elements exist
    if (!inquiryDropdownMenuButton || !inquiryList || !hiddenInput) {
        console.error('One or more elements not found');
        return;
    }

    // Array of genres
    const topics = [
        "Special Order",
        "Shipping",
        "Book Recommendation",
        "Complaint/Concern",
        "Other"
    ];

    // Populate the dropdown list with genres
    topics.forEach(topic => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.className = 'dropdown-item fs-5';
        a.href = '#';
        a.textContent = topic;
        li.appendChild(a);
        genreList.appendChild(li);

        // Add event listener to each item
        a.addEventListener('click', function (e) {
            e.preventDefault(); // Prevent the default anchor behavior
            genreDropdown.querySelector('span').textContent = topic;
            hiddenInput.value = topic;
        });
    });
});
