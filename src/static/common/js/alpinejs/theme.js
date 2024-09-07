document.addEventListener("alpine:init", () => {
  Alpine.store("theme", {
    name:
      localStorage.getItem("appTheme") ||
      document.querySelector("html").getAttribute("data-theme"),
    toggle() {
      this.name = this.name === "light" ? "dark" : "light";
      document.querySelector("html").setAttribute("data-theme", this.name);
      localStorage.setItem("appTheme", this.name);
    },
    syncTheme() {
      const _name = localStorage.getItem("appTheme");
      if (_name === null) {
        return;
      } else if (_name === "light") {
        this.name = "light";
        document.querySelector("html").setAttribute("data-theme", "light");
      } else if (_name === "dark") {
        this.name = "dark";
        document.querySelector("html").setAttribute("data-theme", "dark");
      }
    },
    isDark() {
      return this.name === "dark";
    },
  });
});
