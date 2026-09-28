{
  const initializeTrialFilters = () => {
    document.querySelectorAll("[data-trial-list]").forEach((list) => {
      const controls = list.querySelector(".trial-filters");
      if (!controls || controls.dataset.initialized) return;

      const buttons = [...controls.querySelectorAll("button")];
      const cards = [...list.querySelectorAll(".trial-card")];

      controls.addEventListener("click", (event) => {
        const selected = event.target.closest("button");
        if (!selected || !buttons.includes(selected)) return;

        const showAll = selected.hasAttribute("data-filter-all");
        const productType = selected.dataset.productType;
        cards.forEach((card) => {
          card.hidden = !showAll && card.dataset.productType !== productType;
        });
        buttons.forEach((button) => {
          button.setAttribute("aria-pressed", String(button === selected));
        });
      });

      controls.dataset.initialized = "true";
      controls.hidden = false;
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeTrialFilters, {
      once: true,
    });
  } else {
    initializeTrialFilters();
  }
}
