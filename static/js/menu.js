window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.menu');
    menuItem = document.querySelectorAll('.menu_item');
    hamburger = document.querySelector('.hamburger');

    hamburger.addEventListener('click', () => {
        menu.classList.toggle('menu_active');
        hamburger.classList.toggle('hamburger_active');
    });

    menuItem.forEach(item => {
        item.addEventListener('click', () => {
            hamburger.classList.toggle('hamburger_active');
            menu.classList.toggle('menu_active');
        });
    });
});