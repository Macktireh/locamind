document.addEventListener("alpine:init", () => {
  Alpine.data("toast", (message) => ({
    show: message ? true : false,
    onCloseToast() {
      this.show = false;
    },
    onOpenToast() {
      this.show = true;
      setTimeout(() => {
        this.onCloseToast();
      }, 4000);
    },
  }));
});
