// Отправка на создание поста
document.getElementById('addPostForm').addEventListener('sudmit', function(e) {
  e.preventDefault();

  let formData = new FormData(this);

  fetch("{% url 'create_post' %}", {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRToken': '{{ csrf_token }}'
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      console.log('Пост успешно создан!');
    } else {
      console.log('Произошла ошибка при создании поста.');
    }
  })
  .catch(error => {
    console.error('Ошибка:', error);
    alert('Произошла ошибка при создании поста.');
  })
})