(function () {
	const MEASUREMENT_ID = 'G-8CLD3DJBFM';
	const STORAGE_KEY = 'linke_cookie_consent_v1';
	const ACCEPTED_VALUE = 'accepted';

	function hasConsent() {
		try {
			return localStorage.getItem(STORAGE_KEY) === ACCEPTED_VALUE;
		} catch (_) {
			return false;
		}
	}

	function loadGoogleTag() {
		if (window.__linkeGtagLoaded) return;
		if (!hasConsent()) return;

		window.__linkeGtagLoaded = true;

		// Load gtag.js
		const script = document.createElement('script');
		script.async = true;
		script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(MEASUREMENT_ID);
		document.head.appendChild(script);

		// Initialize dataLayer/gtag
		window.dataLayer = window.dataLayer || [];
		function gtag() {
			window.dataLayer.push(arguments);
		}
		window.gtag = window.gtag || gtag;

		window.gtag('js', new Date());
		window.gtag('config', MEASUREMENT_ID, {
			anonymize_ip: true
		});
	}

	// Try to load immediately (if user already accepted)
	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', loadGoogleTag);
	} else {
		loadGoogleTag();
	}

	// Load as soon as user accepts in this session
	window.addEventListener('linke:cookie-consent-accepted', loadGoogleTag);
})();
