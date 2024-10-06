document.addEventListener('DOMContentLoaded', function() {
    const fileUploadForm = document.getElementById('file-upload-form');
    const uploadStatus = document.getElementById('upload-status');
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const usersTableBody = document.querySelector('#users-table tbody');

    // Функция для получения CSRF токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    fileUploadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const fileInput = document.getElementById('file-input');
        if (!fileInput.files.length) {
            uploadStatus.textContent = 'Выбирете файл';
            return;
        }

        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));

        uploadStatus.textContent = 'Загрузка...';

        fetch('/api/users/upload/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            uploadStatus.textContent = data.message;
            fetchUsers();
        })
        .catch(error => {
            uploadStatus.textContent = 'Ошибка';
            console.error('Error:', error);
        });
    });

    searchButton.addEventListener('click', function() {
        const query = searchInput.value;
        fetchUsers(query);
    });

    function fetchUsers(query = '') {
        fetch(`/api/users/?search=${query}`)
        .then(response => response.json())
        .then(data => {
            usersTableBody.innerHTML = '';
            data.forEach(user => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${user.name}</td>
                    <td>${user.age}</td>
                    <td>${user.email}</td>
                    <td>${user.tel}</td>
                `;
                usersTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Initial fetch of users
    fetchUsers();
});
