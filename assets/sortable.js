function initSortable() {
  const container = document.getElementById("section-sortable-container");
  if (!container || container.sortableInstance) return;

  container.sortableInstance = new Sortable(container, {
    animation: 150,

    // ✅ ONLY this part is draggable
    handle: ".drag-handle",

    onEnd: function () {
      const order = Array.from(container.children).map(el => el.id);
      document.dispatchEvent(
        new CustomEvent("sectionOrderChanged", { detail: order })
      );
    }
  });
}

const observer = new MutationObserver(initSortable);
observer.observe(document.body, { childList: true, subtree: true });

document.addEventListener("DOMContentLoaded", initSortable);
