// Shared burger menu functionality - works with element IDs: f33cef5 (index), 5dde0be (other pages)

document.addEventListener('DOMContentLoaded', function() {
    // Support both element IDs
    const elementIds = ['elementor-element-f33cef5', 'elementor-element-5dde0be'];
    
    elementIds.forEach(elementId => {
        const mobileMenuWidget = document.querySelector('.' + elementId);
        if (!mobileMenuWidget) return;
        
        const burgerButton = mobileMenuWidget.querySelector('.elementor-menu-toggle');
        const dropdownMenu = mobileMenuWidget.querySelector('.elementor-nav-menu--dropdown');
        const menuLinks = dropdownMenu ? dropdownMenu.querySelectorAll('.menu-item a, .elementor-item') : [];
        
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
});
