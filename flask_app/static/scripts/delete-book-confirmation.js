const deleteBookButton = document.getElementById('deleteBookButton');

deleteBookButton.addEventListener('click', function(action) {
    // Get the title value
    const title = document.getElementById('title').value;

    // Show confirmation dialog
    const continueToRoute = confirm("Are you sure that you want to delete \"" + title + "\"?");

    if (!continueToRoute) {
        action.preventDefault()
    };
});