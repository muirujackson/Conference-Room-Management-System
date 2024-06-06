document.getElementById('bookingForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const room = document.getElementById('room').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    const bookingList = document.getElementById('bookingList');
    const bookingItem = document.createElement('li');
    bookingItem.textContent = `Room: ${room}, Date: ${date}, Time: ${time}`;
    bookingList.appendChild(bookingItem);

    document.getElementById('bookingForm').reset();
});

const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});