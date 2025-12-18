(function () {
    "use strict";

    function supportsWebp() {
        try {
            var canvas = document.createElement("canvas");
            if (!canvas.getContext) return false;
            return canvas.toDataURL("image/webp").indexOf("data:image/webp") === 0;
        } catch (e) {
            return false;
        }
    }

    var _supportsWebp = null;

    function pickUrl(el) {
        if (_supportsWebp === null) _supportsWebp = supportsWebp();

        var webp = el.getAttribute("data-bg-webp");
        var fallback = el.getAttribute("data-bg");
        return (_supportsWebp && webp) ? webp : fallback;
    }

    function loadBackground(el) {
        var url = pickUrl(el);
        if (!url) return;

        // Preload first to avoid flashing a blank card while the image downloads.
        var img = new Image();
        img.decoding = "async";
        img.onload = function () {
            // Important is required because Elementor CSS may set background-image too.
            el.style.setProperty("background-image", 'url("' + url + '")', "important");
            el.classList.add("lazy-bg-loaded");
        };
        img.src = url;
    }

    function init() {
        var elements = document.querySelectorAll("[data-bg]");
        if (!elements.length) return;

        if (!("IntersectionObserver" in window)) {
            elements.forEach(loadBackground);
            return;
        }

        var io = new IntersectionObserver(
            function (entries, observer) {
                entries.forEach(function (entry) {
                    if (!entry.isIntersecting) return;
                    loadBackground(entry.target);
                    observer.unobserve(entry.target);
                });
            },
            // Larger rootMargin helps start downloading before the section is visible.
            { rootMargin: "1200px 0px", threshold: 0.01 }
        );

        elements.forEach(function (el) {
            io.observe(el);
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
