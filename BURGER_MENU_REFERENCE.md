# Burger Menu Reference - Complete Code from index.html

This is the exact burger menu dropdown implementation from index.html for reference.

## Widget Class ID
- **index.html**: `elementor-element-f33cef5`
- **Other pages** (solucoes, sobre-nos, contato): `elementor-element-5dde0be`

## HTML Structure

```html
<div class="elementor-menu-toggle" role="button" tabindex="0" aria-label="Menu Toggle" aria-expanded="false">
    <svg aria-hidden="true" role="presentation" class="elementor-menu-toggle__icon--open e-font-icon-svg e-eicon-menu-bar" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
        <path d="M104 333H896C929 333 958 304 958 271S929 208 896 208H104C71 208 42 237 42 271S71 333 104 333ZM104 583H896C929 583 958 554 958 521S929 458 896 458H104C71 458 42 487 42 521S71 583 104 583ZM104 833H896C929 833 958 804 958 771S929 708 896 708H104C71 708 42 737 42 771S71 833 104 833Z"></path>
    </svg>
    <svg aria-hidden="true" role="presentation" class="elementor-menu-toggle__icon--close e-font-icon-svg e-eicon-close" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
        <path d="M742 167L500 408 258 167C246 154 233 150 217 150 196 150 179 158 167 167 154 179 150 196 150 212 150 229 154 242 171 254L408 500 167 742C138 771 138 800 167 829 196 858 225 858 254 829L496 587 738 829C750 842 767 846 783 846 800 846 817 842 829 829 842 817 846 804 846 783 846 767 842 750 829 737L588 500 833 258C863 229 863 200 833 171 804 137 775 137 742 167Z"></path>
    </svg>
</div>
<nav class="elementor-nav-menu--dropdown elementor-nav-menu__container" aria-hidden="true">
    <ul id="menu-2-f33cef5" class="elementor-nav-menu">
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-2009 current_page_item menu-item-2770">
            <a href="index.html" aria-current="page" class="elementor-item elementor-item-active" tabindex="-1">Home</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-34">
            <a href="solucoes.html" class="elementor-item" tabindex="-1">Soluções</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-31">
            <a href="sobre-nos.html" class="elementor-item" tabindex="-1">Sobre Nós</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-32">
            <a href="contato.html" class="elementor-item" tabindex="-1">Contato</a>
        </li>
        <li class="menu-item menu-item-type-custom" style="border-top: 1px solid rgba(255,255,255,0.1); margin-top: 12px; padding-top: 12px;">
            <a href="/area-cliente.html" class="elementor-item" tabindex="-1">
                <span class="elementor-button-icon" style="margin-right: 8px; display: inline-block;">
                    <i aria-hidden="true" class="arrow_right-up"></i>
                </span>
                <span>Área de Cliente</span>
            </a>
        </li>
    </ul>
</nav>
```

## CSS Styling

```css
/* Mobile menu dropdown styling */
.elementor-element-f33cef5 {
    position: relative;
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown {
    display: none !important;
    position: fixed !important;
    top: 75px !important;
    left: 0 !important;
    width: 100% !important;
    max-height: calc(100vh - 56px) !important;
    overflow-y: auto !important;
    background: linear-gradient(135deg, rgba(10, 10, 30, 0.98) 0%, rgba(20, 20, 50, 0.98) 100%) !important;
    border-top: 2px solid rgba(255, 255, 255, 0.2) !important;
    z-index: 9999 !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5) !important;
    animation: slideDown 300ms ease-out forwards !important;
    visibility: visible !important;
    opacity: 1 !important;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown[aria-hidden="false"] {
    display: block !important;
    opacity: 1 !important;
    visibility: visible !important;
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown .elementor-nav-menu {
    list-style: none !important;
    padding: 8px 0 !important;
    margin: 0 !important;
    flex-direction: column !important;
    display: flex !important;
    width: 100% !important;
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown .menu-item {
    display: block !important;
    margin: 0 !important;
    width: 100% !important;
    list-style: none !important;
    opacity: 1 !important;
    visibility: visible !important;
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown .menu-item a,
.elementor-element-f33cef5 .elementor-nav-menu--dropdown .elementor-item {
    display: block !important;
    width: 100% !important;
    padding: 12px 20px !important;
    color: #FFFFFF !important;
    text-decoration: none !important;
    transition: background-color 200ms ease !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    background-color: transparent !important;
    opacity: 1 !important;
    visibility: visible !important;
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown .menu-item a:hover,
.elementor-element-f33cef5 .elementor-nav-menu--dropdown .elementor-item:hover {
    background-color: rgba(255, 255, 255, 0.12) !important;
    color: #FFFFFF !important;
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown .menu-item.menu-item-type-custom a,
.elementor-element-f33cef5 .elementor-nav-menu--dropdown .menu-item.menu-item-type-custom .elementor-item {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    padding: 12px 20px !important;
}

.elementor-element-f33cef5 .elementor-nav-menu--dropdown .menu-item.menu-item-type-custom a:hover,
.elementor-element-f33cef5 .elementor-nav-menu--dropdown .menu-item.menu-item-type-custom .elementor-item:hover {
    background-color: rgba(255, 255, 255, 0.18) !important;
}

.elementor-element-f33cef5 .elementor-menu-toggle {
    cursor: pointer;
    transition: opacity 200ms ease;
}

.elementor-element-f33cef5 .elementor-menu-toggle:active {
    opacity: 0.7;
}
```

## JavaScript

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuWidget = document.querySelector('.elementor-element-f33cef5');
    if (!mobileMenuWidget) return;
    
    const burgerButton = mobileMenuWidget.querySelector('.elementor-menu-toggle');
    const dropdownMenu = mobileMenuWidget.querySelector('.elementor-nav-menu--dropdown');
    const menuLinks = dropdownMenu ? dropdownMenu.querySelectorAll('.menu-item a') : [];
    
    if (!burgerButton || !dropdownMenu) return;
    
    // Toggle menu on burger click
    burgerButton.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const isExpanded = burgerButton.getAttribute('aria-expanded') === 'true';
        burgerButton.setAttribute('aria-expanded', !isExpanded);
        dropdownMenu.setAttribute('aria-hidden', isExpanded);
    });
    
    // Close menu when a link is clicked
    menuLinks.forEach(link => {
        link.addEventListener('click', function() {
            burgerButton.setAttribute('aria-expanded', 'false');
            dropdownMenu.setAttribute('aria-hidden', 'true');
        });
    });
    
    // Close menu on outside click
    document.addEventListener('click', function(e) {
        if (!mobileMenuWidget.contains(e.target)) {
            burgerButton.setAttribute('aria-expanded', 'false');
            dropdownMenu.setAttribute('aria-hidden', 'true');
        }
    });
});
```

## Key Features

- **Fixed positioning** at top: 75px (adjust as needed)
- **Full width** dropdown menu
- **Dark gradient background** (rgba colors for transparency)
- **Smooth slide-down animation** (300ms)
- **Hover effects** on menu items
- **Z-index: 9999** to stay on top
- **Accessibility**: Uses aria-expanded and aria-hidden attributes
- **Outside-click detection** to close menu
- **Menu closes** when a link is clicked

## How to Use for Other Pages

When applying to other pages with widget class `elementor-element-5dde0be`:
1. Replace `.elementor-element-f33cef5` with `.elementor-element-5dde0be` in all CSS selectors
2. Adjust the menu links (href values) for each page
3. Use the same HTML structure and JavaScript logic
4. Keep the same CSS styling and animations
