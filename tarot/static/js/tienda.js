document.addEventListener("DOMContentLoaded", function () {
    const addToCartButtons = document.querySelectorAll(".button");
    const cartList = document.getElementById("cart-list");
    const cartTotal = document.getElementById("cart-total");
    const categoryFilter = document.getElementById("categoryFilter");
    const priceMinFilter = document.getElementById("priceMinFilter");
    const priceMaxFilter = document.getElementById("priceMaxFilter");
    const applyFiltersButton = document.querySelector(".button1"); // Botón para aplicar filtros
    const resetFiltersButton = document.querySelector(".button1 + button"); // Botón para reiniciar filtros
    let total = 0;

    // Función para aplicar filtros
    function applyFilters() {
        const selectedCategory = categoryFilter.value;
        const priceMin = parseFloat(priceMinFilter.value);
        const priceMax = parseFloat(priceMaxFilter.value);

        const products = document.querySelectorAll(".producto");
        products.forEach(product => {
            const productCategory = product.getAttribute("data-categoria");
            const productPrice = parseFloat(product.getAttribute("data-precio"));

            // Comprobar si el producto coincide con los criterios de filtro
            const matchesCategory = selectedCategory === "all" || productCategory === selectedCategory;
            const matchesPrice = productPrice >= priceMin && productPrice <= priceMax;

            // Mostrar u ocultar el producto según los filtros
            if (matchesCategory && matchesPrice) {
                product.style.display = "block";
            } else {
                product.style.display = "none";
            }
        });
    }

    // Función para reiniciar filtros
    function resetFilters() {
        categoryFilter.value = "all"; // Restablece la categoría a "Todas"
        priceMinFilter.value = "0"; // Restablece el precio mínimo a 0
        priceMaxFilter.value = "60000"; // Restablece el precio máximo a 20000
        
        // Mostrar todos los productos
        const products = document.querySelectorAll(".producto");
        products.forEach(product => {
            product.style.display = "block"; // Asegura que todos los productos sean visibles
        });
    }

    // Agregar evento al botón de aplicar filtros
    applyFiltersButton.addEventListener("click", applyFilters);

    // Agregar evento al botón de reiniciar filtros
    resetFiltersButton.addEventListener("click", resetFilters);

    addToCartButtons.forEach(button => {
        button.addEventListener("click", function () {
            const productCard = this.closest(".producto");
            const productName = productCard.querySelector("h5").textContent;

            const productPriceElement = productCard.querySelector("p");
            let productPrice = 0;
            if (productPriceElement) {
                const priceText = productPriceElement.textContent.replace(/[^0-9.]/g, "");
                productPrice = parseFloat(priceText);
            }

            const listItem = document.createElement("li");
            listItem.classList.add("list-group-item", "d-flex", "justify-content-between", "align-items-center");
            listItem.textContent = `${productName} - $${formatCurrency(productPrice)}`;

            const removeButton = document.createElement("button");
            removeButton.classList.add("btn", "btn-danger", "btn-sm");
            removeButton.textContent = "Eliminar";
            removeButton.addEventListener("click", function () {
                cartList.removeChild(listItem);
                total -= productPrice;
                cartTotal.textContent = formatCurrency(total);
            });

            listItem.appendChild(removeButton);
            cartList.appendChild(listItem);
            total += productPrice;
            cartTotal.textContent = formatCurrency(total);
        });
    });

    function formatCurrency(value) {
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
});

