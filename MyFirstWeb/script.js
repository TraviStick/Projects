let cart = [];
let totalPrice = 0;
const cartElement = document.querySelector('.cart');
const showCartButton = document.querySelector('.show-cart svg');
// Toggle cart visibility on show-cart click
showCartButton.onclick = () => {
    const isCartVisible = cartElement.style.display === 'block';
    cartElement.style.display = isCartVisible ? 'none' : 'block';
};

// Hide the cart when "close-cart" button is clicked
document.getElementById('close-cart').onclick = () => {
    cartElement.style.display = 'none';
};

// Existing product preview functionality
let previewContainer = document.querySelector('.products-preview');
let previewBox = previewContainer.querySelectorAll('.preview');

document.querySelectorAll('.products-container .product').forEach(product => {
    product.onclick = () => {
        previewContainer.style.display = 'flex';
        let name = product.getAttribute('data-name');
        let price = parseFloat(product.getAttribute('data-price')); // Ensure data-price is set in your HTML

        // Prompt user for quantity
        let quantity = prompt(`How many of ${name} would you like to add?`, "1");
        quantity = parseInt(quantity) || 1; // Default to 1 if input is invalid

        // Add product to cart
        addToCart(name, price, quantity);

        previewBox.forEach(preview => {
            let target = preview.getAttribute('data-target');
            if (name === target) {
                preview.classList.add('active');
            }
        });
    };
});



function filterProducts() {
    const searchInput = document.getElementById('searchBar').value.toLowerCase();
    document.querySelectorAll('.products-container .product').forEach(product => {
        const productName = product.querySelector('h3').textContent.toLowerCase();
        product.style.display = productName.includes(searchInput) ? '' : 'none';
    });
}

// Function to add items to the cart
function addToCart(name, price, quantity) {
    const existingItemIndex = cart.findIndex(item => item.name === name);
    if (existingItemIndex !== -1) {
        // If item exists, increase the quantity
        cart[existingItemIndex].quantity += quantity;
    } else {
        // If item doesn't exist, add it with the specified quantity
        cart.push({ name, price, quantity });
    }
    updateCartDisplay();
}

// Function to update the cart display
function updateCartDisplay() {
    const cartItemsContainer = document.querySelector('.cart-items');
    cartItemsContainer.innerHTML = ''; // Clear existing items
    totalPrice = 0;

    cart.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.textContent = `${item.name} - ₱${item.price.toFixed(2)} x ${item.quantity} = ₱${(item.price * item.quantity).toFixed(2)}`;
        cartItemsContainer.appendChild(itemElement);
        totalPrice += item.price * item.quantity; // Calculate total price based on quantity
    });

    document.getElementById('total').textContent = totalPrice.toFixed(2);
}

// Checkout button functionality
document.getElementById('checkout').onclick = () => {
    if (cart.length > 0) {
        alert(`Total amount to pay: ₱${totalPrice.toFixed(2)}`);
        
        // Clear the cart after checkout
        cart = [];
        updateCartDisplay();
    } else {
        alert("Your cart is empty!");
    }
};

// Close preview functionality
previewBox.forEach(close => {
    close.querySelector('.fa-times').onclick = () => {
        close.classList.remove('active');
        previewContainer.style.display = 'none';
    };
});

// Add event listener for remove all button
document.getElementById('remove-all').onclick = () => {
    removeAllFromCart();
};

// Function to remove all items from the cart
function removeAllFromCart() {
    cart = []; // Clear the cart array
    totalPrice = 0; // Reset total price
    updateCartDisplay(); // Update the display
}
