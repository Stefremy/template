(function(){
    const STORAGE_KEY = 'linke_cookie_consent_v1';
    const ALLOWED_PAGES = ['index', 'contato', 'solucoes', 'sobre-nos'];
    
    function shouldShow() {
        // Get current page filename without extension
        const currentPath = window.location.pathname.toLowerCase();
        const fileName = currentPath.split('/').pop().split('.')[0] || 'index';
        
        console.log('Cookie banner debug:', {
            pathname: window.location.pathname,
            fileName: fileName,
            allowed: ALLOWED_PAGES,
            shouldShow: ALLOWED_PAGES.includes(fileName)
        });
        
        return ALLOWED_PAGES.includes(fileName);
    }
    
    function createBanner() {
        console.log('Creating cookie banner...');
        const banner = document.createElement('div');
        banner.id = 'linke-cookie-consent';
        banner.setAttribute('role', 'complementary');
        banner.setAttribute('aria-label', 'Cookie consent');
        
        banner.innerHTML = `
            <div class="lc-inner">
                <div class="lc-text">
                    <strong>Usamos cookies</strong>
                    <span>Usamos cookies para melhorar a sua experiência e analisar tráfego. Ao continuar, concorda com o uso de cookies.</span>
                </div>
                <div class="lc-actions">
                    <button class="lc-accept" type="button">Aceitar</button>
                    <button class="lc-settings" type="button">Configurações</button>
                </div>
            </div>
        `;
        
        document.body.appendChild(banner);
        console.log('Banner added to DOM');
        
        // Force reflow to trigger CSS transition
        void banner.offsetWidth;
        
        // Add visible class to trigger animation
        setTimeout(() => {
            banner.classList.add('lc-visible');
            console.log('Banner visibility triggered');
        }, 10);
        
        const acceptBtn = banner.querySelector('.lc-accept');
        const settingsBtn = banner.querySelector('.lc-settings');
        
        if (acceptBtn) {
            acceptBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                localStorage.setItem(STORAGE_KEY, 'accepted');
                banner.classList.remove('lc-visible');
                setTimeout(() => banner.remove(), 300);
            });
        }
        
        if (settingsBtn) {
            settingsBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                window.location.href = 'cookies.html';
            });
        }
    }
    
    function init() {
        console.log('Cookie consent script initialized');
        
        // Only show on allowed pages
        if (!shouldShow()) {
            console.log('Page not in allowed list, banner not shown');
            return;
        }
        
        try {
            const status = localStorage.getItem(STORAGE_KEY);
            console.log('LocalStorage status:', status);
            
            if (!status || status !== 'accepted') {
                createBanner();
            } else {
                console.log('User already accepted cookies');
            }
        } catch (e) {
            console.log('LocalStorage error:', e);
            // localStorage not available, show banner anyway
            createBanner();
        }
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
