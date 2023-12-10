console.log("Hello");
document.getElementById("id_reservation_date").type="date"

const date = new Date();
document.getElementById('reservation_date').value = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate().toString().padStart(2, '0')}`;

console.log(document.getElementById('reservation_date').value);
getBookings();

const reservation_date = document.getElementById('reservation_date');
reservation_date.addEventListener('change', function () {
  getBookings();
});

function getBookings() {
  console.log('Reservation date changed! Updating bookings...');

  let reserved_slots = [];
  const date = document.getElementById('reservation_date').value;
  document.getElementById('today').innerHTML = date;

  fetch("{% url 'bookings' %}" + '?date=' + date)
    .then(r => r.json())
    .then(data => {
      reserved_slots = [];
      let bookingsString = '';
      console.log('Received date:',data);

      for (let i = 0; i < data.length; i++) {
        const item = data[i];
        console.log(item.fields);
        reserved_slots.push(item.fields.reservation_slot);
        bookingsString += `<p>${item.fields.first_name} - ${formatTime(item.fields.reservation_slot)}</p>`;
      }

      let slot_options = '<option value="0" disabled>Select time</option>';

      for (let i = 11; i < 20; i++) {
        const label = formatTime(i);

        if (reserved_slots.includes(i)) {
          slot_options += `<option value=${i} disabled>${label}</option>`;
        } else {
          slot_options += `<option value=${i}>${label}</option>`;
        }
      }

      document.getElementById('reservation_slot').innerHTML = slot_options;
      if (bookingsString === '') {
        bookingsString = 'No bookings';
      }
      document.getElementById('bookings').innerHTML = bookingsString;
    })
    .catch(error => console.error('Error fetching data:', error));
}

function formatTime(time) {
  const ampm = time < 12 ? 'AM' : 'PM';
  const t = time < 12 ? time : time > 12 ? time - 12 : time;
  const label = `${t} ${ampm}`;
  return label;
}

document.getElementById('button').addEventListener('click', function (e) {
  const formdata = {
    first_name: document.getElementById('first_name').value,
    email: document.getElementById('email').value,
    phone_num: document.getElementById('phone_num').value,
    reservation_date: document.getElementById('reservation_date').value,
    reservation_slot: document.getElementById('reservation_slot').value,
    people: document.getElementById('people').value,
    comment: document.getElementById('talk').value,
  };

  fetch("{% url 'bookings' %}", { method: 'POST', body: JSON.stringify(formdata) })
    .then(r => r.text())
    .then(data => {
      getBookings();
    });
});