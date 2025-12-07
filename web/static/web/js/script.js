document.addEventListener('DOMContentLoaded', () => {

    // --- MENÚ MÓVIL ---
    const menuToggle = document.getElementById('mobile-menu');
    const navLinks = document.getElementById('nav-links');
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = menuToggle.querySelector('i');
            navLinks.classList.contains('active') ?
                (icon.classList.remove('fa-bars'), icon.classList.add('fa-times')) :
                (icon.classList.remove('fa-times'), icon.classList.add('fa-bars'));
        });
    }

    // --- CARRITO DE COMPRAS ---
    let cart = JSON.parse(localStorage.getItem('dulcesCart')) || [];

    // Elementos del DOM
    const cartFloat = document.getElementById('cart-float');
    const cartSidebar = document.getElementById('cart-sidebar');
    const cartOverlay = document.getElementById('cart-overlay'); // NUEVO
    const closeCartBtn = document.getElementById('close-cart');
    const clearCartBtn = document.getElementById('clear-cart-btn'); // NUEVO
    const cartItemsContainer = document.getElementById('cart-items-container');
    const cartCount = document.getElementById('cart-count');
    const cartTotal = document.getElementById('cart-total-price');
    const checkoutBtn = document.getElementById('checkout-btn');
    const addToCartBtn = document.getElementById('add-to-cart');

    let currentProduct = {};

    // Funciones de Apertura/Cierre
    function openCart() {
        cartSidebar.classList.add('open');
        cartOverlay.classList.add('open'); // Mostrar fondo oscuro
        document.body.style.overflow = 'hidden'; // Evitar scroll de fondo
    }

    function closeCart() {
        cartSidebar.classList.remove('open');
        cartOverlay.classList.remove('open'); // Ocultar fondo oscuro
        document.body.style.overflow = 'auto'; // Permitir scroll
    }

    // Eventos de Apertura/Cierre
    cartFloat.addEventListener('click', openCart);
    closeCartBtn.addEventListener('click', closeCart);

    // CERRAR AL HACER CLIC AFUERA (NUEVO)
    cartOverlay.addEventListener('click', closeCart);

    // Función: Vaciar Carrito (NUEVO)
    if (clearCartBtn) {
        clearCartBtn.addEventListener('click', () => {
            if (confirm('¿Estás seguro de que quieres vaciar tu lista?')) {
                cart = [];
                updateCartUI();
            }
        });
    }

    // Función: Actualizar Interfaz
    function updateCartUI() {
        cartItemsContainer.innerHTML = '';
        let total = 0;

        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p class="empty-cart-msg">Tu lista está vacía.</p>';
            cartFloat.style.display = 'none';
        } else {
            cartFloat.style.display = 'flex';
            cart.forEach((item, index) => {
                total += parseInt(item.precio || 0);
                const itemEl = document.createElement('div');
                itemEl.classList.add('cart-item');
                itemEl.innerHTML = `
                    <div class="cart-item-info">
                        <h4>${item.nombre}</h4>
                        <span class="cart-item-price">$${item.precio || 'Consultar'}</span>
                    </div>
                    <i class="fas fa-trash-alt remove-item" data-index="${index}"></i>
                `;
                cartItemsContainer.appendChild(itemEl);
            });
        }

        cartCount.innerText = cart.length;
        cartTotal.innerText = '$' + total;
        localStorage.setItem('dulcesCart', JSON.stringify(cart));
    }

    // Agregar al carrito desde el Modal
    if (addToCartBtn) {
        addToCartBtn.addEventListener('click', () => {
            cart.push(currentProduct);
            updateCartUI();

            // Cerrar modal y abrir carrito
            document.getElementById('tortaModal').classList.remove('show');
            setTimeout(() => {
                document.getElementById('tortaModal').style.display = 'none';
                openCart(); // Usamos la nueva función
            }, 300);
        });
    }

    // Eliminar item individual
    cartItemsContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('remove-item')) {
            const index = e.target.getAttribute('data-index');
            cart.splice(index, 1);
            updateCartUI();
        }
    });

    // Checkout WhatsApp
    checkoutBtn.addEventListener('click', () => {
        if (cart.length === 0) return;

        let mensaje = "Hola Dulces Anylonso! 👋 Quisiera cotizar los siguientes productos de mi lista:\n\n";
        let totalEstimado = 0;

        cart.forEach(item => {
            mensaje += `🍰 *${item.nombre}*`;
            if (item.precio) {
                mensaje += ` ($${item.precio})`;
                totalEstimado += parseInt(item.precio);
            }
            mensaje += "\n";
        });

        mensaje += `\n💰 *Total Aprox:* $${totalEstimado}`;
        mensaje += "\n\nQuedo atento a su confirmación.";

        const telefono = "56957796610";
        window.open(`https://wa.me/${telefono}?text=${encodeURIComponent(mensaje)}`, '_blank');
    });

    // --- LÓGICA DEL MODAL DE PRODUCTO ---
    const modal = document.getElementById('tortaModal');
    const closeModal = document.querySelector('.close-modal');
    const openModalBtns = document.querySelectorAll('.open-modal');

    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-title');
    const modalDesc = document.getElementById('modal-desc');
    const modalPrice = document.getElementById('modal-price');
    const modalWhatsapp = document.getElementById('modal-whatsapp');

    openModalBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (e.target.closest('.btn-card-text')) return;

            const div = btn.closest('.card');
            const nombre = div.getAttribute('data-nombre');
            const desc = div.getAttribute('data-desc');
            const img = div.getAttribute('data-img');
            const precio = div.getAttribute('data-precio');

            currentProduct = { nombre, precio };

            modalImg.src = img;
            modalTitle.textContent = nombre;
            modalDesc.textContent = desc;

            if (precio) {
                modalPrice.textContent = '$' + precio;
                modalPrice.style.display = 'block';
            } else {
                modalPrice.style.display = 'none';
            }

            const telefono = "56957796610";
            const mensaje = `Hola, me interesó la torta "${nombre}".`;
            modalWhatsapp.href = `https://wa.me/${telefono}?text=${encodeURIComponent(mensaje)}`;

            modal.style.display = 'flex';
            setTimeout(() => modal.classList.add('show'), 10);
        });
    });

    // Cerrar Modal
    function cerrarModal() {
        modal.classList.remove('show');
        setTimeout(() => modal.style.display = 'none', 300);
    }
    if (closeModal) closeModal.addEventListener('click', cerrarModal);
    window.addEventListener('click', (e) => { if (e.target == modal) cerrarModal(); });

    // --- FILTRADO DE CATEGORÍAS ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filterValue = btn.getAttribute('data-filter');
            cards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                if (filterValue === 'all' || filterValue === cardCategory) {
                    card.style.display = 'flex';
                    setTimeout(() => card.style.opacity = '1', 50);
                } else {
                    card.style.display = 'none';
                    card.style.opacity = '0';
                }
            });
        });
    });

    // Inicializar
    updateCartUI();
});