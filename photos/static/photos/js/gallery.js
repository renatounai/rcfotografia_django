document.querySelectorAll('.gallery__photo').forEach((photo) => {
    photo.addEventListener('click', (e) => {
        e.preventDefault();
        const modal = document.getElementById('photo-modal');
        modal.classList.add('modal-open');

        document.querySelector('.modal__img').setAttribute('src', photo.getAttribute('src'));

        const exits = modal.querySelectorAll('.modal-exit');
        exits.forEach(function (exit) {
            exit.addEventListener('click', function (event) {
                event.preventDefault();
                modal.classList.remove('modal-open');
            });
        });
    });
});
