module.exports = {
  proxy: "http://127.0.0.1:8080",
  files: ["static/*", "templates/**/*.html"],
  port: 3000,
  open: true,
  notify: false,
};
