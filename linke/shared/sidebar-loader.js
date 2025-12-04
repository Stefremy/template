document.addEventListener('DOMContentLoaded', function () {
  const placeholders = document.querySelectorAll('[data-sidebar]');
  placeholders.forEach(async (node) => {
    const url = node.getAttribute('data-sidebar');
    try {
      const res = await fetch(url, {cache: 'no-cache'});
      if (!res.ok) throw new Error('Failed to fetch sidebar');
      const html = await res.text();
      node.innerHTML = html;
      // Set active item if requested
      const activeId = window.SIDEBAR_ACTIVE;
      if (activeId) {
        const el = node.querySelector('#' + activeId);
        if (el) el.classList.add('active');
      }
    } catch (e) {
      console.error('Sidebar include failed:', e);
    }
  });
});
