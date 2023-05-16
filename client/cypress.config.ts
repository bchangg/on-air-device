import { defineConfig } from "cypress";

export default defineConfig({
  projectId: "3tmb2v",

  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },

  component: {
    devServer: {
      framework: "next",
      bundler: "webpack",
    },
  },
});
