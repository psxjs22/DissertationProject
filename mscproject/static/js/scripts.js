
// Function to highlight list items on hover
function highlightListItem() {
    var listItems = document.querySelectorAll('li');
    listItems.forEach(item => {
        item.addEventListener('mouseover', function() {
            this.style.backgroundColor = 'red';
        });
        item.addEventListener('mouseout', function() {
            this.style.backgroundColor = '';
        });
    });
}