(function () {
    "use strict";

    function loadBackground(el) {
        var url = el.getAttribute("data-bg");
        if (!url) return;

        // Important is required because Elementor CSS may set background-image too.
        el.style.setProperty("background-image", 'url("' + url + '")', "important");
        el.classList.add("lazy-bg-loaded");
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
            { rootMargin: "300px 0px", threshold: 0.01 }
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
